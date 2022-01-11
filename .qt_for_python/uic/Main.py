# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
        self.First_line = QLineEdit(self.centralwidget)
        self.First_line.setObjectName(u"First_line")
        self.First_line.setGeometry(QRect(800, 310, 251, 41))
        self.First_line.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"")
        self.middle_line = QLineEdit(self.centralwidget)
        self.middle_line.setObjectName(u"middle_line")
        self.middle_line.setGeometry(QRect(80, 310, 261, 41))
        self.middle_line.setStyleSheet(u"background: #fff;\n"
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
        self.last_line = QLineEdit(self.centralwidget)
        self.last_line.setObjectName(u"last_line")
        self.last_line.setGeometry(QRect(410, 310, 271, 41))
        self.last_line.setStyleSheet(u"background: #fff;\n"
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
        self.addphoto_button.setGeometry(QRect(1230, 340, 141, 51))
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
        self.comboBox_10 = QComboBox(self.centralwidget)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(590, 440, 111, 41))
        self.comboBox_10.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(500, 390, 151, 21))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox_8 = QComboBox(self.centralwidget)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(470, 440, 81, 41))
        self.comboBox_8.setStyleSheet(u" border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.comboBox_9 = QComboBox(self.centralwidget)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(730, 440, 121, 41))
        self.comboBox_9.setStyleSheet(u" border-radius: 20px;\n"
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
        self.lineEdit_26 = QLineEdit(self.centralwidget)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(90, 570, 581, 41))
        self.lineEdit_26.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_68 = QLabel(self.centralwidget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(120, 650, 171, 31))
        self.label_68.setFont(font1)
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_27 = QLineEdit(self.centralwidget)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(410, 700, 281, 41))
        self.lineEdit_27.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"")
        self.lineEdit_28 = QLineEdit(self.centralwidget)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(100, 700, 251, 41))
        self.lineEdit_28.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(830, 860, 191, 61))
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"\n"
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
        self.comboBox_35 = QComboBox(self.centralwidget)
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.setObjectName(u"comboBox_35")
        self.comboBox_35.setGeometry(QRect(810, 580, 271, 41))
        self.comboBox_35.setStyleSheet(u"background: #fff;\n"
"font: 12pt \"Microsoft JhengHei\";\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_83 = QLabel(self.centralwidget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(880, 520, 151, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox_36 = QComboBox(self.centralwidget)
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.setObjectName(u"comboBox_36")
        self.comboBox_36.setGeometry(QRect(1170, 710, 271, 41))
        self.comboBox_36.setStyleSheet(u"background: #fff;\n"
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
        self.comboBox_37 = QComboBox(self.centralwidget)
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.setObjectName(u"comboBox_37")
        self.comboBox_37.setGeometry(QRect(1160, 580, 281, 41))
        self.comboBox_37.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;\n"
"font: 12pt \"Microsoft JhengHei\";")
        self.label_86 = QLabel(self.centralwidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1180, 530, 100, 21))
        self.label_86.setFont(font2)
        self.label_86.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.comboBox_38 = QComboBox(self.centralwidget)
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.setObjectName(u"comboBox_38")
        self.comboBox_38.setGeometry(QRect(830, 710, 241, 41))
        self.comboBox_38.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(600, 860, 181, 61))
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setMouseTracking(True)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setFlat(True)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(100, 440, 81, 20))
        self.checkBox.setStyleSheet(u"font: 12pt \"Microsoft JhengHei\";")
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(210, 440, 101, 21))
        self.checkBox_2.setStyleSheet(u"font: 12pt \"Microsoft JhengHei\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.addphoto_button.setDefault(True)
        self.pushButton_14.setDefault(True)


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
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"1999", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"1998", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"1997", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"1996", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"1995", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"1994", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("MainWindow", u"1993", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("MainWindow", u"1992", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("MainWindow", u"1991", None))
        self.comboBox_10.setItemText(9, QCoreApplication.translate("MainWindow", u"1990", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_8.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_8.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_8.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_8.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_8.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_8.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_8.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_8.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_8.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_8.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_8.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_8.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_8.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_8.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_8.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_8.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_8.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_8.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_8.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_8.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_8.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.comboBox_8.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_8.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_8.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_8.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"January", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"February", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"March", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"April", None))
        self.comboBox_9.setItemText(4, QCoreApplication.translate("MainWindow", u"May", None))
        self.comboBox_9.setItemText(5, QCoreApplication.translate("MainWindow", u"June", None))
        self.comboBox_9.setItemText(6, QCoreApplication.translate("MainWindow", u"July", None))
        self.comboBox_9.setItemText(7, QCoreApplication.translate("MainWindow", u"August", None))
        self.comboBox_9.setItemText(8, QCoreApplication.translate("MainWindow", u"september", None))
        self.comboBox_9.setItemText(9, QCoreApplication.translate("MainWindow", u"October", None))
        self.comboBox_9.setItemText(10, QCoreApplication.translate("MainWindow", u"November", None))
        self.comboBox_9.setItemText(11, QCoreApplication.translate("MainWindow", u"December", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.comboBox_35.setItemText(0, "")
        self.comboBox_35.setItemText(1, QCoreApplication.translate("MainWindow", u"Management", None))
        self.comboBox_35.setItemText(2, QCoreApplication.translate("MainWindow", u"Information Technology", None))
        self.comboBox_35.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.comboBox_35.setItemText(4, QCoreApplication.translate("MainWindow", u"Accounting", None))
        self.comboBox_35.setItemText(5, QCoreApplication.translate("MainWindow", u"Security", None))
        self.comboBox_35.setItemText(6, QCoreApplication.translate("MainWindow", u"Housekeeping", None))

        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.comboBox_36.setItemText(0, "")
        self.comboBox_36.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox_36.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_36.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))

        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Access Categroy", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Attendance Scheme ", None))
        self.comboBox_37.setItemText(0, "")
        self.comboBox_37.setItemText(1, QCoreApplication.translate("MainWindow", u"General manager", None))
        self.comboBox_37.setItemText(2, QCoreApplication.translate("MainWindow", u"Head Security", None))
        self.comboBox_37.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales employee", None))

        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.comboBox_38.setItemText(0, "")
        self.comboBox_38.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_38.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_38.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Female", None))
    # retranslateUi

