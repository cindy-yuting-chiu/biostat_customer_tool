# Healthcare Booking Tool
**Developers:** Cindy Chiu, Jaya Khan 
**Target Industry:** Health care (Clinic/Doctor’s Office)

This tool is aiming to help a clinic build a tool for patients to book a doctor’s appointment. We want to check if the doctor is available at a certain time/location. 

### Project development plan 
The project will be developed in two parts, the first part is to build a simple API or database that has all the doctor’s availability. We will store doctors’ information in a Doctor’s table, store patient information in a Patient table, and we’ll have an appointment table that can link appointment information with patient and doctor information. The API should be able to update the availability database if the patient makes an appointment using the tool. The second part will be building the user interface. It will either be a mobile application (native or hybrid) using Python framework (kivy or beeware) or a web application using Python framework (flask probably). 


### Testing
We’ll generate synthetic data with doctor’s information and availability and create a separate file for testings. Users should be able to run the testing file separately. 

### Reference: 

https://realpython.com/mobile-app-kivy-python/  

https://www.activestate.com/blog/the-best-python-frameworks-for-mobile-development-and-how-to-use-them/

