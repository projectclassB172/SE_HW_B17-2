#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
#创建数据库表；
#新增联系人；
#按姓名查询联系人详细信息；
#删除联系人；
import sqlite3
def db():
    hcon = sqlite3.connect("lhf.db")#创建数据库
    c = hcon.cursor()#连接数据库
    sql = '''create table xx 
    (id int primary key NOT NULL,
    name TEXT NOT NULL, 
    phone char(11), 
    company char(20), 
    addr char(20))'''
    c.execute(sql)
    c.close()
    hcon.close()
    print("创建表成功")
def addperson(hcon,hc):
    id = int(input('ID: '))
    name = str(input('名字: '))
    phone = str(input('手机号: '))
    company = str(input('公司: '))
    addr = str(input('地址: '))
    sql="insert into xx(id,name,phone,company,addr) values(?,?,?,?,?)"
    hc.execute(sql, (id,name,phone,company,addr))
    hcon.commit()
    print("添加用户成功")
    hcon.rollback()
def delete(hcon,hc):
	selectmail(hcon,hc)
	did=int(input('删除的id： '))
	sql="delete from xx where id=?"
	hc.execute(sql,(did,))
	hcon.commit()
def selectmail(hcon, hc):
    hc.execute('select * from xx where name like "刘%"')
    print(hc.fetchall())
def choice():
    print(".。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
    print("功能")
    print("增:1")
    print("查:2")
    print("删:3")
    print(".。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
    Button = 9
    while (Button>5 or Button<0 ):
        Button = int(input("请输入:"))
    return Button
import os
def main():
    if os.path.exists('lhf.db') == False:
        db()
    hcon = sqlite3.connect('lhf.db')
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

    #D:\pythion\python3.8.2\python.exe D:\pythion\lx\hw9_1720365.py
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#功能
#增:1
#查:2
#删:3
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#请输入:1
#ID: 2
#名字: 刘三
#手机号: 0
#公司: 9
#地址: 8
#添加用户成功
#结束
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#功能
#增:1
#查:2
#删:3
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#请输入:2
#[(1, '刘海峰', '3', '4', '5'), (2, '刘三', '0', '9', '8')]
#结束
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#功能
#增:1
#查:2
#删:3
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#请输入:3
#[(1, '刘海峰', '3', '4', '5'), (2, '刘三', '0', '9', '8')]
#删除的id： 2
#结束
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
#功能
#增:1
#查:2
#删:3
#.。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
