# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 200)
        MainWindow.setFixedSize(400, 200)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameLineEdit.setGeometry(QtCore.QRect(180, 50, 113, 22))
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.userNameLineEdit.setValidator(QtGui.QIntValidator(10000000, 99999999))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 60, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(180, 100, 113, 22))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setValidator(QtGui.QIntValidator(10000000, 9999999))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "单行文本框LineEdit"))
        self.label.setText(_translate("MainWindow", "系统登录"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密    码："))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./doughnut.ico"))
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())