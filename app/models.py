from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship
# import the connection to this file 
from .database import Base

# Class for doctors table
class Doctors(Base):
    __tablename__ = "doctors"

    DoctorID = Column(Integer, primary_key=True, index=True)
    DoctorName = Column(String(255))
    Speciality = Column(String(255))
    AvailableTime = Column(String(1225))
    # relationship between these two tables 
    # can be called using Doctors.appointment
    appointment = relationship("Appointments", back_populates="doctor")

# Class for appointments table 
class Appointments(Base):
    __tablename__ = "appointments"

    AppointID = Column(Integer, primary_key=True, index=True)
    DoctorID = Column(Integer, ForeignKey("doctors.DoctorID"))
    AppointmentTime = Column(DateTime)
    PatientID = Column(String(225))
    # relationship between these two tables 
    # can be called using Appointments.doctor
    doctor = relationship("Doctors", back_populates="appointment")
