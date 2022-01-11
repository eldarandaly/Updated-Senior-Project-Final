# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainTest.ui'
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
        Dialog.resize(1018, 650)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 490, 171, 51))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 30, 641, 461))
        self.FeedLabel = QLabel(self.groupBox)
        self.FeedLabel.setObjectName(u"FeedLabel")
        self.FeedLabel.setGeometry(QRect(30, 30, 601, 421))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 490, 171, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"open camera", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Camera Window ", None))
        self.FeedLabel.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"detect face", None))
    # retranslateUi

