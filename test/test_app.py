import pytest
from fastapi.testclient import TestClient 
from healthcare_booking.models import Base
from healthcare_booking.main import app, get_db

from sqlmodel import Session,  create_engine
from sqlmodel.pool import StaticPool

## pytest fixtures
## these fixtures help us use the testing database instead of production
@pytest.fixture(name="session")
def session_fixture():
    # create a separate database for testing 
    engine = create_engine(
        "sqlite:///testing.db", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session



@pytest.fixture(name="client")   
def client_fixture(session: Session):  
    def get_session_override():  
        return session
    # over-ride the app connection to using the test database
    app.dependency_overrides[get_db] = get_session_override  

    client = TestClient(app)  #test client
    yield client  
    app.dependency_overrides.clear()  


def test_create_doctor(client:TestClient):
    """
    Testing to create a valid doctor 
    """
    response = client.post(  
            "/doctors/", 
            json = {
  "DoctorName": "Jaya Khan",
  "Speciality": "Physician",
  "AvailableTime": "2022-04-26T15:43:55.143Z",
  "DoctorID": 90}
    )
    data = response.json()
    assert response.status_code == 200  
    assert data["DoctorID"] == 90 
    assert data["DoctorName"] == "Jaya Khan" 


def test_bad_create_doctor(client:TestClient):
    """
    Testing if we try inserting a doctor using the same DoctorID
    the app should reject it
    """
    response = client.post(  
            "/doctors/", 
            json = {
  "DoctorName": "Cindy Chiu",
  "Speciality": "Physician",
  "AvailableTime": "2022-04-26T15:43:55.143Z",
  "DoctorID": 90}
    )
    data = response.json()
    assert response.status_code == 400  



def test_loaddata(client: TestClient):
    """
    Testing to load all the data from the sample file
    (including appointment and doctor) 
    """
    response = client.post("/loaddata/")
    assert response.status_code == 200
    assert response.json() == {"ok": True}
 

def test_read_doctors(session: Session, client: TestClient):
    """
    Testing to read all the doctors we generated 
    """
    response = client.get("/doctors/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 11
    assert data[-1]["DoctorName"] == 'Jaya Khan'
 
def test_read_appointments(client: TestClient):
    """
    Testing to read all the appointments we generated 
    """
    response = client.get("/appointments/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 10


def test_create_appointments(client: TestClient):
    """
    Testing to create a valid appiontment
    """
    response = client.post("/appointment/", 
                json = {
  "DoctorID": 10,
  "AppointmentTime": "2022-04-26T15:29:44.155Z",
  "PatientID": "cinchiu",
  "AppointID": 12
})
    assert response.status_code == 200

def test_bad_create_appointments(client: TestClient):
    """
    Testing to create a invalid appiontment
    The doctor is not available
    """
    response = client.post("/appointment/", 
                json = {
  "DoctorID": 20,
  "AppointmentTime": "2022-04-27T15:29:44.155Z",
  "PatientID": "cinchiu",
  "AppointID": 13
})
    assert response.status_code == 400

## test clearing the database
## needs to be in the last testing functions 
## so the user can re-run the test
def test_clearall_doctor(client: TestClient):
    """
    Testing to remove all the records in the doctor table 
    """
    response = client.delete("/cleardata/doctor")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 


def test_clearall_appointment(client: TestClient):
    """
    Testing to remove all the records in the appointment table 
    """
    response = client.delete("/cleardata/appointment")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 

