<h1> ABOUT </h1>
<b>Medical Online System</b>
<p>• Getting queue numbers online</p>
<p>• Online appointment booking</p>
<p>• Online health and medication notes viewing</p>

<h2> LANGUAGES AND FRAMEWORKS USED </h2>
<p>• Python Language as Controller, with Flask framework in PyCharm Environment</p>
<p>• Shelve module - Persistent Storage for arbitrary Python objects</p>

<h2> SETUP </h2>
<p>App.py needs to run on a local host port</p>
<p>Set up Python Interpreter configuration and download pycharm modules/packages</p>
<p>Download: matplotlib, flask, flask-mail, wtforms</p>

<h3>NOTES</h3>
<p>Website is old and only partially functionable</p>
<p>Features I want to showcase is stated below in my contributions</p>

<h2> MY CONTRIBUTION </h2>
<p>• Patient User Sign-up and Login Procedure and Validation</p>
<p> 
<p>• Doctor’s View: Verification of Existing Patient’s NRIC before proceeding to create health
notes, including the availability of all CRUD operations</p>
<p> Firstly, login as a staff/doctor - http://127.0.0.1:5000/stafflogin: using Chit Boon, password</p>
<p> Secondly, http://127.0.0.1:5000/allreports/staffname: show verification of NRIC before creating report, and CRUD update</p>
<p> Soft delete the health record </p>
<p>• Patient and Doctor’s View: Patient and Doctor respectively can soft delete the health note
record and restore it if they ever need it again. Similar feature to Google Drive’s Bin function</p>
<p> Thirdly, http://127.0.0.1:5000/discardedreports/staffname: either recover soft deleted health record or hard (permanently) delete the health record</p>

