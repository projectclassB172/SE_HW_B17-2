#encoding=utf8

"""
"""
import sqlite3
import os
import sys

con = sqlite3.connect("contact.db")
cursor = con.cursor()

print('请输入个人信息：')
id      = int(input('ID: '))
name    = str(input('姓名: '))
mobile  = str(input('电话: '))
company = str(input('公司: '))
address = str(input('地址: '))

sql="insert into contact(id, name, mobile, company, address) values(?,?,?,?,?)"
try: 
    cursor.execute(sql, (id, name, mobile, company, address))
except Exception as e: 
    con.rollback()
    print("internal error")

    sys.exit(0)

con.commit()
print("保存成功")

#"F:\BaiduNetdiskDownload\PyCharm 2019.3.4\工程文件\venv\Scripts\python.exe" "F:/BaiduNetdiskDownload/PyCharm 2019.3.4/工程文件/venv/通讯录/add.py"
#请输入个人信息：
#ID: 4
#姓名: 艾
#电话: 15125230878
#公司: 西奈
#地址: 天津
#保存成功

#Process finished with exit code 0
