# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QStatusBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.button = QtWidgets.QPushButton("1s后\n清除临时通知", MainWindow)
        self.button.setGeometry(QtCore.QRect(10, 10, 100, 50))
        self.button_stop = QtWidgets.QPushButton("关闭1s后\n清除临时通知", MainWindow)
        self.button_stop.setGeometry(QtCore.QRect(110, 10, 100, 50))
        self.button_stop.setEnabled(False)

        MainWindow.setStatusBar(self.statusbar)

        self.statusbar.addPermanentWidget(QtWidgets.QLabel("这是一个常驻控件！"))
        self.statusbar.showMessage("倒计时3s，该通知消失！", 3000)
        self.timer = QTimer()
        self.timer.timeout.connect(self.clearMessage)
        self.button.clicked.connect(self.startTimer)
        self.button_stop.clicked.connect(self.stopTimer)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startTimer(self):
        self.timer.start(3000)
        self.button.setEnabled(False)
        self.button_stop.setEnabled(True)
        # 设置几秒后自动退出应用程序
        # self.timer.singleShot(9000, app.quit)

    def stopTimer(self):
        self.timer.stop()
        self.button.setEnabled(True)
        self.button_stop.setEnabled(False)

    def clearMessage(self):
        QMessageBox.information(self.MainWindow, "Tip", "Clear Message", QMessageBox.Ok)
        self.statusbar.clearMessage()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "状态栏Demo"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("./doughnut.ico"))
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
