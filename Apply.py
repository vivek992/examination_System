from PyQt5 import QtCore, QtGui, QtWidgets

class G:
    def time(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("EXAM TIME TABLE")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = G()
    ui.time(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

