import sys
import re
from PyQt5.uic import loadUi ,loadUiType
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import os
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import cv2
from datetime import date
from datetime import datetime
import numpy as np
import pandas as pd
from PIL import Image
import pyqtcss
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array
######
root_dir = os.getcwd()
# Load Face Detection Model
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
# Load Anti-Spoofing Model graph
json_file = open('antispoofing_models/antispoofing_model.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load antispoofing model weights 
model.load_weights('antispoofing_models/antispoofing_model.h5')
print("Model loaded from disk")
######


######################################################## StartUp window #############################################
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("./GUI_SCREENS/WelcomeScreen - Copy.ui",self) # load the GUI file
        self.login.clicked.connect(self.gotologin) # event handel for button login 
        self.setWindowTitle("Welcome Screen")
        #self.setGeometry(0,0,1487,973)
        self.setFixedWidth(371)
        self.setFixedHeight(661)
        self.setGeometry(50,50,371,661) #set fixed size for window 
    
    def gotologin(self):

        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # showing the next widget (screen) that in the above line (loginScreen)
        widget.setFixedWidth(548)
        widget.setFixedHeight(755)
        widget.setGeometry(50,50,1538,926)
        widget.setWindowTitle("Login Screen")



######################################################## StartUpWondow #############################################

######################################################## LoginScreen #############################################
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("./GUI_SCREENS/login - Copy.ui",self)
        self.setFixedWidth(548)
        self.setFixedHeight(755)
        self.setGeometry(50,50,548,755)

        #self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.clicked.connect(self.loginfunction)
        self.CancelButton.clicked.connect(self.goBack)

        self.setWindowTitle("Login")

        #self.mainwin=MainWin()


    def loginfunction(self):

        self.user = self.user_line.text()

        self.password = self.pass_line.text()


        if len(self.user)==0 or len(self.password)==0:
            self.error.setText("Please input all fields.")

        else:
            
            conn = sqlite3.connect("./DataBaseTabletest.db")
            cur = conn.cursor()

            query = 'SELECT User_Password FROM Users WHERE User_Name =\''+self.user+"\'"
            cur.execute(query)
            query_result  = cur.fetchone()
            #print(result_pass)
           # result_pass = query_result[0]

            if query_result is not None:
                if query_result[0] == self.password:
                    QMessageBox.about(self, "alert", "Successfully logged in \n"+self.user)
                    print("Successfully logged in.")
                    self.gotomaintest()
                else:
                    self.error.setText("Invalid username or password")
            else:        
                self.error.setText("Invalid username or password")
                


    def gotomaintest(self):
        mainwint=MainWin()
        widget.addWidget(mainwint)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")

        
    def goBack(self):
        back2wle = WelcomeScreen()
        widget.addWidget(back2wle)
        widget.setCurrentIndex(widget.currentIndex()+1)  
        widget.setFixedWidth(371)
        widget.setFixedHeight(661)
        widget.setGeometry(50,50,371,661)
        widget.setWindowTitle("Welcome Screen")


######################################################## LoginScreen #############################################

######################################################## NewEmployeeScreen #############################################
class NewEmployeeScreen(QDialog):
    def __init__(self):
        super(NewEmployeeScreen, self).__init__()
        loadUi("./GUI_SCREENS/NewEmployeeRegistration - Copy.ui",self)
        #self.setupUi(self)
        self.handel_buttons()
        self.handel_Lines()
        self.handel_photo()
        self.handel_Ui()

        
        self.capture_Emp_ID=''  

        self.getCompayinfo()  

        self.firstname1=self.first_line.text()
        self.middlename1=self.middle_line.text()
        self.lastname1=self.last_line.text()
        self.gender=self.radioButton.isChecked()
        self.address=self.address_line.text()

        self.DOB=self.dateEdit.date()
        self.var_name = self.DOB.toPyDate()


    def handel_buttons(self):
        self.save_button.clicked.connect(self.DB)
        self.save_button.clicked.connect(self.handel_Lines)
        self.cancel_button.clicked.connect(self.handel_Lines)
        self.capture_button.clicked.connect(self.Caputer_Images)
        self.BackButton.clicked.connect(self.BacktoMain)


    def handel_photo(self):
        self.addphoto_button.clicked.connect(self.BrowseImage)

    def handel_Lines(self):
        self.first_line.clear()
        self.middle_line.clear()
        self.last_line.clear()
        self.address_line.clear()
        self.phone_line.clear()
        self.email_line.clear()
        

        

    def handel_Ui(self):
        self.setFixedWidth(1538)
        self.setFixedHeight(926)
        self.setGeometry(50,50,1538,926)   

    def genID(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()
           
            for row in cursor.execute('SELECT Emp_ID FROM Employees ORDER BY Emp_ID DESC LIMIT 1;'):
                #print(row)
                printIDint=int(row[0])
                printIDint+=1
                printIDstr=str(printIDint)
                self.capture_Emp_ID=printIDstr   
            #self.IDlable.setText(printIDstr)
            #self.lcdNumber.display(printIDint)
            
            #QMessageBox.about(self, "alert", "Employee Added its ID"+self.capture_Emp_ID)

    def getCompayinfo(self):

        conn = sqlite3.connect("./DataBaseTabletest.db")
        conn.text_factory=str
        cursor = conn.cursor()
            
        cursor.execute('SELECT Dept_Name FROM DepartmentsTable;')
        dept_names=cursor.fetchall()
        dept_names1=[r[0] for r in dept_names]

        cursor.execute('SELECT JobDesc FROM JobTittle;')
        JobTitles=cursor.fetchall()
        JobTitles1=[r[0] for r in JobTitles]

        cursor.execute('SELECT AttendanceDesc FROM Attendance_Schemes_Table;')
        attendanceSchem=cursor.fetchall()
        attendanceSchem1=[r[0] for r in attendanceSchem]

        cursor.execute('SELECT Category FROM AccessScheme;')
        accesSchem=cursor.fetchall()
        accesSchem1=[r[0] for r in accesSchem]

        #print(dept_names[1])
        #print(dept_names1)


        deptlen=len(dept_names1)
        joblen=len(JobTitles1)
        attendanceSchLen=len(attendanceSchem1)
        accesSchemLen=len(accesSchem1)
        
        if dept_names1 == []:
            print("you cant add New Employee you must First ADD Company Dept's")
            self.E2.setText("Go To Company Information To Add Dept")
            self.save_button.setEnabled(False)   
        else:
            count=0
            for i in range (deptlen):
                self.dep_drop.addItem(dept_names1[count])
                count+=1


        if  JobTitles == []:
            print("you cant add New Employee you must First ADD Company Job Titles's")
            self.E2.setText("Go To Company Information To Add Job Tiltle")
            self.save_button.setEnabled(False)     
        else:
            count=0
            for i in range (joblen):
                self.job_drop.addItem(JobTitles1[count])
                count+=1      

        if attendanceSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company attendance Schem")
            self.E2.setText("Go To Company Information To Add attendance Schem") 
            self.save_button.setEnabled(False)     
        else:
            count=0 
            for i in range (attendanceSchLen):
                self.attend_drop.addItem(attendanceSchem1[count])
                count+=1    

        if accesSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company Access Schem")  
            self.E2.setText("Go To Company Information To Add Access Schem") 
            self.save_button.setEnabled(False)      
        else:
            count=0 
            for i in range (accesSchemLen):
                self.access_drop.addItem(accesSchem1[count])
                count+=1    

         

    def DB(self):
            conn = sqlite3.connect("./DataBaseTabletest.db")
            conn.text_factory=str
            cursor = conn.cursor()
            
            self.firstname1=self.first_line.text()
            self.middlename1=self.middle_line.text()
            self.lastname1=self.last_line.text()
            self.gender=self.radioButton.isChecked()
            self.address=self.address_line.text()
            self.DOB=self.dateEdit.date()
            self.var_name = self.DOB.toPyDate()

            self.dep=self.dep_drop.currentText()
            self.jobTitle=self.job_drop.currentText()
            self.attendSch=self.attend_drop.currentText()
            self.accessCat=self.access_drop.currentText()

            #cursor.execute('SELECT Category FROM AccessScheme;')
            #accesSchem=cursor.fetchall()
            #accesSchem1=[r[0] for r in accesSchem]

            dep_query = 'SELECT Dept_ID FROM DepartmentsTable WHERE Dept_Name =\''+self.dep+"\'"
            cursor.execute(dep_query)
            dep_query_result  = cursor.fetchone()
           # dep_query_result_str=[r[0] for r in dep_query_result]

            Job_query = 'SELECT Emp_Job_ID FROM JobTittle WHERE JobDesc =\''+self.jobTitle+"\'"
            cursor.execute(Job_query)
            Job_query_result  = cursor.fetchone()
            #Job_query_result_str=[r[0] for r in Job_query_result]

            attendSch_query = 'SELECT AttendanceSchemes_ID FROM Attendance_Schemes_Table WHERE AttendanceDesc =\''+self.attendSch+"\'"
            cursor.execute(attendSch_query)
            attendSch_query_result  = cursor.fetchone()
            #attendSch_query_result_str=[r[0] for r in attendSch_query_result]

            AccessCat_query = 'SELECT AccessSchemID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
            cursor.execute(AccessCat_query)
            AccessCat_query_result  = cursor.fetchone()
            #AccessCat_query_result_str=[r[0] for r in AccessCat_query_result]



            #cursor.fetchone()
           # Emp_info=[self.firstname1,self.middlename1,self.lastname1,self.address,self.var_name,dep_query_result[0],Job_query_result[0],attendSch_query_result[0],AccessCat_query_result[0]]
            
         #   print(cursor.execute("INSERT INTO Employees (Emp_First_Name) VALUES(?);",self.firstname1))

            #print(cursor.execute("INSERT INTO Employees (Emp_First_Name, Emp_Middle_Name, Emp_Last_Name,Emp_Address,Emp_DOB,Emp_Dpet_ID,Emp_Job_ID,Emp_Attendace_SchemeID,Emp_Access_ID) VALUES (?,?,?,?,?,?,?,?,?);",Emp_info))
            
           # NewEmployeeScreen.genID(self)

            #aa=dep_query_result[0]
            if dep_query_result is None :
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")
                self.error.setText("Please Fill the Missing Parts")

            elif dep_query_result is not None:
                Emp_info=[self.firstname1,self.middlename1,self.lastname1,self.address,self.var_name,dep_query_result[0],Job_query_result[0],attendSch_query_result[0],AccessCat_query_result[0]]

                cursor.execute("INSERT INTO Employees (Emp_First_Name, Emp_Middle_Name, Emp_Last_Name,Emp_Address,Emp_DOB,Emp_Dpet_ID,Emp_Job_ID,Emp_Attendace_SchemeID,Emp_Access_ID) VALUES (?,?,?,?,?,?,?,?,?);",Emp_info)
            for row in cursor.execute('SELECT Emp_ID FROM Employees ORDER BY Emp_ID DESC LIMIT 1;'):
                #print(row)
                printIDint=int(row[0])
                #printIDint+=1
                printIDstr=str(printIDint)
                self.capture_Emp_ID=printIDstr  
                QMessageBox.about(self, "alert", "Employee Added its ID"+self.capture_Emp_ID)
                NewEmployeeScreen.genID(self)


            else:
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")
                self.error.setText("Please Fill the Missing Parts")
    
                conn.commit()
                conn.close()
    

    def BrowseImage(self):

        filename = QFileDialog.getOpenFileName(self,'Open File','D\\','Image files (*.jpg *.png )')
        imgpath=filename[0]
        
        pixmap=QPixmap(imgpath)
        self.photo_label.setPixmap(pixmap)
        self.photo_label.setScaledContents(True)



    def Caputer_Images(self): # caputer Employee Face for Dataset 


        if not os.path.exists("./dataset"):
            os.makedirs("./dataset")
            pass
            
        
        face_classifier=cv2.CascadeClassifier("./Resources/haarcascade_frontalface_default.xml")
        NewEmployeeScreen.genID(self)
        def face_ext(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.2,5)
            if faces is():
                return None
            for(x,y,w,h) in faces:
                cropped_face=img[y:y+h,x:x+w]
                return cropped_face

        cap=cv2.VideoCapture(1)
        count=0

        while True :
            ret,frame=cap.read()
            firstnameCap=self.first_line.text()
            if face_ext(frame) is not None:
                count+=1
                face=cv2.resize(face_ext(frame),(400,400))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="dataset/"+firstnameCap+"."+self.capture_Emp_ID+'.'+str(count)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,255,0),3)
                cv2.imshow("Getting Emp face",face)
            else:
                print("face not not found")
                pass
            if cv2.waitKey(1)==13 or count == 75:
                break
        cap.release()
        cv2.destroyAllWindows()
        QMessageBox.about(self,"alert","Images has been saved")
        
            #print("error")    
    
    

    def BacktoMain(self):
        back2Main = MainWin()
        widget.addWidget(back2Main)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")
       
