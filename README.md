# Online Medical System
This is a team project following Object-Oriented Programming (OOP) principles, during my polytechnic studies. <br> <br>
Based on the concept of Electronic Health Records, this website is developed while taking into account security features and convenience for the users who are patients and doctors. <br>

Home page of our website <br>
      ![Display homepage](https://github.com/user-attachments/assets/4711c48d-f7f9-4814-91b9-1ad240b5dda8)

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
1. Login as a staff/doctor - http://127.0.0.1:5000/stafflogin <br>
      Hardcoded ID for demo: Chit Boon, Password: password <br>
                        ![Login as staff called Chit Boon](https://github.com/user-attachments/assets/752bc47f-3a91-48ec-be1d-71b7de6249be)

      
2. Health reports display - http://127.0.0.1:5000/allreports/staffname <br>
     a. Filter reports: by patient's name into the search bar <br>
     b. Add reports: Security feature demo-ed - Verification of particular patient's NRIC to be able to add report <br>
                             ![Add patient report but not allowed because patient ID does not exist in record](https://github.com/user-attachments/assets/4d317a07-90d7-4375-bcca-ac1e6f45e731) <br> <br> <br>
                             ![Add patient report after verifying patient ID exist in record](https://github.com/user-attachments/assets/00b222b9-950f-43e8-88c5-c7f0550a8dbc)

     c. Update reports: Logic demoed-ed - Certain fields are restricted as it is tied to the patient's identity <br>
                             ![Update patient record](https://github.com/user-attachments/assets/2ae7176d-8d33-4f7f-9e96-f6a0d6afa754)

     d. Soft Delete reports: Discard the report, with confirmation prompt <br>
      - Patient and Doctor’s View: Patient and Doctor can both soft delete their reports and be able to restore them if needed <br>
                              ![Delete patient record](https://github.com/user-attachments/assets/2fb466aa-9186-48f0-bcef-93466fa771e4)


      - http://127.0.0.1:5000/discardedreports/staffname: Recover reports soft deleted or hard (permanently) delete them <br>
                              ![Recover patient record from recovery bin](https://github.com/user-attachments/assets/0e4353b6-f342-4e2c-982f-63231c67e47e)


#### As patient
1. Sign-up as a patient - http://127.0.0.1:5000/register <br>
      ![Patient Adam register an account](https://github.com/user-attachments/assets/bdbdc7ee-9928-4fb9-89c2-d09312496327)

2. Login as a patient - http://127.0.0.1:5000/login <br>
      ![Patient Adam login to his account](https://github.com/user-attachments/assets/85583536-b2dc-411d-bc7a-597559c5705c)


3. Navigate the website as a patient - http://127.0.0.1:5000/home <br>
    a. View your own health reports created by doctor - http://127.0.0.1:5000/allreports/patient <br>
         ![Patient Adam views his health records, which are created by the doctor](https://github.com/user-attachments/assets/3330b79f-c956-44c6-8794-262e96810dc3)
   
    b. View report status in live-time, i.e. discarded by self or the doctor <br>
         ![Livetime update of discarded report](https://github.com/user-attachments/assets/cb43bb7f-473f-474c-bc42-dd74c60422ae)


     
## Languages and Frameworks used
- Python Language as Controller, with Flask framework in PyCharm Environment <br>
- Shelve module - Persistent Storage for arbitrary Python objects <br>

## My contributions
- Sign-up logic for users who are patients, with login procedure and validation <br> 
- Doctor’s interaction with creating reports for patients: <br>
      - Verify if NRIC exist in current database prior to creation of health reports for the patient<br>
      - Auto-fills patient's information when creating a report
- Recovery bin logic for "soft" deleting reports. Syncs across patients and doctors' display to ensure there are no discrepancy in report status


## Notes
Website is not updated and only partially functionable. Main goal is to showcase some functionalities I have dabbled in.<br>
Features I want to showcase is stated above in _My contributions_ and _Some storylines/features_.
