# coding = utf8
import os

os.path.abspath(".")
"""
    @Project:PyQt5Project
    @File:connectPADS.py
    @Author:十二点前要睡觉
    @Date:2022/4/25 16:52
"""

from win32com import client

# pads = client.Dispatch("PowerPCB.Application")
# print(pads.name)

if __name__ == '__main__':
    pads = client.Dispatch("PowerPCB.Application")
    print(pads.name)
    print(pads)
