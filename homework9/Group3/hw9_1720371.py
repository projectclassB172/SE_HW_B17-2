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

class ConnDB:
    def __init__(self): #初始化
        self.conn = sqlite3.connect("addr.db") #创建一个数据库
        self.c = self.conn.cursor() #初始化游标c

        while True:
            print("-----这是你的通讯录-----\n可进行以下操作:\n")
            print("1.创建数据库表\n2.新增联系人\n3.按姓名查询联系人详细信息\n4.删除联系人\n")
            opt = input("您的操作是（数字）:")
            if opt == '1':
                self.create_table()
            elif opt == '2':
                self.contacts(self.init_data())
            elif opt == '3':
                self.find(self.input_name())
            elif opt == '4':
                self.delete(self.input_name())
                break
            else:
                print("抱歉！没有这个选项！请重新输入！")


    #关闭数据库,每次对数据库进行操作后，都要记得进行关闭操作
    def close(self):
        self.sql.close()
        self.conn.close()

    # 创建数据库表，id为主键，name为姓名，tel为电话，address为住址
    def create_table(self):
        try:
            self.c.execute('''CREATE TABLE list
                (id INTEGER NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                tel TEXT NOT NULL ,
                company TEXT NULL ,
                address TEXT NULL);''')
            self.conn.commit() #提交，否则无法保存
            print("创建数据库表成功！\n")
        except:
            print("此数据库表已存在！\n")

    #保存用户输入的数据，并以列表形式返回
    def init_data(self):
        try:
            #Id = getpass.getpass("请输入您的ID:")
            Id = input("请输入您的ID:")
            name = input("请输入您的姓名:")
            phone = input("请输入您的电话:")
            company = input("请输入您的公司:")
            address = input("请输入您的住址:")
            init = [Id, name, phone, company, address]
            return init
        except:
            print("获取数据错误，请重新输入！")

    #在数据库中插入用户输入的数据
    def contacts(self, init):
        try:
            #增加了读取6个个参数values(?,?,?,?,?)字段里的5个?号，对应了5个参数
            self.c.execute("INSERT INTO list(id, name, tel, company, address) VALUES(?,?,?,?,?)", (init[0], init[1], init[2], init[3], init[4]))
            self.conn.commit()
            print("添加成功！")
        except:
            print("用户已存在！")

    def input_name(self):
        name = input("请输入您要查找的姓名：")
        return name

    #输入姓名查找信息，在for循环中遍历
    def find(self, name):
        try:
            result = self.c.execute("SELECT * FROM list WHERE name LIKE '%"+name+"%'")
            if result:
                for each in result:
                    print("ID:%d Name:%s Tel:%s Company:%s Address:%s" % (each[0], each[1], each[2], each[3], each[4]))
            else:
                print("用户不存在")
        except:
            print("用户不存在")

    #删除
    def delete(self, name):
        try:
            self.c.execute("DELETE FROM list WHERE name='%s'" % (name))
            self.conn.commit()
            print("删除成功！")
        except:
            print("请先创建数据库表!")


if __name__ == "__main__":
    connect = ConnDB()
    connect.close()


结果：
E:\Workspython\venv\Scripts\python.exe E:/Workspython/venv/sql.py
-----这是你的通讯录-----
可进行以下操作:

1.创建数据库表
2.新增联系人
3.按姓名查询联系人详细信息
4.删除联系人

您的操作是（数字）:1
此数据库表已存在！

-----这是你的通讯录-----
可进行以下操作:

1.创建数据库表
2.新增联系人
3.按姓名查询联系人详细信息
4.删除联系人

您的操作是（数字）:2
请输入您的ID:371
请输入您的姓名:师溥然
请输入您的电话:1
请输入您的公司:上海建桥学院
请输入您的住址:1
添加成功！
-----这是你的通讯录-----
可进行以下操作:

1.创建数据库表
2.新增联系人
3.按姓名查询联系人详细信息
4.删除联系人

您的操作是（数字）:3
请输入您要查找的姓名：师溥然
ID:371 Name:师溥然 Tel:1 Company:上海建桥学院 Address:1
-----这是你的通讯录-----
可进行以下操作:

1.创建数据库表
2.新增联系人
3.按姓名查询联系人详细信息
4.删除联系人

您的操作是（数字）:4
请输入您要查找的姓名：师溥然
删除成功！
-----这是你的通讯录-----
可进行以下操作:

1.创建数据库表
2.新增联系人
3.按姓名查询联系人详细信息
4.删除联系人

您的操作是（数字）: