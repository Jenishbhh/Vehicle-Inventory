# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(620, 620)
        SignUp.setStyleSheet(u"background-color: rgb(255,162,154);")
        self.label = QLabel(SignUp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 210, 611, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(SignUp)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 300, 461, 21))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(SignUp)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 340, 461, 21))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(SignUp)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 380, 461, 21))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cpassword = QLineEdit(SignUp)
        self.cpassword.setObjectName(u"cpassword")
        self.cpassword.setGeometry(QRect(340, 380, 161, 21))
        font = QFont()
        font.setPointSize(9)
        self.cpassword.setFont(font)
        self.cpassword.setStyleSheet(u"")
        self.password = QLineEdit(SignUp)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(340, 340, 161, 21))
        self.password.setFont(font)
        self.password.setStyleSheet(u"")
        self.email = QLineEdit(SignUp)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(340, 300, 161, 21))
        self.email.setFont(font)
        self.email.setStyleSheet(u"")
        self.signup = QPushButton(SignUp)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(430, 430, 71, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.signup.setFont(font1)
        self.signup.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.invalid = QLabel(SignUp)
        self.invalid.setObjectName(u"invalid")
        self.invalid.setGeometry(QRect(150, 430, 461, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(9)
        self.invalid.setFont(font2)
        self.invalid.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.invalid.setAlignment(Qt.AlignCenter)
        self.invalid.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.cpassword.raise_()
        self.password.raise_()
        self.email.raise_()
        self.signup.raise_()

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.label_5.setText(QCoreApplication.translate("SignUp", u"              Email : ", None))
        self.label_6.setText(QCoreApplication.translate("SignUp", u"              Password : ", None))
        self.label_7.setText(QCoreApplication.translate("SignUp", u"              Confirm Password : ", None))
        self.cpassword.setText("")
        self.password.setText("")
        self.email.setText("")
        self.signup.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.invalid.setText(QCoreApplication.translate("SignUp", u"Invalid Email!", None))
    # retranslateUi

