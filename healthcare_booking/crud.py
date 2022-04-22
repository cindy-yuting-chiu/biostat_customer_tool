"""Utility functions to interact with the data in the database."""
from sqlalchemy.orm import Session
from . import models, schemas


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


"""Add a delete docotor funtion and use it in main file"""
