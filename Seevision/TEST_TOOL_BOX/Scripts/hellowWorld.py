# coding = utf8
import os
import sys
from time import sleep

os.path.abspath("..")
"""
    @Project:PyQt5Project
    @File:hellowWorld.py
    @Author:十二点前要睡觉
    @Date:2022/3/31 16:25
"""

if __name__ == '__main__':
    # while True:
    for i in range(99):
        sleep(2)
        print("Hello World! {}".format(i))
