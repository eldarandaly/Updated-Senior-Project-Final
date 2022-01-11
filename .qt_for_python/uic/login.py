# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Dialog.resize(1600, 1000)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(150,150,150, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 110, 221, 91))
        font = QFont()
        font.setFamily(u"Old Antic Bold")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u" color:rgb(255, 255, 255)")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 200, 391, 41))
        self.label_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.login = QPushButton(self.bgwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(440, 570, 341, 51))
        self.login.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.emailfield = QLineEdit(self.bgwidget)
        self.emailfield.setObjectName(u"emailfield")
        self.emailfield.setGeometry(QRect(440, 330, 341, 51))
        self.emailfield.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;")
        self.passwordfield = QLineEdit(self.bgwidget)
        self.passwordfield.setObjectName(u"passwordfield")
        self.passwordfield.setGeometry(QRect(440, 460, 341, 51))
        self.passwordfield.setStyleSheet(u"background-color:white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"")
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 290, 111, 21))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.bgwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 420, 121, 21))
        self.label_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.error = QLabel(self.bgwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(450, 530, 341, 20))
        self.error.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.CancelButton = QPushButton(self.bgwidget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(440, 640, 341, 51))
        self.CancelButton.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.bgwidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sign in to your existing account", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Log in", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.error.setText("")
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

