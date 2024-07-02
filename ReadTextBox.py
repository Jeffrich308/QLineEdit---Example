# -------------------------------------------------------------------------------
# Name:             Generic Startup Loading a UI File
# Purpose:          Simplify a GUI interface app
#
# Author:           Jeffreaux
#
# Created:          20Mar23
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("ReadTextBox_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")
        self.txtInputBox = self.findChild(QLineEdit, "txtInputBox")
        self.btnGo = self.findChild(QPushButton, "btnGo")
        self.label = self.findChild(QLabel, "label")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)
        self.btnGo.clicked.connect(self.print_label)

        # Show the app
        self.show()

    def print_label(self):
        print("Will print to label")
        print(self.txtInputBox.text())
        self.label.setText(str(self.txtInputBox.text()))
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
