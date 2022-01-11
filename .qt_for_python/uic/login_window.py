# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(619, 556)
        login.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"background-color: rgb(155, 204, 255);")
        self.login_button = QPushButton(login)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(230, 370, 141, 51))
        font = QFont()
        font.setFamily(u"Microsoft JhengHei")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setMouseTracking(True)
        self.login_button.setStyleSheet(u"QPushButton {\n"
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
        self.login_button.setAutoDefault(True)
        self.login_button.setFlat(True)
        self.pass_line = QLineEdit(login)
        self.pass_line.setObjectName(u"pass_line")
        self.pass_line.setGeometry(QRect(160, 270, 271, 41))
        self.pass_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.user_line = QLineEdit(login)
        self.user_line.setObjectName(u"user_line")
        self.user_line.setGeometry(QRect(160, 170, 271, 41))
        self.user_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 110, 141, 51))
        self.label.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 230, 131, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(login)

        self.login_button.setDefault(True)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"login", None))
        self.login_button.setText(QCoreApplication.translate("login", u"login", None))
        self.label.setText(QCoreApplication.translate("login", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Password:", None))
    # retranslateUi

