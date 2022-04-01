# coding = utf8
import os
import subprocess
import sys
from time import sleep

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox

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
    elif script_name == "getBetteryHealthd":
        script_path = "./Scripts/getBatteryHealthd.py"
    ScriptControlBar(script_path)


def ScriptControlBar(script_path):
    """
    # BAD!!!!!!
    该工具需要管理员模式运行：当前执行脚本后的log接收，必须在每个脚本的log都写入log.txt中，待后续使用QThread进行优化重构
    :param script_path:
    :return:
    """
    global logProcess
    log_path = ".\log.txt"
    # logProcess = subprocess.Popen("python {} one two 2>&1 | tee {}".format(script_path, log_path), shell=True)
    logProcess = subprocess.Popen("python {} ".format(script_path), shell=True)
    ui.statusbar.showMessage("正在运行脚本：【{}】".format(script_path), -1)
    # logProcess = subprocess.Popen("python {}".format(script_path), shell=True, stdout=subprocess.PIPE,
    #                               stderr=subprocess.PIPE, bufsize=1)
    # while logProcess.poll() is None:
    #     line_data = logProcess.stdout.readline().decode("utf-8")
    #     ui.log_output_EditText.appendPlainText(str(line_data))
    #     QApplication.processEvents()
    QMessageBox.information(mainWindow, "提示", "等待3s创建log文件……", QMessageBox.Ok)
    sleep(3)
    if logProcess:
        QMessageBox.information(mainWindow, "提示", "脚本运行成功：【{}】".format(script_path), QMessageBox.Ok)
        ui.log_output_EditText.appendPlainText("Here is log output Console:")
        QApplication.processEvents()
        with open(log_path, "r") as log_file:
            while True:
                line_data = log_file.readline()
                if line_data != "":
                    ui.log_output_EditText.appendPlainText(str(line_data).strip())
                QApplication.processEvents()
    else:
        ui.statusbar.showMessage("脚本运行失败：【{}】".format(script_path), -1)
        QMessageBox.information(mainWindow, "提示", "脚本运行失败：【{}】".format(script_path), QMessageBox.Ok)


def launchSoftware(software_path):
    global software
    software = subprocess.Popen(software_path)
    ui.statusbar.showMessage("软件正在运行：【{}】".format(software_path), -1)


def closeSoftware():
    if software:
        software.kill()


# 停止当前运行的脚本
def stopRunningScript():
    try:
        # if logProcess:
        #     logProcess.kill()
        #     sys.exit()
        if logProcess.poll() is None:
            reply = QMessageBox.question(mainWindow, "提示", "将会停止当前运行的脚本并退出程序后台……", QMessageBox.Yes | QMessageBox.No)
            if int(reply) == 16384:
                sys.exit()
            elif int(reply) == 65536:
                pass
    except NameError:
        QMessageBox.information(mainWindow, "提示", "当前无脚本运行，无需STOP")


def ui_connect():
    # Tool part
    ui.btn_hidTool_2_4.clicked.connect(lambda: HidToolToolBar("hidTool2_4"))
    ui.btn_hidTool_2_5.clicked.connect(lambda: HidToolToolBar("hidTool2_5"))
    ui.btn_FlashTest.clicked.connect(lambda: HidToolToolBar("flashTest"))
    ui.btn_SwitchResolutionTest.clicked.connect(lambda: HidToolToolBar("switchResolutionTest"))
    ui.btn_BadPointCheck.clicked.connect(lambda: HidToolToolBar("badPointCheck"))

    # Script part
    ui.btn_Script_HelloWorld.clicked.connect(lambda: ScriptListControlBar("hellowWorld"))
    ui.btn_Script_GetBetteryHealthd.clicked.connect(lambda: ScriptListControlBar("getBetteryHealthd"))

    # common part
    ui.menuItem_logClear.triggered.connect(clearLogOutput)
    ui.menuItem_logDelete.triggered.connect(deleteLogFile)
    ui.menuItem_stopScript.triggered.connect(stopRunningScript)


# 清除log输出显示内容
def clearLogOutput():
    if ui.log_output_EditText.getPaintContext() != "":
        reply = QMessageBox.question(mainWindow, "提示", "将会清除以下Log：{}".format(str(ui.log_output_EditText.toPlainText())),
                                     QMessageBox.Yes | QMessageBox.No)
        if int(reply) == 16384:
            ui.log_output_EditText.clear()
            ui.statusbar.showMessage("Log已清除完毕……", -1)
        elif int(reply) == 65536:
            pass


# 删除log文件./log.txt
def deleteLogFile():
    if os.path.exists("./log.txt"):
        reply = QMessageBox.question(mainWindow, "提示", "将会删除本地根目录下的log.txt文件……", QMessageBox.Yes | QMessageBox.No)
        if int(reply) == 16384:
            os.remove("./log.txt")
            ui.statusbar.showMessage("Log文件已删除……", -1)
        elif int(reply) == 65536:
            pass


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
