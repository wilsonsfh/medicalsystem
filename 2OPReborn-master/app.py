import os
import matplotlib.pyplot as plt
from os.path import join,dirname,realpath
from flask import Flask, render_template, request, flash, redirect, url_for, session, session,send_from_directory,send_file
from flask_mail import Mail, Message
import shelve
# <<<<<<< HEAD
from wtforms import Form, StringField, BooleanField, TextAreaField, RadioField, SelectField, validators, PasswordField, \
    DateField, SubmitField,FloatField,IntegerField, FileField, SelectMultipleField, widgets, DateTimeField, TimeField
from wtforms.validators import DataRequired, Length
from datetime import datetime
import datetime as dt
import uuid
from wtforms.widgets import ListWidget, CheckboxInput
from werkzeug.utils import secure_filename
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



app = Flask(__name__)
app.secret_key = 'secret123'



class User:
    def __init__(self):
        self.name = ''
        self.password = ''


users = shelve.open('users.db')


def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]


def get_users():
    user_list = []
    klist = list(users.keys())
    for key in klist:
        user_list.append(users[key])
    return user_list


def init_users():
    clear_user()
    for i in range(5):
        create_user('user' + str(i), 'pass' + str(i))


def get_user(id, password):
    db_read = shelve.open("users.db")
    print("hello")

    try:
        userlist = db_read["users"]

    except:
        userlist = {}

    for key in userlist:


        if userlist[key].getpassword() == password:
            if userlist[key].getname() == id:
                return userlist[key]
    return None


def create_user(name, password):
    u = User()
    u.name = name
    u.password = password
    users[name] = u

#== Wilson's Classes ==

class SearchItems(Form):
    item_name = StringField('', validators=[DataRequired()])


class RegistrationItems:
    def __init__(self, name, password, nric, age, dateofbirth, gender, countryoforigin, allergy):
        self.__patientid = 0
        self.__name = name
        self.__password = password
        self.__nric = nric
        self.__age = age
        self.__dateofbirth = dateofbirth
        self.__gender = gender
        self.__countryoforigin = countryoforigin
        self.__allergy = allergy

    def getpatientid(self):
        return self.__patientid

    def getname(self):
        return self.__name

    def getpassword(self):
        return self.__password

    def getnric(self):
        return self.__nric

    def getage(self):
        return self.__age

    def getdateofbirth(self):
        return self.__dateofbirth

    def getgender(self):
        return self.__gender

    def getcountryoforigin(self):
        return self.__countryoforigin

    def getallergy(self):
        return self.__allergy

    def setpatientid(self, patientid):
        self.__patientid = patientid

    def setname(self, name):
        self.__name = name

    def setpassword(self, password):
        self.__password = password

    def setnric(self, nric):
        self.__nric = nric

    def setage(self, age):
        self.__age = age

    def setdateofbirth(self, dateofbirth):
        self.__dateofbirth = dateofbirth

    def setgender(self, gender):
        self.__gender = gender

    def setcountryoforigin(self, countryoforigin):
        self.__countryoforigin = countryoforigin

    def setallergy(self, allergy):
        self.__allergy = allergy


class ReportsItems(RegistrationItems):
    def __init__(self, pname, rtitle, rdate, rtime, reportdesc, name, password, nric, age, dateofbirth, gender,
                 countryoforigin, allergy):
        super().__init__(name, password, nric, age, dateofbirth, gender, countryoforigin, allergy)
        self.__status = 1
        self.__reportid = 0
        self.__pname = pname
        self.__rtitle = rtitle
        self.__rdate = rdate
        self.__rtime = rtime
        self.__reportdesc = reportdesc

    def getstatus(self):
        return self.__status

    def getreportid(self):
        return self.__reportid

    def getpname(self):
        return self.__pname

    def getrtitle(self):
        return self.__rtitle

    def getrdate(self):
        return self.__rdate

    def getrtime(self):
        return self.__rtime

    def getreportdesc(self):
        return self.__reportdesc

    def setstatus(self, status):
        self.__status = status

    def setreportid(self, reportid):
        self.__reportid = reportid

    def setpname(self, pname):
        self.__pname = pname

    def setrtitle(self, rtitle):
        self.__rtitle = rtitle

    def setrdate(self, rdate):
        self.__rdate = rdate

    def setrtime(self, rtime):
        self.__rtime = rtime

    def setreportdesc(self, reportdesc):
        self.__reportdesc = reportdesc


class RegisterForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[validators.DataRequired()])
    nric = StringField('NRIC', validators=[validators.DataRequired()])
    age = IntegerField('Age', validators=[validators.DataRequired()])
    dateofbirth = DateField('Date of Birth', validators=[validators.DataRequired()])
    gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    countryoforigin = StringField('Country of Origin', validators=[validators.DataRequired()])
    allergy = StringField('Allergy', validators=[validators.DataRequired()])
    submit = SubmitField('Register')


class AddReports(Form):
    pname = StringField("Patient's Name", validators=[validators.DataRequired()])
    rtitle = StringField("Title of Medical Report", validators=[validators.DataRequired()])
    rdate = DateField("Date of Medical Report", validators=[validators.DataRequired()])
    rtime = TimeField("Time of Medical Report", validators=[validators.DataRequired()])
    reportdesc = TextAreaField("Report Description", validators=[validators.DataRequired()])
    nric = StringField('NRIC', validators=[validators.DataRequired()])
    age = IntegerField('Age', validators=[validators.DataRequired()])
    dateofbirth = DateField('Date of Birth', validators=[validators.DataRequired()])
    gender = RadioField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    countryoforigin = StringField('Country of Origin', validators=[validators.DataRequired()])
    allergy = StringField('Allergy', validators=[validators.DataRequired()])
    submit = SubmitField('Register')

#=== Kai Jie's Classes End ==

@app.route('/getnumber', methods=['GET', 'POST'])
def get_q():
    print("helllo are un in here")
    queue1 = shelve.open('queue')
    if request.method == "POST":
        print("post")
        nric = request.form["nric"]
        print(len(queue1))
        if len(queue1) == 0:
            date_of_visit = dt.datetime.now().strftime("%d-%m-%y")
            id = date_of_visit + nric
            q = Queue(id, nric, 1)
            queue1[id] = q

            print(queue1)

            print(q.get_num())

            # return template
        else:

            klist = list(queue1.keys())
            date_of_visit = dt.datetime.now().strftime("%d-%m-%y")
            x = []
            for i in klist:
                if queue1[i].get_timest() == dt.datetime.now().strftime("%d-%m-%y"):
                    x.append(queue1[i])
            id = date_of_visit + nric
            q = Queue(id, nric, len(x) + 1)
            queue1[id] = q

            print(q)
            print("Number", len(queue1))
        return render_template("getaqueuenumber.html", title="Get Queue", queuenumber=len(queue1))

    return render_template("getaqueuenumber.html", title="Get Queue", queuenumber=len(queue1))
# @app.route('/getaqueuenumber', methods=['GET', 'POST'])
# def get_queue():
#
#     print("helllo are un in here")
#     queue1 = shelve.open('queue')
#     if request.method == "POST":
#         nric = request.form["nric"]
#         if len(queue1) == 0:
#             date_of_visit = dt.datetime.now().strftime("%d-%m-%y")
#             id = date_of_visit + nric
#             q = Queue(id, nric, 1)
#             queue1[id] = q
#
#             print(queue1)
#
#             print(q.get_num())
#
#             #return template
#         else:
#             klist = list(queue1.keys())
#             date_of_visit = dt.datetime.now().strftime("%d-%m-%y")
#             x = []
#             for i in klist:
#                 if queue1[i].get_timest() == dt.datetime.now().strftime("%d-%m-%y"):
#                     x.append(queue1[i])
#             id = date_of_visit + nric
#             q = Queue(id, nric, len(x) + 1)
#             queue1[id] = q
#
#             print(q)
#             print("Number", len(queue1))
#         return  render_template("getaqueuenumber.html", title="Get Queue", queuenumber=len(queue1))
#
#
#     return render_template("getaqueuenumber.html", title="Get Queue", queuenumber=0)
@app.route('/allreports/patient', methods=['GET', 'POST'])
def allreportspatient():

    db_read = shelve.open("reports.db")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    sessionperson = []

    for nric in userlist:
        nricc = userlist[nric]
        if nricc.getname() == session['name']:
            sessionperson.append(nricc.getname())

    list_reports = []

    for stuff in ReportList:
        patient = ReportList.get(stuff)
        for patientname in sessionperson:
            if patientname == session['name']:
                list_reports.append(patient)
                list_reports.sort(key=lambda x: x.getrtitle())

    form = SearchItems(request.form)

    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            for patientname in sessionperson:
                if patientname == session['name']:
                    if ReportList[reportid].getrtitle().upper().find(keyword.upper()) > -1 or \
                            ReportList[reportid].getrtitle().lower().find(keyword.lower()) > -1:
                        searchedreports.append(ReportList[reportid])
                        return render_template("patientreportssearched.html", title="Medical Reports All Search",
                                               form=form, ReportList=searchedreports, name=session['name'])
        nothingfound = []
        nothingfound.append('1')
        return render_template("patientreportssearched.html", title="Search: Nothing Found", form=form,
                               nothingfound=nothingfound, name=session['name'])

    db_read.close()
    return render_template("allreports.html", reports=list_reports, title="Medical Reports View - Patient", form=form, name=session['name'])


