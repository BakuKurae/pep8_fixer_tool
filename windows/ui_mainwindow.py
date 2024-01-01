# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_tool.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setFixedSize(400, 300)
        MainWindow.setWindowIcon(QIcon('Assets/icon.png'))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 381, 191))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 190, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(10, 10, 70, 19))
        self.checkButton = QPushButton(self.centralwidget)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(330, 10, 62, 19))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(85, 10, 241, 20))
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.markButton = QPushButton(self.centralwidget)
        self.markButton.setObjectName(u"markButton")
        self.markButton.setGeometry(QRect(10, 270, 62, 19))
        self.fixButton = QPushButton(self.centralwidget)
        self.fixButton.setObjectName(u"fixButton")
        self.fixButton.setGeometry(QRect(330, 270, 62, 19))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 270, 241, 20))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.detailButton = QPushButton(self.centralwidget)
        self.detailButton.setObjectName(u"detailButton")
        self.detailButton.setGeometry(QRect(160, 245, 91, 19))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PEP8 auto-fixer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mark all the codes you need to fix:", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.markButton.setText(QCoreApplication.translate("MainWindow", u"Mark all", None))
        self.fixButton.setText(QCoreApplication.translate("MainWindow", u"Fix!", None))
        self.detailButton.setText(QCoreApplication.translate("MainWindow", u"Issue Details", None))
    # retranslateUi

