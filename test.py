#from ..healthcare_booking.models import Doctors, Appointments, Base
#from ..healthcare_booking.database import SessionLocal, engine
import sqlite3
from healthcare_booking.models import Doctors, Appointments, Base
from healthcare_booking.database import SessionLocal, engine
# connect to database
db = SessionLocal()



def test_doctor_data():
    """
    Test whether we've loaded doctor data to the right place
    """
    assert db.query(Doctors)[0].DoctorName == "John Doe"
    assert db.query(Doctors)[-1].DoctorID == 10
    assert sorted([i.Speciality for i in db.query(Doctors).all()]) == sorted(
        [
            "Dermatologists",
            "Family Physicians",
            "Physiatrists",
            "Urologists",
            "Obstetricians and Gynecologists",
            "Family Physicians",
            "Obstetricians and Gynecologists",
            "Family Physicians",
            "Urologists",
            "Physiatrists",
        ]
    )


def test_appointment_data():
    """
    Test whether the appointment data is loaded
    """
    
    pass
