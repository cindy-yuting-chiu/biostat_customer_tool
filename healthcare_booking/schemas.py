"""This file is used to create pydantic models (validate field types of SQLAlchemy models)."""
from pydantic import BaseModel


class DoctorsBase(BaseModel):
    """Common attributes of doctors."""

    DoctorName: str
    Speciality: str
    AvailableTime: str


class DoctorCreate(DoctorsBase):
    pass


class Doctors(DoctorsBase):
    """Unique attributes of doctor."""

    DoctorID: int

    class Config:
        """Provide configurations to Pydantic."""

        orm_mode = True


class AppointmentsBase(BaseModel):
    """Common attributes of appointment."""

    DoctorID: int
    AppointmentTime: str


class AppointmentCreate(AppointmentsBase):
    pass


class Appointments(AppointmentsBase):
    """Unique attributes of appointment."""

    AppointID: int
    PatientID: str

    class Config:
        """Provide configurations to Pydantic."""

        orm_mode = True
