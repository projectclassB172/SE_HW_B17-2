'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
    创建数据库表；
    新增联系人；
    按姓名查询联系人详细信息；
    删除联系人；
'''
import sqlite3
conn = sqlite3.connect('D:\student_admin\student_admin.db')
print("数据库打开成功")
conn.close()

#创建数据库表
def table():
    conn = sqlite3.connect('D:\student_admin\student_admin.db')
    conn.execute('''create table Info(id int primary key , name char(10) not null , tel int not null , company char(30) not null , address char(30) not null);''')
    print("数据表创建成功")
    conn.close()

#新增联系人
def insert():
    conn = sqlite3.connect('D:\student_admin\student_admin.db')
    conn.execute("INSERT INTO Info(id , name , tel , company , address)"
                 "VALUES(1 , 'HHR' , '10086' , 'Tencent' , 'SHANGHAI')")
    conn.execute("INSERT INTO Info(id , name , tel , company , address)"
                 "VALUES(2 , 'MHT' , '10000' , 'Tencent' , 'SHENZHEN')")
    conn.commit()
    num1 = conn.total_changes
    print("{0}rows changed in table Info.".format(num1))
    print("数据插入成功")

#按姓名查询联系人详细信息；
def search():
    conn = sqlite3.connect('D:\student_admin\student_admin.db')
    name = input('输入要查询的姓名:')
    cursor1 = conn.execute("SELECT id , name , tel , company , address from Info where name=?;",(name,))
    for row in cursor1:
        print('id = ' , row[0])
        print('name = ' , row[1])
        print('tel = ' , row[2])
        print('company = ' , row[3])
        print('address = ' , row[4])
    conn.close()

#删除联系人
def delete():
    conn = sqlite3.connect('D:\student_admin\student_admin.db')
    name = input('输入要删除的姓名：')
    conn.execute('delete from Info where name=?;',(name,))
    print('删除成功')
    conn.commit()
    conn.close()

table()
insert()
search()
delete()

'''
数据库打开成功
数据表创建成功
2rows changed in table Info.
数据插入成功
输入要查询的姓名:HHR
id =  1
name =  HHR
tel =  10086
company =  Tencent
address =  SHANGHAI
输入要删除的姓名：MHT
删除成功
'''