from datetime import datetime
from . import models

# connect to database
# db = database.SessionLocal()
# models.Base.metadata.create_all(bind=database.engine)


def loaddata(db):
    with open("sample_data/doctor_test_table.txt", "r", encoding="utf-8-sig") as f:
        # skip header in the file
        next(f)
        for line in f:
            row = line.strip().split("\t")
            # add records to the doctors table
            db_record = models.Doctors(
                DoctorID=row[0],
                DoctorName=row[1],
                Speciality=row[2],
                AvailableTime=datetime.strptime(row[3], "%Y-%m-%d %H:%M"),
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

    db.close()
