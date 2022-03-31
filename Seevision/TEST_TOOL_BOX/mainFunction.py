# coding = utf8
import os
import subprocess
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QApplication

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
    elif btn_type == "badPointCheck":
        software_path = "./Tools/BadPointCheck/BadPointCheck.exe"
    launchSoftware(software_path)


def ScriptListControlBar(script_name):
    script_path = ""
    if script_name == "hellowWorld":
        script_path = "./Scripts/hellowWorld.py"
    ScriptControlBar(script_path)


def ScriptControlBar(script_path):
    log_path = ".\log.txt"
    logProcess = subprocess.Popen("python {} > {}".format(script_path, log_path), shell=True)
    if logProcess:
        QMessageBox.information(mainWindow, "提示", "脚本运行成功：【{}】".format(script_path), QMessageBox.Ok)
        ui.log_output_EditText.appendPlainText("Here is log output Console:")
        QApplication.processEvents()
        with open(log_path, "r") as log_file:
            while True:
                line_data = log_file.readline()
                if line_data != "":
                    ui.log_output_EditText.appendPlainText(str(line_data))
                QApplication.processEvents()
    else:
        QMessageBox.information(mainWindow, "提示", "脚本运行失败：【{}】".format(script_path), QMessageBox.Ok)


def launchSoftware(software_path):
    global software
    software = subprocess.Popen(software_path)


def closeSoftware():
    if software:
        software.kill()


def ui_connect():
    # Tool part
    ui.btn_hidTool_2_4.clicked.connect(lambda: HidToolToolBar("hidTool2_4"))
    ui.btn_hidTool_2_5.clicked.connect(lambda: HidToolToolBar("hidTool2_5"))
    ui.btn_FlashTest.clicked.connect(lambda: HidToolToolBar("flashTest"))
    ui.btn_SwitchResolutionTest.clicked.connect(lambda: HidToolToolBar("switchResolutionTest"))
    ui.btn_BadPointCheck.clicked.connect(lambda: HidToolToolBar("badPointCheck"))

    # Script part
    ui.btn_Script_HelloWorld.clicked.connect(lambda: ScriptListControlBar("hellowWorld"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./seevi_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    mainWindow.setWindowIcon(icon)
    ui_connect()
    mainWindow.show()
    sys.exit(app.exec_())
