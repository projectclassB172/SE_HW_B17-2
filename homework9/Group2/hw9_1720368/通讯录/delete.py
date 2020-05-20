#encoding=utf8

"""
"""
import sqlite3
import os
import sys

con = sqlite3.connect("contact.db")
cursor = con.cursor()

did=int(input('请输入你要删除的id： '))

sql="delete from contact where id=?"

cursor.execute(sql,(did,))
con.commit()
print('删除成功')

#"F:\BaiduNetdiskDownload\PyCharm 2019.3.4\工程文件\venv\Scripts\python.exe" "F:/BaiduNetdiskDownload/PyCharm 2019.3.4/工程文件/venv/通讯录/delete.py"
#请输入你要删除的id： 2
#删除成功

#Process finished with exit code 0
