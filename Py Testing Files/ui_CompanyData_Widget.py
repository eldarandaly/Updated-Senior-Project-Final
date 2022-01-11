# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CompanyData_WidgetffaLqz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1101, 711)
        Form.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Info_Tabs = QTabWidget(Form)
        self.Info_Tabs.setObjectName(u"Info_Tabs")
        font = QFont()
        font.setFamily(u"Old Antic Bold")
        font.setPointSize(14)
        font.setKerning(True)
        self.Info_Tabs.setFont(font)
        self.Info_Tabs.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"\n"
"")
        self.DepTap = QWidget()
        self.DepTap.setObjectName(u"DepTap")
        self.label = QLabel(self.DepTap)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 291, 101))
        font1 = QFont()
        font1.setFamily(u"Old Antic Bold")
        font1.setPointSize(32)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.DepTap)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 290, 211, 31))
        font2 = QFont()
        font2.setFamily(u"Old Antic Bold")
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.DepTap)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 210, 191, 51))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.insertdep_button = QPushButton(self.DepTap)
        self.insertdep_button.setObjectName(u"insertdep_button")
        self.insertdep_button.setGeometry(QRect(120, 420, 141, 61))
        self.insertdep_button.setFont(font2)
        self.insertdep_button.setStyleSheet(u"color: White;\n"
"\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.dep_line = QLineEdit(self.DepTap)
        self.dep_line.setObjectName(u"dep_line")
        self.dep_line.setGeometry(QRect(260, 290, 161, 41))
        font3 = QFont()
        font3.setFamily(u"Old Antic Bold")
        font3.setPointSize(14)
        self.dep_line.setFont(font3)
        self.dep_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.dep_line.setClearButtonEnabled(True)
        self.depid_line = QLineEdit(self.DepTap)
        self.depid_line.setObjectName(u"depid_line")
        self.depid_line.setGeometry(QRect(240, 220, 161, 41))
        self.depid_line.setFont(font3)
        self.depid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.depid_line.setClearButtonEnabled(True)
        self.updep_button = QPushButton(self.DepTap)
        self.updep_button.setObjectName(u"updep_button")
        self.updep_button.setGeometry(QRect(330, 420, 151, 61))
        self.updep_button.setFont(font2)
        self.updep_button.setStyleSheet(u"color: White;\n"
"\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.depid_line_2 = QLineEdit(self.DepTap)
        self.depid_line_2.setObjectName(u"depid_line_2")
        self.depid_line_2.setGeometry(QRect(20, 120, 341, 41))
        self.depid_line_2.setFont(font3)
        self.depid_line_2.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.depid_line_2.setClearButtonEnabled(True)
        self.pushButton = QPushButton(self.DepTap)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 110, 75, 23))
        self.pushButton_2 = QPushButton(self.DepTap)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 210, 75, 23))
        self.Info_Tabs.addTab(self.DepTap, "")
        self.JobTab = QWidget()
        self.JobTab.setObjectName(u"JobTab")
        self.label_6 = QLabel(self.JobTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 371, 71))
        font4 = QFont()
        font4.setFamily(u"Old Antic Bold")
        font4.setPointSize(32)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.upjob_button = QPushButton(self.JobTab)
        self.upjob_button.setObjectName(u"upjob_button")
        self.upjob_button.setGeometry(QRect(290, 380, 141, 61))
        self.upjob_button.setFont(font2)
        self.upjob_button.setStyleSheet(u"color: White;\n"
"\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.insertjob_button = QPushButton(self.JobTab)
        self.insertjob_button.setObjectName(u"insertjob_button")
        self.insertjob_button.setGeometry(QRect(120, 380, 141, 61))
        self.insertjob_button.setFont(font2)
        self.insertjob_button.setStyleSheet(u"color: White;\n"
"\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.jobid_line = QLineEdit(self.JobTab)
        self.jobid_line.setObjectName(u"jobid_line")
        self.jobid_line.setGeometry(QRect(260, 260, 171, 41))
        font5 = QFont()
        font5.setPointSize(22)
        self.jobid_line.setFont(font5)
        self.jobid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.job_line = QLineEdit(self.JobTab)
        self.job_line.setObjectName(u"job_line")
        self.job_line.setGeometry(QRect(260, 190, 171, 41))
        self.job_line.setFont(font5)
        self.job_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_9 = QLabel(self.JobTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 250, 141, 41))
        font6 = QFont()
        font6.setFamily(u"Old Antic Bold")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_8 = QLabel(self.JobTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 190, 151, 31))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.depid_line_3 = QLineEdit(self.JobTab)
        self.depid_line_3.setObjectName(u"depid_line_3")
        self.depid_line_3.setGeometry(QRect(30, 100, 341, 41))
        self.depid_line_3.setFont(font3)
        self.depid_line_3.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.depid_line_3.setClearButtonEnabled(True)
        self.Info_Tabs.addTab(self.JobTab, "")
        self.AttendanceTab = QWidget()
        self.AttendanceTab.setObjectName(u"AttendanceTab")
        self.attid_line = QLineEdit(self.AttendanceTab)
        self.attid_line.setObjectName(u"attid_line")
        self.attid_line.setGeometry(QRect(450, 110, 221, 41))
        self.attid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_10 = QLabel(self.AttendanceTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 330, 191, 51))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.AttendanceTab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 100, 301, 61))
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.insertatt_button = QPushButton(self.AttendanceTab)
        self.insertatt_button.setObjectName(u"insertatt_button")
        self.insertatt_button.setGeometry(QRect(680, 570, 151, 61))
        self.insertatt_button.setFont(font2)
        self.insertatt_button.setStyleSheet(u"color: White;\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.label_17 = QLabel(self.AttendanceTab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(140, 430, 181, 51))
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.attjob_drop = QComboBox(self.AttendanceTab)
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.setObjectName(u"attjob_drop")
        self.attjob_drop.setGeometry(QRect(450, 210, 221, 41))
        self.attjob_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_18 = QLabel(self.AttendanceTab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(150, 210, 181, 51))
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.insertatt_button_2 = QPushButton(self.AttendanceTab)
        self.insertatt_button_2.setObjectName(u"insertatt_button_2")
        self.insertatt_button_2.setGeometry(QRect(860, 570, 151, 61))
        self.insertatt_button_2.setFont(font2)
        self.insertatt_button_2.setStyleSheet(u"color: White;\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.attid_line_3 = QLineEdit(self.AttendanceTab)
        self.attid_line_3.setObjectName(u"attid_line_3")
        self.attid_line_3.setGeometry(QRect(450, 340, 221, 41))
        self.attid_line_3.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.attid_line_4 = QLineEdit(self.AttendanceTab)
        self.attid_line_4.setObjectName(u"attid_line_4")
        self.attid_line_4.setGeometry(QRect(450, 430, 221, 41))
        self.attid_line_4.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.Info_Tabs.addTab(self.AttendanceTab, "")
        self.AccesTab = QWidget()
        self.AccesTab.setObjectName(u"AccesTab")
        self.label_12 = QLabel(self.AccesTab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(150, 280, 201, 51))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.AccesTab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(150, 110, 211, 51))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.acc_line = QLineEdit(self.AccesTab)
        self.acc_line.setObjectName(u"acc_line")
        self.acc_line.setGeometry(QRect(460, 290, 221, 41))
        self.acc_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.insertacc_button = QPushButton(self.AccesTab)
        self.insertacc_button.setObjectName(u"insertacc_button")
        self.insertacc_button.setGeometry(QRect(360, 510, 151, 61))
        self.insertacc_button.setFont(font2)
        self.insertacc_button.setStyleSheet(u"color: White;\n"
"\n"
"background-color: #303030 ;\n"
"border-radius: 12px;")
        self.accid_line = QLineEdit(self.AccesTab)
        self.accid_line.setObjectName(u"accid_line")
        self.accid_line.setGeometry(QRect(450, 110, 221, 41))
        self.accid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.gate_drop = QComboBox(self.AccesTab)
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.setObjectName(u"gate_drop")
        self.gate_drop.setGeometry(QRect(460, 390, 221, 41))
        self.gate_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_19 = QLabel(self.AccesTab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(150, 210, 201, 51))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.AccesTab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(160, 380, 201, 51))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.accjob_drop = QComboBox(self.AccesTab)
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.setObjectName(u"accjob_drop")
        self.accjob_drop.setGeometry(QRect(450, 210, 221, 41))
        self.accjob_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.Info_Tabs.addTab(self.AccesTab, "")

        self.verticalLayout.addWidget(self.Info_Tabs)


        self.retranslateUi(Form)

        self.Info_Tabs.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Information ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Departments", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Department Desc.", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Department ID", None))
        self.insertdep_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.updep_button.setText(QCoreApplication.translate("Form", u"Update", None))
        self.depid_line_2.setPlaceholderText(QCoreApplication.translate("Form", u"Serach Bar", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.Info_Tabs.setTabText(self.Info_Tabs.indexOf(self.DepTap), QCoreApplication.translate("Form", u"Department", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Job Description", None))
        self.upjob_button.setText(QCoreApplication.translate("Form", u"Update", None))
        self.insertjob_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Job_ID", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Job title", None))
        self.depid_line_3.setPlaceholderText(QCoreApplication.translate("Form", u"Serach Bar", None))
        self.Info_Tabs.setTabText(self.Info_Tabs.indexOf(self.JobTab), QCoreApplication.translate("Form", u"Job", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Arriving Time", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Attendence Scheme ID", None))
        self.insertatt_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Leaving Time", None))
        self.attjob_drop.setItemText(0, "")
        self.attjob_drop.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.attjob_drop.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))
        self.attjob_drop.setItemText(3, QCoreApplication.translate("Form", u"New Item", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"Assigned Job", None))
        self.insertatt_button_2.setText(QCoreApplication.translate("Form", u"Update", None))
        self.Info_Tabs.setTabText(self.Info_Tabs.indexOf(self.AttendanceTab), QCoreApplication.translate("Form", u"Attendance", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Access Category", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Acess Scheme ID", None))
        self.insertacc_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.gate_drop.setItemText(0, "")
        self.gate_drop.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.gate_drop.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))
        self.gate_drop.setItemText(3, QCoreApplication.translate("Form", u"New Item", None))

        self.label_19.setText(QCoreApplication.translate("Form", u"Allowed Jobs", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Gate", None))
        self.accjob_drop.setItemText(0, "")
        self.accjob_drop.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.accjob_drop.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))
        self.accjob_drop.setItemText(3, QCoreApplication.translate("Form", u"New Item", None))

        self.Info_Tabs.setTabText(self.Info_Tabs.indexOf(self.AccesTab), QCoreApplication.translate("Form", u"Access", None))
    # retranslateUi

