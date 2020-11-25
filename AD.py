from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import image
import sys
import mix
import option
import search
import AD_2

class B:

   def student(self, MainWindow_1):

        def back(self) :
            self.MainWindow=QtWidgets.QMainWindow()
            self.ui=mix.A();
            self.ui.login(self.MainWindow)
            MainWindow_1.close();
            self.MainWindow.show()
        def enter(self):
            password=self.lineEdit_2.text();
            username=self.lineEdit.text();
            count=search.admin(username,password);
            imp=password;
            try :
            	if username == count[0] and password == count[1] :
                    	MainWindow_1.close();
                    	self.MainWindow_2=QtWidgets.QMainWindow()
                    	self.ui=AD_2.C();
                    	self.ui.option(self.MainWindow_2)
                    	self.MainWindow_2.show();
            except :
                print("nahi");
                msg=QMessageBox()
                msg.setText("Invalid username or Password");
                msg.setWindowTitle(" ");
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()

            
            
            

        MainWindow_1.resize(778, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow_1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 778, 379))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label_9.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 220, 111, 41))
        self.pushButton.setFont(font)
        self.pushButton_2.setText("Back")
        self.pushButton_2.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 160, 211, 31))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 110, 211, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password);
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 121, 51))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 150, 121, 51))
        MainWindow_1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_1)
        MainWindow_1.setWindowTitle("Admin login")
        self.pushButton.setText("Enter")
        self.label_3.setText("User Name")
        self.label_2.setText("Password")
        self.pushButton_2.clicked.connect(lambda checked:back(self));
        self.pushButton.clicked.connect(lambda checked :enter(self));


if __name__ == "__main__":
       app = QtWidgets.QApplication(sys.argv)
       MainWindow_1=QtWidgets.QMainWindow()
       ui=B()
       ui.student(MainWindow_1)
       MainWindow_1.show()
       sys.exit(app.exec_())

