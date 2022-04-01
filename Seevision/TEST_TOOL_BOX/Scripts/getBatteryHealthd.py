# coding = utf8
import os
import subprocess
from time import sleep

os.path.abspath(".")
"""
    @Project:PycharmProjects
    @File:getBatteryHealthd.py
    @Author:十二点前要睡觉
    @Date:2021/12/20 17:36s
"""


def toTxt(log):
    with open(".\log.txt", "a+") as f:
        f.write(str(log) + "\n")


if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        print("第{}次dump电池充电数据情况：\n".format(str(i)))
        toTxt("第{}次dump电池充电数据情况：\n".format(str(i)))
        toTxt(subprocess.Popen("adb shell dmesg | grep healthd", shell=True).communicate())
        sleep(3)