######################################################## NewEmployeeScreen #############################################

######################################################## CompanyInformationWindow #############################################
class TabWidget(QDialog):

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Compay information")
        tabwidget = QTabWidget()
        tabwidget.addTab(DepTab(),"Departments")
        tabwidget.addTab(JobTab(),"Job Title")
        tabwidget.addTab(AttendanceTab(),"Attendance Scheme ")
        tabwidget.addTab(GatesTab(),"Gates")
        tabwidget.addTab(AccesTab(),"Access Scheme")

        BackButton=QPushButton()
        BackButton.setText("Back")
        BackButton.setStyleSheet(u"font: 14pt; color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")    
    
        style_string = pyqtcss.get_style("dark_orange")
        self.setStyleSheet(style_string)
        tabwidget.setStyleSheet("font: 20pt barlow;")

        vbox = QFormLayout()

        vbox.addWidget (tabwidget)
        vbox.addWidget(BackButton)
        self.setLayout(vbox)

        BackButton.clicked.connect(self.back2Main)

 

       # tabwidget.setStyleSheet(u"background-color: rgb(200, 200, 200);"" font: 18pt Old Antic Bold;""\n""\n")            
        self.setFixedWidth(1200)
        self.setFixedHeight(800)
        self.setGeometry(50,50,1200,800)

    def back2Main(self):
        mainwint=MainWin()
        widget.addWidget(mainwint)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")


