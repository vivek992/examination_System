from PyQt5 import QtCore, QtGui, QtWidgets
import search
import regular

class A:

    def regular(self, MainWindow):
     
        def main(self) :

             sid=self.listWidget.currentItem().text();
             print(sid);
             self.MainWindow=QtWidgets.QMainWindow()
             self.ui=regular.E();
             self.ui.result(self.MainWindow,sid)
             self.MainWindow.show()

        MainWindow.resize(800, 600)
        result=search.regular();
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 800, 600))
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/watermark.PNG"))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 391, 21))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 191, 31))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 781, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 781, 441))
        i=0
        for x in result:
            new=result[i];
            self.listWidget.addItems(new)
            i+=1;
            
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Student List")
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:9pt;\">Student Registration ID</span></p></body></html>")
        self.listWidget.currentItemChanged.connect(lambda checked : main(self));
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = A()
    ui.regular(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
