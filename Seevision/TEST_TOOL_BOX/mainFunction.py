# coding = utf8
import os
import subprocess
import sys

from PyQt5 import QtWidgets

from SeevisionToolBox import Ui_MainWindow

os.path.abspath(".")

# 设置递归限制，防止程序中的循环使得python内存溢出
sys.setrecursionlimit(5000)
"""
    @Project:PyQt5Project
    @File:mainFunction.py
    @Author:十二点前要睡觉
    @Date:2022/3/31 15:05
"""


def HidToolToolBar(btn_type):
    software_path = ""
    if btn_type == "hidTool2_4":
        software_path = "./Tools/HIDTools_2_4/HIDTool.exe"
    elif btn_type == "hidTool2_5":
        software_path = "./Tools/HIDTools_2_5/HIDTool_2_5.exe"
    elif btn_type == "flashTest":
        software_path = "./Tools/FlashTest/FlastTest.exe"
    elif btn_type == "switchResolutionTest":
        software_path = "./Tools/SwitchResolutionTest/SwitchResolutionTest.exe"
    launchSoftware(software_path)


def ScriptListControlBar():
    pass


def ScriptControlBar():
    pass


def launchSoftware(software_path):
    global software
    software = subprocess.Popen(software_path)


def closeSoftware():
    if software:
        software.kill()


def ui_connect():
    ui.btn_hidTool_2_4.clicked.connect(lambda: HidToolToolBar("hidTool2_4"))
    ui.btn_hidTool_2_5.clicked.connect(lambda: HidToolToolBar("hidTool2_5"))
    ui.btn_FlashTest.clicked.connect(lambda: HidToolToolBar("flashTest"))
    ui.btn_SwitchResolutionTest.clicked.connect(lambda: HidToolToolBar("switchResolutionTest"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui_connect()
    mainWindow.show()
    sys.exit(app.exec_())
