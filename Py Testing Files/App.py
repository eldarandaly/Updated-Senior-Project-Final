from PyQt5 import  QtSql , QtWidgets
from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import PyQt5
import sys
from ui_Regstarion_Form import Ui_MainWindow


class myApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.Ui=Ui_MainWindow()
        self.Ui.setupUi(self)
        #loadUi("E:/Gradution Project/New folder/Python_Files/Regstarion_Form.ui",self)
        #self.show()
        self.openDB()
        self.pushButton.Clicked.connect(self.checkUser)
        

    def openDB (self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("DataBaseTable.db")
        if not self.db.open():
          print("Error")
        self.query = QtSql.QSqlQuery()


    def checkUser(self):
        UserName1=self.lineEdit_ID.text()
        PassWord1=self.lineEdit_2.text()
        print(UserName1,PassWord1)


if __name__ == "__main__":
    app= QApplication(sys.argv)
    mainwin=myApp()
    mainwin.show()
    #ui.show()
    #Form.show()
    sys.exit(app.exec_())
