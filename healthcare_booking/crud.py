"""Utility functions to interact with the data in the database."""
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    """Fetch doctors data from Doctors table."""
    return db.query(models.Doctors).offset(skip).limit(limit).all()


def get_doctor_by_id(db: Session, DoctorID: int):
    """Fetch doctor data by DoctorID from Doctors table."""
    return db.query(models.Doctors).filter(models.Doctors.DoctorID == DoctorID).first()


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


def load_data(db: Session):
    """
    Load sample files to the database for initialization
    """
    with open("sample_data/doctor_test_table.txt", "r", encoding="utf-8-sig") as f:
    # skip header in the file
        next(f)
        for line in f:
            row = line.strip().split("\t")
            # add records to the doctors table
            db_record = models.Doctors(
                DoctorID=row[0], DoctorName=row[1], Speciality=row[2], AvailableTime=row[3]
            )
            db.add(db_record)

    with open("sample_data/appointment_table.txt", "r", encoding="utf-8-sig") as f:
        # skip header in the file
        next(f)
        for line in f:
            row = line.strip().split("\t")
            # add records to the appointment table
            db_record = models.Appointments(
                AppointID=row[0],
                DoctorID=row[1],
                AppointmentTime=datetime.strptime(row[2], "%Y-%m-%d %H:%M"),
                PatientID=row[3],
            )
            db.add(db_record)
    db.commit()