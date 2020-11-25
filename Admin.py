from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QFontDialog 
from PyQt5.QtWidgets import QMessageBox
import sys
import image
import option
import insert as w
class D:

	
    def per(self,MainWindow,password):
        
        def rej(self) :
            MainWindow.close();

        def sumbit(self) :
            try :
            	gender=self.lineEdit_6.text();
            	add=self.lineEdit_2.text();
            	sid=self.lineEdit.text();
            	first=self.lineEdit_4.text();
            	con_2=self.lineEdit_11.text();
            	con_1=self.lineEdit_10.text();
            	age=self.lineEdit_8.text();
            	last=self.lineEdit_5.text();
            	email=self.lineEdit_9.text();
            	middle=self.lineEdit_3.text();
            	dob=self.lineEdit_7.text();
            	name=first+" "+middle+" "+last;
            	w.Admin(sid,name,add,gender,dob,age,email,con_1,con_2);
            	msg=QMessageBox()
            	msg.setText("Succesfully Sumbitted");
            	msg.setWindowTitle(" ");
            	msg.setIcon(QMessageBox.Information)
            	x=msg.exec_() 
            	MainWindow.close();            
            except :
            	msg=QMessageBox()
            	msg.setText("Data Is Already Entered");
            	msg.setWindowTitle(" ");
            	msg.setIcon(QMessageBox.Critical)
            	x=msg.exec_()
            	MainWindow.close();

        MainWindow.resize(800, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.label_9.setStyleSheet("background-image: url(:/newPrefix/watermark.PNG);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label_9.setScaledContents(True)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 190, 151, 22))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 150, 681, 22))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 40, 113, 21))
        self.lineEdit.setText(password);
        self.lineEdit.setReadOnly(True);
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 121, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 221, 22))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 779, 7))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 61, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 71, 21))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 81, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(580, 230, 151, 22))
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(410, 230, 151, 22))
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(520, 310, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.label_4=QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 71, 41))
        self.lineEdit_5=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 100, 221, 22))
        self.lineEdit_9=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 230, 221, 22))
        self.label_6=QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 190, 61, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lineEdit_3=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 100, 221, 22))
        self.lineEdit_7=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(370, 190, 171, 22))
        self.label_20=QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(220, 30, 221, 31))
        self.label_20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_8=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(620, 190, 151, 22))
        self.label_8=QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 230, 71, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("PERSONAL DETAILS")
        self.label_5.setText("Date of birth :")
        self.label_2.setText("Name :")
        self.label_7.setText("Email :")
        self.label_3.setText("Address :")
        self.label_4.setText("Gender :")
        self.label_6.setText("Age :")
        self.label_20.setText("Student registertation id :")
        self.label_8.setText("Contact :")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font);
        self.label_2.setFont(font);
        self.label_7.setFont(font);
        self.label_3.setFont(font);
        self.label_4.setFont(font);
        self.label_6.setFont(font);
        self.label_20.setFont(font);
        self.label_8.setFont(font);
        self.buttonBox.rejected.connect(lambda :rej(self));
        self.buttonBox.accepted.connect(lambda :sumbit(self));
	
    
if __name__ == "__main__":
      app = QtWidgets.QApplication(sys.argv)
      MainWindow=QtWidgets.QMainWindow()
      ui=D()
      ui.per(MainWindow)
      MainWindow.show()
      sys.exit(app.exec_())
