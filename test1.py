print("Hello world")
print("I love uestc")
import sys
import untitled1
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
<<<<<<< HEAD
    a = 6
    print("hello %d\n"%a)
=======
>>>>>>> parent of 71035d2 (Update test1.py)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = untitled1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
