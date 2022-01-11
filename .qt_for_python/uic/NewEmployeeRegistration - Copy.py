# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewEmployeeRegistration - Copy.ui'
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
        Dialog.setStyleSheet(u"\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #ffffff;\n"
"    background-color: #323232;\n"
"	font: 75 20pt \"Barlow\";\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGra"
                        "dient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    bord"
                        "er-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
""
                        "QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-rig"
                        "ht-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop:"
                        " 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
""
                        "QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      b"
                        "ackground: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    back"
                        "ground-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::h"
                        "andle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1"
                        "px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::ind"
                        "icator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4p"
                        "x;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"")
        self.first_line = QLineEdit(Dialog)
        self.first_line.setObjectName(u"first_line")
        self.first_line.setGeometry(QRect(40, 300, 261, 41))
        font = QFont()
        font.setFamily(u"Barlow")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.first_line.setFont(font)
        self.first_line.setStyleSheet(u"\n"
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
        font1.setFamily(u"Barlow")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(True)
        font1.setWeight(9)
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"")
        self.middle_line = QLineEdit(Dialog)
        self.middle_line.setObjectName(u"middle_line")
        self.middle_line.setGeometry(QRect(370, 300, 271, 41))
        self.middle_line.setFont(font)
        self.middle_line.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.middle_line.setClearButtonEnabled(True)
        self.last_line = QLineEdit(Dialog)
        self.last_line.setObjectName(u"last_line")
        self.last_line.setGeometry(QRect(730, 300, 251, 41))
        self.last_line.setFont(font)
        self.last_line.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.last_line.setClearButtonEnabled(True)
        self.job_drop = QComboBox(Dialog)
        self.job_drop.setObjectName(u"job_drop")
        self.job_drop.setGeometry(QRect(1120, 570, 281, 41))
        self.job_drop.setFont(font)
        self.job_drop.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.job_drop.setIconSize(QSize(16, 16))
        self.job_drop.setFrame(True)
        self.label_83 = QLabel(Dialog)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(840, 530, 151, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"")
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(600, 840, 161, 61))
        font2 = QFont()
        font2.setFamily(u"Barlow")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.cancel_button.setFont(font2)
        self.cancel_button.setStyleSheet(u"    border-radius: 20px;")
        self.label_86 = QLabel(Dialog)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1170, 530, 111, 31))
        self.label_86.setFont(font1)
        self.label_86.setStyleSheet(u"")
        self.label_84 = QLabel(Dialog)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(1140, 630, 231, 41))
        self.label_84.setFont(font1)
        self.label_84.setStyleSheet(u"")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 441, 71))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"")
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_66 = QLabel(Dialog)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(460, 640, 91, 31))
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"")
        self.attend_drop = QComboBox(Dialog)
        self.attend_drop.setObjectName(u"attend_drop")
        self.attend_drop.setGeometry(QRect(790, 690, 271, 41))
        self.attend_drop.setFont(font)
        self.attend_drop.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.photo_label = QLabel(Dialog)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(1060, 20, 431, 271))
        self.photo_label.setFont(font)
        self.photo_label.setAutoFillBackground(False)
        self.photo_label.setStyleSheet(u"\n"
"border-radius: 90px;")
        self.photo_label.setFrameShape(QFrame.Box)
        self.email_line = QLineEdit(Dialog)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(330, 690, 411, 41))
        self.email_line.setFont(font)
        self.email_line.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.email_line.setClearButtonEnabled(True)
        self.phone_line = QLineEdit(Dialog)
        self.phone_line.setObjectName(u"phone_line")
        self.phone_line.setGeometry(QRect(60, 690, 251, 41))
        self.phone_line.setFont(font)
        self.phone_line.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.phone_line.setClearButtonEnabled(True)
        self.label_68 = QLabel(Dialog)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(80, 640, 191, 31))
        self.label_68.setFont(font1)
        self.label_68.setStyleSheet(u"")
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(400, 840, 171, 61))
        self.save_button.setFont(font2)
        self.save_button.setMouseTracking(True)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setStyleSheet(u"    border-radius: 20px;")
        self.save_button.setAutoDefault(True)
        self.save_button.setFlat(True)
        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(790, 250, 161, 41))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(430, 250, 161, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"")
        self.access_drop = QComboBox(Dialog)
        self.access_drop.setObjectName(u"access_drop")
        self.access_drop.setGeometry(QRect(1120, 690, 281, 41))
        self.access_drop.setFont(font)
        self.access_drop.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.label_67 = QLabel(Dialog)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(80, 510, 221, 41))
        self.label_67.setFont(font1)
        self.label_67.setStyleSheet(u"")
        self.address_line = QLineEdit(Dialog)
        self.address_line.setObjectName(u"address_line")
        self.address_line.setGeometry(QRect(50, 560, 581, 41))
        self.address_line.setFont(font)
        self.address_line.setStyleSheet(u"\n"
"\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.address_line.setClearButtonEnabled(True)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 250, 141, 41))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")
        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(460, 380, 151, 31))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"")
        self.dep_drop = QComboBox(Dialog)
        self.dep_drop.setObjectName(u"dep_drop")
        self.dep_drop.setGeometry(QRect(790, 570, 271, 41))
        self.dep_drop.setFont(font)
        self.dep_drop.setStyleSheet(u"width: 100px;\n"
"height: 100px;\n"
"border-radius: 20px;\n"
"")
        self.dep_drop.setFrame(True)
        self.addphoto_button = QPushButton(Dialog)
        self.addphoto_button.setObjectName(u"addphoto_button")
        self.addphoto_button.setGeometry(QRect(1150, 330, 151, 51))
        self.addphoto_button.setFont(font2)
        self.addphoto_button.setMouseTracking(True)
        self.addphoto_button.setStyleSheet(u"    border-radius: 20px;")
        self.addphoto_button.setAutoDefault(True)
        self.addphoto_button.setFlat(True)
        self.capture_button = QPushButton(Dialog)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setGeometry(QRect(800, 840, 301, 61))
        self.capture_button.setFont(font2)
        self.capture_button.setMouseTracking(True)
        self.capture_button.setStyleSheet(u"    border-radius: 20px;")
        self.capture_button.setAutoDefault(True)
        self.capture_button.setFlat(True)
        self.takephoto = QPushButton(Dialog)
        self.takephoto.setObjectName(u"takephoto")
        self.takephoto.setGeometry(QRect(1310, 330, 151, 51))
        self.takephoto.setFont(font2)
        self.takephoto.setMouseTracking(True)
        self.takephoto.setStyleSheet(u"    border-radius: 20px;")
        self.takephoto.setAutoDefault(True)
        self.takephoto.setFlat(True)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(460, 430, 201, 71))
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QDateTime(QDate(1972, 12, 20), QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setTimeSpec(Qt.LocalTime)
        self.BackButton = QPushButton(Dialog)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(1270, 840, 151, 61))
        self.BackButton.setFont(font2)
        self.BackButton.setMouseTracking(True)
        self.BackButton.setStyleSheet(u"    border-radius: 20px;")
        self.BackButton.setAutoDefault(True)
        self.BackButton.setFlat(True)
        self.error = QLabel(Dialog)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(460, 130, 361, 51))
        self.error.setFont(font)
        self.error.setStyleSheet(u"color:red")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(50, 370, 331, 141))
        self.groupBox_2.setStyleSheet(u"font-size:20px\n"
"")
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 90, 121, 31))
        self.radioButton_2.setFont(font2)
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QRect(10, 50, 82, 31))
        self.radioButton.setFont(font2)
        self.E2 = QLabel(Dialog)
        self.E2.setObjectName(u"E2")
        self.E2.setGeometry(QRect(910, 440, 361, 51))
        self.E2.setFont(font)
        self.E2.setStyleSheet(u"color:red")

        self.retranslateUi(Dialog)

        self.save_button.setDefault(True)
        self.addphoto_button.setDefault(True)
        self.capture_button.setDefault(True)
        self.takephoto.setDefault(True)
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
        self.job_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Job Title ", None))
        self.label_83.setText(QCoreApplication.translate("Dialog", u"Department", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_86.setText(QCoreApplication.translate("Dialog", u"Job Title", None))
        self.label_84.setText(QCoreApplication.translate("Dialog", u"Access Categroy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Employee Registration", None))
        self.label_66.setText(QCoreApplication.translate("Dialog", u"E-Mail", None))
        self.attend_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Attendance Scheme ", None))
        self.photo_label.setText("")
        self.email_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Email", None))
        self.phone_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Phone Number", None))
        self.label_68.setText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Middle Name", None))
        self.access_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Acess Categroy", None))
        self.label_67.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.address_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Address", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"First Name ", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Date of birth", None))
        self.dep_drop.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select Department", None))
        self.addphoto_button.setText(QCoreApplication.translate("Dialog", u"Add Photo", None))
        self.capture_button.setText(QCoreApplication.translate("Dialog", u"Capture model images", None))
        self.takephoto.setText(QCoreApplication.translate("Dialog", u"Take Photo", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"d/M/yyyy", None))
        self.BackButton.setText(QCoreApplication.translate("Dialog", u"BACK", None))
        self.error.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Gender", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Female", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.E2.setText("")
    # retranslateUi

