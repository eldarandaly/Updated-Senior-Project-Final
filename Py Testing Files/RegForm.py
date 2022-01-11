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
from PyQt5.QtWidgets import QMessageBox


FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"Employee_Reg_win.ui"))

class Regform(QMainWindow, FORM_CLASS):
    def __init__ (self, parent=None):
        
        super(Regform,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_buttons()
        self.handel_Lines()
        self.handel_photo()
        self.handel_Ui()
        
    def handel_buttons(self):
        self.save_button.clicked.connect(self.DB)
        self.save_button.clicked.connect(self.handel_Lines)
        self.cancel_button.clicked.connect(self.handel_Lines)

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
        self.setGeometry(0,0,1487,973)   

    def DB(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()

            firstname1=self.first_line.text()
            middlename1=self.middle_line.text()
            lastname1=self.last_line.text()
            #gender=self.radioButton.selected()
            address=self.address_line.text()
           # Emp_ID=self.IDNum.value()



            cursor.execute("INSERT INTO Employees (Emp_First_Name, Emp_Middle_Name, Emp_Last_Name,Emp_Address) VALUES (?,?,?,?);",(firstname1,middlename1,lastname1,address))
            if not cursor.fetchone():
                QMessageBox.about(self, "alert", "Employee Added")
                
            else:
                QMessageBox.about(self, "alert", "Wrong Data")


    def BrowseImage(self):

        filename=QFileDialog.getOpenFileName(self,'Open File','D\\','Image files (*.jpg *.png )')
        imgpath=filename[0]
        pixmap=QPixmap(imgpath)
        self.photo_label.setPixmap(pixmap)


def main():
    app=QApplication(sys.argv)
    window =Regform()
    window.show()
    app.exec_()

if __name__ =='__main__':
    main()