class DepTab(QWidget):
    def __init__(self):
        super().__init__()
      
        self.DepID=QLabel("Dep ID :")
        self.DepIDline=QLineEdit()
        
        self.DepIDline.setPlaceholderText("Enter only Numbers")
        self.DepIDline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")


        self.DepDesc=QLabel("Dep Desc :")
        self.DepDescline=QLineEdit()
        
        self.DepDescline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")
        self.onlyInt = QIntValidator() 
        self.DepIDline.setValidator(self.onlyInt)

        layout=QVBoxLayout()

        layout.addWidget(self.DepID)
        layout.addWidget(self.DepIDline)
        layout.addWidget(self.DepDesc)
        layout.addWidget(self.DepDescline)

        self.insertbtn = QPushButton("Insert")
        self.cancelbtn = QPushButton("cancel")
       
        self.insertbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
        self.cancelbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
                  
        layout.addWidget (self.insertbtn)  
        layout.addWidget (self.cancelbtn)  
        self.setLayout(layout)
        self.handel_buttons()

    def handel_lines(self):

        self.DepIDline.clear()
        self.DepDescline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.DepDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def DepDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            DepID1=self.DepIDline.text()
            DepDesc1=self.DepDescline.text()



           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1)))
            print(cursor.fetchone())
        if not cursor.fetchone():

            QMessageBox.about(self, "alert", "Departments Added")
        
        else:
            QMessageBox.about(self, "alert", "Wrong Data")   
            
