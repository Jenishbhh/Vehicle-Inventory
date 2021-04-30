# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login3.ui'
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
        MainWindow.resize(380, 420)
        MainWindow.setMinimumSize(QSize(380, 420))
        MainWindow.setMaximumSize(QSize(380, 420))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(360, 400))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.signUp_layout = QFrame(self.bg)
        self.signUp_layout.setObjectName(u"signUp_layout")
        self.signUp_layout.setGeometry(QRect(0, 20, 360, 780))
        self.signUp_layout.setMinimumSize(QSize(320, 780))
        self.signUp_layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.signUp_layout)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.ogin_layout = QFrame(self.signUp_layout)
        self.ogin_layout.setObjectName(u"ogin_layout")
        self.ogin_layout.setMinimumSize(QSize(320, 360))
        self.ogin_layout.setStyleSheet(u"background-color: rgb(255, 85, 0,30);")
        self.verticalLayout_3 = QVBoxLayout(self.ogin_layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Logo_2 = QFrame(self.ogin_layout)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setMinimumSize(QSize(0, 191))
        self.Logo_2.setMaximumSize(QSize(16777215, 191))
        self.Logo_2.setStyleSheet(u"image: url(:/newPrefix/kisspng-car-ald-automotive-fleet-management-vehicle-adreno-5b134886c28d07.6753176615279904067969.png);\n"
"border-radius: 10px;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background: transparent;")
        self.Logo_2.setFrameShape(QFrame.StyledPanel)
        self.Logo_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.Logo_2)

        self.Email = QLineEdit(self.ogin_layout)
        self.Email.setObjectName(u"Email")
        self.Email.setMinimumSize(QSize(0, 40))
        self.Email.setMaximumSize(QSize(16777215, 40))
        self.Email.setStyleSheet(u"\n"
"QLineEdit {\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(199, 199, 199);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	background: transparent;}\n"
"")
        self.Email.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.verticalLayout_3.addWidget(self.Email)

        self.Password_2 = QLineEdit(self.ogin_layout)
        self.Password_2.setObjectName(u"Password_2")
        self.Password_2.setMinimumSize(QSize(0, 40))
        self.Password_2.setMaximumSize(QSize(16777215, 40))
        self.Password_2.setStyleSheet(u"\n"
"QLineEdit {\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(199, 199, 199);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	background: transparent;}\n"
"")
        self.Password_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.Password_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.Password_2)

        self.Invalid_2 = QLabel(self.ogin_layout)
        self.Invalid_2.setObjectName(u"Invalid_2")
        self.Invalid_2.setMinimumSize(QSize(0, 15))
        self.Invalid_2.setMaximumSize(QSize(16777215, 15))
        self.Invalid_2.setStyleSheet(u"background:transparent;\n"
"\n"
"color: rgb(255, 0, 0);\n"
"")

        self.verticalLayout_3.addWidget(self.Invalid_2, 0, Qt.AlignRight)

        self.pushButton = QPushButton(self.ogin_layout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 15))
        self.pushButton.setMaximumSize(QSize(60, 30))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;")

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.ogin_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Logo = QFrame(self.signUp_layout)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(0, 191))
        self.Logo.setMaximumSize(QSize(16777215, 191))
        self.Logo.setStyleSheet(u"image: url(:/newPrefix/kisspng-car-ald-automotive-fleet-management-vehicle-adreno-5b134886c28d07.6753176615279904067969.png);\n"
"border-radius: 10px;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background: transparent;")
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.Logo)

        self.Email_2 = QLineEdit(self.signUp_layout)
        self.Email_2.setObjectName(u"Email_2")
        self.Email_2.setMinimumSize(QSize(0, 40))
        self.Email_2.setMaximumSize(QSize(16777215, 40))
        self.Email_2.setStyleSheet(u"\n"
"QLineEdit {\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(199, 199, 199);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	background: transparent;}\n"
"")
        self.Email_2.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.verticalLayout_2.addWidget(self.Email_2)

        self.Password = QLineEdit(self.signUp_layout)
        self.Password.setObjectName(u"Password")
        self.Password.setMinimumSize(QSize(0, 40))
        self.Password.setMaximumSize(QSize(16777215, 40))
        self.Password.setStyleSheet(u"\n"
"QLineEdit {\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(199, 199, 199);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	background: transparent;}\n"
"")
        self.Password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.Password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.Password)

        self.c_password = QLineEdit(self.signUp_layout)
        self.c_password.setObjectName(u"c_password")
        self.c_password.setMinimumSize(QSize(0, 40))
        self.c_password.setMaximumSize(QSize(16777215, 40))
        self.c_password.setStyleSheet(u"\n"
"QLineEdit {\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(199, 199, 199);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgbrgb(255, 85, 0);\n"
"	background: transparent;}\n"
"")
        self.c_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.c_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.c_password)

        self.label = QLabel(self.signUp_layout)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setStyleSheet(u"background:transparent;\n"
"\n"
"color: rgb(255, 0, 0);\n"
"")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
        self.Password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.Invalid_2.setText(QCoreApplication.translate("MainWindow", u"    Invalid Email Or Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.Email_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Passeowd", None))
        self.c_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Confirm Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Invalid Email", None))
    # retranslateUi

