# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1487, 973)
        MainWindow.setStyleSheet(u"\n"
"	background-color: rgb(155, 204, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 30, 351, 71))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(120, 140, 61, 21))
        font1 = QFont()
        font1.setFamily(u"Microsoft JhengHei")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30.setFrameShape(QFrame.NoFrame)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(810, 270, 151, 21))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 250, 141, 41))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(450, 260, 151, 21))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.last_line = QLineEdit(self.centralwidget)
        self.last_line.setObjectName(u"last_line")
        self.last_line.setGeometry(QRect(770, 310, 251, 41))
        self.last_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"")
        self.first_line = QLineEdit(self.centralwidget)
        self.first_line.setObjectName(u"first_line")
        self.first_line.setGeometry(QRect(80, 310, 261, 41))
        self.first_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.ID_line = QLineEdit(self.centralwidget)
        self.ID_line.setObjectName(u"ID_line")
        self.ID_line.setGeometry(QRect(80, 190, 251, 41))
        self.ID_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.middle_line = QLineEdit(self.centralwidget)
        self.middle_line.setObjectName(u"middle_line")
        self.middle_line.setGeometry(QRect(410, 310, 271, 41))
        self.middle_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.photo_label = QLabel(self.centralwidget)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(1190, 100, 201, 201))
        self.photo_label.setStyleSheet(u"background-image: url(\"D:/ahmos/Desktop/user1.jpg\");\n"
"border-radius: 90px;")
        self.addphoto_button = QPushButton(self.centralwidget)
        self.addphoto_button.setObjectName(u"addphoto_button")
        self.addphoto_button.setGeometry(QRect(1210, 340, 141, 51))
        self.addphoto_button.setFont(font1)
        self.addphoto_button.setMouseTracking(True)
        self.addphoto_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.addphoto_button.setAutoDefault(True)
        self.addphoto_button.setFlat(True)
        self.year_drop = QComboBox(self.centralwidget)
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.addItem("")
        self.year_drop.setObjectName(u"year_drop")
        self.year_drop.setGeometry(QRect(750, 440, 111, 41))
        self.year_drop.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(550, 390, 151, 21))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.day_drop = QComboBox(self.centralwidget)
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.addItem("")
        self.day_drop.setObjectName(u"day_drop")
        self.day_drop.setGeometry(QRect(470, 440, 81, 41))
        self.day_drop.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.month_drop = QComboBox(self.centralwidget)
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.addItem("")
        self.month_drop.setObjectName(u"month_drop")
        self.month_drop.setGeometry(QRect(590, 440, 121, 41))
        self.month_drop.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(110, 380, 151, 21))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_66 = QLabel(self.centralwidget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(500, 640, 71, 31))
        font2 = QFont()
        font2.setFamily(u"Microsoft JhengHei")
        font2.setPointSize(14)
        self.label_66.setFont(font2)
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_67 = QLabel(self.centralwidget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(120, 520, 91, 41))
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.address_line = QLineEdit(self.centralwidget)
        self.address_line.setObjectName(u"address_line")
        self.address_line.setGeometry(QRect(90, 570, 581, 41))
        self.address_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_68 = QLabel(self.centralwidget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(120, 650, 171, 31))
        self.label_68.setFont(font1)
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email_line = QLineEdit(self.centralwidget)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(410, 700, 281, 41))
        self.email_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"")
        self.phone_line = QLineEdit(self.centralwidget)
        self.phone_line.setObjectName(u"phone_line")
        self.phone_line.setGeometry(QRect(100, 700, 251, 41))
        self.phone_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(830, 860, 191, 61))
        self.cancel_button.setFont(font2)
        self.cancel_button.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #008CBA ;\n"