@app.route('/discardedreports/patient', methods=['GET', 'POST'])
def binreportspatient():

    db_read = shelve.open("reports.db")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    sessionperson = []

    for nric in userlist:
        nricc = userlist[nric]
        if nricc.getname() == session['name']:
            sessionperson.append(nricc.getname())

    list_reports = [] #keys

    for stuff in ReportList:
        patient = ReportList.get(stuff)
        for patientname in sessionperson:
            if patientname == session['name']:
                list_reports.append(patient)
                list_reports.sort(key=lambda x: x.getrtitle())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            if ReportList[reportid].getrtitle().upper().find(keyword.upper()) > -1 or ReportList[
                reportid].getrtitle().lower().find(keyword.lower()) > -1:
                searchedreports.append(ReportList[reportid])
                return render_template("discardedpatientreportssearched.html", title="Medical Reports Bin Search",
                                   form=form, ReportList=searchedreports, name=session['name'])
        nothingfound = []
        nothingfound.append('asdfasdfsdf1')
        return render_template("discardedpatientreportssearched.html", title="Search: Nothing Found", form=form,
                               nothingfound=nothingfound, name=session['name'])

    db_read.close()
    db_read2.close()

    return render_template("discardedreports_patient.html", reports=list_reports, title="Medical Reports Bin - Patient Name", form=form, name=session['name'])
@app.route('/discardreportpatient/<reportid>', methods=['POST'])
def discardreportpatient(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))
        ##del cList[reportid]
        reportitem.setstatus(0) #status = 0 is inactive, and status = 1 is active


        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully discarded.', 'success')

        return redirect(url_for('allreportspatient'))

    except:
        flash('Error: Medical Report has not been discarded.', 'danger')
        return redirect(url_for('allreportspatient'))

@app.route('/retrievereportpatient/<reportid>', methods=['POST'])
def retrievereportpatient(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(1)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully recovered.', 'success')

        return redirect(url_for('binreportspatient'))

    except:
        flash('Error: Medical Report has not been recovered.', 'danger')
        return redirect(url_for('binreportspatient'))

@app.route('/permadeletereportpatient/<reportid>', methods=['POST'])
def permadeletereportpatient(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(2)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been permanently deleted.', 'success')

        return redirect(url_for('binreportspatient'))

    except:
        flash('Error: Medical Report has not been deleted.', 'danger')
        return redirect(url_for('binreportspatient'))


@app.route('/allreports/staffreport', methods=['GET', 'POST'])
def allreportsreport():

    db_read = shelve.open("reports.db", "r")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    list_reports = []  # keys

    for stuff in ReportList:
        list_reports.append(ReportList.get(stuff))  # ReportList[stuff]
        list_reports.sort(key=lambda x: x.getrtitle())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            if ReportList[reportid].getrtitle().upper().find(keyword.upper()) > -1 or ReportList[reportid].getrtitle().lower().find(keyword.lower()) > -1:
                searchedreports.append(ReportList[reportid])
                return render_template("staffreportsreportssearched.html", title="Medical Reports ALL Search",form=form, ReportList=searchedreports)

        nothingfound = []
        nothingfound.append('1')
        return render_template("staffreportsreportssearched.html", title="Search: Nothing Found", form=form, nothingfound=nothingfound)
    db_read.close()
    db_read2.close()
    return render_template("allreportsstaff_report.html", reports=list_reports, title="Medical Reports View - Report Title", form=form)


@app.route('/allreports/staffname', methods=['GET', 'POST'])
def allreportsname():

    db_read = shelve.open("reports.db", "r")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    list_reports = [] #keys

    for stuff in ReportList:
        list_reports.append(ReportList.get(stuff)) #ReportList[stuff]
        list_reports.sort(key=lambda x: x.getpname())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            if ReportList[reportid].getpname().upper().find(keyword.upper()) > -1 or ReportList[reportid].getpname().lower().find(keyword.lower()) > -1:
                searchedreports.append(ReportList[reportid])
                return render_template("staffreportsnamesearched.html", title="Medical Reports ALL Search", form=form, ReportList=searchedreports)

        nothingfound = []
        nothingfound.append('1')

        return render_template("staffreportsnamesearched.html", title="Search: Nothing Found", form=form,
                               nothingfound=nothingfound)

    db_read.close()
    db_read2.close()

    return render_template("allreportsstaff_name.html", reports=list_reports, title="Medical Reports View - Patient Name", form=form)

@app.route('/discardedreports/staffname', methods=['GET', 'POST'])
def binreportsname():

    db_read = shelve.open("reports.db", "r")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    list_reports = [] #keys

    for stuff in ReportList:
        list_reports.append(ReportList.get(stuff)) #ReportList[stuff]
        list_reports.sort(key=lambda x: x.getpname())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            if ReportList[reportid].getpname().upper().find(keyword.upper()) > -1 or ReportList[
                reportid].getpname().lower().find(keyword.lower()) > -1:
                searchedreports.append(ReportList[reportid])
                return render_template("staffdiscardednamesearched.html", title="Medical Reports Bin Search",
                                   form=form, ReportList=searchedreports)
        nothingfound = []
        nothingfound.append('asdfasdfsdf1')
        return render_template("staffdiscardednamesearched.html", title="Search: Nothing Found", form=form,
                               nothingfound=nothingfound)

    db_read.close()
    db_read2.close()

    return render_template("discardedreports_name.html", reports=list_reports, title="Medical Reports Bin - Patient Name", form=form)

@app.route('/discardedreports/staffreport', methods=['GET', 'POST'])
def binreportsreport():

    db_read = shelve.open("reports.db", "r")
    db_read2 = shelve.open('users.db')

    ReportList = db_read["reports"]
    userlist = db_read2['users']

    list_reports = [] #keys

    for stuff in ReportList:
        list_reports.append(ReportList.get(stuff)) #ReportList[stuff]
        list_reports.sort(key=lambda x: x.getrtitle())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedreports = []
        ReportList = db_read["reports"]
        for reportid in ReportList:
            if ReportList[reportid].getrtitle().upper().find(keyword.upper()) > -1 or ReportList[
                reportid].getrtitle().lower().find(keyword.lower()) > -1:
                searchedreports.append(ReportList[reportid])
                return render_template("staffdiscardedreportssearched.html", title="Search: Bin - Report Title",
                                       form=form, ReportList=searchedreports)
        nothingfound = []
        nothingfound.append('1')

        return render_template("staffdiscardedreportssearched.html", title="Search: Nothing Found", form=form,
                               nothingfound=nothingfound)

    db_read.close()
    db_read2.close()

    return render_template("discardedreports_report.html", reports=list_reports, title="Medical Reports Bin - Report Title", form=form)

@app.route('/addreports/searchNRIC', methods=['GET', 'POST'])
def searchnric():
    print("in searchnric()")
    report_form = AddReports(request.form)

    db_read = shelve.open("users.db")

    try:
        userlist = db_read["users"]
    except:
        userlist = {}

    if request.method == 'POST':
        print('inside request for searchnric()')
        keyword = report_form.nric.data

        error = None
        if not keyword:
            error = 'Please enter a valid NRIC.'
        else:
            pass

        if error == 'Please enter a valid NRIC':
            flash('Please enter a valid NRIC', 'danger')
            return redirect(url_for('allreportsname'))
        else:
            pass

        for nric in userlist:
            if userlist[nric].getnric().upper()  == keyword.upper() or userlist[nric].getnric().lower() == keyword.lower():
                db_read.close()
                flash('Search Results: NRIC is registered. Personal Information have been auto-filled.', 'success')
                return redirect(url_for('newreport', nricc=keyword))

        flash('Search Results: NRIC is not registered. Please check if you have entered correctly.', 'danger')
        return render_template("addreportsSTAFFsearched.html", report_form=report_form, userlist=userlist, title="New Medical Report", keyword=keyword)

    return render_template("addreportsSTAFFsearched.html", report_form=report_form, userlist=userlist,
                           title="New Medical Report",)


@app.route('/addreports/<nricc>', methods=['GET', 'POST'])
def newreport(nricc):
    print("in newreport()")
    report_form = AddReports(request.form)

    db_read = shelve.open("reports.db")
    print('1st database - reports.db opened in newreport()')
    db_read2 = shelve.open("users.db")
    print('2nd database - users.db opened in newreport()')

    try:
        ReportList = db_read["reports"]
        userlist = db_read2["users"]
        print('db_read and db_read2 successful')
    except:
        ReportList = {}
        userlist = {}


    if request.method == 'POST' and report_form.validate():
        print("in post of addreports, report_form")
        eachreport = userlist.get(nricc)

        pname = report_form.pname.data
        rtitle = report_form.rtitle.data
        rdate = report_form.rdate.data
        rtime = report_form.rtime.data
        reportdesc = report_form.reportdesc.data
        nric = report_form.nric.data
        age = report_form.age.data
        dateofbirth = report_form.dateofbirth.data
        gender = report_form.gender.data
        countryoforigin = report_form.countryoforigin.data
        allergy = report_form.allergy.data

        error = None
        if not pname:
            error = 'Patient Name is required.'
        elif not rtitle:
            error = 'Report Title is required.'
        elif not rdate:
            error = 'Report Date is required.'
        elif not reportdesc:
            error = 'Report Description is required.'
        elif not nric:
            error = 'NRIC is required.'
        elif not age:
            error = 'Age is required.'
        elif not dateofbirth:
            error = 'Date of Birth is required.'
        elif not gender:
            error = 'Gender is required.'
        elif not countryoforigin:
            error = 'Country of Origin is required.'
        elif not allergy:
            error = 'Allergy is required.'

        if error != None:
            flash('Oops! ' + error, 'danger')
            return render_template("addreportsSTAFF.html", report_form=report_form, userlist=userlist,
                                   title="New Medical Report", eachreport=eachreport)

        mr = ReportsItems(pname, rtitle, rdate, rtime, reportdesc, '', '', nric, age, dateofbirth, gender, countryoforigin, allergy)
        now = dt.datetime.now()
        print(now.year)
        reportid = str(nric) + str(now.year) + str(now.month) + str(now.date)

        mr.setreportid(reportid)
        pid_nric = str(nric)#userlist[nric].getnric()
        mr.setpatientid(pid_nric)
        ReportList[reportid] = mr

        db_read["reports"] = ReportList
        db_read.close()
        print("reports.db closed - addreports")
        db_read2["users"] = userlist
        db_read2.close()
        print("users.db closed - registrationitems")

        flash('Medical Report added successfully. Medical Reports sorted by Patient Name on current page.', 'success')
        return redirect(url_for('allreportsname'))

    else: #'GET'
        print("in retrieving")
        userlist = db_read2["users"]
        eachreport = userlist.get(nricc)
        print(nricc)
        print(eachreport)
        report_form.pname.data = eachreport.getname()
        report_form.nric.data = eachreport.getnric()
        report_form.age.data = eachreport.getage()
        report_form.dateofbirth.data = eachreport.getdateofbirth()
        report_form.gender.data = eachreport.getgender()
        report_form.countryoforigin.data = eachreport.getcountryoforigin()
        report_form.allergy.data = eachreport.getallergy()

        return render_template('addreportsSTAFF.html', report_form=report_form, eachreport=eachreport)



@app.route('/discardreportname/<reportid>', methods=['POST'])
def discardreportname(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))
        ##del cList[reportid]
        reportitem.setstatus(0) #status = 0 is inactive, and status = 1 is active


        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully discarded.', 'success')

        return redirect(url_for('allreportsname'))

    except:
        flash('Error: Medical Report has not been discarded.', 'danger')
        return redirect(url_for('allreportsname'))


@app.route('/discardreportreport/<reportid>', methods=['POST'])
def discardreportreport(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))
        reportitem.setstatus(0)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully discarded.', 'success')

        return redirect(url_for('allreportsreport'))

    except:
        flash('Error: Medical Report has not been discarded.', 'danger')
        return redirect(url_for('allreportsreport'))


