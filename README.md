# Medical Online System
This is a team project following Object-Oriented Programming (OOP) principles, during my polytechnic studies. <br> <br>
Based on the concept of Electronic Health Records, this website is developed while taking into account security features and convenience for the users who are patients and doctors. <br>

## Functionalities
- Getting queue numbers online <br>
- Online appointment booking <br>
- Online health and medication notes viewing <br>

## Setup
1. App.py needs to run on a local host port <br>
2. Set up Python Interpreter configuration and download pycharm modules/packages <br>
3. Install: matplotlib, flask, flask-mail, wtforms <br>

## Running the program
### Some storylines/features
- 1. login as a staff/doctor - http://127.0.0.1:5000/stafflogin: using Chit Boon, password <br>
- 2. http://127.0.0.1:5000/allreports/staffname: show verification of NRIC before creating report, and CRUD update <br>
- 3. Soft delete the health record <br>
-   Patient and Doctor’s View: Patient and Doctor respectively can soft delete the health note record and restore it if they ever need it again. Similar feature to Google Drive’s Bin function <br>
- 4. http://127.0.0.1:5000/discardedreports/staffname: either recover soft deleted health record or hard (permanently) delete the health record
  

## Languages and Frameworks used
- Python Language as Controller, with Flask framework in PyCharm Environment <br>
- Shelve module - Persistent Storage for arbitrary Python objects <br>

## My contributions
- Patient User Sign-up and Login Procedure and Validation <br> 
-   Doctor’s display: Verification of Existing Patient’s NRIC prior to creation of health notes. <br>    Includes the availability of all CRUD operations <br>


## Notes
Website is not updated and only partially functionable. Main goal is to showcase some functionalities I have dabbled in.<br>
Features I want to showcase is stated above in _My contributions_ and _Some storylines/features_.
