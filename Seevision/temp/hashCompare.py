# coding = utf8
import os

import imagehash
from PIL import Image

os.path.abspath(".")
"""
    @Project:PyQt5Project
    @File:hashCompare.py
    @Author:十二点前要睡觉
    @Date:2022/4/25 15:11
"""


def compare(A, B):
    A_picture = imagehash.average_hash(Image.open(A))
    B_picture = imagehash.average_hash(Image.open(B))
    print(A_picture)
    print(B_picture)
    print(A_picture - B_picture)
    return A_picture, B_picture


if __name__ == '__main__':
    A = "./pictures/D19.jpeg"
    B = "./pictures/D20.jpeg"
    compare(A, B)