class JobTab(QWidget):
    def __init__(self):
        super().__init__()

        JobID=QLabel("Job ID :")
        self.JobIDline=QLineEdit()
        self.JobIDline.setPlaceholderText("Enter only Numbers")
        self.JobIDline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")

        JobDesc=QLabel("Job Desc :")
        self.JobDescline=QLineEdit()
        self.JobDescline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        self.onlyInt = QIntValidator() 
        self.JobIDline.setValidator(self.onlyInt)
        layout=QVBoxLayout()

        layout.addWidget(JobID)
        layout.addWidget(self.JobIDline)
        layout.addWidget(JobDesc)
        layout.addWidget(self.JobDescline)

        self.insertbtn = QPushButton("Insert")
        self.cancelbtn = QPushButton("cancel")

        self.insertbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
        self.cancelbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")  

        layout.addWidget (self.insertbtn)  
        layout.addWidget (self.cancelbtn)  

        self.setLayout(layout)
        self.handel_buttons()

    def handel_lines(self):

        self.JobIDline.clear()
        self.JobDescline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.JobDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def JobDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            jobID1=self.JobIDline.text()
            jobDesc1=self.JobDescline.text()

           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT OR IGNORE INTO JobTittle (Emp_Job_ID, JobDesc) VALUES (?,?);",(jobID1,jobDesc1)))
            print(cursor.fetchone())
        if not cursor.fetchone():

            QMessageBox.about(self, "alert", "Job Title Added")
        
        else:
            QMessageBox.about(self, "alert", "Wrong Data")   
            
