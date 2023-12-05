import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QAbstractItemView, QDialog
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow
import os
import pycodestyle
import autopep8
import re
from io import StringIO

file_name = ""
path = ""
codes = {}
ignore = []

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
        self.ui.markButton.clicked.connect(self.markAll)
        self.ui.fixButton.clicked.connect(self.selectionChanged)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ui.listWidget.itemClicked.connect(self.selectionChanged)
        self.ui.listWidget.itemDoubleClicked.connect(self.detailsItem)
        self.ui.progressBar.setValue(100)
        self.ui.progressBar.setVisible(False)

    def detailsItem(self):
        print("Details")

    def selectionChanged(self):
        if len(self.ui.listWidget.selectedItems()) > 0:
            self.ui.fixButton.setEnabled(True)
        else:
            self.ui.fixButton.setEnabled(False)

    def browseFile(self):
        global path
        path, _ = QFileDialog.getOpenFileName(self, 
                                                  'Single File', 
                                                  QDir.rootPath(), 
                                                  '*.py')
        global file_name
        file_name = os.path.basename(path)
        self.ui.lineEdit.setText(file_name)
        self.ui.checkButton.setEnabled(True)
    
    def checkFile(self):
        global codes
        codes = {}
        global ignore
        ignore = []
        old_stdout = sys.stdout
        sys.stdout = stdout_data = StringIO()
        file_checker = pycodestyle.Checker(file_name, show_source=False)
        file_errors = file_checker.check_all()
        sys.stdout = old_stdout
        print("Found %s errors (and warnings)" % file_errors)
        for code in stdout_data.getvalue().split("\n")[:-1]:
            print(code)
            key = re.findall("(?<=: )(.{4})", code)[0]
            if key in codes:
                codes[key].append(re.findall("(?<=:)(.*?)(?=:)", code)[0])
            else:
                ignore.append(key)
                codes[key] = []

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(codes.keys())
        if len(codes) > 0:
            self.ui.markButton.setEnabled(True)
            # self.ui.fixButton.setEnabled(True)
        else:
            self.success()
    
    def markAll(self):
        self.ui.listWidget.selectAll()
    
    def fix(self):
        global ignore
        for item in self.ui.listWidget.selectedItems():
            ignore.pop(ignore.index(item.text()))
        print(ignore)
        file_data = open(path, "r")
        data = file_data.read()
        fixed_data = autopep8.fix_code(data, options={'ignore': ignore})
        prefix_path = re.sub(file_name, "", path)
        prefix_file = "fixed_"
        fixed_file = open(f"{prefix_path}{prefix_file}{file_name}", "w")
        fixed_file.write(fixed_data)
        fixed_file.close()
        print("Fixed!")

    def success(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Fixed!")
        dlg.setFixedSize(300, 100)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())