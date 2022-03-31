# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeevisionToolBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/CHENGUANGTAO/.designer/backup/seevi_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 541))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.btn_hidTool_2_4 = QtWidgets.QPushButton(self.groupBox)
        self.btn_hidTool_2_4.setGeometry(QtCore.QRect(10, 20, 211, 23))
        self.btn_hidTool_2_4.setObjectName("btn_hidTool_2_4")
        self.btn_FlashTest = QtWidgets.QPushButton(self.groupBox)
        self.btn_FlashTest.setGeometry(QtCore.QRect(10, 80, 211, 23))
        self.btn_FlashTest.setObjectName("btn_FlashTest")
        self.btn_SwitchResolutionTest = QtWidgets.QPushButton(self.groupBox)
        self.btn_SwitchResolutionTest.setGeometry(QtCore.QRect(10, 110, 211, 23))
        self.btn_SwitchResolutionTest.setObjectName("btn_SwitchResolutionTest")
        self.btn_hidTool_2_5 = QtWidgets.QPushButton(self.groupBox)
        self.btn_hidTool_2_5.setGeometry(QtCore.QRect(10, 50, 211, 23))
        self.btn_hidTool_2_5.setObjectName("btn_hidTool_2_5")
        self.btn_BadPointCheck = QtWidgets.QPushButton(self.groupBox)
        self.btn_BadPointCheck.setGeometry(QtCore.QRect(10, 140, 211, 23))
        self.btn_BadPointCheck.setObjectName("btn_BadPointCheck")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 311, 541))
        self.groupBox_2.setToolTip("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_Script_HelloWorld = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_Script_HelloWorld.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.btn_Script_HelloWorld.setObjectName("btn_Script_HelloWorld")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(570, 10, 221, 541))
        self.groupBox_3.setObjectName("groupBox_3")
        self.log_output_EditText = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.log_output_EditText.setGeometry(QtCore.QRect(10, 20, 201, 511))
        self.log_output_EditText.setObjectName("log_output_EditText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视熙测试工具箱"))
        MainWindow.setToolTip(_translate("MainWindow", "视熙科技测试部工具箱"))
        self.groupBox.setTitle(_translate("MainWindow", "测试工具栏"))
        self.btn_hidTool_2_4.setToolTip(_translate("MainWindow", "点击打开HidTool 2.4"))
        self.btn_hidTool_2_4.setText(_translate("MainWindow", "HIDTool 2.4"))
        self.btn_FlashTest.setToolTip(_translate("MainWindow", "点击打开FlashTest测试工具"))
        self.btn_FlashTest.setText(_translate("MainWindow", "FlashTest"))
        self.btn_SwitchResolutionTest.setToolTip(_translate("MainWindow", "点击打开分辨率切换测试页面"))
        self.btn_SwitchResolutionTest.setText(_translate("MainWindow", "SwitchResolutionTest"))
        self.btn_hidTool_2_5.setToolTip(_translate("MainWindow", "点击打开HidTool 2.5"))
        self.btn_hidTool_2_5.setText(_translate("MainWindow", "HIDTool 2.5"))
        self.btn_BadPointCheck.setToolTip(_translate("MainWindow", "点击打开分辨率切换测试页面"))
        self.btn_BadPointCheck.setText(_translate("MainWindow", "坏点检测工具"))
        self.groupBox_2.setTitle(_translate("MainWindow", "脚本列表"))
        self.btn_Script_HelloWorld.setToolTip(_translate("MainWindow", "点击运行helloWorld.py脚本"))
        self.btn_Script_HelloWorld.setText(_translate("MainWindow", "helloWorld.py"))
        self.groupBox_3.setTitle(_translate("MainWindow", "脚本运行输出内容"))