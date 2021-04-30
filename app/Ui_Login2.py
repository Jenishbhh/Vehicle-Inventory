# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 455)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(10, 10, 601, 421))
        self.bg.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"QLabel {\n"
"	color:  rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-top: 20px;\n"
"}\n"
".QLineEdit {\n"
"	border: 3px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.bg)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 581, 401))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.horizontalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Login = QFrame(self.frame)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(10, 10, 291, 371))
        self.Login.setStyleSheet(u"alternate-background-color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Login.setFrameShape(QFrame.StyledPanel)
        self.Login.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.Login)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 230, 251, 41))
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.username.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.password = QLineEdit(self.Login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 280, 251, 41))
        self.password.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.frame_2 = QFrame(self.Login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 271, 191))
        self.frame_2.setStyleSheet(u"\n"
"image: url(:/newPrefix/kisspng-car-ald-automotive-fleet-management-vehicle-adreno-5b134886c28d07.6753176615279904067969.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(146, 330, 111, 16))
        self.Signup = QFrame(self.frame)
        self.Signup.setObjectName(u"Signup")
        self.Signup.setGeometry(QRect(300, 10, 261, 371))
        self.Signup.setStyleSheet(u"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.Signup.setFrameShape(QFrame.StyledPanel)
        self.Signup.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.Signup)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 40, 221, 291))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 181, 201))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 19pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 210, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Forgot your Password", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hello, There!\n"
"Welcome To \n"
"ALD Automotive\n"
"", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
    # retranslateUi

