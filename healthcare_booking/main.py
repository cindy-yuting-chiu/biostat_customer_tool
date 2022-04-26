"""Main file to run FastAPI."""
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from . import models, schemas, crud, load_data
from .database import SessionLocal, engine

# Create database tables.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Custom function for Status 500 error.
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


############ Create APIs ###############


@app.post("/loaddata/")
def loaddata(db: Session = Depends(get_db)):
    """Load data from text file to database."""
    load_data.loaddata(db)


@app.get("/doctors/", response_model=list[schemas.Doctors])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Fetch doctors records from Doctors Table."""
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors


@app.get("/appointments/", response_model=list[schemas.Appointments])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Fetch appointments records from Appointments Table."""
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments


@app.post("/doctors/", response_model=schemas.Doctors)
def create_doctor(doctor: schemas.Doctors, db: Session = Depends(get_db)):
    """Add a doctor to Doctors table."""
    db_user = crud.get_doctor_by_id(db, DoctorID=doctor.DoctorID)
    if db_user:
        raise HTTPException(status_code=400, detail="ID already registered.")
    return crud.create_doctor(db=db, doctor=doctor)


@app.post("/appointment/", response_model=schemas.Appointments)
def create_appointment(
    appointment: schemas.Appointments, db: Session = Depends(get_db)
):
    """Add an appointment to Appointment table."""
    return crud.create_appointment(db=db, appointment=appointment)


@app.delete("/doctors/{DoctorID}")
def delete_doctor(DoctorID: int):
    """Delete a doctor from Doctors table."""
    with Session(engine) as session:
        doctor = session.get(models.Doctors, DoctorID)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        session.delete(doctor)
        session.commit()
        return {"ok": True}
