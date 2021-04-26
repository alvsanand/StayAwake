import sys
from datetime import datetime, timedelta
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon, qApp

import StayAwake.images_qr  # workaround to get it to compile to .exe with pyinstaller

from StayAwake.PreventSleep import PreventSleep
from StayAwake.StayAwakeWindow import StayAwakeWindow

# since window is fixed, prevents it from showing small on high resolution screens
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


# main GUI class, inherits from QMainWindow
class StayAwakeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(StayAwakeApp, self).__init__()
        self.ui = StayAwakeWindow()
        self.ui.setupUi(self)
        # set logo in app window (workaround for pyinstaller)
        self.ui.label_2.setPixmap(QtGui.QPixmap(":icons/32x32.png"))
        # listener for when toggle button is pressed
        self.ui.toggle.clicked.connect(self.togglePressed)

        self.running = False  # flag to check if program is on or off
        self.preventSleep = None  # initializing to hold PreventSleep instance
        self.trayIcon = None  # initializing to hold tray icon instance
        self.status = "off"

        self.setupTray()  # setup tray icon and menu

    # handle single click on tray icon event
    def trayIconSingleClick(self, reason):
        if reason == self.trayIcon.Trigger:
            self.showNormal()
            self.activateWindow()

    # setup tray icon and menu
    def setupTray(self):
        self.trayIcon = QSystemTrayIcon(self)  # instance of QSystemTrayIcon
        # set tray icon image
        self.trayIcon.setIcon(QIcon(":icons/StayAwakeOpaque.ico"))
        self.trayIcon.setToolTip("Stay Awake")
        self.trayIcon.activated.connect(
            self.trayIconSingleClick)  # Icon clicked trigger

        openAction = QAction("Open", self)  # "open" right click option in tray
        quitAction = QAction("Quit", self)  # "quit" right click option in tray
        openAction.triggered.connect(self.showNormal)  # open app trigger
        quitAction.triggered.connect(qApp.quit)  # quit app trigger
        trayMenu = QMenu()  # QMenu class instance
        trayMenu.addAction(openAction)  # add open action
        trayMenu.addAction(quitAction)  # add quit action
        self.trayIcon.setContextMenu(trayMenu)  # sets menu actions
        self.trayIcon.show()  # makes tray icon visible

    # handle toggle button states and calling prevent sleep
    def togglePressed(self):
        if self.running:
            self.ui.toggle.setText("Start")  # set toggle button text to "Off"
            self.status = "off"
            self.running = False  # update state
            self.preventSleep.stop()  # terminate prevent sleep thread
        else:
            self.ui.toggle.setText("Stop")  # set toggle button text to "On"
            self.status = "on"
            self.running = True  # update state
            self.preventSleep = PreventSleep()  # create instance of PreventSleep class
            self.preventSleep.start()  # start prevent sleep thread

    # making "minimize" button minimizes to tray instead of taskbar
    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:  # if minimize button is pressed
                event.ignore()  # ignore "minimize to taskbar" event
                self.hide()  # hide the window
                self.trayIcon.show()  # show tray icon
                self.trayIcon.showMessage(
                    "Stay Awake is currently " + self.status + ".",
                    "Minimized to tray.", QSystemTrayIcon.Information)  # show tray message popup


# set icon for window
def _setAppIcon(app):
    appIcon = QtGui.QIcon()  # create instance of QIcon class
    # adding different sized icons
    appIcon.addFile(':icons/16x16.png', QtCore.QSize(16, 16))
    appIcon.addFile(':icons/32x32.png', QtCore.QSize(32, 32))
    appIcon.addFile(':icons/48x48.png', QtCore.QSize(48, 48))
    appIcon.addFile(':icons/192x192.png', QtCore.QSize(192, 192))
    appIcon.addFile(':icons/512x512.png', QtCore.QSize(512, 512))
    app.setWindowIcon(appIcon)  # set correct window icon


def start():
    app = QtWidgets.QApplication([])

    _setAppIcon(app)

    application = StayAwakeApp()
    application.togglePressed()
    sys.exit(app.exec())
