__author__ = 'ed'


import sys, pickle

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *




class Window(QtGui.QMainWindow):

    def __init__(self):
        global bookmarks
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







        self.centralwidget = QtGui.QWidget(self)

        self.line = QtGui.QLineEdit(self)
        self.line.setMinimumSize(1150,30)
        self.line.setStyleSheet("font-size:15px;")

        self.enter = QtGui.QPushButton(self)
        self.enter.resize(0,0)
        self.enter.clicked.connect(self.Enter)
        self.enter.setShortcut("Return")

        self.reload = QtGui.QPushButton("↻",self)
        self.reload.setMinimumSize(35,30)
        self.reload.setShortcut("F5")
        self.reload.setStyleSheet("font-size:23px;")
        self.reload.clicked.connect(self.Reload)

        self.back = QtGui.QPushButton("◀",self)
        self.back.setMinimumSize(35,30)
        self.back.setStyleSheet("font-size:23px;")
        self.back.clicked.connect(self.Back)

        self.forw = QtGui.QPushButton("▶",self)
        self.forw.setMinimumSize(35,30)
        self.forw.setStyleSheet("font-size:23px;")
        self.forw.clicked.connect(self.Forward)

        self.book = QtGui.QPushButton("☆",self)
        self.book.setMinimumSize(35,30)
        self.book.clicked.connect(self.Bookmark)
        self.book.setStyleSheet("font-size:18px;")

        self.pbar = QtGui.QProgressBar()
        self.pbar.setMaximumWidth(120)

        self.web = QWebView(loadProgress = self.pbar.setValue, loadFinished = self.pbar.hide, loadStarted = self.pbar.show, titleChanged = self.setWindowTitle)
        self.web.setMinimumSize(1360,700)

        self.list = QtGui.QComboBox(self)
        self.list.setMinimumSize(35,30)

        for i in bookmarks:
            self.list.addItem(i)

        self.list.activated[str].connect(self.handleBookmarks)
        self.list.view().setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)

        self.web.urlChanged.connect(self.UrlChanged)

        self.web.page().linkHovered.connect(self.LinkHovered)

        grid = QtGui.QGridLayout()

        grid.addWidget(self.back,0,0, 1, 1)
        grid.addWidget(self.line,0,3, 1, 1)
        grid.addWidget(self.book,0,4, 1, 1)
        grid.addWidget(self.forw,0,1, 1, 1)
        grid.addWidget(self.reload,0,2, 1, 1)
        grid.addWidget(self.list,0,5, 1, 1)
        grid.addWidget(self.web, 2, 0, 1, 6)

        self.centralwidget.setLayout(grid)


    def Enter(self):
        global url
        global bookmarks

        url = self.line.text()

        http = "http://"
        www = "www."

        if www in url and http not in url:
            url = http + url

        elif "." not in url:
            url = "http://www.google.com/search?q="+url

        elif http in url and www not in url:
            url = url[:7] + www + url[7:]

        elif http and www not in url:
            url = http + www + url


        self.line.setText(url)

        self.web.load(QtCore.QUrl(url))

        if url in bookmarks:
            self.book.setText("★")

        else:
            self.book.setText("☆")

        self.status.show()
    def Bookmark(self):
        global url
        global bookmarks

        bookmarks.append(url)

        b = open("bookmarks.txt","wb")
        pickle.dump(bookmarks,b)
        b.close()

        self.list.addItem(url)
        self.book.setText("★")




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


