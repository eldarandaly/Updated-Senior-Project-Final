# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Employee_Reg_win.ui'
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
"	background-color: rgb(200, 200, 200);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 30, 441, 71))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(80, 130, 71, 51))
        font1 = QFont()
        font1.setFamily(u"Old Antic Bold")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_30.setFrameShape(QFrame.NoFrame)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(830, 260, 161, 41))
        font2 = QFont()
        font2.setFamily(u"Old Antic Bold")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setUnderline(True)
        font2.setWeight(50)
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 260, 141, 41))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(470, 260, 161, 41))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.last_line = QLineEdit(self.centralwidget)
        self.last_line.setObjectName(u"last_line")
        self.last_line.setGeometry(QRect(770, 310, 251, 41))
        font3 = QFont()
        font3.setFamily(u"Old Antic Bold")
        font3.setPointSize(18)
        self.last_line.setFont(font3)
        self.last_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.last_line.setClearButtonEnabled(True)
        self.first_line = QLineEdit(self.centralwidget)
        self.first_line.setObjectName(u"first_line")
        self.first_line.setGeometry(QRect(80, 310, 261, 41))
        self.first_line.setFont(font3)
        self.first_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.first_line.setFrame(True)
        self.first_line.setEchoMode(QLineEdit.Normal)
        self.first_line.setClearButtonEnabled(True)
        self.middle_line = QLineEdit(self.centralwidget)
        self.middle_line.setObjectName(u"middle_line")
        self.middle_line.setGeometry(QRect(410, 310, 271, 41))
        self.middle_line.setFont(font3)
        self.middle_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.middle_line.setClearButtonEnabled(True)
        self.photo_label = QLabel(self.centralwidget)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(1090, 30, 341, 271))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setWeight(75)
        self.photo_label.setFont(font4)
        self.photo_label.setAutoFillBackground(False)
        self.photo_label.setStyleSheet(u"\n"
"border-radius: 90px;")
        self.addphoto_button = QPushButton(self.centralwidget)
        self.addphoto_button.setObjectName(u"addphoto_button")
        self.addphoto_button.setGeometry(QRect(1210, 340, 151, 51))
        self.addphoto_button.setFont(font1)
        self.addphoto_button.setMouseTracking(True)
        self.addphoto_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #303030 ;\n"
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
        self.year_drop.setGeometry(QRect(690, 440, 111, 41))
        self.year_drop.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(500, 390, 151, 31))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 0);")
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
        self.day_drop.setGeometry(QRect(410, 440, 81, 41))
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
        self.month_drop.setGeometry(QRect(530, 440, 121, 41))
        self.month_drop.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(80, 380, 101, 31))
        font5 = QFont()
        font5.setFamily(u"Old Antic Bold")
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setUnderline(True)
        font5.setWeight(50)
        font5.setKerning(True)
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_66 = QLabel(self.centralwidget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(500, 640, 71, 31))
        font6 = QFont()
        font6.setFamily(u"Old Antic Bold")
        font6.setPointSize(20)
        font6.setUnderline(True)
        self.label_66.setFont(font6)
        self.label_66.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_67 = QLabel(self.centralwidget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(120, 520, 221, 41))
        self.label_67.setFont(font6)
        self.label_67.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.address_line = QLineEdit(self.centralwidget)
        self.address_line.setObjectName(u"address_line")
        self.address_line.setGeometry(QRect(90, 570, 581, 41))
        self.address_line.setFont(font3)
        self.address_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.address_line.setClearButtonEnabled(True)
        self.label_68 = QLabel(self.centralwidget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(120, 650, 191, 31))
        self.label_68.setFont(font2)
        self.label_68.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.email_line = QLineEdit(self.centralwidget)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(410, 700, 281, 41))
        self.email_line.setFont(font3)
        self.email_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.email_line.setClearButtonEnabled(True)
        self.phone_line = QLineEdit(self.centralwidget)
        self.phone_line.setObjectName(u"phone_line")
        self.phone_line.setGeometry(QRect(100, 700, 251, 41))
        self.phone_line.setFont(font3)
        self.phone_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.phone_line.setClearButtonEnabled(True)
        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(830, 860, 191, 61))
        font7 = QFont()
        font7.setFamily(u"Old Antic Bold")
        font7.setPointSize(20)
        self.cancel_button.setFont(font7)
        self.cancel_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #303030 ;\n"
