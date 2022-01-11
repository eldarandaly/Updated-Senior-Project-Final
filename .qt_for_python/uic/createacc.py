# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createacc.ui'
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
        Dialog.resize(1542, 963)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 1551, 1031))
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(620, 150, 211, 71))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.signup = QPushButton(self.bgwidget)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(430, 770, 341, 51))
        self.signup.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.emailfield = QLineEdit(self.bgwidget)
        self.emailfield.setObjectName(u"emailfield")
        self.emailfield.setGeometry(QRect(590, 440, 341, 51))
        self.emailfield.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.emailfield.setClearButtonEnabled(True)
        self.passwordfield = QLineEdit(self.bgwidget)
        self.passwordfield.setObjectName(u"passwordfield")
        self.passwordfield.setGeometry(QRect(590, 570, 341, 51))
        self.passwordfield.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.passwordfield.setClearButtonEnabled(True)
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 390, 171, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.bgwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(600, 520, 121, 21))
        self.label_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.error = QLabel(self.bgwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(440, 540, 341, 20))
        self.error.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.label_5 = QLabel(self.bgwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(600, 640, 201, 21))
        self.label_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.confirmpasswordfield = QLineEdit(self.bgwidget)
        self.confirmpasswordfield.setObjectName(u"confirmpasswordfield")
        self.confirmpasswordfield.setGeometry(QRect(590, 690, 341, 51))
        self.confirmpasswordfield.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.confirmpasswordfield.setClearButtonEnabled(True)
        self.label_7 = QLabel(self.bgwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(600, 270, 171, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.empid = QLineEdit(self.bgwidget)
        self.empid.setObjectName(u"empid")
        self.empid.setGeometry(QRect(590, 320, 341, 51))
        self.empid.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.empid.setClearButtonEnabled(True)
        self.CancelButton = QPushButton(self.bgwidget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(790, 770, 341, 51))
        self.CancelButton.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.signup.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.emailfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Employee User Name", None))
        self.passwordfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Employee Password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.error.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.confirmpasswordfield.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm Employee Password", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Employee ID", None))
        self.empid.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Employee ID", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

