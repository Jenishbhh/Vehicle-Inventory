

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from pyrebase import pyrebase
import firebase_admin
from firebase_admin import firestore 
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


firebaseConfig={
    'apiKey': "AIzaSyC1_YiXiG7iZEZDP3On60F9YpylViXChsQ",
    'authDomain': "vehicle-inventory-ae254.firebaseapp.com",
    'databaseURL': "https://vehicle-inventory-ae254-default-rtdb.firebaseio.com",
    'projectId': "vehicle-inventory-ae254",
    'storageBucket': "vehicle-inventory-ae254.appspot.com",
    'messagingSenderId': "388336737592",
    'appId': "1:388336737592:web:af0b61b4f1505c6940b5cd",
    'measurementId': "G-GQHKFQN7N6"
}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

## ==> SPLASH SCREEN
from Ui_sceen import Ui_screen



## ==> Log in Window
from Ui_Login import Ui_Login


## ==> Sign Up Class

from Ui_signup import Ui_SignUp

## ==> Add details class

from Ui_User_Details import Ui_User_details

## ==> Booking class
from Ui_Booking import Ui_Booking

## ==> GLOBALS
counter = 0


####################################################################
#  SPLASH SCREEN
####################################################################

class screen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_screen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

##
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropframe.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Login()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

#================================================#
#Login Screen
#================================================#

class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.loginbutton.clicked.connect(self.loginfunction)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.signup.clicked.connect(self.gosignup)
        self.ui.invalid.setVisible(False)

    def loginfunction(self):
        email=self.ui.email.text()
        password=self.ui.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.main=Booking()
            self.main.show()
            self.close()
            
        except:
            self.ui.invalid.setVisible(True)


    def gosignup(self):
        self.main=Signup()
        self.main.show()
        self.close()
        

#================================================#
#signup Screen
#================================================#

class Signup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        self.ui.signup.clicked.connect(self.signupfunction) 
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.invalid.setVisible(False)





    def signupfunction(self):
        
        email=self.ui.email.text()
        if self.ui.password.text()==self.ui.cpassword.text():
            password=self.ui.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                self.main=User_details()
                self.main.show()
                self.close()
                
            except:
                self.ui.invalid.setVisible(True)
            

#================================================#
#Add details
#================================================#

class User_details(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_User_details()
        self.ui.setupUi(self)
        self.ui.submit.clicked.connect(self.user_details_function)


    def user_details_function(self):
        name=self.ui.Name.text()
        address=self.ui.Address.text()
        phone=self.ui.Phone.text()
        v_make=self.ui.V_make.text()
        v_model=self.ui.V_model.text()
        v_year=self.ui.V_year.text()
        user_data={'Name': name, 'Address': address, 'Phone': phone}
        v_data={'Vehicle Make': v_make,'Vehicle Model':v_model,'Vehicle Year': v_year}

        db.collection('User Side').document('User Info').collection(name).document('Persnol Info').set(user_data)
        db.collection('User Side').document('User Info').collection(name).document('Vehicle').collection('Vehicle Info').document(v_make).set(v_data)
        self.main=Booking()
        self.main.show()
        self.close()



            
        
#================================================#
#Booking
#================================================#

class Booking(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Booking()
        self.ui.setupUi(self)

        

        
            

            
        



                                                 










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = screen()
    sys.exit(app.exec_())