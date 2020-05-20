#创建数据库表；
import sqlite3
conn=sqlite3.connect('D:\\untitled\\phone.db')
print("打开数据库成功")
conn.execute('''CREATE TABLE USER 
   (PHONENUMBER INT PRIMARY KEY NOT NULL, 
    NAME  TEXT NOT NULL ,
    ADDRESS  TEXT ,
    COMPANY CHAR(50));''')
print("表创建成功")
conn.close()
#运行结果：
#打开数据库成功
#表创建成功


#新增联系人；
import sqlite3
conn=sqlite3.connect('D:\\untitled\\phone.db')
print("打开数据库成功")
conn.execute("INSERT INTO USER (PHONENUMBER,NAME,ADDRESS,COMPANY) \
     VALUES (11245655, '张三', '上海浦东', '阿里巴巴')")
conn.commit()
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))
#运行结果：
#打开数据库成功
#1 rows changed in table USER.


#按姓名查询联系人详细信息；
import sqlite3
conn=sqlite3.connect('D:\\untitled\\phone.db')
print("打开数据库成功")
cursor1 = conn.execute("SELECT PHONENUMBER,ADDRESS,COMPANY from USER where NAME ='张三'")
for row in cursor1:
   print("phone= ", row[0])
   print("ADDRESS = ", row[1])
   print("COMPANY = ", row[2])
conn.close()
#运行结果：
#phone=  11245655
#ADDRESS =  上海浦东
#OMPANY =  阿里巴巴



#删除联系人；
import sqlite3
conn=sqlite3.connect('D:\\untitled\\phone.db')
print("打开数据库成功")
conn.execute("delete from USER where NAME='张三'")
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1=conn.total_changes
print("{0} rows changed in table USER.".format(num1))
conn.close()
#运行结果：
#打开数据库成功
#Total number of rows updated : 1
#1 rows changed in table USER.



