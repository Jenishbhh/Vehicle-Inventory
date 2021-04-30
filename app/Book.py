from os import name
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import firebase_admin 
from firebase_admin import credentials,firestore
from main import *

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

from Ui_booking2 import Book

class screen(QMainWindow, Login, User_details):
    def __init__(self):
        Login().__init__((self))
        QMainWindow.__init__(self)
        self.ui = Book()
        self.ui.setupUi(self)
        self.ui.loaddata()
        
        

    def loaddata(self):
        result=db.collection('User Side').document('User Info').collection(User_d).document('Vehicle').collection(v_make).get()
        row=0
        self















        self.show()











if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = screen()
    sys.exit(app.exec_())