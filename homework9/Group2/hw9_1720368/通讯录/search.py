import sqlite3
import os

con = sqlite3.connect("contact.db")
cursor = con.cursor()

name = str(input('请输入要查找的姓名: '))
sql = "select * from contact WHERE name = ?"
arr = cursor.execute(sql, (name, ))

values = cursor.fetchall()
if len(values) == 0: 
    print('not found')
    
for item in values:
    print(item)
    print('id: %s, name: %s, mobile: %s, company: %s, address: %s' % (
        item[0],
        item[1],
        item[2],
        item[3],
        item[4]
        ))

#"F:\BaiduNetdiskDownload\PyCharm 2019.3.4\工程文件\venv\Scripts\python.exe" "F:/BaiduNetdiskDownload/PyCharm 2019.3.4/工程文件/venv/通讯录/search.py"
#请输入要查找的姓名: 吴
#(1, '吴', '15911221124', '巴啦啦', '大理')
#id: 1, name: 吴, mobile: 15911221124, company: 巴啦啦, address: 大理

#Process finished with exit code 0
