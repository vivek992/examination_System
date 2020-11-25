from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import image
import option
import search
class E:
    
    def result(self, MainWindow,password):
        def rej(self) :
             MainWindow.close();
             """con_1=self.lineEdit_10.text();
             email=self.lineEdit_9.text();
             middle=self.lineEdit_3.text();
             con_2=self.lineEdit_11.text();
             add=self.lineEdit_2.text();
             gender=self.lineEdit_6.text();
             age=self.lineEdit_8.text();
             dob=self.lineEdit_7.text();
             first=self.lineEdit_4.text();
             course=self.lineEdit_12.text();
             course_id=self.lineEdit_13.text();
             year=self.lineEdit_14.text();
             ssc=self.lineEdit_15.text();
             hsc=self.lineEdit_16.text();
             jee=self.lineEdit_17.text();
             cet=self.lineEdit_18.text();
             diploma=self.lineEdit_19.text();
             sem_1=self.lineEdit_20.text();
             sem_3=self.lineEdit_21.text();
             sem_5=self.lineEdit_22.text();
             sem_4=self.lineEdit_23.text();
             sem_2=self.lineEdit_24.text();
             sem_7=self.lineEdit_25.text();
             sem_8=self.lineEdit_26.text();
             sem_6=self.lineEdit_27.text();
             last=self.lineEdit_5.text();
             print("gender ",gender);
             print("con_1 ",con_1);
             print("con_2 ",con_2);
             print("age ",age);
             print("add ",add);
             print("sid ",sid);
             print("first ",first);
             print("last ",last);
             print("middle ",middle);
             print("email ",email);
             print("dob ",dob);
             print("jee ",jee);
             print("sem_1 ",sem_1);
             print("sem_2 ",sem_2);
             print("sem_3 ",sem_3);
             print("sem_4 ",sem_4);
             print("sem_5 ",sem_5);
             print("sem_6 ",sem_6);
             print("sem_7 ",sem_7);
             print("sem_8 ",sem_8);
             print("cet ",cet);
             print("year ",year);
             print("course ",course);
             print("course_id ",course_id);
             print("hsc ",hsc);
             print("ssc ",ssc);
             print("diploma ",diploma);"""
        MainWindow.resize(800, 600)
        rows=search.result(password);
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setStyleSheet("background-image: url(:/newPrefix/watermark.PNG);")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(550, 520, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-5, 80, 71, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(410, 210, 151, 22))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 779, 7))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 71, 41))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 210, 71, 21))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 170, 61, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 20, 113, 21))
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 210, 221, 22))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 130, 681, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 170, 151, 22))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 170, 121, 31))
        self.label_5.setAcceptDrops(True)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(False)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(620, 170, 151, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(370, 170, 171, 22))
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(220, 10, 221, 31))
        self.label_20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 81, 21))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 120, 91, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 80, 621, 22))
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 260, 779, 7))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(260, 300, 16, 161))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(520, 300, 16, 161))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 280, 131, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 280, 131, 21))
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 280, 131, 21))
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 320, 71, 21))
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 320, 131, 21))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_12.setDragEnabled(True)
        self.lineEdit_12.setReadOnly(False)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 370, 91, 21))
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 370, 131, 21))
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_13.setDragEnabled(True)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 420, 71, 21))
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(120, 420, 131, 21))
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_14.setDragEnabled(True)
        self.lineEdit_14.setReadOnly(False)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 320, 71, 21))
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(320, 320, 61, 21))
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_15.setDragEnabled(True)
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(320, 360, 61, 21))
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_16.setDragEnabled(True)
        self.lineEdit_16.setReadOnly(False)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 360, 71, 21))
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(440, 360, 81, 21))
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_17.setDragEnabled(True)
        self.lineEdit_17.setReadOnly(False)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(390, 360, 71, 21))
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(440, 320, 81, 21))
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_18.setDragEnabled(True)
        self.lineEdit_18.setReadOnly(False)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(390, 320, 71, 21))
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(270, 400, 91, 21))
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(360, 400, 161, 21))
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_19.setDragEnabled(True)
        self.lineEdit_19.setReadOnly(False)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(590, 320, 51, 21))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_20.setDragEnabled(True)
        self.lineEdit_20.setReadOnly(False)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(530, 320, 71, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(530, 400, 71, 21))
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(590, 400, 51, 21))
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_21.setDragEnabled(True)
        self.lineEdit_21.setReadOnly(False)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(660, 320, 71, 21))
        self.label_23.setObjectName("label_23")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(720, 320, 51, 21))
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_22.setDragEnabled(True)
        self.lineEdit_22.setReadOnly(False)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(530, 440, 71, 21))
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(590, 440, 51, 21))
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_23.setDragEnabled(True)
        self.lineEdit_23.setReadOnly(False)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(530, 360, 71, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(590, 360, 51, 21))
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_24.setDragEnabled(True)
        self.lineEdit_24.setReadOnly(False)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(660, 400, 71, 21))
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(720, 400, 51, 21))
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_25.setDragEnabled(True)
        self.lineEdit_25.setReadOnly(False)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(660, 440, 71, 21))
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(720, 440, 51, 21))
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_26.setDragEnabled(True)
        self.lineEdit_26.setReadOnly(False)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(660, 360, 71, 21))
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setGeometry(QtCore.QRect(720, 360, 51, 21))
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_27.setDragEnabled(True)
        self.lineEdit_27.setReadOnly(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont()
        font.setPointSize(10)
        fo = QtGui.QFont()
        fo.setPointSize(11)
        self.label_2.setText("Name:")
        self.label_4.setText("Gender:")
        self.label_8.setText("Contact:")
        self.label_6.setText("Age:")
        self.label_5.setText("Date of Birth:")
        self.label_20.setText("Student registertation id :")
        self.label_7.setText("Email:")
        self.label_3.setText("Address:")
        self.label_2.setFont(font);
        self.label_4.setFont(font);
        self.label_6.setFont(font);
        self.label_8.setFont(font);
        self.label_5.setFont(font);
        self.label_20.setFont(font);
        self.label_7.setFont(font);
        self.label_3.setFont(font);
        MainWindow.setWindowTitle("RESULT")
        self.label_9.setText("Course Details:")
        self.label_10.setText("Past Academics:")
        self.label_11.setText("Current Records:")
        self.label_12.setText("Course:")
        self.label_13.setText("Course ID:")
        self.label_14.setText("Year:")
        self.label_15.setText("SSC:")
        self.label_16.setText("HSC:")
        self.label_17.setText("JEE:")
        self.label_18.setText("CET:")
        self.label_19.setText("DIPLOMA:")
        self.label_21.setText("SEM 1:")
        self.label_22.setText("SEM 3:")
        self.label_23.setText("SEM 5:")
        self.label_24.setText("SEM 4:")
        self.label_25.setText("SEM 2:")
        self.label_26.setText("SEM 7:")
        self.label_27.setText("SEM 8:")
        self.label_28.setText("SEM 6:")
        self.label_9.setFont(fo);
        self.label_10.setFont(fo);
        self.label_11.setFont(fo);
        self.label_12.setFont(fo);
        self.label_13.setFont(fo);
        self.label_14.setFont(fo);
        self.label_15.setFont(fo);
        self.label_16.setFont(fo);
        self.label_17.setFont(fo);
        self.label_18.setFont(fo);
        self.label_19.setFont(fo);
        self.label_20.setFont(fo);
        self.label_21.setFont(fo);
        self.label_22.setFont(fo);
        self.label_23.setFont(fo);
        self.label_24.setFont(fo);
        self.label_25.setFont(fo);
        self.label_26.setFont(fo);
        self.label_27.setFont(fo);
        self.label_28.setFont(fo);
        self.lineEdit.setText(rows[0]);
        self.lineEdit.setReadOnly(True);
        self.lineEdit_4.setText(rows[1]);
        self.lineEdit_2.setText(rows[2]);
        self.lineEdit_6.setText(rows[3]);
        self.lineEdit_7.setText(rows[4]);
        self.lineEdit_8.setText(rows[5]);
        self.lineEdit_9.setText(rows[6]);
        self.lineEdit_10.setText(rows[7]);
        self.lineEdit_12.setText(rows[8]);
        self.lineEdit_13.setText(rows[9]);
        self.lineEdit_14.setText(rows[10]);
        self.lineEdit_15.setText(rows[11]);
        self.lineEdit_18.setText(rows[12]);
        self.lineEdit_16.setText(rows[13]);
        self.lineEdit_17.setText(rows[14]);
        self.lineEdit_19.setText(rows[15]);
        self.lineEdit_20.setText(rows[16]);
        self.lineEdit_24.setText(rows[17]);
        self.lineEdit_21.setText(rows[18]);
        self.lineEdit_23.setText(rows[19]);
        self.lineEdit_22.setText(rows[20]);
        self.lineEdit_27.setText(rows[21]); 
        self.lineEdit_25.setText(rows[22]);
        self.lineEdit_26.setText(rows[23]);
        self.lineEdit_4.setReadOnly(True);
        self.lineEdit_2.setReadOnly(True);
        self.lineEdit_6.setReadOnly(True);
        self.lineEdit_7.setReadOnly(True);
        self.lineEdit_8.setReadOnly(True);
        self.lineEdit_9.setReadOnly(True);
        self.lineEdit_10.setReadOnly(True);
        self.lineEdit_12.setReadOnly(True);
        self.lineEdit_13.setReadOnly(True);
        self.lineEdit_14.setReadOnly(True);
        self.lineEdit_15.setReadOnly(True);
        self.lineEdit_18.setReadOnly(True);
        self.lineEdit_16.setReadOnly(True);
        self.lineEdit_17.setReadOnly(True);
        self.lineEdit_19.setReadOnly(True);
        self.lineEdit_20.setReadOnly(True);
        self.lineEdit_24.setReadOnly(True); 
        self.lineEdit_21.setReadOnly(True);
        self.lineEdit_23.setReadOnly(True);
        self.lineEdit_22.setReadOnly(True);
        self.lineEdit_27.setReadOnly(True);
        self.lineEdit_25.setReadOnly(True);
        self.lineEdit_26.setReadOnly(True);
        self.buttonBox.rejected.connect(lambda :rej(self));
        
if __name__ == "__main__":
      app = QtWidgets.QApplication(sys.argv)
      MainWindow= QtWidgets.QMainWindow()
      ui=E()
      ui.result(MainWindow)
      MainWindow.show()
      sys.exit(app.exec_())

