from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton,QVBoxLayout,QDialogButtonBox, QApplication, QDialog,QTabWidget, QWidget,QMessageBox 
import sys
import os
from os import path
import sqlite3

from PySide2.QtGui import QFont




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
     

        vbox = QVBoxLayout()
        vbox.addWidget (tabwidget)
        self.setLayout(vbox)


        tabwidget.setStyleSheet(u"background-color: rgb(200, 200, 200);"" font: 18pt Old Antic Bold;""\n""\n")            
        self.setGeometry(500,50,1000,1000)
        


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
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
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

        self.self.JobIDline.clear()
        self.self.JobDescline.clear()

    def handel_buttons(self):
        self.cancelbtn.clicked.connect(self.handel_lines)
        self.insertbtn.clicked.connect(self.JobDB)
        self.insertbtn.clicked.connect(self.handel_lines)

    def JobDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
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
        layout.addWidget(LeavingTime)
        layout.addWidget(self.LeavingTimeline)
        layout.addWidget(ArrivingTime)
        layout.addWidget(self.ArrivingTimeline)

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
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            AttendanceSchemeID1=self.AttendanceIDline.text()
            LeavingTime1=self.LeavingTimeline.text()
            ArrivingTime1=self.ArrivingTimeline.text()
            AttendanceDescline1=self.AttendanceDescline.text()

           # cursor.execute("INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?);",(DepID1,DepDesc1))
            print( cursor.execute("INSERT OR IGNORE INTO AttendanceSchemesTable (AttendanceSchemes_ID, Entry_Time,Leave_Time,AttendanceDesc) VALUES (?,?,?,?);",(AttendanceSchemeID1,ArrivingTime1,LeavingTime1,AttendanceDescline1)))
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
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
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
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
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
                    


app=QApplication(sys.argv)
tabwidget=TabWidget()
tabwidget.show()
app.exec()