@app.route('/retrievereportname/<reportid>', methods=['POST'])
def retrievereportname(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(1)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully recovered.', 'success')

        return redirect(url_for('binreportsname'))

    except:
        flash('Error: Medical Report has not been recovered.', 'danger')
        return redirect(url_for('binreportsname'))

@app.route('/retrievereportreport/<reportid>', methods=['POST'])
def retrievereportreport(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(1)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been successfully retrieved.', 'success')

        return redirect(url_for('binreportsreport'))

    except:
        flash('Error: Medical Report has not been retrieved.', 'danger')
        return redirect(url_for('binreportsreport'))


@app.route('/permadeletereportname/<reportid>', methods=['POST'])
def permadeletereportname(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(2)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been permanently deleted.', 'success')

        return redirect(url_for('binreportsname'))

    except:
        flash('Error: Medical Report has not been deleted.', 'danger')
        return redirect(url_for('binreportsname'))


@app.route('/permadeletereportreport/<reportid>', methods=['POST'])
def permadeletereportreport(reportid):
    db_read = shelve.open("reports.db")

    try:
        ReportList = db_read["reports"]
        reportitem = (ReportList.get(reportid))

        reportitem.setstatus(2)

        db_read["reports"] = ReportList
        db_read.close()

        flash('Medical Report has been permanently deleted.', 'success')

        return redirect(url_for('binreportsreport'))

    except:
        flash('Error: Medical Report has not been deleted.', 'danger')
        return redirect(url_for('binreportsreport'))

@app.route('/<id>/', methods=['GET','POST'])
def report_details(id):
    print("hrllo")
    db_read = shelve.open("reports.db")
    db_read2 = shelve.open("users.db")

    ReportList = db_read['reports']
    userlist = db_read2['users']

    list_reports = []

    list_reports.append(ReportList.get(id))

    db_read.close()
    db_read2.close()

    return render_template("reportdetails.html", title="Medical Report Details", reports=list_reports)

@app.route('/<id>/staffreportdetails', methods=['GET','POST'])
def report_detailsstaff(id):
    print("hrllo")
    db_read = shelve.open("reports.db")
    db_read2 = shelve.open("users.db")

    ReportList = db_read['reports']
    userlist = db_read2['users']

    list_reports = []

    list_reports.append(ReportList.get(id))

    db_read.close()
    db_read2.close()

    return render_template("reportdetails_staff.html", title="Medical Report Details", reports=list_reports)

@app.route('/<id>/updatereports', methods=['GET', 'POST'])
def update_reports(id):

    report_form = AddReports(request.form)
    db_read = shelve.open("reports.db")
    db_read2 = shelve.open("users.db")

    # try:
    ReportList = db_read['reports']
    userlist = db_read2['users']

    if request.method == 'POST' and report_form.validate():
        print('Successfully POST and validated in.')
        eachreport = ReportList.get(id)  # key

        pname = report_form.pname.data
        rtitle = report_form.rtitle.data
        rdate = report_form.rdate.data
        rtime = report_form.rtime.data
        reportdesc = report_form.reportdesc.data
        nric = report_form.nric.data
        age = report_form.age.data
        dateofbirth = report_form.dateofbirth.data
        gender = report_form.gender.data
        countryoforigin = report_form.countryoforigin.data
        allergy = report_form.allergy.data

        error = None
        if not pname:
            error ='Patient Name is required.'
        elif not rtitle:
            error ='Report Title is required.'
        elif not rdate:
            error= 'Report Date is required.'
        elif not reportdesc:
            error = 'Report Description is required.'
        elif not nric:
            error = 'NRIC is required.'
        elif not age:
            error= 'Age is required.'
        elif not dateofbirth:
            error ='Date of Birth is required.'
        elif not gender:
            error = 'Gender is required.'
        elif not countryoforigin:
            error = 'Country of Origin is required.'
        elif not allergy:
            error = 'Allergy is required.'

        mr = ReportsItems(pname, rtitle, rdate, rtime, reportdesc,'', '', nric, age, dateofbirth, gender,
                          countryoforigin, allergy)

        mr.setreportid(id)

        ReportList[id] = mr

        db_read["reports"] = ReportList
        db_read.close()
        db_read2["users"] = userlist
        db_read2.close()

        if error == None:
            flash('Medical Report updated successfully. Medical Reports sorted by Patient Name on current page.', 'success')
            return redirect(url_for('allreportsname'))
        else:
            flash('Oops! ' + error, 'danger')
            return redirect(url_for('update_reports', id=ReportList.get(id)))

    else: #'GET'
        print("in retrieving")
        ReportList = db_read["reports"]
        #print(id)
        #print(ReportList)
        #print('ReportList')
        #print(ReportList.keys())
        eachreport = ReportList.get(id) #key
        print(eachreport)
        report_form.pname.data = eachreport.getpname()
        report_form.rtitle.data = eachreport.getrtitle()
        report_form.rdate.data = eachreport.getrdate()
        report_form.rtime.data = eachreport.getrtime()
        report_form.reportdesc.data = eachreport.getreportdesc()
        report_form.nric.data = eachreport.getnric()
        report_form.age.data = eachreport.getage()
        report_form.dateofbirth.data = eachreport.getdateofbirth()
        report_form.gender.data = eachreport.getgender()
        report_form.countryoforigin.data = eachreport.getcountryoforigin()
        report_form.allergy.data = eachreport.getallergy()

        return render_template('updatereports.html', report_form=report_form, eachreport=eachreport)
    # except:
    #     print("update not working - except ")

    # return render_template('updatereports.html', report_form=report_form)


class Queue:
    #name,your queue number,estimated time,venue) status when patient is completed, time estimate if not possible do not put, venue instead put queuing to see doctor or take medicine
    def __init__(self, id, nric, num):
        self.__id = id
        self.__nric = nric
        self.__num = num
        self.__timest = dt.datetime.now().strftime("%H:%M")
        print(self.__timest)
        self.__type = 'DOCTOR'
        self.__dateofvisit = dt.datetime.now().strftime("%d-%m-%y")
        print(self.__dateofvisit)

    def get_nric(self):
        return self.__nric

    def get_num(self):
        return self.__num

    def get_timest(self):
        return self.__timest

    def get_venue(self):
        return self.__venue

    def set_nric(self,nric):
         self.__nric=nric

    def set_num(self,num):
        self.__num=num

    def set_timest(self,timest):
        self.__timest=timest

    def set_venue(self,venue):
        self.__venue=venue




#== Wilson's Classes END ==


@app.route('/inde', methods=['GET', 'POST'])
def inde():
    db_read = shelve.open("users.db", "r")
    user = db_read['users']
    list = []
    print(user)
    for i in user:
        patient_info = user[i]
        list.append(patient_info)
    print(list)
    return render_template('inde.html',list = list,user = session['name'] )

@app.route('/')
@app.route('/home')
def default():
    return render_template('home.html')
@app.route('/myprofile',methods=['GET','POST'])
def myprofile():
    db_read = shelve.open("users.db","r")
    user = db_read['users']
    list = []
    print(user)
    for i in user:
        patient_info = user[i]
        print(patient_info.getname())
        if patient_info.getname()  == session['name']:
            list.append(patient_info)
    print(list)
    return render_template('myprofile.html',name = session['name'],list=list )

class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):

        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)

class LoginForm(Form):
    id = StringField('Name', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')


class SearchItems(Form):
    item_name = StringField('', validators=[DataRequired()])

@app.route('/register', methods=('GET','POST'))
def register():

    print("in register() of register")
    register_form = RegisterForm(request.form)

    db_read = shelve.open("users.db")

    try:
        userlist = db_read["users"]

    except:
        userlist = {}

    if request.method == 'POST' and register_form.validate():
        print("in POST of register, register_form")
        name = register_form.name.data
        password = register_form.password.data
        password2 = register_form.password2.data
        nric = register_form.nric.data
        age = register_form.age.data
        dateofbirth = register_form.dateofbirth.data
        gender = register_form.gender.data
        countryoforigin = register_form.countryoforigin.data
        allergy = register_form.allergy.data

        error = None
        if not name:
            error = 'Name is required.'
        elif not password:
            error = 'Password is required.'
        elif password != password2:
            error = 'Password does not match.'
        elif not nric:
            error = 'NRIC is required.'
        elif not age:
            error = 'Age is required.'
        elif not dateofbirth:
            error = 'Date of Birth is required.'
        elif not gender:
            error = 'Gender is required.'
        elif not countryoforigin:
            error = 'Country of Origin is required.'
        elif not allergy:
            error = 'Allergy is required. If none, put NIL.'

        if error != None:
            flash('Oops! ' + error, 'danger')
            return redirect(url_for('register'))

        ri = RegistrationItems(name, password, nric, age, dateofbirth, gender, countryoforigin, allergy)


        pid_nric = ri.getnric()
        print(pid_nric)
        ri.setpatientid(pid_nric)

        userlist[pid_nric] = ri

        db_read["users"] = userlist

        db_read.close()
        print("user.db closed")


        flash('You have successfully registered a new account.', 'success')
        return redirect(url_for('login'))



    return render_template("register.html", form=register_form, title="Registration")


@app.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':

        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Wrong name and password'
        else:
            session['name'] = user.getname()
            return redirect(url_for('default'))
        flash(error)
    return render_template('login.html', form=login_form)


class AdminLoginForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    
    
@app.route('/ahh')
def ahh():
    return render_template("ahh.html")


@app.route('/stafflogin',methods=('GET','POST'))
def stafflogin():
    staff_form = AdminLoginForm(request.form)
    if request.method == 'POST' and staff_form.validate():
        name = staff_form.name.data
        password = staff_form.password.data

        if name == 'Chit Boon' and password == 'password':  # harcoded name and password
            session['logged_in'] = True
            session['name'] = name
            db_read = shelve.open("medicalitems.db")

            medicalitems = db_read["medicalitems"]

            print(medicalitems)

            list = []

            for medid in medicalitems:
                list.append(medicalitems.get(medid))

            exceed = "norm"
            lowed = "norm"
            exceedlist = []
            lowlist = []
            for medicalitem in list:
                if medicalitem.get_qty() > medicalitem.get_max() and medicalitem.get_status() == 'A':
                    exceed = "exceeded"
                    exceedlist.append(medicalitem.get_name())
                    print("exceeded")

                if medicalitem.get_qty() < medicalitem.get_min() and medicalitem.get_status() == 'A':
                    lowed = "low"
                    lowlist.append(medicalitem.get_name())
                    print("low")

            if exceed == "exceeded":
                msg = Message('Dear staff, please note that there is stock excess on medicine',
                              sender='serveit1801@gmail.com', recipients=['soh.zixiang01@gmail.com'])
                msg.body = str(','.join(
                    exceedlist)) + " has exceeded"+".Do remember to not order any more stock and update the quantity on the website!"
                mail.send(msg)
                print(','.join(exceedlist))

            if lowed == "low":
                msg = Message('Dear staff, please note that there is low stock on medicine',
                              sender='serveit1801@gmail.com', recipients=['soh.zixiang01@gmail.com'])
                msg.body = str(','.join(
                    lowlist)) + " is below the minimum threshhold." + "Do remember to order more stock and update the quantity on the website!"
                mail.send(msg)


            return redirect(url_for('inde'))
        else:
            error = 'Invalid login'
            flash(error, 'danger')
            return render_template('stafflogin.html', staff_form= staff_form)
        
    return render_template('stafflogin.html',staff_form=staff_form)


@app.route('/stafflogout')
def stafflogout():
    session.clear()

    return redirect(url_for('stafflogin'))


class AppointmentSearch(Form):
    app_name= StringField('Search', validators=[DataRequired()])


class slots_search(Form):
    app_date = StringField('Search',validators= [DataRequired()])


@app.route('/staffappointment',methods=('GET','POST'))
def appointment():
    db_read = shelve.open("Appointment.db", "r")
    appointment = db_read['Appointment']
    print(appointment)
    list = []
    for id in appointment:
        list.append(appointment.get(id))
    db_read.close()
    form = AppointmentSearch(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.app_name.data
        searchedappointment = []
        db_read = shelve.open("Appointment.db")
        appointmentitems = db_read["Appointment"]
        dict = appointmentitems
        for k in dict:

            if dict[k].get_patient_name().upper().find(keyword.upper()) > -1 or dict[k].get_patient_name().lower().find(keyword.lower()) >-1:
                searchedappointment.append(dict[k])
                return render_template("appsearch.html", title="Appointment Status ", form=form, appointmentitems=searchedappointment)
    return render_template('appointmentstatus.html',appointment= list,form=form )


@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    flash("You are now logged out", 'success')
    return redirect(url_for('guest'))




# Timeslot for Doctor

#Feedback

@app.route('/index')
def staffhomepage():
    return render_template('index.html',staff = session['name'])

class Timeslots:
    def __init__(self, day, available_timeslots):
        self.__day = day
        self.__available_timeslot = available_timeslots
    def get_day(self):
        return self.__day
    def set_day(self,day):
        self.__day = day



class Time:
    def __init__(self, timeslot, booking_id, status):
        self.__timeslot = timeslot
        self.__booking_id = booking_id
        self.__status = status

    def get_timeslot(self
                     ):
        return self.__timeslot

    def set_timeslot(self, timeslot):
        self.__timeslot = timeslot

        # class that stores with 2 attributes ; 1 - timeslot 2- patient's name/booking id 3- status
        # store data in db.
        # python function pass dictionary into templates
        # templates loop through the dictionary
        # get the key for day (outerloop)
        # interlist - list of orders time slot [interloop]

    # Make a dictionary instead , {"mon": class that have the timeslot and fields that indicates if it's empty/booked/on leave}
    # if dict is empty , will be a checkbox (suggested only) for them to book
    # if dict is booked, they can choose their status like (Not free/free etc..)
    # Every staff timeslot; a dictionary ; weekly.




class doctor_selection:
    def __init__(self, mon_reserved, tue_reserved, wed_reserved, thu_reserved, fri_reserved, sat_reserved):
        self.__mon_reserved = mon_reserved
        self.__tue_reserved = tue_reserved
        self.__wed_reserved = wed_reserved
        self.__thu_reserved = thu_reserved
        self.__fri_reserved = fri_reserved
        self.__sat_reserved = sat_reserved

    def get_mon_reserved(self):
        return self.__mon_reserved

    def get_tue_reserved(self):
        return self.__tue_reserved

    def get_wed_reserved(self):
        return self.__wed_reserved

    def get_thu_reserved(self):
        return self.__thu_reserved

    def get_fri_reserved(self):
        return self.__fri_reserved

    def get_sat_reserved(self):
        return self.__sat_reserved

    def set_mon_reserved(self, mon_reserved):
        self.__mon_reserved = mon_reserved

    def set_tue_reserved(self, tue_reserved):
        self.__tue_reserved = tue_reserved

    def set_wed_reserved(self, wed_reserved):
        self.__wed_reserved = wed_reserved

    def set_thu_reserved(self, thu_reserved):
        self.__thu_reserved = thu_reserved

    def set_fri_reserved(self, fri_reserved):
        self.__fri_reserved = fri_reserved

    def set_sat_reserved(self, sat_reserved):
        self.__sat_reserved = sat_reserved


# WTF forms for Doctor Use ---
class MultiCheckboxField(SelectMultipleField):


    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class DoctorDetails:

    def __init__(self,doctor_name,day,time):
        self.__doctor_name = doctor_name
        self.__day = day
        self.__time = time
    def get_doctor_name(self):
        self.__doctor_name  = session['name']
    def get_day(self):
        return self.__day
    def set_day(self,day):
        self.__day = day
    def get_time(self):
        return self.__time
    def set_time(self,time):
        self.__time = time


class AppointmentDetails:

    def __init__(self, reserved_date, appointment_type, reserved_time, reserved_day):
        self.__appointment_type = appointment_type
        self.__status = "Active"
        self.__patient_name=  session['name']
        self.__id = ""
        self.__reserved_time = reserved_time
        self.__reserved_date = reserved_date
        self.__reserved_day  = reserved_day


    def get_patient_name(self):
        return self.__patient_name
    def set_patient_name(self,patient_name):
        self.__patient_name = patient_name

    def get_reserved_day(self):
        return self.__reserved_day

    def set_reserved_day(self,reserved_day):
        self.__reserved_day = reserved_day

    def get_reserved_time(self):
        return self.__reserved_time

    def set_reserved_time(self, reserved_time):
        self.__reserved_time = reserved_time

    def get_reserved_date(self):
        return self.__reserved_date

    def set_reserved_date(self, reserved_date):
        self.__reserved_date = reserved_date

    def get_appointment_type(self):
        return self.__appointment_type

    def get_id(self):
        return self.__id

    def set_appointment_type(self, appointment_type):
        self.__appointment_type = appointment_type

    def set_status(self,status):

        self.__status = status

    def get_status(self):
        return self.__status

    def set_id(self, id):
        self.__id = id


# Appointment Form For Patient
class AppointmentForm(Form):
    reservation_date = DateField('Date : ', default=datetime.today().date(),
                                 validators=[DataRequired()])
    reservation_time = SelectField( " Time:",[validators.DataRequired()],choices=[("8AM","8AM"),("9AM","9AM"),
                                                                                                  ("10AM","10AM"),("11AM","11AM"),("12PM","12PM"),
                                                                                                  ("1PM", "1PM"),("2PM","2PM"),("3PM","3PM"),
                                                                                                  ("4PM", "4PM"),("5PM","5PM"), ("6PM","6PM")])

    appointment_type = SelectField("Appointment Type:", [validators.DataRequired()], choices=[("Family Medicine", "Family Medicine"),
                                                                                              (
                                                                                                  "Gastroenterology",

                                                                                                  "Gastroenterology"),
                                                                                              ("Specialist Service",
                                                                                               "Specialist Services"), (
                                                                                                  "Health Screening",
                                                                                                  "Health Screening")],
                                   default="Choose your option")








#----------------- Jun En's Staff Appointment for Doctor Use -----------------------------------------------------
@app.route('/status', methods=['GET', 'POST'])
def indexs():
    db_read = shelve.open("doctor.db", "r")
    monday= db_read['Monday']
    tuesday = db_read['Tuesday']
    wednesday= db_read['Wednesday']
    thursday = db_read ["Thursday"]
    friday = db_read ["Friday"]
    saturday = db_read["Saturday"]
    db_read.close()
    return render_template("doctorstatus.html", title="Appointment Status", mon=monday,tue=tuesday,wed=wednesday,thu=thursday,fri=friday,sat=saturday)

class TimeSlot:
    def __init__(self, date, time):
        self.date = date
        self.time = time
    def get_date(self):
        return self.date
    def get_time(self):
        return self.time


@app.route('/delete_appointment/<int:id>', methods=['POST'])
def delete_appointment(id):
    db_read = shelve.open("Appointment.db")

    try:
        List = db_read["Appointment"]
        print("id, ", id)
        print("List before: ", List)

        List.pop(id)

        print(List)
        db_read["Appointment"] = List
        db_read.close()

        flash('Appointment Deleted', 'success')

        return redirect(url_for('vieappointmentlist'))

    except:
        flash('Appointment Slot Not Deleted', 'danger')
        return redirect(url_for('appointment'))

@app.route('/cancel_appointment/<int:id>', methods=['POST'])
def cancel_appointment(id):
    db_read = shelve.open("Appointment.db")

    try:
        List = db_read["Appointment"]
        print("id, ", id)
        print("List before: ", List)

        List.pop(id)

        print(List)
        db_read["Appointment"] = List
        db_read.close()

        flash('Appointment has been cancelled ', 'success')

        return redirect(url_for('myappointment'))

    except:
        flash('Appointment Slot Not Deleted', 'danger')
        return redirect(url_for('myappointment'))


@app.route('/doctorslots/', methods=['POST', 'GET'])
def index():
    weekdays = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    timeslots     = ['8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM']
    db_read = shelve.open("doctor.db")

    if request.method == "POST":

        data = dict((key, request.form.getlist(key) if len(
            request.form.getlist(key)) > 1 else request.form.getlist(key)[0])
            for key in request.form.keys())


        db_read["doctor"] = data
        Monday = []
        Tuesday = []
        Wednesday = []
        Thursday = []
        Friday = []
        Saturday = []
        for i in data:
            if  'Mon' in i:
                Monday.append(i[4:])
                mon = DoctorDetails(session['name'],"Mon",Monday)
                db_read["Monday"] = mon
                print(mon.get_day())
            if "Tue" in i:
                Tuesday.append(i[4:])
                tue = DoctorDetails(session['name'],"Tuesday",Tuesday)
                db_read["Tuesday"] = tue
            if "Wed" in i:
                Wednesday.append(i[4:])
                wed = DoctorDetails(session['name'],"Wednesday",Wednesday)
                db_read["Wednesday"] = wed
            if "Thu" in i:
                Thursday.append(i[5:])
                thu = DoctorDetails(session['name'],'Thursday',Thursday)
                db_read["Thursday"] = thu
            if "Fri" in i:
                Friday.append(i[4:])
                fri = DoctorDetails( session['name'],"Friday",Friday)
                db_read["Friday"] = fri
            if "Sat" in i:
                Saturday.append(i[4:])
                sat =  DoctorDetails(session['name'], "Saturday", Saturday)
                db_read["Saturday"] = sat


        db_read.close()
        flash('You have successfully booked!', 'success')
    return render_template('doctorbooking.html', weekdays = weekdays,timeslots = timeslots)





#----------------------------Jun En's Appointment for Patient Use---------------------------------------------
@app.route('/bookanappointment', methods=['GET', 'POST'])

def addappointment():
    appointmentform = AppointmentForm(request.form)
    db_read = shelve.open("Appointment.db", "r")
    appointment = db_read['Appointment']
    db_read = shelve.open("users.db", "r")
    user = db_read['users']
    plist = []
    for i in user:
        patient_info = user[i]
        print(patient_info.getname())
        if patient_info.getname() == session['name']:
            plist.append(patient_info)
    print(plist)

    mon_time = []
    tue_time = []
    wed_time = []
    thu_time = []
    fri_time = []
    sat_time = []

    for id in appointment:
        patient = appointment.get(id)
        if patient.get_reserved_day() == "Mon":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            mon_time.append(ts)

        elif patient.get_reserved_day() == "Tue":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            tue_time.append(ts)

        elif patient.get_reserved_day() == "Wed":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            wed_time.append(ts)
        elif patient.get_reserved_day() == "Thu":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            thu_time.append(ts)
        elif patient.get_reserved_day() == "Fri":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            fri_time.append(ts)
        elif patient.get_reserved_day() == "Sat":
            ts = TimeSlot(patient.get_reserved_date(), patient.get_reserved_time())
            sat_time.append(ts)

    db_read = shelve.open("Appointment.db")
    doctor_db = shelve.open("doctor.db")
    monday = doctor_db["Monday"]
    tuesday = doctor_db["Tuesday"]
    wednesday = doctor_db["Wednesday"]
    thursday = doctor_db["Thursday"]
    friday = doctor_db["Friday"]
    saturday = doctor_db["Saturday"]
    try:
        appointmentlist = db_read["Appointment"]

    except:
        appointmentlist = {}


    if request.method == "POST":


        if appointmentform.reservation_date.data < datetime.now().date():
            flash("You cannot book dates in the past")
            return redirect('/bookanappointment')



        else:
            reserved_date = appointmentform.reservation_date.data
            reserved_day = reserved_date.weekday()

            if reserved_day == 0:
                reserved_day = "Mon"

                if appointmentform.reservation_time.data in monday.get_time():
                    if appointmentform.reservation_time.data in mon_time:
                        flash("This timeslot has been taken!")
                        return redirect('/bookanappointment')
                    else:
                        for i in mon_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')

                            flash("Successfully booked!")

                else:
                    flash("This timeslot is not available ")
                    return redirect('/bookanappointment')

            elif reserved_day == 1:
                reserved_day = "Tue"


                if appointmentform.reservation_time.data in tuesday.get_time():
                    if appointmentform.reservation_time.data in tue_time:

                      flash("This timeslot has been taken!")
                      return redirect('/bookanappointment')
                    else:
                        for i in tue_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                print(appointmentform.reservation_date.data)
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')


                else:
                    flash('This timeslot is not available')
                    return redirect('/bookanappointment')

            elif reserved_day == 2:
                reserved_day = "Wed"

                if appointmentform.reservation_time.data in wednesday.get_time():
                    if appointmentform.reservation_time.data in wed_time:
                        flash("This timeslot has been taken!")
                        return redirect('/bookanappointment')
                    else:

                        for i in wed_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                print(appointmentform.reservation_date.data)
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')


                else:
                    flash("This timeslot is not available")
                    return redirect('/bookanappointment')

            elif reserved_day == 3:
                reserved_day = "Thu"

                if appointmentform.reservation_time.data in thursday.get_time():
                    if appointmentform.reservation_time.data in thu_time:
                        flash("This timeslot has been taken!")
                        return redirect('/bookanappointment')
                    else:
                        for i in thu_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                print(appointmentform.reservation_date.data)
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')




            elif reserved_day == 4:
                reserved_day = "Fri"

                if appointmentform.reservation_time.data in friday.get_time():
                    if appointmentform.reservation_time.data in fri_time:
                        flash("This timeslot has been taken!")
                        return redirect('/bookanappointment')
                    else:
                        for i in fri_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                print(appointmentform.reservation_date.data)
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')





            elif reserved_day == 5:
                reserved_day = "Sat"
                if appointmentform.reservation_time.data in saturday.get_time():
                    if appointmentform.reservation_time.data in sat_time:
                        flash("This timeslot has been taken!")
                        return redirect('/bookanappointment')
                    else:
                        for i in sat_time:
                            if i.get_date() == appointmentform.reservation_date.data:
                                print(appointmentform.reservation_date.data)
                                if i.get_time() == appointmentform.reservation_time.data:
                                    flash('This timeslot has been taken!')
                                    return redirect('/bookanappointment')


            elif reserved_day == 6:
                reserved_day = "Sun"

                if reserved_day == "Sun":
                    flash("Sorry, We are closed on Sunday!")
                    return redirect('/bookanappointment')





        appointment_type = appointmentform.appointment_type.data
        reserved_time = appointmentform.reservation_time.data
        app = AppointmentDetails(reserved_date, appointment_type, reserved_time,reserved_day)
        app.get_status()
        app.get_patient_name()

        id = len(appointmentlist) + 1

        app.set_id(id)

        appointmentlist[id] = app


        db_read["Appointment"] = appointmentlist
        db_read.close()




        return redirect(url_for('myappointment'))
    return render_template("bookanappointment.html", aform=appointmentform , title="Book An Appointment", name =  session['name'], list = appointmentlist, plist = plist )


@app.route('/myappointment', methods=['GET', 'POST'])
def myappointment():
    db_read = shelve.open("Appointment.db", "r")
    appointment = db_read['Appointment']
    list = []
    count  = 0 
    for id in appointment:
     patient = appointment.get(id)
     if patient.get_patient_name() == session['name']:
         count += 1 
         list.append(patient)
        
    print(list)


    db_read.close()
    return render_template("myappointment.html", title="My Appointment", name = session['name'],list=list,count = count )


@app.route('/appointment')
def appointmentsc():
    return render_template("appointment.html")
@app.route('/inventoryoverview')
def inventoryoverview():
    return render_template("inventoryoverview.html")
@app.route('/healthnotesoverview')
def healthnotesoverview():
    return render_template('healthnotesoverview.html')
@app.route('/eregister')
def eregister():
    return render_template('eregister.html')
@app.route('/receipt')
def ereceipt():
    return render_template('receipt.html')


#----------- Jun En's About Us Page ------------------------------
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html", title="About Us")




#======== ZX DOMAIN===========================================================================================
# ZX DOMAIN




#email attemppts
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'serveit1801@gmail.com'
app.config['MAIL_PASSWORD'] = 'IT1801@NYP'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/barchart', methods=['GET', 'POST'])
def barchart():
    fig = plt.figure(figsize=(7,5))

    db_read = shelve.open("Appointment.db","r")
    appointment = db_read['Appointment']
    print(appointment)

    for i in appointment:
        print(appointment[i].get_reserved_day())




    monday_count = 0
    tuesday_count = 0
    wednesday_count =0
    thursday_count = 0
    friday_count = 0
    saturday_count = 0
    sunday_count = 0
    total = 0




    for id in appointment:
        patient = appointment.get(id)
        if patient.get_reserved_day() == "Mon":
            monday_count += 1
            total += 1
        elif patient.get_reserved_day() == "Tue":
            tuesday_count +=1
            total += 1
        elif patient.get_reserved_day() == "Wed":
            wednesday_count += 1
            total += 1
        elif patient.get_reserved_day() == "Thu":
            thursday_count += 1
            total += 1
        elif patient.get_reserved_day() == "Fri":
            friday_count += 1
            total += 1
        elif patient.get_reserved_day() == "Sat":
            saturday_count += 1
            total += 1
        elif patient.get_reserved_day() == "Sun":
            sunday_count += 1
            total += 1


    names = ["Monday","Tuesday","Wednesday","Friday","Saturday","Sunday"]
    counts = [monday_count,tuesday_count,wednesday_count,thursday_count,friday_count,saturday_count,sunday_count]
    positions = [0,1,2,3,4,5,6]
    plt.bar(positions,counts,width=0.5,color="#32c69a")
    plt.xticks(positions,names)
    plt.show()
    fig.savefig('Appointmentpeakhours.png')
    db_read.close()
    return render_template("barchart.html", title="BarChart", chart=plt,total = total)

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = plt.figure(figsize=(7, 5))

    db_read = shelve.open("Appointment.db", "r")
    appointment = db_read['Appointment']
    print(appointment)

    for i in appointment:
        print(appointment[i].get_reserved_day())

    monday_count = 0
    tuesday_count = 0
    wednesday_count = 0
    thursday_count = 0
    friday_count = 0
    saturday_count = 0
    sunday_count = 0

    for id in appointment:
        patient = appointment.get(id)
        if patient.get_reserved_day() == "Mon":
            monday_count += 1
        elif patient.get_reserved_day() == "Tue":
            tuesday_count += 1
        elif patient.get_reserved_day() == "Wed":
            wednesday_count += 1
        elif patient.get_reserved_day() == "Thu":
            thursday_count += 1
        elif patient.get_reserved_day() == "Fri":
            friday_count += 1
        elif patient.get_reserved_day() == "Sat":
            saturday_count += 1
        elif patient.get_reserved_day() == "Sun":
            sunday_count += 1

    names = ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday", "Sunday"]
    counts = [monday_count, tuesday_count, wednesday_count, thursday_count, friday_count, saturday_count, sunday_count]
    positions = [0, 1, 2, 3, 4, 5, 6]
    plt.bar(positions, counts, width=0.5, color="#32c69a")
    plt.xticks(positions, names)
    plt.show()
    fig.savefig('Appointmentpeakhours.png')
    db_read.close()
    return fig


@app.route('/invgraph')
def invgraph():
    fig= plt.figure(figsize=(7,5))
    db_read=shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    ok=[]

    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medicine":
            if medicalitems.get(medid).get_status() == "A":
                ok.append(medicalitems.get(medid))
    a=len(ok)
    plt.figure(figsize=(7,5))
    print("hi")
    print(a)

    labels = []
    values=[]
    position=[]
    for i in range(a):
        position.append(i)
    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medicine":
            if medicalitems.get(medid).get_status() == "A":
                labels.append(medicalitems.get(medid).get_name())
                values.append(medicalitems.get(medid).get_qty())
    plt.bar(position,values,width=0.5)
    plt.xticks(position,labels)
    plt.ylabel("Quantity")
    plt.xlabel("Medical item")
    plt.show()
    fig.savefig('invgraph.png')
    db_read.close()
    return redirect(url_for("inv"))
    return render_template("invgraph.html", title="Invgraph", chart=plt)

@app.route('/invplot.png')
def invplot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_invfigure():
    db_read = shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    ok = []
    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medicine":
            if medicalitems.get(medid).get_status() == "A":
                ok.append(medicalitems.get(medid))
    a = len(ok)
    plt.figure(figsize=(7, 5))
    print("hi")
    print(a)

    labels = []
    values = []
    position = []
    for i in range(a):
        position.append(i)
    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medicine":
            if medicalitems.get(medid).get_status() == "A":
                labels.append(medicalitems.get(medid).get_name())
                values.append(medicalitems.get(medid).get_qty())
    plt.bar(position, values, width=0.5)
    plt.xticks(position, labels)
    plt.interactive(False)
    plt.ylabel("Quantity")
    plt.xlabel("Medical item")
    plt.show()
    fig.savefig('invgraph.png')
    db_read.close()
    return fig


@app.route('/medtoolsinvgraph')
def medtoolsinvgraph():
    db_read=shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    ok=[]
    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medical tools":
            if medicalitems.get(medid).get_status() == "A":
                ok.append(medicalitems.get(medid))
    a=len(ok)
    plt.figure(figsize=(7,5))
    print("hi")
    print(a)




    labels = []
    values=[]
    position=[]
    for i in range(a):
        position.append(i)
    for medid in medicalitems:
        if medicalitems.get(medid).get_type().lower() == "medicine":
            if medicalitems.get(medid).get_status() == "A":
                labels.append(medicalitems.get(medid).get_name())
                values.append(medicalitems.get(medid).get_qty())
    plt.bar(position,values,width=0.5)
    plt.xticks(position,labels)
    plt.interactive(False)
    plt.ylabel("Quantity")
    plt.xlabel("Medical item")
    plt.show(block=True)
    return redirect(url_for("medtools"))



class SearchItems(Form):
    item_name = StringField('Search', validators=[DataRequired()])

@app.route('/inventory' ,methods=['GET', 'POST'])
def inv():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))


    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword=form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory",form=form, medicalitems=searchedinv)

        return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("inventory.html", title="Inventory",form=form, medicalitems=list)




@app.route('/sortbyname/inventory',methods=['GET', 'POST'])
def invsortbyname():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_name().lower())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("invsortbyname.html", title="Inventory",form=form, medicalitems=list)



