# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。 
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址； 
# 设计相应的函数完成以下数据库操作： 
# 创建数据库表； 
# 新增联系人； 
# 按姓名查询联系人详细信息； 
# 删除联系人

import sqlite3
conn = sqlite3.connect('D:\\lfaimr\\test.db')
print("成功打开数据库！");

conn.execute('''CREATE TABLE USER
(ID INT PRIMARY KEY     NOT NULL, 
NAME           TEXT    NOT NULL,  
TELEPHONE      CHAR(50) NOT NULL,
COMPANY        TEXT    NOT NULL,
ADDRESS        TEXT    NOT NULL);''')
print("用户表创建成功！");

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (1, 'Sam', 13166254782, 拼多多','杭州')")

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (2, 'Lee', 15698535475, '京东','北京')")

conn.execute("INSERT INTO USER (ID,NAME,TELEPHONE,COMPANY,ADDRESS) \
    VALUES (3, 'Lucy', 18936529863, '美团','上海')")

conn.commit()
print("创建成功")



conn = sqlite3.connect('D:\\lfaimr\\test.db')
print("成功打开数据库！");

cursor1 = conn.execute("SELECT ID,NAME,TELEPHONE,COMPANY,ADDRESS from USER where ID=2")
for row in cursor1:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("TELEPHONE = ", row[2])
   print("COMPANY = ", row[3])
   print("ADDRESS = ", row[4])
   print("操作完成")

conn = sqlite3.connect('D:\\lfaimr\\test.db')
print("成功打开数据库！");
conn.execute("delete from USER where COMPANY='京东'")
conn.commit()
print("用户删除成功！")
    conn.close()