"  color: white;\n"
"\n"
"border-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: #008CBA;\n"
"selection-background-color: rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 12px;\n"
"selection-background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"};\n"
"\n"
"hover {\n"
"  background-color: #4CAF50; /* Green */\n"
"  color: white;\n"
"}")
        self.dep_drop = QComboBox(self.centralwidget)
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.setObjectName(u"dep_drop")
        self.dep_drop.setGeometry(QRect(810, 580, 271, 41))
        self.dep_drop.setStyleSheet(u"background: #fff;\n"
"font: 12pt \"Microsoft JhengHei\";\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_83 = QLabel(self.centralwidget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(880, 520, 151, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.access_drop = QComboBox(self.centralwidget)
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.setObjectName(u"access_drop")
        self.access_drop.setGeometry(QRect(1160, 710, 281, 41))
        self.access_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_84 = QLabel(self.centralwidget)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(1180, 640, 191, 41))
        self.label_84.setFont(font1)
        self.label_84.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_85 = QLabel(self.centralwidget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(830, 650, 221, 41))
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.job_drop = QComboBox(self.centralwidget)
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.setObjectName(u"job_drop")
        self.job_drop.setGeometry(QRect(1160, 580, 281, 41))
        self.job_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_86 = QLabel(self.centralwidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1180, 530, 100, 21))
        self.label_86.setFont(font2)
        self.label_86.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.attend_drop = QComboBox(self.centralwidget)
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.setObjectName(u"attend_drop")
        self.attend_drop.setGeometry(QRect(810, 700, 271, 41))
        self.attend_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(600, 860, 181, 61))
        self.save_button.setFont(font1)
        self.save_button.setMouseTracking(True)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.save_button.setAutoDefault(True)
        self.save_button.setFlat(True)
        self.male_check = QCheckBox(self.centralwidget)
        self.male_check.setObjectName(u"male_check")
        self.male_check.setGeometry(QRect(100, 440, 81, 20))
        self.male_check.setStyleSheet(u"font: 12pt \"Microsoft JhengHei\";")
        self.female_check = QCheckBox(self.centralwidget)
        self.female_check.setObjectName(u"female_check")
        self.female_check.setGeometry(QRect(210, 440, 101, 21))
        self.female_check.setStyleSheet(u"font: 12pt \"Microsoft JhengHei\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.addphoto_button.setDefault(True)
        self.save_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main widnow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"New Employee", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"First Name ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.photo_label.setText("")
        self.addphoto_button.setText(QCoreApplication.translate("MainWindow", u"Add Photo", None))
        self.year_drop.setItemText(0, QCoreApplication.translate("MainWindow", u"1999", None))
        self.year_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"1998", None))
        self.year_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"1997", None))
        self.year_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"1996", None))
        self.year_drop.setItemText(4, QCoreApplication.translate("MainWindow", u"1995", None))
        self.year_drop.setItemText(5, QCoreApplication.translate("MainWindow", u"1994", None))
        self.year_drop.setItemText(6, QCoreApplication.translate("MainWindow", u"1993", None))
        self.year_drop.setItemText(7, QCoreApplication.translate("MainWindow", u"1992", None))
        self.year_drop.setItemText(8, QCoreApplication.translate("MainWindow", u"1991", None))
        self.year_drop.setItemText(9, QCoreApplication.translate("MainWindow", u"1990", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.day_drop.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.day_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.day_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.day_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.day_drop.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.day_drop.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.day_drop.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.day_drop.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.day_drop.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.day_drop.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.day_drop.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.day_drop.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.day_drop.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.day_drop.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.day_drop.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.day_drop.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.day_drop.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.day_drop.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.day_drop.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.day_drop.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.day_drop.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.day_drop.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.day_drop.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.day_drop.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.day_drop.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.day_drop.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.day_drop.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.day_drop.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.day_drop.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.day_drop.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.day_drop.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.month_drop.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.month_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.month_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.month_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.month_drop.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.month_drop.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.month_drop.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.month_drop.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.month_drop.setItemText(8, QCoreApplication.translate("MainWindow", u"september", None))
        self.month_drop.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.month_drop.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.month_drop.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.dep_drop.setItemText(0, "")
        self.dep_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"Management", None))
        self.dep_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"Information Technology", None))
        self.dep_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.dep_drop.setItemText(4, QCoreApplication.translate("MainWindow", u"Accounting", None))
        self.dep_drop.setItemText(5, QCoreApplication.translate("MainWindow", u"Security", None))
        self.dep_drop.setItemText(6, QCoreApplication.translate("MainWindow", u"Housekeeping", None))

        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.access_drop.setItemText(0, "")
        self.access_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.access_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.access_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))

        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Access Categroy", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Attendance Scheme ", None))
        self.job_drop.setItemText(0, "")
        self.job_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"General manager", None))
        self.job_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"Head Security", None))
        self.job_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales employee", None))

        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.attend_drop.setItemText(0, "")
        self.attend_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.attend_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.attend_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.male_check.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.female_check.setText(QCoreApplication.translate("MainWindow", u"Female", None))
    # retranslateUi

