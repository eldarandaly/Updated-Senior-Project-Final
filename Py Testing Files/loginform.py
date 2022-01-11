
from sqlite3.dbapi2 import Cursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
from PyQt5 import  QtSql 
import sys 
from PyQt5 import QtWidgets
from PyQt5 import QtSql
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from ui_Regstarion_Form import Ui_MainWindow


FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"login_Widget.ui"))

class login_form(QWidget, FORM_CLASS):
    def __init__ (self, parent=None):
        super(login_form,self).__init__(parent)
      #  QtWidgets.__init__(self)
        self.setupUi(self)
        #self.openDB()
        self.handel_buttons()
        
        
    def handel_buttons(self):
        self.login_button.clicked.connect(self.login)
        

    def login(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
        with sqlite3.connect(db_path) as db:
            #db=sqlite3.connect("D:/Project/DataBaseTable.db")
            cursor=db.cursor()
            UserName1=self.user_line.text()
            PassWord1=self.pass_line.text()
            cursor.execute("select * from Users where User_Name=? and User_Password=?",(UserName1,PassWord1))
            row=cursor.fetchone()
            if row :
                QMessageBox.about(self, "Login successful", "welcome"+" "+ UserName1)
                print("login successful")
            else:
                QMessageBox.about(self, "Login Failed", "please Enter a vaild User Name OR PassWord ")
                print("failed")




def main():
    app=QApplication(sys.argv)
    window =login_form()
    window.show()
    app.exec_()

if __name__ =='__main__':
    main()

