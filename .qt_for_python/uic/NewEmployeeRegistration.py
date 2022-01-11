# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewEmployeeRegistration.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1538, 926)
        Dialog.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"")
        self.first_line = QLineEdit(Dialog)
        self.first_line.setObjectName(u"first_line")
        self.first_line.setGeometry(QRect(40, 300, 261, 41))
        font = QFont()
        font.setFamily(u"Old Antic Bold")
        font.setPointSize(18)
        self.first_line.setFont(font)
        self.first_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.first_line.setFrame(True)
        self.first_line.setEchoMode(QLineEdit.Normal)
        self.first_line.setClearButtonEnabled(True)
        self.label_85 = QLabel(Dialog)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(800, 640, 261, 41))
        font1 = QFont()
        font1.setFamily(u"Old Antic Bold")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setUnderline(True)
        font1.setWeight(50)
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.middle_line = QLineEdit(Dialog)
        self.middle_line.setObjectName(u"middle_line")
        self.middle_line.setGeometry(QRect(370, 300, 271, 41))
        self.middle_line.setFont(font)
        self.middle_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.middle_line.setClearButtonEnabled(True)
        self.last_line = QLineEdit(Dialog)
        self.last_line.setObjectName(u"last_line")
        self.last_line.setGeometry(QRect(730, 300, 251, 41))
        self.last_line.setFont(font)
        self.last_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.last_line.setClearButtonEnabled(True)
        self.job_drop = QComboBox(Dialog)
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.addItem("")
        self.job_drop.setObjectName(u"job_drop")
        self.job_drop.setGeometry(QRect(1120, 570, 281, 41))
        font2 = QFont()
        font2.setFamily(u"Old Antic Bold")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.job_drop.setFont(font2)
        self.job_drop.setStyleSheet(u"background: #fff;\n"
"   width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.job_drop.setIconSize(QSize(16, 16))
        self.job_drop.setFrame(True)
        self.label_83 = QLabel(Dialog)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(840, 530, 151, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(620, 840, 161, 61))
        font3 = QFont()
        font3.setFamily(u"Old Antic Bold")
        font3.setPointSize(20)
        self.cancel_button.setFont(font3)
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
        self.label_86 = QLabel(Dialog)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1170, 530, 101, 31))
        self.label_86.setFont(font1)
        self.label_86.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_84 = QLabel(Dialog)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(1140, 630, 231, 41))
        self.label_84.setFont(font1)
        self.label_84.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 441, 71))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(30)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_66 = QLabel(Dialog)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(460, 630, 71, 31))
        font5 = QFont()
        font5.setFamily(u"Old Antic Bold")
        font5.setPointSize(20)
        font5.setUnderline(True)
        self.label_66.setFont(font5)
        self.label_66.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 370, 101, 31))
        font6 = QFont()
        font6.setFamily(u"Old Antic Bold")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setUnderline(True)
        font6.setWeight(50)
        font6.setKerning(True)
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.attend_drop = QComboBox(Dialog)
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.addItem("")
        self.attend_drop.setObjectName(u"attend_drop")
        self.attend_drop.setGeometry(QRect(770, 690, 271, 41))
        self.attend_drop.setFont(font)
        self.attend_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.photo_label = QLabel(Dialog)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(1060, 20, 431, 271))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setWeight(75)
        self.photo_label.setFont(font7)
        self.photo_label.setAutoFillBackground(False)
        self.photo_label.setStyleSheet(u"\n"
"border-radius: 90px;")
        self.email_line = QLineEdit(Dialog)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(370, 690, 281, 41))
        self.email_line.setFont(font)
        self.email_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.email_line.setClearButtonEnabled(True)
        self.phone_line = QLineEdit(Dialog)
        self.phone_line.setObjectName(u"phone_line")
        self.phone_line.setGeometry(QRect(60, 690, 251, 41))
        self.phone_line.setFont(font)
        self.phone_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.phone_line.setClearButtonEnabled(True)
        self.label_68 = QLabel(Dialog)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(80, 640, 191, 31))
        self.label_68.setFont(font1)
        self.label_68.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(400, 840, 171, 61))
        font8 = QFont()
        font8.setFamily(u"Old Antic Bold")
        font8.setPointSize(20)
        font8.setBold(False)
        font8.setWeight(50)
        self.save_button.setFont(font8)
        self.save_button.setMouseTracking(True)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #303030 ;\n"
