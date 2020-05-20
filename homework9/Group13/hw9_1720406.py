import sqlite3
import os
def create_table():

    try:
        sql='''create table USER (id int primary key, name varchar(20), number char(11), company char(20), addr char(20))'''
        con.execute(sql)
        print("USER 创建成功!\n")
    except sqlite3.OperationalError as reason:
        print("错误: 创建失败： " + str(reason) + "\n")

def information(con,cur):
    id = int(input('请输入你的ID: '))
    name = str(input('请输入你的名字: '))
    number = str(input('请输入你的手机号: '))
    company = str(input('请输入你的公司: '))
    addr = str(input('请输入你的地址: '))
    sql = "insert into user(id,name,number,company,addr) values(?,?,?,?,?)"
    cur.execute(sql, (id, name, number, company, addr))
    con.commit()
    print("保持成功")
    con.rollback()

def select (con,cur):

    try:
        name = input("请输入要查询的人的姓名:")
        cur.execute("SELECT * From user WHERE  name='{}'".format(name))
        print("查询结果为:{}".fomat.cur.fetchall())

    except:
        print("输入有误,跳过查询\n")

def delete(con,cur):
    try:
        id1=int(input('请输入你要删除的id： '))
        con.execute("delete from user where ID=?;",(id1,))
        con.commit()
        print("删除成功")
    except:
        print("删除失败")

def menu():
    print("欢迎使用通讯录")
    print("1.新增联系人")
    print("2.按姓名查询 ")
    print("3.删除联系人")
    print("0.退出")
    Button = int(input("请输入:"))
    return Button

def main():
    while (True):
        Button = menu()
        if (Button == 0):
            print("成功退出系统...")
            return
        elif (Button == 1):
            information(con,cur)
        elif(Button == 2):
            select(con,cur)
        elif(Button == 3):
            delete(con,cur)
        else:
            break
        print("结束")

if __name__=="__main__":
    # 连接数据库(如果不存在则创建)
    con = sqlite3.connect('addr.db')
    print("数据库连接成功！")
    # 创建游标
    cur = con.cursor()
    main()
    # 关闭数据库操作
    cur.close()
    con.close
    print("数据库连接已关闭！")