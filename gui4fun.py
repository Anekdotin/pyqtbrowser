__author__ = 'ed'
import sys
import os
from PyQt4 import QtCore, QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50, 1200, 800)
        self.setWindowTitle("Bowser")
        self.setWindowIcon(QtGui.QIcon('mariologo.png'))


        ##########actions#########

        extraAction = QtGui.QAction("Exot me", self)
        extraAction.setShortcut("Ctrl+Q")
        extraAction.setStatusTip('Leave the program')
        extraAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extraAction)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        self.show()

    def close_application(self):
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()


