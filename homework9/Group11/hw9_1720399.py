"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；
"""
#创建数据库表；
import sqlite3
conn=sqlite3.connect('D:\\qym\\phone.db')
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

import sqlite3
def create_table():#新建通讯录表
    conn=sqlite3.connect("D:\\qym\\phone.db")
    cursor=conn.cursor()
    sql='''create table myaddressbook(id integer primary key autoincrement,
    name text,
    tel int,
    company text,
    address text)'''
    cursor.execute(sql)
    cursor.close()
    print('新建通讯录表')
#插入数据
def insert_data(name,tel,company,address):
    conn=sqlite3.connect('D:\\qym\\phone.db')
    cursor=conn.cursor()
    sql='''insert into myaddressbook(name,tel,company,address)values
    (?,?,?,?)'''
    cursor.execute(sql,(name,tel,company,address))
    conn.commit()
    cursor.close()
    print('新建联系人')
#按姓名查询联系人详细信息
try:
    name = input("请输入要查询的人的姓名")
    cursor.execute("SELECT id,name,phone,company,address From user WHERE name=?;",(name,))
    user = cursor.fetchone()
    print("查询结果为:")
    print(user)
except:
    print("输入有误,跳过查询\n")
'''
删除联系人
'''
try:
    id1 = input("请输入要删除的id:")
    id1 = int(id1)
    conn.execute("delete from user where ID=?;",(id1,))
    conn.commit()
    print("删除成功")
except:
    print("删除失败")
#打印全部数据
cursor.execute("SELECT id,name,company,address From user")
users = cursor.fetchall()
print("打印全部数据：\n")
print(users)
cursor.close()
conn.close()
if __name__ == "__main__":
    # 连接数据库(如果不存在则创建)
    conn = sqlite3.connect('address_book.db')
    print("数据库连接成功！")
    # 创建游标
    cr = conn.cursor()
    db=DB()#创建对象
    db.main()#调用main方法
    # 关闭数据库操作
    cr.close()
    print("数据库连接已关闭！")


