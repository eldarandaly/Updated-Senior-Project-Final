# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form - untitled.ui'
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
        Form.resize(1023, 663)
        Form.setStyleSheet(u"background-color: rgb(155, 204, 255);")
        self.info = QTabWidget(Form)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(0, 0, 1241, 761))
        self.info.setStyleSheet(u"background-color: rgb(155, 204, 255);\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 291, 101))
        self.label.setStyleSheet(u"font: 24pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 210, 191, 31))
        self.label_2.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 260, 191, 51))
        self.label_3.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.insertdep_button = QPushButton(self.tab)
        self.insertdep_button.setObjectName(u"insertdep_button")
        self.insertdep_button.setGeometry(QRect(120, 420, 141, 61))
        self.insertdep_button.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.dep_line = QLineEdit(self.tab)
        self.dep_line.setObjectName(u"dep_line")
        self.dep_line.setGeometry(QRect(330, 210, 161, 41))
        self.dep_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.depid_line = QLineEdit(self.tab)
        self.depid_line.setObjectName(u"depid_line")
        self.depid_line.setGeometry(QRect(330, 270, 161, 41))
        self.depid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.updep_button = QPushButton(self.tab)
        self.updep_button.setObjectName(u"updep_button")
        self.updep_button.setGeometry(QRect(330, 420, 151, 61))
        self.updep_button.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.dept_table = QTableWidget(self.tab)
        if (self.dept_table.columnCount() < 2):
            self.dept_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dept_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dept_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.dept_table.rowCount() < 9):
            self.dept_table.setRowCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dept_table.setVerticalHeaderItem(8, __qtablewidgetitem10)
        self.dept_table.setObjectName(u"dept_table")
        self.dept_table.setGeometry(QRect(660, 100, 261, 371))
        self.info.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 20, 331, 101))
        self.label_6.setStyleSheet(u"font: 26pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.job_table = QTableWidget(self.tab_2)
        if (self.job_table.columnCount() < 2):
            self.job_table.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.job_table.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.job_table.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.job_table.rowCount() < 9):
            self.job_table.setRowCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.job_table.setVerticalHeaderItem(8, __qtablewidgetitem21)
        self.job_table.setObjectName(u"job_table")
        self.job_table.setGeometry(QRect(670, 110, 261, 371))
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 140, 581, 411))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.upjob_button = QPushButton(self.frame)
        self.upjob_button.setObjectName(u"upjob_button")
        self.upjob_button.setGeometry(QRect(290, 240, 141, 61))
        self.upjob_button.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 20, 151, 31))
        self.label_8.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.insertjob_button = QPushButton(self.frame)
        self.insertjob_button.setObjectName(u"insertjob_button")
        self.insertjob_button.setGeometry(QRect(120, 240, 141, 61))
        self.insertjob_button.setStyleSheet(u"color: White;\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;\n"
"font: 16pt \"Microsoft JhengHei\";")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 80, 141, 41))
        self.label_9.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.jobid_line = QLineEdit(self.frame)
        self.jobid_line.setObjectName(u"jobid_line")
        self.jobid_line.setGeometry(QRect(320, 90, 171, 41))
        self.jobid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.job_line = QLineEdit(self.frame)
        self.job_line.setObjectName(u"job_line")
        self.job_line.setGeometry(QRect(320, 20, 171, 41))
        self.job_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.info.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.arrive_line = QLineEdit(self.tab_3)
        self.arrive_line.setObjectName(u"arrive_line")
        self.arrive_line.setGeometry(QRect(460, 100, 221, 41))
        self.arrive_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.attid_line = QLineEdit(self.tab_3)
        self.attid_line.setObjectName(u"attid_line")
        self.attid_line.setGeometry(QRect(460, 310, 221, 41))
        self.attid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(160, 100, 191, 51))
        self.label_10.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 300, 271, 61))
        self.label_11.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.insertatt_button = QPushButton(self.tab_3)
        self.insertatt_button.setObjectName(u"insertatt_button")
        self.insertatt_button.setGeometry(QRect(420, 520, 151, 61))
        self.insertatt_button.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.leave_line = QLineEdit(self.tab_3)
        self.leave_line.setObjectName(u"leave_line")
        self.leave_line.setGeometry(QRect(460, 200, 221, 41))
        self.leave_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(160, 200, 181, 51))
        self.label_17.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.attjob_drop = QComboBox(self.tab_3)
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.addItem("")
        self.attjob_drop.setObjectName(u"attjob_drop")
        self.attjob_drop.setGeometry(QRect(460, 410, 221, 41))
        self.attjob_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(160, 410, 181, 51))
        self.label_18.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.info.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 90, 201, 51))
        self.label_12.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(170, 290, 211, 51))
        self.label_13.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.acc_line = QLineEdit(self.tab_4)
        self.acc_line.setObjectName(u"acc_line")
        self.acc_line.setGeometry(QRect(470, 100, 221, 41))
        self.acc_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.insertacc_button = QPushButton(self.tab_4)
        self.insertacc_button.setObjectName(u"insertacc_button")
        self.insertacc_button.setGeometry(QRect(420, 510, 151, 61))
        self.insertacc_button.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.accid_line = QLineEdit(self.tab_4)
        self.accid_line.setObjectName(u"accid_line")
        self.accid_line.setGeometry(QRect(470, 290, 221, 41))
        self.accid_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.gate_drop = QComboBox(self.tab_4)
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.addItem("")
        self.gate_drop.setObjectName(u"gate_drop")
        self.gate_drop.setGeometry(QRect(470, 200, 221, 41))
        self.gate_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_19 = QLabel(self.tab_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 390, 201, 51))
        self.label_19.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.tab_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 190, 201, 51))
        self.label_20.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.accjob_drop = QComboBox(self.tab_4)
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.addItem("")
        self.accjob_drop.setObjectName(u"accjob_drop")
        self.accjob_drop.setGeometry(QRect(470, 390, 221, 41))
        self.accjob_drop.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.info.addTab(self.tab_4, "")

        self.retranslateUi(Form)

        self.info.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Information ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Departments", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Department", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Department ID", None))
        self.insertdep_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.updep_button.setText(QCoreApplication.translate("Form", u"Update", None))
        ___qtablewidgetitem = self.dept_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Department", None));
        ___qtablewidgetitem1 = self.dept_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Dep_ID", None));
        self.info.setTabText(self.info.indexOf(self.tab), QCoreApplication.translate("Form", u"Department", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Job Description", None))
        ___qtablewidgetitem2 = self.job_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Job Title", None));
        ___qtablewidgetitem3 = self.job_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Job ID", None));
        self.upjob_button.setText(QCoreApplication.translate("Form", u"Update", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Job title", None))
        self.insertjob_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Job_ID", None))
        self.info.setTabText(self.info.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Job", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Arriving Time", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Attendence Scheme ID", None))
        self.insertatt_button.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Leaving Time", None))
        self.attjob_drop.setItemText(0, "")
        self.attjob_drop.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.attjob_drop.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))
        self.attjob_drop.setItemText(3, QCoreApplication.translate("Form", u"New Item", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"Assigned Job", None))
        self.info.setTabText(self.info.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Attendance", None))
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

        self.info.setTabText(self.info.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Access", None))
    # retranslateUi

