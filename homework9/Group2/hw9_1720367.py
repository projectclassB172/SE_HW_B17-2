
'''编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
v设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人；'''
import sqlite3
import os
def conphonenumber():
    hcon = sqlite3.connect("users.db")#创建数据库
    c = hcon.cursor()#连接数据库
    # 创建表
    sql = '''create table person (id int primary key, name varchar(20), number char(11), company char(20), addr char(20))'''
    c.execute(sql)
    c.close()
    hcon.close()
    print("成功创建")
    # 创建表
    # 保存更改
    # 关闭与数据库的连接
def addperson(hcon,c):
    id = int(input('请输入你的账号: '))
    name = str(input('请输入你的名字: '))
    number = str(input('请输入你的手机号: '))
    company = str(input('请输入你的公司: '))
    addr = str(input('请输入你的地址: '))
    sql="insert into person(Uid,Uname,Unumber,Ucompany,Uaddr) values(?,?,?,?,?)"
    c.execute(sql, (id,name,number,company,addr))
    hcon.commit()
    print("保持成功")
    hcon.rollback()





def selectmail(hcon,c):
    c.execute('select * from person where name like "余%"')
    print(c.fetchall())

def delete(hcon,c):
	selectmail(hcon,c)
	did=int(input('请输入你要删除的账号： '))
	sql="delete from person where id=?"
	c.execute(sql,(did,))
	hcon.commit()


def choice():
    print("添加联系人请输入:1")
    print("查询联系人请输入:2")
    print("删除联系人请输入:3")
    print("退出请按5")
    Button = 9
    while (Button>5 or Button<0 ):
        Button = int(input("请输入:"))
    return Button

def main():
    if os.path.exists('phonenumber.db') == False:
        conphonenumber()
    hcon = sqlite3.connect('phonenumber.db')
    c = hcon.cursor()
    while (True):
        Button = choice()
        if (Button == 1):
            addperson(hcon,c)
        elif(Button == 2):
            selectmail(hcon,c)
        elif(Button == 3):
            delete(hcon, c)
        else:
            break
        print("结束")


    c.close()
    hcon.close()

if __name__=="__main__":
	main()

'''C:\Users\10951\PycharmProjects\untitled7\venv\Scripts\python.exe C:/Users/10951/PycharmProjects/untitled7/hw9_1720367.py
成功创建
添加联系人请输入:1
查询联系人请输入:2
删除联系人请输入:3
退出请按5
请输入:1
请输入你的账号: 1720367
请输入你的名字: 余杭逍
请输入你的手机号: 16628745417
请输入你的公司: 建桥
请输入你的地址: 云南'''