class AttendanceTab(QWidget):
    def __init__(self):
        super().__init__()
        AttendanceID=QLabel("Attendance Scheme ID :")
        self.AttendanceIDline=QLineEdit()
        self.AttendanceIDline.setPlaceholderText("Enter only Numbers")
        self.AttendanceIDline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        AttendanceDesc=QLabel("Attendance Desc :")
        self.AttendanceDescline=QLineEdit()
        self.AttendanceDescline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        LeavingTime=QLabel("LeavingTime:")
        self.LeavingTimeline=QLineEdit()
        self.LeavingTimeline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        
        
        ArrivingTime=QLabel("ArrivingTime")
        self.ArrivingTimeline=QLineEdit()
        self.ArrivingTimeline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        layout=QVBoxLayout()

        self.onlyInt = QIntValidator() 
        self.AttendanceIDline.setValidator(self.onlyInt)

        layout.addWidget(AttendanceID)
        layout.addWidget(self.AttendanceIDline)
        layout.addWidget(AttendanceDesc)
        layout.addWidget(self.AttendanceDescline)

        layout.addWidget(ArrivingTime)
        layout.addWidget(self.ArrivingTimeline)

        layout.addWidget(LeavingTime)
        layout.addWidget(self.LeavingTimeline)

        self.insertbtn = QPushButton("Insert")
        self.cancelbtn = QPushButton("cancel")

        self.insertbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
        self.cancelbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")          
        layout.addWidget (self.insertbtn)  
        layout.addWidget (self.cancelbtn)  

        self.setLayout(layout)
        self.handel_buttons()

    def handel_lines(self):

        self.AttendanceIDline.clear()
        self.LeavingTimeline.clear()
        self.ArrivingTimeline.clear()
        self.AttendanceDescline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.AttendanceDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def AttendanceDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            AttendanceSchemeID1=self.AttendanceIDline.text()
            LeavingTime1=self.LeavingTimeline.text()
            ArrivingTime1=self.ArrivingTimeline.text()
            AttendanceDescline1=self.AttendanceDescline.text()

           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT OR IGNORE INTO Attendance_Schemes_Table (AttendanceSchemes_ID, Entry_Time,Leave_Time,AttendanceDesc) VALUES (?,?,?,?);",(AttendanceSchemeID1,ArrivingTime1,LeavingTime1,AttendanceDescline1)))
            print(cursor.fetchone())
        if not cursor.fetchone():

            QMessageBox.about(self, "alert", "AttendanceSchemes Added")
        
        else:
            QMessageBox.about(self, "alert", "Wrong Data")   
                    
