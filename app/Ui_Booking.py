# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Booking.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Booking(object):
    def setupUi(self, Booking):
        if not Booking.objectName():
            Booking.setObjectName(u"Booking")
        Booking.resize(800, 600)
        self.centralwidget = QWidget(Booking)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 110, 771, 61))
        font = QFont()
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)
        self.Cust_num = QLabel(self.centralwidget)
        self.Cust_num.setObjectName(u"Cust_num")
        self.Cust_num.setGeometry(QRect(40, 50, 121, 21))
        font1 = QFont()
        font1.setPointSize(13)
        self.Cust_num.setFont(font1)
        self.Cust_name = QLabel(self.centralwidget)
        self.Cust_name.setObjectName(u"Cust_name")
        self.Cust_name.setGeometry(QRect(40, 80, 121, 16))
        self.Cust_name.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 210, 51, 21))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_2.setFont(font2)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(340, 210, 110, 22))
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"")
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(340, 250, 118, 22))
        self.timeEdit.setFont(font2)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 250, 51, 21))
        self.label_5.setFont(font2)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(460, 210, 25, 19))
        self.toolButton.setCheckable(False)
        self.toolButton.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(460, 250, 25, 19))
        self.problem = QTextEdit(self.centralwidget)
        self.problem.setObjectName(u"problem")
        self.problem.setGeometry(QRect(330, 290, 221, 121))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(236, 300, 81, 20))
        self.label_6.setFont(font2)
        self.submit = QPushButton(self.centralwidget)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(330, 420, 75, 23))
        self.submit.setFont(font1)
        self.reset = QPushButton(self.centralwidget)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(330, 460, 75, 23))
        self.reset.setFont(font1)
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(470, 420, 75, 23))
        self.back.setFont(font1)
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(470, 460, 75, 23))
        self.exit.setFont(font1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 791, 601))
        self.frame.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        Booking.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.Title.raise_()
        self.Cust_num.raise_()
        self.Cust_name.raise_()
        self.label_2.raise_()
        self.dateEdit.raise_()
        self.timeEdit.raise_()
        self.label_5.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        self.label_6.raise_()
        self.submit.raise_()
        self.reset.raise_()
        self.back.raise_()
        self.exit.raise_()
        self.problem.raise_()

        self.retranslateUi(Booking)

        QMetaObject.connectSlotsByName(Booking)
    # setupUi

    def retranslateUi(self, Booking):
        Booking.setWindowTitle(QCoreApplication.translate("Booking", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("Booking", u"Booking ", None))
        self.Cust_num.setText(QCoreApplication.translate("Booking", u"Cust Num: ", None))
        self.Cust_name.setText(QCoreApplication.translate("Booking", u"Cust Name: ", None))
        self.label_2.setText(QCoreApplication.translate("Booking", u"Date:", None))
        self.label_5.setText(QCoreApplication.translate("Booking", u"Time:", None))
        self.toolButton.setText("")
        self.toolButton_2.setText(QCoreApplication.translate("Booking", u"...", None))
        self.problem.setHtml(QCoreApplication.translate("Booking", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.problem.setPlaceholderText(QCoreApplication.translate("Booking", u"Please Enter the Problem that you faced...", None))
        self.label_6.setText(QCoreApplication.translate("Booking", u"Problem:", None))
        self.submit.setText(QCoreApplication.translate("Booking", u"Submit", None))
        self.reset.setText(QCoreApplication.translate("Booking", u"Reset", None))
        self.back.setText(QCoreApplication.translate("Booking", u"Back", None))
        self.exit.setText(QCoreApplication.translate("Booking", u"Exit", None))
    # retranslateUi

