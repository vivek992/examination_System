from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import option
import insert
from PyQt5.QtWidgets import QMessageBox
class H:


    def KT(self, MainWindow,password):



        def cancel(self) :
        
           MainWindow.close()

        def sumbit(self) :
           try :
           	fathername=self.lineEdit_2.text();
           	name=self.lineEdit.text();
           	center=self.lineEdit_7.text();
           	sem=self.lineEdit_6.text();
           	roll=self.lineEdit_3.text();
           	college=self.lineEdit_8.text();
           	course=self.lineEdit_4.text();
           	result=self.lineEdit_5.text();
           	insert.KT(name,roll,college,result,center,fathername,sem,course);
           	print("name ",name);
           	print("fathername ",fathername);
           	print("college ",college);
           	print("sem ",sem);
           	print("result ",result);
           	print("center ",center);
           	print("course ",course);
           	print("roll ",roll);
           	msg=QMessageBox()
           	msg.setText("Succesfully Saved");
           	msg.setWindowTitle(" ");
           	msg.setIcon(QMessageBox.Information)
           	x=msg.exec_() 
           	MainWindow.close();  
           except :
           	msg=QMessageBox()
           	msg.setText("You've Already Applied");
           	msg.setWindowTitle(" ");
           	msg.setIcon(QMessageBox.Critical)
           	x=msg.exec_() 
           	MainWindow.close();
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label_9.setScaledContents(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 171, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 50, 171, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 131, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 520, 93, 28))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 520, 93, 28))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 781, 192))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setAutoScrollMargin(14)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 481, 22))
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAutoFillBackground(False)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 130, 161, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 481, 22))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 460, 93, 28))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 31))
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 460, 261, 21))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 170, 141, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(400, 180, 341, 21))
        self.lineEdit_7.setTabletTracking(False)
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 180, 131, 21))
        self.lineEdit_6.setTabletTracking(False)
        self.lineEdit_6.setAutoFillBackground(False)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 130, 131, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 140, 81, 21))
        self.lineEdit_3.setText(password);
        self.lineEdit_3.setReadOnly(True);
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 220, 481, 21))
        self.lineEdit_8.setTabletTracking(False)
        self.lineEdit_8.setAutoFillBackground(False)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 140, 111, 21))
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setAutoFillBackground(False)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(270, 460, 27, 22))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("New folder/download.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("New folder/download.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("New folder/download.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("New folder/download.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 140, 81, 21))
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setText("2. Father's Name :")
        self.label_2.setText("1.  Name of Candidate :")
        self.label_7.setText("6. Sem/Year :")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font);
        self.label_2.setFont(font);
        self.label_7.setFont(font);
        MainWindow.setWindowTitle("KT FORM")
        self.label_10.setText("8. College :")
        self.label_6.setText("5. Result(pass/fail) :")
        self.label_8.setText("7. Exam Centre :")
        self.label_5.setText("4. ExamCourse :")
        self.label_4.setText("3. Roll No :")
        self.label_6.setFont(font);
        self.label_4.setFont(font);
        self.label_5.setFont(font);
        self.label_8.setFont(font);
        self.label.setText("APPLICATION FOR REVALUTION OF RESULTS")
        self.label_11.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Upload Photocopy Of Marksheet  </span><span style=\" font-size:10pt; color:#ff0000;\">* </span><span style=\" font-size:10pt;\">:</span></p></body></html>")
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">APPLICATION FOR REVALUTION OF RESULTS</span></p></body></html>")
        self.pushButton_2.setText("SUBMIT")
        self.pushButton_3.setText("CANCEL")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Exam paper no")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Title of paper")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Serial no of paper")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Date of exam taken")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Marks Obtained")
        self.pushButton.setText("Upload")
        self.pushButton_3.clicked.connect(lambda checked : cancel(self)); 
        self.pushButton_2.clicked.connect(lambda checked : sumbit(self));
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = H()
    ui.KT(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