@app.route('/sortbynamedesc/inventory',methods=['GET', 'POST'])
def invsortbynamedesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_name().lower(), reverse=True)

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("invsortbynamedesc.html", title="Inventory",form=form, medicalitems=list)


@app.route('/sortbytype/inventory',methods=['GET', 'POST'])
def invsortbytype():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_type())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("invsortbyname.html", title="Inventory", form=form, medicalitems=list)

    return render_template("invsortbytype.html", title="Inventory",form=form, medicalitems=list)


@app.route('/sortbyprice/inventory',methods=['GET', 'POST'])
def invsortbyprice():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_price())
    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("invsortbyprice.html", title="Inventory",form=form, medicalitems=list)


@app.route('/sortbypricedesc/inventory',methods=['GET', 'POST'])
def invsortbypricedesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_price(),reverse=True)
    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("invsortbypricedesc.html", title="Inventory",form=form, medicalitems=list)


@app.route('/sortbyqty/inventory',methods=['GET', 'POST'])
def invsortbyqty():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_qty())
    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("invsortbyqty.html", title="Inventory",form=form, medicalitems=list)

@app.route('/sortbyqtydesc/inventory',methods=['GET', 'POST'])
def invsortbyqtydesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_qty(), reverse=True)
    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("invsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("invsortbyqtydesc.html", title="Inventory",form=form, medicalitems=list)


@app.route('/medtools',methods=['GET', 'POST'])
def medtools():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))

    exceed = "norm"
    lowed = "norm"
    for medicalitem in list:
        if medicalitem.get_qty() > medicalitem.get_max() and medicalitem.get_status == 'A':
            exceed = "exceeded"
            print("exceeded")
        if medicalitem.get_qty() < medicalitem.get_min() and medicalitem.get_status == 'A':
            lowed = "low"
            print("low")

    if exceed == "exceeded":
        msg = Message('Dear staff, please note that there is stock excess on medical tools',
                      sender='serveit1801@gmail.com', recipients=['soh.zixiang01@gmail.com'])
        msg.body = "do remember to not order any more stock and update the quantity on the website!"
        mail.send(msg)
        flash('Inventory has excess stock,Email has been sent', 'success')

    if lowed == "low":
        msg = Message('Dear staff, please note that there is low stock on medical tools',
                      sender='serveit1801@gmail.com', recipients=['soh.zixiang01@gmail.com'])
        msg.body = "do remember to order more stock and update the quantity on the website!"
        mail.send(msg)
        flash('Inventory is low on stock, Email has been sent', 'success')

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtools.html", title="Medical Tools",form=form, medicalitems=list)