class AccesTab(QWidget):
    def __init__(self):
        super().__init__()

        AcessSchemeID=QLabel("Acess Scheme ID :")
        self.AcessSchemeIDline=QLineEdit()
        self.AcessSchemeIDline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        self.AcessSchemeIDline.setPlaceholderText("Enter only Numbers")

        self.onlyInt = QIntValidator() 
        self.AcessSchemeIDline.setValidator(self.onlyInt)

        AcessDesc=QLabel("Acess Desc :")
        self.AcessDescline=QLineEdit()
        self.AcessDescline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        #self.AcessDescline.addItems(list)

        AccessCategory=QLabel("Access Category :")
        self.AccessCategoryline=QLineEdit()
        self.AccessCategoryline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        
        
        GateId=QLabel("Gate ID:")
        self.Gateline=QLineEdit()
        self.Gateline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        #self.Gateline.addItems(list)
        layout=QVBoxLayout()

        layout.addWidget(AcessSchemeID)
        layout.addWidget(self.AcessSchemeIDline)
        layout.addWidget(GateId)
        layout.addWidget(self.Gateline)
        layout.addWidget(AcessDesc)
        layout.addWidget(self.AcessDescline)
        layout.addWidget(AccessCategory)
        layout.addWidget(self.AccessCategoryline)

      

        self.insertbtn = QPushButton("Insert")
        self.cancelbtn = QPushButton("cancel")

        self.insertbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
        self.cancelbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")          
        layout.addWidget (self.insertbtn)  
        layout.addWidget (self.cancelbtn)  

        self.setLayout(layout)
        self.handel_buttons()

    def handel_lines(self):

        self.AcessSchemeIDline.clear()
        self.AccessCategoryline.clear()
        self.Gateline.clear()
        self.AcessDescline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.AccesDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def AccesDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            AcessSchemeID1=self.AcessSchemeIDline.text()
            Category1=self.AccessCategoryline.text()
            gateID=self.Gateline.text()
            JobsAllowed1=self.AcessDescline.text()

           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT INTO AccessScheme (AccessSchemID, GateID,JobsAllowed,Category) VALUES (?,?,?,?);",(AcessSchemeID1,gateID,JobsAllowed1,Category1)))
            print(cursor.fetchone())
        if not cursor.fetchone():

            QMessageBox.about(self, "alert", "AttendanceSchemes Added")
        
        else:
            QMessageBox.about(self, "alert", "Wrong Data")  

class GatesTab(QWidget):
    def __init__(self):
        super().__init__()

        GateId=QLabel("Gate ID :")
        self.GateIdline=QLineEdit()
        self.GateIdline.setPlaceholderText("Enter only Numbers")
        self.GateIdline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        GateName=QLabel("Gate Name :")
        self.GateNameline=QLineEdit()
        self.GateNameline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        GateCameraIP=QLabel("Gate Camera IP:")
        self.GateCameraIPline=QLineEdit()
        self.GateCameraIPline.setPlaceholderText("Enter only Numbers AND ")
        self.GateCameraIPline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        
       
        GateDoorLockIp=QLabel("Gate Door Lock Ip :")
        self.GateDoorLockIpline=QLineEdit()
        self.GateDoorLockIpline.setPlaceholderText("Enter only Numbers AND . ")
        self.GateDoorLockIpline.setStyleSheet(u"background:#fff;\n""width: 50px;\n""height: 50px;\n""border-radius: 20px;")        

        layout=QVBoxLayout()

        self.onlyInt = QIntValidator() 
        self.GateIdline.setValidator(self.onlyInt)
        #self.GateCameraIPline.setValidator(self.onlyInt)
        #self.GateDoorLockIpline.setValidator(self.onlyInt)
       

        layout.addWidget(GateId)
        layout.addWidget(self.GateIdline)
        layout.addWidget(GateName)
        layout.addWidget(self.GateNameline)
        layout.addWidget(GateCameraIP)
        layout.addWidget(self.GateCameraIPline)
        layout.addWidget(GateDoorLockIp)
        layout.addWidget(self.GateDoorLockIpline)

        self.insertbtn = QPushButton("Insert")
        self.cancelbtn = QPushButton("cancel")

        self.insertbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;")
        self.cancelbtn.setStyleSheet(u"color: White;\n""\n""background-color: #303030 ;\n""border-radius: 12px;") 
                
        layout.addWidget (self.insertbtn)  
        layout.addWidget (self.cancelbtn)  

        self.setLayout(layout)
        self.handel_buttons()

    def handel_lines(self):

        self.GateIdline.clear()
        self.GateNameline.clear()
        self.GateCameraIPline.clear()
        self.GateDoorLockIpline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.GatesDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def GatesDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            GateIdline1=self.GateIdline.text()
            GateNameline1=self.GateNameline.text()
            GateCameraIPline1=self.GateCameraIPline.text()
            GateDoorLockIpline1=self.GateDoorLockIpline.text()

           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT INTO GatesTable (Gate_ID, Gate_Name,Gate_Camera_IP,Gate_Door_Lock_IP) VALUES (?,?,?,?);",(GateIdline1,GateNameline1,GateCameraIPline1,GateDoorLockIpline1)))
            print(cursor.fetchone())
        if not cursor.fetchone():

            QMessageBox.about(self, "alert", "Gate Added")
        
        else:
            QMessageBox.about(self, "alert", "Wrong Data")   

