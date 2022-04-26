"""Utility functions to interact with the data in the database."""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    """Fetch doctors data from Doctors table."""
    return db.query(models.Doctors).offset(skip).limit(limit).all()


def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    """Fetch appointments data from Appointments table."""
    return db.query(models.Appointments).offset(skip).limit(limit).all()


def get_doctor_by_id(db: Session, DoctorID: int):
    """Fetch doctor data by DoctorID from Doctors table."""
    return db.query(models.Doctors).filter(models.Doctors.DoctorID == DoctorID).first()


"""Add a delete doctor funtion and use it in main file"""


def delete_available_slot(db: Session, DoctorID: str, AppointmentTime: str):
    print("inside delete slot function########")
    print(DoctorID, AppointmentTime)
    return (
        db.query(models.Appointments)
        .filter(models.Appointments.doctor == DoctorID)
        .delete()
    )


def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    """Add a doctor to Doctors table."""
    db_user = models.Doctors(
        DoctorID=doctor.DoctorID,
        DoctorName=doctor.DoctorName,
        Speciality=doctor.Speciality,
        AvailableTime=doctor.AvailableTime,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    """Add an appointment to the Appointment table."""
    db_appointment = models.Appointments(
        AppointID=appointment.AppointID,
        DoctorID=appointment.DoctorID,
        AppointmentTime=appointment.AppointmentTime,
        PatientID=appointment.PatientID,
    )
    db.query(models.Doctors).filter(
        models.Doctors.DoctorID == db_appointment.DoctorID
    ).delete()
    db.add(db_appointment)
    db.query()
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


# def load_data(db: Session):
#     ld = Loaddata()
#     ld.load_data(db)
#     return {"ok": True}


def delete_doctor(db: Session, DoctorID):
    pass
    # doctor = db.get(models.Doctors, DoctorID)
    # if not doctor:
    #     raise HTTPException(status_code=404, detail="Doctor not found")
    # db.delete(doctor)
    # db.commit()
    # return {"ok": True}
