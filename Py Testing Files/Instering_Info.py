from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
from PyQt5 import  QtSql 
import sys 
from PyQt5 import QtWidgets
import sqlite3
from ui_Regstarion_Form import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox ,QTabWidget


FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"CompanyData_Widget.ui"))

class InfoForm(QWidget, FORM_CLASS):
    def __init__ (self, parent=None):
        super(InfoForm,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        tabwidget=QTabWidget()
      #  tabwidget.setCurrentWidget(DepTab())
        tabwidget.setLayout(DepTab)
       # self.handel_buttons()
        #self.handel_Lines()
        #self.handel_Ui()
       # self.Info_Tabs.currentChanged.connect(self.GetIndex)


class DepTab(QWidget):
    def __init__(self):
        super().__init__()
        print("here1")
        depID=self.depid_line.text()
        depDesc=self.dep_line.text()


class JobTab(QWidget):
    def __init__(self):
        super().__init__()
        print("here2")

class AttendanceTab(QWidget):
    def __init__(self):
        super().__init__()
        print("here3")

class AccesTab(QWidget):
    def __init__(self):
        super().__init__()
        print("here4")

    ''' def handel_buttons(self):
        self.save_button.clicked.connect(self.DB)
        self.save_button.clicked.connect(self.handel_Lines)
        self.cancel_button.clicked.connect(self.handel_Lines)'''


    ''' def handel_Lines(self):
        self.first_line.clear()
        self.middle_line.clear()
        self.last_line.clear()
        self.address_line.clear()
        self.phone_line.clear()
        self.email_line.clear()'''

    def handel_Ui(self):
        self.setGeometry(0,0,1487,973)   

    def GetIndex(self):
        print("tab changed to ",self.Info_Tabs.currentIndex())

    def DepTab(self):
        pass

    def JobTab(self):
        pass

    def AttendaceTab(self):
        pass

    def AccesTab(self):
        pass


    def depDB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            cursor.execute("INSERT INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?,?,?);",(depID,depDesc))
            if not cursor.fetchone():
                QMessageBox.about(self, "alert", "Employee Added")
                
            else:
                QMessageBox.about(self, "alert", "Wrong Data")





def main():
    app=QApplication(sys.argv)
    window =InfoForm()
    window.show()
    app.exec_()

if __name__ =='__main__':
    main()