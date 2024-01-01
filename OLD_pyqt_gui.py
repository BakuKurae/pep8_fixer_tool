import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QScrollArea, QMainWindow, QFileDialog, QAbstractItemView, QDialog, QLabel, QDialogButtonBox, QListWidget, QHBoxLayout, QLineEdit
from PySide6.QtCore import *
from PySide6.QtGui import QIcon
from windows.ui_mainwindow import Ui_MainWindow
import os
import pycodestyle
import autopep8
import re
from io import StringIO

file_name = ""
path = ""
codes = {}
ignore = []
description_codes = {}

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Issue Details")
        self.setWindowIcon(QIcon('Assets/icon.png'))
        self.setFixedWidth(500)

        self.layout = QHBoxLayout()
        self.lista = QListWidget()

        self.lista.addItems(codes)

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.widget.setLayout(self.vbox)

        self.scroll.setWidgetResizable(True)
        self.message = QLabel("")
        self.message.setWordWrap(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.scroll.setWidget(self.message)
        self.layout.addWidget(self.lista, stretch=1)
        self.layout.addWidget(self.scroll, stretch=3)
        self.setLayout(self.layout)

        self.lista.itemClicked.connect(self.selectionCode)
    

    def selectionCode(self):
        self.message.setText("Error message: {}\nThis error was found in line: {}".format(description_codes[self.lista.currentItem().text()], 
                                                                            codes[self.lista.currentItem().text()]))
        self.message.adjustSize()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.checkButton.setEnabled(False)
        self.ui.markButton.setEnabled(False)
        self.ui.fixButton.setEnabled(False)
        self.ui.detailButton.setEnabled(False)
        self.ui.browseButton.clicked.connect(self.browseFile)
        self.ui.checkButton.clicked.connect(self.checkFile)
        self.ui.markButton.clicked.connect(self.markAll)
        self.ui.fixButton.clicked.connect(self.fix)
        self.ui.detailButton.clicked.connect(self.showDetailsWindow)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ui.listWidget.itemClicked.connect(self.selectionChanged)
        self.ui.progressBar.setValue(100)
        self.ui.progressBar.setVisible(False)
    
    def showDetailsWindow(self):
        CustomDialog().exec()

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
        self.ui.markButton.setEnabled(False)
        self.ui.detailButton.setEnabled(False)
        self.ui.fixButton.setEnabled(False)
        if len(file_name) > 0:
            self.ui.checkButton.setEnabled(True)
        else:
            self.ui.checkButton.setEnabled(False)
    
    def checkFile(self):
        global description_codes
        global codes
        codes = {}
        global ignore
        ignore = []
        old_stdout = sys.stdout
        sys.stdout = stdout_data = StringIO()
        file_checker = pycodestyle.Checker(path, show_source=False)
        file_errors = file_checker.check_all()
        sys.stdout = old_stdout
        for code in stdout_data.getvalue().split("\n")[:-1]:
            print("code: ", code)
            key = re.findall("(?<=: )(.{4})", code)[0]
            if key in codes:
                codes[key].append(re.findall("(?<=:)(.*?)(?=:)", code)[1])
            else:
                ignore.append(key)
                codes[key] = [re.findall("(?<=:)(.*?)(?=:)", code)[1]]
                description_codes[key] = re.findall("(?<={})(.*)".format(key), code)[0]
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(codes.keys())
        if len(codes) > 0:
            self.ui.markButton.setEnabled(True)
            self.ui.detailButton.setEnabled(True)
            self.ui.fixButton.setEnabled(True)
        else:
            self.success()
    
    def markAll(self):
        self.ui.listWidget.selectAll()
        self.ui.fixButton.setEnabled(True)
    
    def fix(self):
        global ignore
        for item in self.ui.listWidget.selectedItems():
            ignore.pop(ignore.index(item.text()))
        file_data = open(path, "r")
        data = file_data.read()
        fixed_data = autopep8.fix_code(data, options={'ignore': ignore})
        prefix_path = re.sub(file_name, "", path)
        prefix_file = "fixed_"
        fixed_file = open(f"{prefix_path}{prefix_file}{file_name}", "w")
        fixed_file.write(fixed_data)
        fixed_file.close()
        self.clean_gui()
        self.success()

    def success(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Done!")
        dlg.setFixedSize(300, 100)
        dlg.layout = QHBoxLayout()
        dlg.scroll = QScrollArea()
        dlg.widget = QWidget()
        dlg.vbox = QVBoxLayout()
        dlg.widget.setLayout(dlg.vbox)
        dlg.scroll.setWidgetResizable(True)
        if len(ignore) > 0:
            dlg.message = QLabel("The fix process is complete, you have skipped these codes: {}".format(ignore))
        else:
            dlg.message = QLabel("All codes have been fixed.")
        dlg.message.setWordWrap(True)
        dlg.message.setAlignment(Qt.AlignLeft)
        dlg.scroll.setWidget(dlg.message)
        dlg.layout.addWidget(dlg.scroll)
        dlg.setLayout(dlg.layout)
        dlg.exec()

    def clean_gui(self):
        global file_name
        file_name = ""
        self.ui.lineEdit.setText(file_name)
        self.ui.markButton.setEnabled(False)
        self.ui.detailButton.setEnabled(False)
        self.ui.fixButton.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.listWidget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())