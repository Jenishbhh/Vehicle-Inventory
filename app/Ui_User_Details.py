# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Details.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_User_details(object):
    def setupUi(self, User_details):
        if not User_details.objectName():
            User_details.setObjectName(u"User_details")
        User_details.resize(680, 680)
        self.frame = QFrame(User_details)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 681, 681))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 150, 671, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(2, 270, 671, 29))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 310, 671, 29))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 350, 671, 29))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 390, 671, 29))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 430, 671, 29))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 470, 671, 29))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.V_model = QLineEdit(self.frame)
        self.V_model.setObjectName(u"V_model")
        self.V_model.setGeometry(QRect(370, 440, 113, 21))
        self.V_model.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.V_year = QLineEdit(self.frame)
        self.V_year.setObjectName(u"V_year")
        self.V_year.setGeometry(QRect(370, 480, 113, 21))
        self.V_year.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.V_make = QLineEdit(self.frame)
        self.V_make.setObjectName(u"V_make")
        self.V_make.setGeometry(QRect(370, 400, 113, 21))
        self.V_make.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Phone = QLineEdit(self.frame)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setGeometry(QRect(370, 360, 113, 21))
        self.Phone.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Address = QLineEdit(self.frame)
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(370, 320, 113, 21))
        self.Address.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Name = QLineEdit(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(370, 280, 113, 21))
        self.Name.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.54, stop:0 rgba(131, 131, 131, 255), stop:1 rgba(255, 255, 255, 255));")
        self.submit = QPushButton(self.frame)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(420, 520, 61, 16))
        font = QFont()
        font.setPointSize(8)
        self.submit.setFont(font)
        self.submit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(188, 188, 188);")

        self.retranslateUi(User_details)

        QMetaObject.connectSlotsByName(User_details)
    # setupUi

    def retranslateUi(self, User_details):
        User_details.setWindowTitle(QCoreApplication.translate("User_details", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("User_details", u"Add Details", None))
        self.label_2.setText(QCoreApplication.translate("User_details", u"                         Name :", None))
        self.label_3.setText(QCoreApplication.translate("User_details", u"                         Address :", None))
        self.label_4.setText(QCoreApplication.translate("User_details", u"                         Phone num :", None))
        self.label_5.setText(QCoreApplication.translate("User_details", u"                         Vehicle Make :", None))
        self.label_6.setText(QCoreApplication.translate("User_details", u"                         Vehicle Model :", None))
        self.label_7.setText(QCoreApplication.translate("User_details", u"                         Vehicle Year :", None))
        self.submit.setText(QCoreApplication.translate("User_details", u"Submit", None))
    # retranslateUi

