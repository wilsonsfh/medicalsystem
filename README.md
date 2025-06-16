# Online Medical System

A team project built to simulate an online Electronic Health Record (EHR) system for doctors and patients. 

Developed with Object-Oriented Programming (OOP) principles and focused on security, and essential healthcare functionalities.

> *Note: This is a proof-of-concept project and not production-ready.*

---

## Preview

**Home Page**  
![Homepage](https://github.com/user-attachments/assets/4711c48d-f7f9-4814-91b9-1ad240b5dda8)

---

## Features

### For Doctors
- Secure login with hardcoded credentials (for demo)
- Add health reports (with NRIC verification)
- View and update existing reports (with field restrictions)
- Soft-delete and recover reports, with a bin-feature

### For Patients
- Sign up and log in securely
- View personal health and medication reports
- Real-time status updates on report deletion/recovery

---

## Setup

### 1. Prerequisites
- Python 3.x
- PyCharm or any Python IDE

### 2. Install Dependencies

```bash
pip install flask flask-mail wtforms matplotlib
```

### 3. Run the App
```bash
python app.py
```

The app will start on `http://127.0.0.1:5000`.

---

## Usage walkthrough

### Doctor Flow

- **Login:**  
  [http://127.0.0.1:5000/stafflogin](http://127.0.0.1:5000/stafflogin)  
  Credentials (demo):  
  - ID: `Chit Boon`  
  - Password: `password`

- **Manage Reports:**  
  - View/Add/Update: [http://127.0.0.1:5000/allreports/staffname](http://127.0.0.1:5000/allreports/staffname)  
    ![Add report - verification](https://github.com/user-attachments/assets/00b222b9-950f-43e8-88c5-c7f0550a8dbc)  
  - Discard/Recover: [http://127.0.0.1:5000/discardedreports/staffname](http://127.0.0.1:5000/discardedreports/staffname)

<br>

### Patient Flow

- **Register:**  
  [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register)  
  ![Register](https://github.com/user-attachments/assets/bdbdc7ee-9928-4fb9-89c2-d09312496327)

- **Login & Dashboard:**  
  [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)  
  [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home)

- **View Reports:**  
  [http://127.0.0.1:5000/allreports/patient](http://127.0.0.1:5000/allreports/patient)  
  ![View Health Reports](https://github.com/user-attachments/assets/3330b79f-c956-44c6-8794-262e96810dc3)

---

## Tech Stack

- Language: Python 
- RESTful Web Framework: Flask
- Database: `shelve` Python object storage
- Libraries (some): `matplotlib`, `flask-mail`, `wtforms` 
- Containerisation: Docker & Docker Compose

---

## My Contributions

- Built patient sign-up and login system with input validation
- Developed NRIC-based verification for secure health report creation
- Auto-filled patient data on doctor-side forms for report creation
- Implemented recovery bin (soft delete) logic for health reports with synchronization across doctor and patient views

---

## Known Limitations

- Website is partially functional and not updated for production use
- All data is stored locally with `shelve` and is not persistent across different systems
- No role-based access control available beyond hardcoded login checks

---
