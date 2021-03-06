# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hellowui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("OK")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 100, 100))
        self.label.setText("This is a label,阿苏妲己是大是大非和速度阿u是否坏话和副i啊辉煌那就下次能看见这次你可记住你曾经你自己")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label.setWordWrap(True)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, Qt.red)

        self.label_link = QtWidgets.QLabel(self.centralwidget)
        self.label_link.setGeometry(QtCore.QRect(200, 100, 300, 30))
        self.label_link.setText("<a href='https://www.baidu.com'>点击进入百度搜索</a>")
        self.label_link.setOpenExternalLinks(True)
        # self.label_link.setPixmap(QPixmap("./eager.jpg"))
        print(self.label_link.text())
        self.label.setPalette(palette)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.resize(400, 300)
        # print(MainWindow.geometry())
        screen = QDesktopWidget().screenGeometry()
        # print(screen)
        # print(f"Screen width  {screen.width()} : Screen height  {screen.height()}")
        palette = QtGui.QPalette()
        # set red color as window backgrounds
        # palette.setColor(QtGui.QPalette.Background, Qt.red)
        # set image as window backgrounds and ignore aspect ratio and make it smooth transformation
        palette.setBrush(QtGui.QPalette.Background, QBrush(
            QPixmap("./eager.jpg").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
                                             QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setWindowFlags(QtCore.Qt.WindowTitleHint)
        MainWindow.setWindowTitle(_translate("OK", "Index"))
        self.pushButton.setText(_translate("OK", "OK"))
        # self.pushButton.clicked.connect(self.showMessage)
        self.pushButton.clicked.connect(self.openAnotherWindow)

    def showMessage(self):
        QMessageBox.information(MainWindow, "提示框", "欢迎进入PyQt5编程世界", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def openAnotherWindow(self):
        import hellowui1
        self.anotherWindow = hellowui1.Ui_MainWindow()
        self.anotherWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("doughnut.ico"))
    # 创建窗体对象
    MainWindow = QtWidgets.QMainWindow()
    # 创建PyQt设计的窗体对象
    ui = Ui_MainWindow()
    # 调用PyQt窗体的方法对窗体对象进行初始化设置
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 程序关闭时退出进程
    sys.exit(app.exec_())
