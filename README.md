# Healthcare Booking Tool

**Developers:** Cindy Chiu, Jaya Khan 

**Target Industry:** Health care (Clinic/Doctor’s Office)

## Abstract
This tool is aiming to help a clinic build a tool for patients to book a doctor’s appointment. We want to check if the doctor is available at a certain time/location. 

## Project Development Plan 
The project will be developed in two parts, the first part is to build a simple API or database that has all the doctor’s availability. We will store doctors’ information in a Doctor’s table, store patient information in a Patient table, and we’ll have an appointment table that can link appointment information with patient and doctor information. The API should be able to update the availability database if the patient makes an appointment using the tool. The second part will be building the user interface. It will either be a mobile application (native or hybrid) using Python framework (kivy or beeware) or a web application using Python framework (flask probably). 

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
    ├── models.py             
    ├── schemas.py            
    └── README.md               

* `__init__` file tells Python that sql with all its modules (Python files) is a package.
* `database.py` file creates a local database session.
* `models.py` file creates models for database tables.
* `schemas.py` file creates pydantic models to further validate field types of SQLAlchemy models: `models.py`.
* `crud.py` files contains utility functions to interact with the data in the database.
* `main.py` file contains the main Fast API code to run the web services.

## Instruction

### Install

1. Build a virtual environment for running python. `python -m venv path/to/virtual/env/folder`
2. Activate virtual environment. `source path/to/virtual/env/folder/bin/activate`
3. Install dependencies using `pip install` command in the new virtual environment.

### Run

`uvicorn healthcare_booking.main:app --reload` will run the web service on the local server.

### Testing
We’ll generate synthetic data with doctor’s information and availability and create a separate file for testings. Users should be able to run the testing file separately. 

## References

[1] Kivy Framework, https://realpython.com/mobile-app-kivy-python/  

[2] Python Frameworks for mobile app development, https://www.activestate.com/blog/the-best-python-frameworks-for-mobile-development-and-how-to-use-them/

[3] SQLAlchemy for FastAPI, https://fastapi.tiangolo.com/tutorial/sql-databases/

