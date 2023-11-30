import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow
import os
import pycodestyle
import re
from io import StringIO

file_name = ""
codes = []

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.checkButton.setEnabled(False)
        self.ui.markButton.setEnabled(False)
        self.ui.fixButton.setEnabled(False)
        self.ui.browseButton.clicked.connect(self.browseFile)
        self.ui.checkButton.clicked.connect(self.checkFile)
        self.ui.listWidget.addItems(codes)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)

    def browseFile(self):
        path, _ = QFileDialog.getOpenFileName(self, 
                                                  'Single File', 
                                                  QDir.rootPath(), 
                                                  '*.py')
        global file_name
        file_name = os.path.basename(path)
        self.ui.lineEdit.setText(file_name)
        self.ui.checkButton.setEnabled(True)
        print(file_name)
    
    def checkFile(self):
        global codes
        codes = []
        old_stdout = sys.stdout
        sys.stdout = stdout_data = StringIO()
        file_checker = pycodestyle.Checker(file_name, show_source=False)
        file_errors = file_checker.check_all()
        sys.stdout = old_stdout
        print("Found %s errors (and warnings)" % file_errors)
        for code in stdout_data.getvalue().split("\n")[:-1]:
            codes.append(re.findall("(?<=: )(.{4})", code)[0])
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(codes)
        print(codes)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())