"border-radius: 12px;\n"
"}\n"
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
        font8 = QFont()
        font8.setFamily(u"Old Antic Bold")
        font8.setPointSize(18)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.dep_drop.setFont(font8)
        self.dep_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_83 = QLabel(self.centralwidget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(880, 540, 151, 31))
        self.label_83.setFont(font2)
        self.label_83.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.access_drop = QComboBox(self.centralwidget)
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.setObjectName(u"access_drop")
        self.access_drop.setGeometry(QRect(1160, 710, 281, 41))
        self.access_drop.setFont(font8)
        self.access_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_84 = QLabel(self.centralwidget)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(1180, 640, 231, 41))
        self.label_84.setFont(font2)
        self.label_84.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_85 = QLabel(self.centralwidget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(840, 650, 261, 41))
        self.label_85.setFont(font2)
        self.label_85.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.job_drop = QComboBox(self.centralwidget)
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.setObjectName(u"job_drop")
        self.job_drop.setGeometry(QRect(1160, 580, 281, 41))
        self.job_drop.setFont(font8)
        self.job_drop.setStyleSheet(u"background: #fff;\n"
"   width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.job_drop.setIconSize(QSize(16, 16))
        self.job_drop.setFrame(True)
        self.label_86 = QLabel(self.centralwidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1190, 530, 111, 31))
        self.label_86.setFont(font6)
        self.label_86.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.attend_drop = QComboBox(self.centralwidget)
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.setObjectName(u"attend_drop")
        self.attend_drop.setGeometry(QRect(810, 700, 271, 41))
        self.attend_drop.setFont(font3)
        self.attend_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(600, 860, 181, 61))
        self.save_button.setFont(font1)
        self.save_button.setMouseTracking(True)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #303030 ;\n"
"border-radius: 12px;\n"
"}")
        self.save_button.setAutoDefault(True)
        self.save_button.setFlat(True)
        self.IDNum = QLCDNumber(self.centralwidget)
        self.IDNum.setObjectName(u"IDNum")
        self.IDNum.setGeometry(QRect(80, 180, 141, 51))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(120, 430, 82, 31))
        font9 = QFont()
        font9.setFamily(u"Old Antic Bold")
        font9.setPointSize(15)
        self.radioButton.setFont(font9)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(120, 470, 121, 31))
        self.radioButton_2.setFont(font9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.first_line, self.middle_line)
        QWidget.setTabOrder(self.middle_line, self.last_line)
        QWidget.setTabOrder(self.last_line, self.day_drop)
        QWidget.setTabOrder(self.day_drop, self.month_drop)
        QWidget.setTabOrder(self.month_drop, self.year_drop)
        QWidget.setTabOrder(self.year_drop, self.address_line)
        QWidget.setTabOrder(self.address_line, self.dep_drop)
        QWidget.setTabOrder(self.dep_drop, self.job_drop)
        QWidget.setTabOrder(self.job_drop, self.phone_line)
        QWidget.setTabOrder(self.phone_line, self.email_line)
        QWidget.setTabOrder(self.email_line, self.attend_drop)
        QWidget.setTabOrder(self.attend_drop, self.access_drop)
        QWidget.setTabOrder(self.access_drop, self.addphoto_button)
        QWidget.setTabOrder(self.addphoto_button, self.save_button)
        QWidget.setTabOrder(self.save_button, self.cancel_button)

        self.retranslateUi(MainWindow)

        self.addphoto_button.setDefault(True)
        self.save_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main widnow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Employee Registration", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"First Name ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.last_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Last Name", None))
        self.first_line.setInputMask("")
        self.first_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter First Name", None))
        self.middle_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Middle Name", None))
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
        self.address_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Address", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.email_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Email", None))
        self.phone_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Phone Number", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.dep_drop.setItemText(0, "")
        self.dep_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"Management", None))
        self.dep_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"Information Technology", None))
        self.dep_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.dep_drop.setItemText(4, QCoreApplication.translate("MainWindow", u"Accounting", None))
        self.dep_drop.setItemText(5, QCoreApplication.translate("MainWindow", u"Security", None))
        self.dep_drop.setItemText(6, QCoreApplication.translate("MainWindow", u"Housekeeping", None))

        self.dep_drop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Department", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.access_drop.setItemText(0, "")
        self.access_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.access_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.access_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))

        self.access_drop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Acess Categroy", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Access Categroy", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Attendance Scheme ", None))
        self.job_drop.setItemText(0, "")
        self.job_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"General manager", None))
        self.job_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"Head Security", None))
        self.job_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales employee", None))

        self.job_drop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Job Title ", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.attend_drop.setItemText(0, "")
        self.attend_drop.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.attend_drop.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.attend_drop.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.attend_drop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Attendance Scheme ", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Female", None))
    # retranslateUi

