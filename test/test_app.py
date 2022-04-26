import pytest
from fastapi.testclient import TestClient 
from healthcare_booking.models import Base
from healthcare_booking.main import app, get_db

from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from sqlalchemy_utils import drop_database


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
    response = client.post(  
            "/doctors/", json={"DoctorID": '90', "DoctorName": "Jaya Khan", "Speciality":"Physician", "AvailableTime":'[]'}
        )
    data = response.json()
    assert response.status_code == 200  
    assert data["DoctorID"] == 90 
    assert data["DoctorName"] == "Jaya Khan" 

def test_loaddata_doctor(client: TestClient):
    response = client.post("/loaddata/doctors")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert response.json() == {"ok": True} 

def test_read_doctors(session: Session, client: TestClient):
    response =  client.post(  # 
            "/doctors/", json={"DoctorID": 100, "DoctorName": "Cindy Chiu", "Speciality":"Physician", "AvailableTime":'[]'}
    )
    session.commit()
    response = client.get("/doctors/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 12
    assert data[-1]["DoctorName"] == 'Cindy Chiu'
 




def test_clearall_doctor(client: TestClient):

    response = client.delete("/cleardata/doctors")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 
