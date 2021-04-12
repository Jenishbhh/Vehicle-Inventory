# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(480, 620)
        Login.setStyleSheet(u"background-color: rgb(150, 244, 211);")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 150, 481, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 260, 461, 21))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email = QLineEdit(Login)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(260, 260, 161, 21))
        font = QFont()
        font.setPointSize(9)
        self.email.setFont(font)
        self.email.setStyleSheet(u"")
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 300, 461, 21))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password = QLineEdit(Login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(260, 300, 161, 21))
        self.password.setFont(font)
        self.loginbutton = QPushButton(Login)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(350, 390, 71, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.loginbutton.setFont(font1)
        self.loginbutton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 330, 461, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(9)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.signup = QPushButton(Login)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(350, 360, 71, 21))
        self.signup.setFont(font1)
        self.signup.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.invalid = QLabel(Login)
        self.invalid.setObjectName(u"invalid")
        self.invalid.setGeometry(QRect(70, 360, 461, 21))
        self.invalid.setFont(font2)
        self.invalid.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.invalid.setAlignment(Qt.AlignCenter)
        self.invalid.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.email.raise_()
        self.label_3.raise_()
        self.password.raise_()
        self.loginbutton.raise_()
        self.label_4.raise_()
        self.signup.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Login", u"Log In", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"              Email : ", None))
        self.email.setText("")
        self.label_3.setText(QCoreApplication.translate("Login", u"              Password : ", None))
#if QT_CONFIG(whatsthis)
        self.password.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.loginbutton.setText(QCoreApplication.translate("Login", u"Log in", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"                                                        Don't Have an Acoount?", None))
        self.signup.setText(QCoreApplication.translate("Login", u"Sign Up", None))
        self.invalid.setText(QCoreApplication.translate("Login", u"Invalid Email!", None))
    # retranslateUi

