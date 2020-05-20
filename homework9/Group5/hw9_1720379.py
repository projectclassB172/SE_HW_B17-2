"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；
"""
import sqlite3
def create_table():#新建通讯录表
    conn=sqlite3.connect("D:\\HhlJunior\\XMSZ\\addressbook1.db")
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
    conn=sqlite3.connect('D:\\HhlJunior\\XMSZ\\addressbook.db')
    cursor=conn.cursor()
    sql='''insert into myaddressbook(name,tel,company,address)values
    (?,?,?,?)'''
    cursor.execute(sql,(name,tel,company,address))
    conn.commit()
    cursor.close()
    print('新建联系人')
#查询所有联系人详细信息
def serach_data():
    print('查询所有联系人详细信息:')
    conn=sqlite3.connect('D:\\HhlJunior\\XMSZ\\addressbook.db')
    cursor=conn.cursor()
    sql='''select * from myaddressbook'''
    recults=cursor.execute(sql)
    recults_all=recults.fetchall()
    for r in recults_all:
        print(r)
    cursor.close()

def Serach_DataOfName(table,name):
    print(f'{name}联系人详细信息:')
    conn=sqlite3.connect('D:\\HhlJunior\\XMSZ\\addressbook.db')
    cursor=conn.cursor()
    sql="select id,tel,company,address from "+table+" where name=?"
    results=cursor.execute(sql,(name,))
    results_all=results.fetchall()
    for r in results_all:
        print(r)
    cursor.close()
    conn.close()
def del_data(table,name):
    f=is_have(table,name)
    if f==0:
        print('查无此人')
        return
    else:
        print(f'删除联系人{name}的数据')
        conn = sqlite3.connect('D:\\HhlJunior\\XMSZ\\addressbook.db')
        cursor = conn.cursor()
        sql = "delete from" + table + "where name=?"
        cursor.execute(sql, (name,))
        conn.commit()
        cursor.close()

def is_have(table,name):
    conn=sqlite3.connect('D:\\HhlJunior\\XMSZ\\addressbook.db')
    cursor=conn.cursor()
    sql="select id,tel,company,address from "+table+" where name=?"
    results=cursor.execute(sql,(name,))
    results_all=results.fetchall()
    if results_all:
        return 1
    else:
        return 0
    cursor.close()
    conn.close()

if __name__ == '__main__':
    #create_table()
    # serach_data()
    # insert_data('李四',19921312287,'南京路','建桥')
    # Serach_DataOfName('myaddressbook','李四')
    # del_data('myaddressbook','何慧俐')
    serach_data()

"""
D:\HhlAfter\AfterPython\venv\Scripts\python.exe D:/HhlAfter/AfterPython/demo0515/hw9_1720379.py
新建通讯录表
查询所有联系人详细信息:
(1, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(2, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(3, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(4, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(5, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(6, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(7, '李四', 19921312287, '南京路', '建桥')
新建联系人
李四联系人详细信息:
(7, 19921312287, '南京路', '建桥')
(8, 19921312287, '南京路', '建桥')
查无此人
查询所有联系人详细信息:
(1, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(2, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(3, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(4, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(5, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(6, '何慧俐', 19921312287, '北环路健身房', '旧州小区')
(7, '李四', 19921312287, '南京路', '建桥')
(8, '李四', 19921312287, '南京路', '建桥')

Process finished with exit code 0

"""