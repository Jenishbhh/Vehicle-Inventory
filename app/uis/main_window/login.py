
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer,QEasingCurve
from PyQt5.QtWidgets import *
from PySide6.QtWidgets import *
import os

from app.uis.main_window.Ui_login3 import Ui_MainWindow

from app.Ui_Booking import Ui_Booking
counter=0
class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui=Ui_MainWindow
        self.ui.setupUi(self)

        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)
        self.ui.Email.keyReleaseEvent = self.check_login
        self.ui.Password.keyReleaseEvent = self.check_login
        self.ui.pushButton.clicked(self.update())

    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.Email.text()
            password = self.ui.Password.text()

            def open_main():
                # SHOW MAIN WINDOW
                self.main = Ui_Booking()
                
                self.main.show()                
                self.close()
            if username and password == "123456":
                QTimer.singleShot(1200, lambda: open_main())

            else:
                self.seacke_window()



    def seacke_window(self):
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
       
        self.animation_login()

        # INCREASE COUNTER
       

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    
    
if __name__ == "__main__":
    # LOAD AND SETUP APP SETTINHS FROM JSON FILE
    

    # APPLICATION
    app = QApplication(sys.argv)
    
    window = LoginWindow()
    sys.exit(app.exec_())



