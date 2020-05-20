# 1.编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 2.采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 1.创建数据库表；
# 2.新增联系人；
# 3.按姓名查询联系人详细信息；
# 4.删除联系人；
import sqlite3
conn = sqlite3.connect('E:\\PythonWork\\week10\\addressbook.db')

#创建数据库表
def data_creat():
    conn.execute('''
    CREATE TABLE ADDRESS(
    ID INT PRIMARY KEY,
    NAME TEXT UNIQUE NOT NULL,
    TEL CHAR(11) NOT NULL,
    COMPANY CHAR(100) NOT NULL,
    ADDRESS CHAR(200) NOT NULL
    );''')
    print("Table ADDRESS created successfully!")
    conn.close()

def data_insert(id,name,tel,company="上海建桥学院",address="沪城环路1111号"):
    conn = sqlite3.connect('E:\\PythonWork\\week10\\addressbook.db')
    conn.execute("INSERT INTO ADDRESS(ID,NAME,TEL,COMPANY,ADDRESS) values('%s', '%s','%s', '%s','%s')" % (id,name,tel,company,address))
    conn.commit()
    num = conn.total_changes
    print("{0} rows changed in table USER.".format(num))
    print("Insert operation successfully")

def data_select(name):
    conn = sqlite3.connect('E:\\PythonWork\\week10\\addressbook.db')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT ID,NAME,TEL,COMPANY,ADDRESS "
                             "from ADDRESS "
                             "where NAME='"+name+"' ")
    row = cursor1.fetchone()
    if row is None:
        print("对不起,没有找到{}联系人".format(name))
    else:
        print("ID=", row[0])
        print("NAME=", row[1])
        print("TEL=", row[2])
        print("COMPANY=", row[3])
        print("ADDRESS=", row[4])
    cursor1.close()
    conn.close()
def data_delete(id):
    conn = sqlite3.connect('E:\\PythonWork\\week10\\addressbook.db')
    conn.execute("delete from ADDRESS where ID="+id)
    conn.commit()
    num = conn.total_changes
    if num==0:
        print("通讯录中无id为{}的联系人".format(id))
    else:
        print("Total number of rows updated :{}".format(num))
        print("删除id="+id+"的联系人")
    conn.close()
def main():
    print('-'*25,"通讯录",'-'*25)

    while 1:
        k = input("请输入指令：")
        if k == 'create':
            print("创建数据库表")
            data_creat()
            temp = input("是否继续操作通讯录？输入y继续，n退出")
            if temp == "n":
                print("成功退出！！")
                break
            else:
                continue
        elif k == 'add':
            print("新增联系人")
            id_1=int(input("请输入联系人id:"))
            name_1=input("请输入联系人名字：")
            tel_1 = input("请输入联系人电话：")
            data_insert(id = id_1, name = name_1,tel = tel_1)
            temp = input("是否继续操作通讯录？输入y继续，n退出")
            if temp == "n":
                print("成功退出！！")
                break
            else:
                continue

        elif k == "search":
            print("按姓名查询联系人详细信息")
            name=input("请输入你要查询的联系人名字:")
            data_select(name)
            temp = input("是否继续操作通讯录？输入y继续，n退出")
            if temp == "n":
                print("成功退出！！")
                break
            else:
                continue

        elif k =='del':
            print("删除联系人")
            id = input("请输入您要删除联系人的id：")
            data_delete(id)
            temp1 = input("是否继续操作通讯录？输入y继续，n退出")
            if temp1 == "n":
                print("成功退出！！")
                break
            else:
                continue


if __name__=='__main__':
    main()


#运行结果
# E:\week10\Scripts\python.exe E:/PythonWork/week10/sql.py
# ------------------------- 通讯录 -------------------------
# 请输入指令：add
# 新增联系人
# 请输入联系人id:1
# 请输入联系人名字：包艺源
# 请输入联系人电话：1720390
# 1 rows changed in table USER.
# Insert operation successfully
# 是否继续操作通讯录？输入y继续，n退出y
# 请输入指令：add
# 新增联系人
# 请输入联系人id:2
# 请输入联系人名字：张三
# 请输入联系人电话：123
# 1 rows changed in table USER.
# Insert operation successfully
# 是否继续操作通讯录？输入y继续，n退出y
# 请输入指令：search
# 按姓名查询联系人详细信息
# 请输入你要查询的联系人名字:包艺源
# ID= 1
# NAME= 包艺源
# TEL= 1720390
# COMPANY= 上海建桥学院
# ADDRESS= 沪城环路1111号
# 是否继续操作通讯录？输入y继续，n退出y
# 请输入指令：search
# 按姓名查询联系人详细信息
# 请输入你要查询的联系人名字:张三
# ID= 2
# NAME= 张三
# TEL= 123
# COMPANY= 上海建桥学院
# ADDRESS= 沪城环路1111号
# 是否继续操作通讯录？输入y继续，n退出y
# 请输入指令：del
# 删除联系人
# 请输入您要删除联系人的id：2
# Total number of rows updated :1
# 删除id=2的联系人
# 是否继续操作通讯录？输入y继续，n退出y
# 请输入指令：search
# 按姓名查询联系人详细信息
# 请输入你要查询的联系人名字:张三
# 对不起,没有找到张三联系人
# 是否继续操作通讯录？输入y继续，n退出
