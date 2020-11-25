from PyQt5 import QtCore, QtGui, QtWidgets
import login_pic
import image
import sys
import student_login
import AD
from PyQt5.QtWidgets import QMessageBox
class A:
    
   def login(self,MainWindow):

       def changefont(self) :
            if self.radioButton.isChecked() : 
            	MainWindow.close();
            	self.MainWindow_1=QtWidgets.QMainWindow()
            	self.ui=student_login.B();
            	self.ui.student(self.MainWindow_1)
            	self.MainWindow_1.show()

            elif self.radioButton_2.isChecked() :
                MainWindow.close();
                self.MainWindow_1=QtWidgets.QMainWindow()
                self.ui=AD.B();
                self.ui.student(self.MainWindow_1)
                self.MainWindow_1.show()

            else :
                msg=QMessageBox()
                msg.setText("Invalid Choice Please Select a Valid choice");  
                msg.setWindowTitle(" ");
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()
 
       MainWindow.resize(800, 525)
       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")
       self.label = QtWidgets.QLabel(self.centralwidget)
       self.label.setGeometry(QtCore.QRect(0, 0, 801, 531))
       self.label.setStyleSheet("background-image: url(:/newPrefix/watermark.PNG);")
       self.label.setText("")
       self.label.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
       self.label.setScaledContents(True)
       self.label_2 = QtWidgets.QLabel(self.centralwidget)
       self.label_2.setGeometry(QtCore.QRect(20, 0, 761, 121))
       self.label_2.setText("")
       self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/logo.png"))
       self.label_2.setScaledContents(True)
       self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
       self.pushButton_2.setGeometry(QtCore.QRect(340, 347, 111, 41))
       self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
       self.radioButton.setGeometry(QtCore.QRect(360, 200, 91, 41))
       self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
       self.radioButton_2.setGeometry(QtCore.QRect(360, 270, 91, 31))
       MainWindow.setCentralWidget(self.centralwidget)
       MainWindow.setWindowTitle("shah and anchor kutchhi engineering college")
       self.pushButton_2.setText("LOGIN")
       self.radioButton.setText("Student")
       self.radioButton_2.setText("Admin")
       self.pushButton_2.clicked.connect(lambda checked:changefont(self))

import mix
if __name__ == "__main__":
      app = QtWidgets.QApplication(sys.argv)
      MainWindow = QtWidgets.QMainWindow()
      ui=A()
      ui.login(MainWindow)
      MainWindow.show()
      sys.exit(app.exec_())

