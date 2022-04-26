# Healthcare Booking Tool

**Developers:** Cindy Chiu, Jaya Khan 

**Target Industry:** Health care (Clinic/Doctor’s Office)

## Abstract
This tool is aiming to help a clinic build a tool for patients to book a doctor’s appointment. We want to check if the doctor is available at a certain time/location. 

## Project Development Plan 
This project is developed in three parts. First, we designed the database tables using SQL Alchemy APIs - Appointments and Doctors tables. Second, we designed the project strucutre using both Fast API and SQL Alchemy APIs. Third, we wrote test cases to test our REST APIs for healthcare booking tool. 

The Appoinments table is linked to Doctors table and every time an appointment is booked, our post API adds an appointment to Appointments table and removes an entry for available slot from Doctors table. 

## Current Limitation and Future Scope
At the moment, we can have just one slot per doctor in Doctors table. We planned to link Doctors table with another table - Slots - to link multiple available slots for a doctor in Doctors table. We also plan to integrate these backened APIs with a front end mobile UI using a Kivy python framework.

## Requirements
The code was tested on:
- SQLAlchemy==1.4.35
- FastAPI==0.1.0
- uvicorn==0.17.6
- python==3.9.5

## Project Structure
                                                                               
    healthcare_booking
    ├── __init__.py
    ├── crud.py                    
    ├── database.py             
    ├── main.py 
    ├── load_data.py           
    ├── models.py             
    ├── schemas.py    
    test
    ├── __init__.py
    ├──test_app.py 
    ├README.md 
    ├requirements.txt 
 

* `__init__.py` file registers healhcare_booking as a package.
* `database.py` file creates a local database session.
* `models.py` file creates models for database tables.
* `schemas.py` file creates pydantic models to further validate field types of SQLAlchemy models: `models.py`.
* `crud.py` files contains utility functions to interact with the data in the database.
* `main.py` file contains the main Fast API code to run the web services.
* `load_data.py` files insert records from text files from `sample_data` folder into database tables.

## Instruction

### Install

1. Build a virtual environment for running python. `python -m venv path/to/virtual/env/folder`
2. Activate virtual environment. `source path/to/virtual/env/folder/bin/activate`
3. Install dependencies using `pip install` command in the new virtual environment.

### Run

1. Execute `uvicorn healthcare_booking.main:app --reload` to run the web service on local server.
2. Hit http://<host_name>:<port_number>/docs on the browser to test the APIs.


### Sample Data
We’ll generate synthetic data with doctor’s information and availability and create a separate file for testings. The sample data can be found under `sample_data` folder. There are two files: `doctor_test_table.txt` has sample doctor information and `appointment_table.txt` has sample appointments information. The user can use the loaddata function in the API to load all the sample data. Please see API docs for more information. 

### Testing
The user can run the test using `pytest test/test_app.py` command. This will generate a test database that is different from the production database and performed tests on the test database. 

## References

[1] Kivy Framework, https://realpython.com/mobile-app-kivy-python/  

[2] Python Frameworks for mobile app development, https://www.activestate.com/blog/the-best-python-frameworks-for-mobile-development-and-how-to-use-them/

[3] SQLAlchemy for FastAPI, https://fastapi.tiangolo.com/tutorial/sql-databases/

[4] Cascade operations, https://docs.sqlalchemy.org/en/14/orm/cascades.html
