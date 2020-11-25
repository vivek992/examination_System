from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import login_pic
import image
import sys
import student_login
import Admin
import untitled
import examform
import Apply
import KT
class C():

   def option(self, MainWindow_3,password):
        
        

        def log(self) :
            self.MainWindow_2=QtWidgets.QMainWindow()
            self.ui=student_login.B()
            self.ui.student(self.MainWindow_2)
            MainWindow_3.close();
            self.MainWindow_2.show();
     
        def com(self) :
            if self.comboBox.currentIndex() == 1 :
                  
                 #MainWindow_3.close();
                 self.MainWindow=QtWidgets.QMainWindow()
                 self.ui=Admin.D();
                 self.ui.per(self.MainWindow,password)
                 self.MainWindow.show()

            if self.comboBox.currentIndex() == 2 :
                 
                 try :
                 	#MainWindow_3.close();
                 	self.MainWindow=QtWidgets.QMainWindow()
                 	self.ui=untitled.E();
                 	self.ui.result(self.MainWindow,password)
                 	self.MainWindow.show()
                 except :
                 	msg=QMessageBox()
                 	msg.setText("Result has been not uploaded");
                 	msg.setWindowTitle(" ");
                 	msg.setIcon(QMessageBox.Information)
                 	x=msg.exec_()
            if self.comboBox.currentIndex() == 3 :

                 #MainWindow_3.close();
                 self.MainWindow=QtWidgets.QMainWindow()
                 self.ui=examform.F();
                 self.ui.exam(self.MainWindow,password)
                 self.MainWindow.show()

            if self.comboBox.currentIndex() == 4 :

                 self.MainWindow=QtWidgets.QMainWindow()
                 self.ui=KT.H();
                 self.ui.KT(self.MainWindow,password)
                 self.MainWindow.show()


            if self.comboBox.currentIndex() == 5 :
                 self.MainWindow=QtWidgets.QMainWindow()
                 self.ui=Apply.G();
                 self.ui.time(self.MainWindow)
                 self.MainWindow.show()

        MainWindow_3.resize(771, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow_3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 761, 281))
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label_9.setScaledContents(True)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(380, 80, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0,"")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 211, 51))
        MainWindow_3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_3)
        MainWindow_3.setStatusBar(self.statusbar)
        self.label.setText("Options for Student")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(600)
        self.label.setFont(font);
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 10, 151, 21))
        self.pushButton.setText("LogOut")
        MainWindow_3.setWindowTitle("STUDENT OPTION")
        self.comboBox.setItemText(1,"PERSONAL DETAILS")
        self.comboBox.setItemText(2,"RESULTS")
        self.comboBox.setItemText(3,"EXAM FORM")
        self.comboBox.setItemText(4,"KT REVALUATION FORM")
        self.comboBox.setItemText(5,"EXAM TIME TABLE")
        #self.buttonBox.accepted.connect(lambda :ok(self));
        #self.buttonBox.rejected.connect(lambda :ok(self));
        self.pushButton.clicked.connect(lambda checked : log(self));
        self.comboBox.currentIndexChanged.connect(lambda checked :com(self))

if __name__ == "__main__":
      app = QtWidgets.QApplication(sys.argv)
      MainWindow_3= QtWidgets.QMainWindow()
      ui=C()
      ui.option(MainWindow_3)
      MainWindow_3.show()
      sys.exit(app.exec_())


