# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestMainWindow.ui'
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
        Dialog.resize(845, 584)
        Dialog.setMinimumSize(QSize(845, 584))
        Dialog.setMaximumSize(QSize(845, 584))
        Dialog.setStyleSheet(u"\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamily(u"Old Antic Bold")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 60, 821, 511))
        font1 = QFont()
        font1.setFamily(u"Old Antic Bold")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox_2.setFont(font1)
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-60, 50, 261, 40))
        font2 = QFont()
        font2.setFamily(u"Old Antic Bold")
        font2.setPointSize(16)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 100, 0);")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-40, 130, 241, 41))
        font3 = QFont()
        font3.setFamily(u"Old Antic Bold")
        font3.setPointSize(18)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.TrainButton = QPushButton(self.groupBox_2)
        self.TrainButton.setObjectName(u"TrainButton")
        self.TrainButton.setGeometry(QRect(-90, 210, 291, 40))
        self.TrainButton.setFont(font2)
        self.TrainButton.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 100, 0);")
        self.TakeAtt = QPushButton(self.groupBox_2)
        self.TakeAtt.setObjectName(u"TakeAtt")
        self.TakeAtt.setGeometry(QRect(-30, 290, 231, 41))
        self.TakeAtt.setFont(font3)
        self.TakeAtt.setStyleSheet(u"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.logoutButton = QPushButton(self.groupBox)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(750, 30, 71, 23))

        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Home", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Tools", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"New Employee", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Company Info", None))
        self.TrainButton.setText(QCoreApplication.translate("Dialog", u"Train Model", None))
        self.TakeAtt.setText(QCoreApplication.translate("Dialog", u"Take Attendace", None))
        self.logoutButton.setText(QCoreApplication.translate("Dialog", u"LogOut", None))
    # retranslateUi

