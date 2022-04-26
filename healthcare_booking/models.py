"""This file is used to create models for database tables."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship
from .database import Base


class Doctors(Base):
    """Create model for Doctors table."""

    __tablename__ = "doctors"
    DoctorID = Column(Integer, primary_key=True, index=True)
    DoctorName = Column(String(255))
    Speciality = Column(String(255))
    AvailableTime = Column(DateTime)
    # relationship between these two tables
    # can be called using Doctors.appointment
    # appointment = relationship("Appointments", uselist=False, backref="doctors")


class Appointments(Base):
    """Create model for Appointments table."""

    __tablename__ = "appointments"
    AppointID = Column(Integer, primary_key=True, index=True)
    AppointmentTime = Column(DateTime)
    PatientID = Column(String(225))
    DoctorID = Column(Integer, ForeignKey("doctors.DoctorID"))

    # relationship between these two tables
    # can be called using Appointments.doctor
    # doctor = relationship("doctors", uselist=False)