@app.route('/sortbyname/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbyname():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_name())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)

    return render_template("medtoolsinvsortbyname.html", title="Inventory",form=form, medicalitems=list)

@app.route('/sortbynamedesc/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbynamedesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_name(),reverse=True)

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbynamedesc.html", title="Inventory",form=form, medicalitems=list)






@app.route('/sortbytype/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbytype():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_type())
    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbytype.html", title="Medical Tools",form=form, medicalitems=list)


@app.route('/sortbyprice/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbyprice():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_price())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbyprice.html", title="Medical Tools",form=form, medicalitems=list)


@app.route('/sortbypricedesc/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbypricedesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_price(),reverse=True)

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbypricedesc.html", title="Medical Tools",form=form, medicalitems=list)


@app.route('/sortbyqty/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbyqty():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_qty())

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbyqty.html", title="Medical Tools",form=form, medicalitems=list)


@app.route('/sortbyqtydesc/medtools',methods=['GET', 'POST'])
def medtoolsinvsortbyqtydesc():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []
    type_list = []
    sorted_list=[]
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
        list.sort(key=lambda x: x.get_qty(),reverse=True)

    form = SearchItems(request.form)
    if request.method == 'POST' and form.validate():
        keyword = form.item_name.data
        searchedinv = []
        db_read = shelve.open("medicalitems.db")
        medicalitems = db_read["medicalitems"]
        dict = medicalitems
        for k in dict:
            if dict[k].get_name().upper().find(keyword.upper()) > -1 or dict[k].get_name().lower().find(
                    keyword.lower()) > -1:
                searchedinv.append(dict[k])
                return render_template("medicaltoolsearched.html", title="Inventory", form=form, medicalitems=searchedinv)


    return render_template("medtoolsinvsortbyqtydesc.html", title="Medical Tools",form=form, medicalitems=list)



@app.route('/excess')
def excess():

    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))

    return render_template("excess.html", title="Excess Inventory", medicalitems=list)


@app.route('/low')
def low():
    db_read = shelve.open("medicalitems.db")

    medicalitems = db_read["medicalitems"]

    print(medicalitems)

    list = []

    for medid in medicalitems:
        list.append(medicalitems.get(medid))

    return render_template("low.html", title="Low Inventory", medicalitems=list, )


@app.route('/delete_item/<int:id>', methods=['POST'])
def delete_item(id):
    db_read = shelve.open("medicalitems.db")

    try:
        list = db_read["medicalitems"]
        print("id, ", id)
        print("list before: ", list)

        ##del pList[id]
        list[id].set_status("I")

        print(list)
        db_read["medicalitems"] = list
        db_read.close()

        flash('Item deleted', 'success')

        return redirect(url_for('inv'))

    except:
        flash('Item Not Deleted', 'danger')
        return redirect(url_for('inv'))

class AddItemsqty(Form):
    item_name = StringField('Name', validators=[DataRequired("Please enter a name")])
    item_price = IntegerField('Price', validators=[DataRequired("Please enter a valid number for price")])
    item_type = SelectField('Type',choices=[('medicine', 'Medicine'), ('Medical Tools', 'Medical Tools'), ],validators=[DataRequired('Please select a type')])
    item_qty = IntegerField('Quantity', validators=[DataRequired("Please enter a valid number for quantity")])
    item_max = IntegerField('Maximum Threshhold', validators=[DataRequired("Please enter a valid number for maximum threshhold")])
    item_min = IntegerField('Minimum Threshhold', validators=[DataRequired("Please enter a valid number for minimum threshhold")])
    item_brief = StringField('Brief Description', validators=[DataRequired("Please enter a brief description")])
    item_description = StringField('Description', validators=[DataRequired("Please enter a description")])
    item_image = FileField('Image')
    item_qty_added=IntegerField('Add Qty: ',default=0)
    item_qty_removed= IntegerField('Remove Qty: ', default=0)



@app.route('/item/update/<int:id>/', methods=['GET', 'POST'])
def update_item(id):
    form = AddItemsqty(request.form)
    db_read = shelve.open("medicalitems.db")
    try:
        list = db_read["medicalitems"]
        if request.method == 'POST' and form.validate():
            briefdesc = form.item_brief.data
            desc = form.item_description.data
            name = form.item_name.data
            price = form.item_price.data
            max = form.item_max.data
            min = form.item_min.data
            type = form.item_type.data
            qty = form.item_qty.data +form.item_qty_added.data - form.item_qty_removed.data
            file_path = form.item_image.data
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                file_path=list.get(id).get_fileurl()
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                print(app.config['UPLOADS_PATH'])
                print(filename)
                file.save(os.path.join(app.config['UPLOADS_PATH'], filename))
                # file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER_MEDTOOLS'], filename))
                file_path = UPLOAD_FOLDER + filename
                print(file_path)
            mi = MedicalItems(name, price, type, qty, max, min, briefdesc, desc, file_path)
            mi.set_id(id)

            list[id] = mi
            db_read["medicalitems"] =list
            db_read.close()
            print("done")
            flash('Item updated Sucessfully.', 'success')
            return redirect(url_for('item_description', id=id))
        else:
            print("in retrieving")
            list = db_read["medicalitems"]
            print(list)
            eachitem = list.get(id)
            form.item_name.data = eachitem.get_name()
            form.item_price.data = eachitem.get_price()
            form.item_type.data = eachitem.get_type()
            form.item_max.data = eachitem.get_max()
            form.item_min.data = eachitem.get_min()
            form.item_qty.data = eachitem.get_qty()
            form.item_image.data = eachitem.get_fileurl()
            print(eachitem.get_fileurl())
            form.item_description.data = eachitem.get_desc()
            form.item_brief.data = eachitem.get_briefdesc()

    except:
        print("in ")
        file_path= list.get(id).get_fileurl()
        mi = MedicalItems(name, price, type, qty, max, min, briefdesc, desc, file_path)
        mi.set_id(id)
        list[id] = mi
        db_read["medicalitems"] = list
        db_read.close()
        print("done")
        flash('Item updated Sucessfully.', 'success')
        return redirect(url_for('item_description', id=id))

    return render_template('updateitem.html', form=form, medicalitems=list.get(id), id=id)

class QtyChange(Form):
    item_qty_added = IntegerField('Quantity to add',default=0)
    item_qty_removed = IntegerField('Quantity to remove',default=0)

@app.route('/item/description/<int:id>/', methods=['GET', 'POST'])
def item_description(id):

    db_read = shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    print(medicalitems)
    for key in medicalitems:
        if key==id:
            item=medicalitems[key]

    form = QtyChange(request.form)
    if request.method == 'POST' and form.validate():
        for key in medicalitems:
            if key == id:
                print("hi")
                item = medicalitems[key]
        qty_added=form.item_qty_added.data
        #qty_removed=form.item_qty_removed.data

        item.add_qty(int(qty_added))
        print(item.get_qty())
        #item.remove_qty(int(qty_removed))
        medicalitems[id] = item
        db_read["medicalitems"]=medicalitems
        db_read.close()
    return render_template("itemdesc.html", form=form, title="description", medicalitems=item)

class MedicalItems:
    def __init__(self, name, price, type, qty, max, min, briefdesc, desc, fileurl):
        self.__id=""
        self.__name = name
        self.__price = price
        self.__type = type
        self.__qty = qty
        self.__max = max
        self.__min = min
        self.__briefdesc = briefdesc
        self.__desc = desc
        self.__fileurl = fileurl
        self.__status = 'A'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_type(self):
        return self.__type

    def get_qty(self):
        return self.__qty

    def get_max(self):
        return self.__max

    def get_min(self):
        return self.__min

    def get_briefdesc(self):
        return self.__briefdesc

    def get_desc(self):
        return self.__desc

    def get_fileurl(self):
        return self.__fileurl

    def get_status(self):
        return self.__status

    def set_id(self,id):
        self.__id=id

    def set_name(self,newName):
        self.__name=newName

    def set_price(self,newPrice):
        self.__price=newPrice

    def set_type(self,newType):
        self.__type=newType

    def set_qty(self,newQty):
        self.__qty=newQty

    def set_max(self,newMax):
        self.__max=newMax

    def set_min(self,newMin):
        self.__min=newMin


    def set_briefdesc(self,newBrief):
        self.__briefdesc=newBrief

    def set_desc(self,newdesc):
        self.__desc=newdesc


    def set_fileurl(self,newFile):
        self.__fileurl=newFile

    def set_status(self,newStatus):
        self.__status=newStatus

    def add_qty(self,amt):
        self.__qty+=amt


    def remove_qty(self, amt):
        self.__qty-= amt


class AddItems(Form):
    item_name = StringField('Name', validators=[DataRequired("Please enter a name")],)
    item_price = IntegerField('Price', validators=[DataRequired("Please enter a valid number for price")])
    item_type = SelectField('Type',choices=[('medicine', 'Medicine'), ('Medical Tools', 'Medical Tools'), ],validators=[DataRequired("Please select item type")])
    item_qty = IntegerField('Quantity', validators=[DataRequired("Please enter a valid number for quantity")])
    item_max = IntegerField('Maximum Threshhold', validators=[DataRequired("Please enter a valid number for maximum threshhold")])
    item_min = IntegerField('Minimum Threshhold', validators=[DataRequired("Please enter a valid number for minimum threshhold")])
    item_brief = StringField('Brief Description', validators=[DataRequired("Please enter a brief description")])
    item_description = StringField('Description', validators=[DataRequired("Please enter a description of the item")])
    item_image = FileField('Image')


UPLOAD_FOLDER= '\\static\\invimage\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOADS_PATH'] = join(dirname(realpath(__file__)), 'static\\invimage\\')

#@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADS_PATH'],
                               filename)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/additem', methods=['GET', 'POST'])
def additem():
    form = AddItems(request.form)
    db_read = shelve.open("medicalitems.db")
    try:
        if request.method == 'POST' and form.validate():
            briefdesc = form.item_brief.data
            print(briefdesc)
            desc = form.item_description.data
            name = form.item_name.data
            price = form.item_price.data
            max = form.item_max.data
            min = form.item_min.data
            type = form.item_type.data
            qty = form.item_qty.data
            file_path = form.item_image.data
            file=request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print(app.config['UPLOADS_PATH'])
                print(filename)
                file.save(os.path.join(app.config['UPLOADS_PATH'], filename))
                    #file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER_MEDTOOLS'], filename))
                file_path =UPLOAD_FOLDER+filename
                print(file_path)
            mi = MedicalItems(name, price, type, qty, max, min, briefdesc, desc, file_path)

            db_read = shelve.open("medicalitems.db")

            try:
                itemList = db_read["medicalitems"]
            except:
                itemList = {}

            id = len(itemList) + 1
            mi.set_id(id)

            itemList[id] = mi

            db_read["medicalitems"] = itemList

            db_read.close()

            flash('Item added Sucessfully.', 'success')
            return redirect(url_for('inv'))
    except:
        file_path = ""
        mi = MedicalItems(name, price, type, qty, max, min, briefdesc, desc, file_path)
        try:
            itemList = db_read["medicalitems"]
        except:
            itemList = {}

        id = len(itemList) + 1
        mi.set_id(id)

        itemList[id] = mi

        db_read["medicalitems"] = itemList

        db_read.close()

        flash('Item added Sucessfully.', 'success')
        return redirect(url_for('inventoryoverview'))
    return render_template("additem.html", form=form, title="Add item")

# ZX ENDS HERE

#RYAN STARTS HERE
class Search_reg(Form):
    item_name = StringField('Search', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()], default=0)
    delete_quantity = IntegerField('Delete', validators=[DataRequired()], default=0)
    nric = StringField('NRIC',validators=[DataRequired(), Length(9)], default='')

class Receipt:
    def __init__(self, itemname, itemprice, itemqty, nric):
        self.itemname = itemname
        self.itemprice = itemprice
        self.itemqty = itemqty
        self.nric = nric

@app.route('/Payment' , methods=['GET',"POST"])

def search():
    searchedinv = []
    form = Search_reg(request.form)
    print(id)
    keyword = form.item_name.data
    db_read = shelve.open("medicalitems.db")
    medical_items = db_read["medicalitems"]
    dict = medical_items
    for k in dict:
        if dict[k].get_name().find(keyword) > -1:
            searchedinv.append(dict[k])
    if searchedinv != []:
        flash("This item has been found")
        print("item found")
    else:
        flash("This item does not exist")
    return render_template("blank.html", title="Payment", form=form, medical_items=searchedinv)


@app.route('/addqty/<int:id>/', methods=['POST', 'GET'])
def addqty(id):
    form = Search_reg(request.form)
    db_read = shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    db_add = shelve.open("addeditems")
    print(medicalitems)
    list = []
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
    if request.method == "POST":
        try:
            added = db_add["added"]
        except:
            added = {}
        print("Still working")
        medicalitems = db_read["medicalitems"]
        for key in medicalitems:
            if medicalitems[key].get_id() == id:
                print("matched", id)
                item = medicalitems.get(key)
                print(item.get_name())
                nric = form.nric.data
                r = Receipt(item.get_name(), item.get_price(), form.item_name.data, nric)
                added[r.nric + str(len(added))] = r
        db_add["added"] = added
        addedlist = []
        for a in added:
            addedlist.append(added.get(a))
        print(db_add["added"])
        return render_template("blank2.html", form=form, medicalitems=list, iadded=addedlist)
    return render_template("blank2.html", form=form, medicalitems=list)

@app.route('/addqty/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
    form = Search_reg(request.form)
    nric = form.nric.data
    db_read = shelve.open("added.db")
    db_read_two = shelve.open("medicalitems.db")
    medicalitems = db_read_two["medicalitems"]
    for key in medicalitems:
        if medicalitems[key].get_id() == id:
            print("matched", id)
            item = medicalitems.get(key)
    try:
        added = db_read["added"]
    except:
        added = {}
    print(added)
    if added != {}:
        del added[nric + str(len(added))]
    else:
        pass
    return redirect(url_for("addqty", id=id))

@app.route('/E-register/image')
def image():
    form = Search_reg(request.form)
    render_template("payment.html", form=form)


def get_receipt(receipt):
    return receipt

@app.route('/viewreceipt', methods=['get','post'])
def receipt():
    form = Search_reg(request.form)
    db_read = shelve.open("medicalitems.db")
    medicalitems = db_read["medicalitems"]
    db_add = shelve.open("addeditems")
    print(medicalitems)
    list = []
    for medid in medicalitems:
        list.append(medicalitems.get(medid))
    if request.method == "POST":
        try:
            added = db_add["added"]
        except:
            added = {}
        print("Still working")
        medicalitems = db_read["medicalitems"]
        for key in medicalitems:
            if medicalitems[key].get_id() == id:
                print("matched", id)
                item = medicalitems.get(key)
                print(item.get_name())
                nric = form.nric.data
                itemqty = form.quantity.data
                r = Receipt(item.get_name(), item.get_price(), itemqty, nric)
                added[r.nric + str(len(added))] = r
        db_add["added"] = added
        addedlist = []
        for a in added:
            addedlist.append(added.get(a))
        print(db_add["added"])
        return render_template("blank3.html", form=form, medicalitems=list, iadded=addedlist)
    return render_template("blank3.html", form=form, medicalitems=list)

#RYAN ENDS HERE

#-------------- JunEn's Feedback ---------------------------

@app.route('/delete_feedback/<int:id>', methods=['POST'])
def delete_feedback(id):
    db_read = shelve.open("feedback.db")

    try:
        List = db_read["feedback"]
        print("id, ", id)
        print("List before: ", List)

        List.pop(id)

        print(List)
        db_read["feedback"] = List
        db_read.close()

        flash('Appointment Deleted', 'success')

        return redirect(url_for('viewfeedback'))

    except:
        flash('Feedback Not Deleted', 'danger')
        return redirect(url_for('feedback'))

class FeedbackForm(Form):

    Topic = StringField('Topic', validators=[DataRequired()])
    Email = StringField('Email Address', validators=[DataRequired()])
    Message = TextAreaField('Message ')

class Feedback:
    def __init__(self,topic,email,message):
        self.__topic = topic
        self.__email = email
        self.__message = message
        self.__id = " "

    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id


    def get_topic(self):
        return self.__topic
    def get_email(self):
        return self.__email
    def get_message(self):
        return self.__message

    def set_topic(self,topic):
        self.__topic = topic
    def set_email(self,email):
        self.__email = email
    def set_message(self,message):
        self.__message = message




@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm(request.form)

    db_read = shelve.open("feedback.db")

    try:
        feedbackList = db_read["feedback"]
    except:
        feedbackList = {}

    if request.method == 'POST' and form.validate():
            topic  = form.Topic.data
            email = form.Email.data
            print(email)
            message = form.Message.data
            msg = Message(topic,
                          sender=("Admin", 'test@test.com'), recipients=['serveit1801@gmail.com'], cc=[email])
            msg.body = message
            mail.send(msg)
            flash('Inventory has excess stock,Email has been sent', 'success')

            feedback = Feedback(topic,email,message)


            id = len(feedbackList) + 1

            feedback.set_id(id)

            feedbackList[id] = feedback

            db_read["feedback"] = feedbackList

            db_read.close()
            return redirect(url_for('summary'))
    return render_template('feedback.html', form=form, title="Contact")


@app.route('/viewfeedback')
def viewfeedback():
    db_read = shelve.open("feedback.db", "r")
    feedback = db_read['feedback']
    list = []
    for id in feedback:
        list.append(feedback.get(id))
    db_read.close()
    return render_template('viewfeedback.html',feedback = list )


@app.route('/summary')
def summary():
    return render_template('summary.html')



#Guest HTML Page..
@app.route('/welcome', methods=['GET', 'POST'])
def guest():
    return render_template("guesthome.html")
# Jun En Doctor's Appointment



#============================================ Wilson ===============================================
#===================== =========== ========= ======= ============== =========== ======== ===========




if __name__ == '__main__':
    app.run(debug=True)