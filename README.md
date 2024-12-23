# Medical Online System
This is a team project following Object-Oriented Programming (OOP) principles, during my polytechnic studies. <br> <br>
Based on the concept of Electronic Health Records, this website is developed while taking into account security features and convenience for the users who are patients and doctors. <br>

## Functionalities
- Getting queue numbers online <br>
- Online appointment booking <br>
- Online health and medication reports viewing <br>

## Setup
1. App.py needs to run on a local host port <br>
2. Set up Python Interpreter configuration and download pycharm modules/packages <br>
3. Install: matplotlib, flask, flask-mail, wtforms <br>

## Running the program
### Some storylines/features
#### As staff/doctor
1. login as a staff/doctor - http://127.0.0.1:5000/stafflogin <br>
      ID: Chit Boon, Password: password <br>
2. Health reports display - http://127.0.0.1:5000/allreports/staffname <br>
     a. Filter reports: by patient's name into the search bar <br>
     b. Add reports: Security feature demo-ed - Verification of particular patient's NRIC to be able to add report <br>
     c. Update reports: Logic demoed-ed - Certain fields are restricted as it is tied to the patient's identity <br>
     d. Soft Delete reports: Discard the report, with confirmation prompt <br>
           -   Patient and Doctor’s View: Patient and Doctor can both soft delete their reports and be able to restore them if needed <br>
           -   http://127.0.0.1:5000/discardedreports/staffname: Recover reports soft deleted or hard (permanently) delete them <br>

#### As patient
1. sign-up as a patient - http://127.0.0.1:5000/register <br>
2. login as a patient - http://127.0.0.1:5000/login <br>
3. Navigate the homepage as a patient - http://127.0.0.1:5000/home <br>
    a. View your own health reports created by doctor - http://127.0.0.1:5000/allreports/patient <br>
     
## Languages and Frameworks used
- Python Language as Controller, with Flask framework in PyCharm Environment <br>
- Shelve module - Persistent Storage for arbitrary Python objects <br>

## My contributions
- Sign-up logic for users who are patients, with login procedure and validation <br> 
- Doctor’s display: Verification of existing patient’s NRIC prior to creation of health reports <br>
    Includes the availability of all CRUD operations <br>


## Notes
Website is not updated and only partially functionable. Main goal is to showcase some functionalities I have dabbled in.<br>
Features I want to showcase is stated above in _My contributions_ and _Some storylines/features_.