"border-radius: 12px;\n"
"}")
        self.save_button.setAutoDefault(True)
        self.save_button.setFlat(True)
        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(790, 250, 161, 41))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(430, 250, 161, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.access_drop = QComboBox(Dialog)
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.addItem("")
        self.access_drop.setObjectName(u"access_drop")
        self.access_drop.setGeometry(QRect(1120, 690, 281, 41))
        self.access_drop.setFont(font2)
        self.access_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_67 = QLabel(Dialog)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(80, 510, 221, 41))
        self.label_67.setFont(font5)
        self.label_67.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.address_line = QLineEdit(Dialog)
        self.address_line.setObjectName(u"address_line")
        self.address_line.setGeometry(QRect(50, 560, 581, 41))
        self.address_line.setFont(font)
        self.address_line.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.address_line.setClearButtonEnabled(True)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(80, 420, 82, 31))
        font9 = QFont()
        font9.setFamily(u"Old Antic Bold")
        font9.setPointSize(15)
        self.radioButton.setFont(font9)
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(80, 460, 121, 31))
        self.radioButton_2.setFont(font9)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 250, 141, 41))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(460, 380, 151, 31))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.dep_drop = QComboBox(Dialog)
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.addItem("")
        self.dep_drop.setObjectName(u"dep_drop")
        self.dep_drop.setGeometry(QRect(770, 570, 271, 41))
        self.dep_drop.setFont(font2)
        self.dep_drop.setStyleSheet(u"background: #fff;\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.addphoto_button = QPushButton(Dialog)
        self.addphoto_button.setObjectName(u"addphoto_button")
        self.addphoto_button.setGeometry(QRect(1150, 330, 151, 51))
        self.addphoto_button.setFont(font8)
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
        self.capture_button = QPushButton(Dialog)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setGeometry(QRect(800, 840, 301, 61))
        self.capture_button.setFont(font8)
        self.capture_button.setMouseTracking(True)
        self.capture_button.setStyleSheet(u"QPushButton {\n"
"color: White;\n"
"background-color: #281198 ;\n"
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
        self.capture_button.setAutoDefault(True)
        self.capture_button.setFlat(True)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 100, 201, 121))
        font10 = QFont()
        font10.setFamily(u"Old Antic Bold")
        font10.setPointSize(14)
        self.groupBox.setFont(font10)
        self.IDlable = QLabel(self.groupBox)
        self.IDlable.setObjectName(u"IDlable")
        self.IDlable.setGeometry(QRect(40, 40, 131, 51))
        self.IDlable.setFont(font3)
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(30, 40, 151, 71))
        self.lcdNumber.setStyleSheet(u"color:red")
        self.addphoto_button_2 = QPushButton(Dialog)
        self.addphoto_button_2.setObjectName(u"addphoto_button_2")
        self.addphoto_button_2.setGeometry(QRect(1310, 330, 151, 51))
        self.addphoto_button_2.setFont(font8)
        self.addphoto_button_2.setMouseTracking(True)
        self.addphoto_button_2.setStyleSheet(u"QPushButton {\n"
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
        self.addphoto_button_2.setAutoDefault(True)
        self.addphoto_button_2.setFlat(True)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(460, 430, 201, 71))
        font11 = QFont()
        font11.setFamily(u"Old Antic Bold")
        font11.setPointSize(20)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(75)
        self.dateEdit.setFont(font11)
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setTimeSpec(Qt.LocalTime)
        self.BackButton = QPushButton(Dialog)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(1120, 850, 151, 51))
        self.BackButton.setFont(font8)
        self.BackButton.setMouseTracking(True)
        self.BackButton.setStyleSheet(u"QPushButton {\n"
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
        self.BackButton.setAutoDefault(True)
        self.BackButton.setFlat(True)
        self.error = QLabel(Dialog)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(460, 130, 361, 51))
        font12 = QFont()
        font12.setFamily(u"Old Antic Bold")
        font12.setPointSize(22)
        self.error.setFont(font12)
        self.error.setStyleSheet(u"color:red")

        self.retranslateUi(Dialog)

        self.save_button.setDefault(True)
        self.addphoto_button.setDefault(True)
        self.capture_button.setDefault(True)
        self.addphoto_button_2.setDefault(True)
        self.BackButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.first_line.setInputMask("")
        self.first_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter First Name", None))
        self.label_85.setText(QCoreApplication.translate("Dialog", u"Attendance Scheme ", None))
        self.middle_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Middle Name", None))
        self.last_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Last Name", None))
        self.job_drop.setItemText(0, QCoreApplication.translate("Dialog", u"General manager", None))
        self.job_drop.setItemText(1, QCoreApplication.translate("Dialog", u"Head Security", None))
        self.job_drop.setItemText(2, QCoreApplication.translate("Dialog", u"Sales employee", None))

        self.job_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Job Title ", None))
        self.label_83.setText(QCoreApplication.translate("Dialog", u"Department", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_86.setText(QCoreApplication.translate("Dialog", u"Job Title", None))
        self.label_84.setText(QCoreApplication.translate("Dialog", u"Access Categroy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Employee Registration", None))
        self.label_66.setText(QCoreApplication.translate("Dialog", u"E-Mail", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Gender", None))
        self.attend_drop.setItemText(0, QCoreApplication.translate("Dialog", u"New Item", None))
        self.attend_drop.setItemText(1, QCoreApplication.translate("Dialog", u"New Item", None))
        self.attend_drop.setItemText(2, QCoreApplication.translate("Dialog", u"New Item", None))

        self.attend_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Attendance Scheme ", None))
        self.photo_label.setText("")
        self.email_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Email", None))
        self.phone_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Phone Number", None))
        self.label_68.setText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Middle Name", None))
        self.access_drop.setItemText(0, QCoreApplication.translate("Dialog", u"A", None))
        self.access_drop.setItemText(1, QCoreApplication.translate("Dialog", u"B", None))
        self.access_drop.setItemText(2, QCoreApplication.translate("Dialog", u"C", None))

        self.access_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Acess Categroy", None))
        self.label_67.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.address_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Address", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Female", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"First Name ", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Date of birth", None))
        self.dep_drop.setItemText(0, QCoreApplication.translate("Dialog", u"Management", None))
        self.dep_drop.setItemText(1, QCoreApplication.translate("Dialog", u"Information Technology", None))
        self.dep_drop.setItemText(2, QCoreApplication.translate("Dialog", u"Sales", None))
        self.dep_drop.setItemText(3, QCoreApplication.translate("Dialog", u"Accounting", None))
        self.dep_drop.setItemText(4, QCoreApplication.translate("Dialog", u"Security", None))
        self.dep_drop.setItemText(5, QCoreApplication.translate("Dialog", u"Housekeeping", None))

        self.dep_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Department", None))
        self.addphoto_button.setText(QCoreApplication.translate("Dialog", u"Add Photo", None))
        self.capture_button.setText(QCoreApplication.translate("Dialog", u"Capture model images", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Employee ID", None))
        self.IDlable.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.addphoto_button_2.setText(QCoreApplication.translate("Dialog", u"take photo", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"d/M/yyyy", None))
        self.BackButton.setText(QCoreApplication.translate("Dialog", u"BACK", None))
        self.error.setText("")
    # retranslateUi

