# coding = utf8
import os

import pymysql

os.path.abspath(".")
"""
    @Project:PyQt5Project
    @File:mysqlController.py
    @Author:十二点前要睡觉
    @Date:2022/4/25 9:57
"""

if __name__ == '__main__':
    conn = pymysql.connect(host="localhost", user="chenguangtao", password="cgt19981002", db="test", charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor)
    print(conn.host)
    print(conn.db)
    print(conn.user)
    print(conn.password)