######################################################## EndCompanyInformationWindow #############################################   
                 
######################################################## MainWindow #############################################

class MainWin(QDialog):
    def __init__(self):    
        super(MainWin, self).__init__()
        loadUi("./GUI_SCREENS/TestMainWindow - Copy.ui",self)
        self.setFixedWidth(861)
        self.setFixedHeight(605)
        self.setGeometry(50,50,861,605)
        self.pushButton.clicked.connect(self.gotonewemp)
        self.pushButton_2.clicked.connect(self.gotoCompanyInfo)
        self.TrainButton.clicked.connect(Trainmodle)
        self.TakeAtt.clicked.connect(TakeingAttendace)
        self.logoutButton.clicked.connect(self.gotoWelcome)
        self.AddNewAdminButton.clicked.connect(self.gotoAddAdmin)
        self.Exit.clicked.connect(self.Exitsys)


    def gotoAddAdmin(self):  
        createProfile=AddNewAdmin()
        widget.addWidget(createProfile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(838)
        widget.setFixedHeight(855)
        widget.setGeometry(50,50,838,855)
        widget.setWindowTitle("Add admin Screen")

    def gotonewemp(self):
        NewEmpScreen = NewEmployeeScreen()
        widget.addWidget(NewEmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1538)
        widget.setFixedHeight(926)
        widget.setGeometry(50,50,1538,926)
        widget.setWindowTitle("New Employee Screen")
    '''   
    def gotoAddADmin(self):
        createProfile=AddNewAdmin()
        widget.addWidget(createProfile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)'''

    def gotoCompanyInfo(self):
        CompInfo = TabWidget()
        widget.addWidget(CompInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        widget.setFixedWidth(1200)
        widget.setFixedHeight(800)
        widget.setGeometry(50,50,1200,800)
        widget.setWindowTitle("Company Information Screen")
    
    def gotoWelcome(self):
        back2Welcome = WelcomeScreen()
        widget.addWidget(back2Welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(371)
        widget.setFixedHeight(661)
        widget.setGeometry(50,50,371,661)
        widget.setWindowTitle("Welcome Screen")

    def Exitsys(self):
        exit(0)

        

######################################################## MainWindow #############################################

################################################# training the model###########
def Trainmodle():
    recognizer = cv2.face.LBPHFaceRecognizer_create() #local binary patterns histograms
    path='dataset'
    if not os.path.exists('./recognizer'):
        os.makedirs('./recognizer')
    def getImageWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training",faceNp)
            cv2.waitKey(4)
        return np.array(IDs), faces
        
    Ids, faces = getImageWithID(path)
    recognizer.train(faces,Ids)
    recognizer.save('recognizer/trainingData.yml')
    cv2.destroyAllWindows()
################################################# training the model###########

#################################################Marking the Attendace###########
def TakeingAttendace():
    if not os.path.exists('./Attendance'):
        os.makedirs('./Attendance')
#try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "DataBaseTabletest.db")
    with sqlite3.connect(db_path) as db:
        cursor=db.cursor()

    fname1 = "recognizer/trainingData.yml"

    if not os.path.isfile(fname1):
        print("Please train the data first")
        exit(0)         

    face_cascade = cv2.CascadeClassifier('./Resources/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(fname1)

    while True: 
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2,5)

        for (x,y,w,h) in faces:

            facesp = img[y-5:y+h+5,x-5:x+w+5]
            try:
                resized_face = cv2.resize(facesp,(160,160))
                resized_face = resized_face.astype("float") / 255.
                resized_face = np.expand_dims(resized_face, axis=0)
            except Exception as e:
                print(str(e))

            preds = model.predict(resized_face)[0]


            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
            
            cursor.execute("select * from Employees where Emp_ID = (?);", (ids,))
            result = cursor.fetchall()
            #print(result)
            Fname = result[0][1]
            Mname= result[0][2]
            Lname= result[0][3]

            rname=str(Fname)+str(Mname)+str(Lname)

            Rname=str(Fname)+" "+str(Lname)
            #print(rname) 
            #Attendance(rname)     

            if conf<75  :
                if preds<0.4:
                    cv2.putText(img, Rname, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

                    label = 'real'
                    Attendance(rname)     

                    cv2.putText(img, label, (x,y - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,), 2)

                else:
                    #cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
                    label = 'spoof'
                    cv2.putText(img, Rname, (x+2,y+h-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
                    cv2.putText(img, label, (x,y - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            else:
                cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

        cv2.imshow('Face Recognizer',img)


        if cv2.waitKey(1) == ord('\r'):
            break
            
    cv2.destroyAllWindows()        



#################################################Marking the Attendace###########
def Attendance(name):
    with open('Attendance.csv','r+') as f:
        attended = f.readlines()
        EmployeeAttended = []
        for line in attended:
            entry = line.split(',')
            EmployeeAttended.append(entry[0])
            
        if name not in EmployeeAttended:
            attendTime = datetime.now().strftime('%H:%M:%S')
            
            f.writelines(f'\n{name},{attendTime}')

######################################################## AddNewAdminWindow #############################################

class AddNewAdmin(QDialog):
    def __init__(self):
        super(AddNewAdmin, self).__init__()
        loadUi("./GUI_SCREENS/createacc - Copy.ui",self)
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.CancelButton.clicked.connect(self.goBack)
        self.setFixedWidth(1551)
        self.setFixedHeight(1031)
        self.setGeometry(50,50,1551,1031)

    def signupfunction(self):
        EmpId=self.empid.text()
        user = self.user_line.text()
        password = self.pass_line.text()
        confirmpassword = self.confirmpass_line.text()



        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")

        else:
            conn = sqlite3.connect("./DataBaseTabletest.db")
            cur = conn.cursor()

            for EmpId in (EmpId):
                cur.execute("SELECT rowid FROM Employees WHERE Emp_ID = ?", (EmpId, ))
            data = cur.fetchall()
            if len(EmpId) ==0:
                print('There is No Employee With This ID %s' % EmpId)
                QMessageBox.about(self, "alert", 'There is No Employee With This ID %s' % EmpId)
            else :
               # print('Employee Found Adding his admin account  %s' % (EmpId, ','.join(map(str, next(zip( * data))))))

                user_info = [user,password,EmpId]
                cur.execute('INSERT INTO Users (User_Name, User_Password,Emp_ID) VALUES (?,?,?)', user_info)

                conn.commit()
                conn.close()
                QMessageBox.about(self, "alert", 'Employee With This ID  %s ->> Admin account Added' % EmpId)
                self.gotologin()

    def gotologin(self):

        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Login Screen")
        widget.setFixedWidth(548)
        widget.setFixedHeight(755)
        widget.setGeometry(50,50,548,755)
           

    def goBack(self):
        back2wle = MainWin()
        widget.addWidget(back2wle)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Main Screen")
        widget.setFixedWidth(861)
        widget.setFixedHeight(605) 
        widget.setGeometry(50,50,861,605)
######################################################## AddNewAdminWindow #############################################

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setGeometry(50,50,371,661)
widget.setWindowTitle("Welcome")


widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")