import sqlite3
conn = sqlite3.connect('1720375.db')#连接数据库
c = conn.cursor()
print("数据库打开成功！")

#创建数据库表
def create():
    global conn
    conn.execute('''CREATE TABLE PERSON_1720375
           (NAME          TEXT    NOT NULL,
           TEL            INT     NOT NULL,
           COMPANY        CHAR(50),
           ADDRESS        CHAR(50));''')
    print("数据库表创建成功！")
    conn.commit()

#添加用户数据
def insert():
    global conn
    c = conn.cursor()
    xname = input("姓名：")
    xtel = input("电话号码:")
    xcompany = input("公司：")
    xaddress = input("地址：")
    person = (xname,xtel,xcompany,xaddress)
    c.execute("INSERT INTO PERSON_1720375 (NAME,TEL,COMPANY,ADDRESS) \
        VALUES (?,?,?,?)", person)
    conn.commit()
    print("用户数据添加成功！")

#查询用户信息
def select():
    global conn
    c = conn.cursor()
    sname=input("请输入所需要查询的用户姓名:")
    c.execute("SELECT NAME,TEL,COMPANY,ADDRESS from PERSON_1720375 WHERE NAME = ?;", (sname,))
    print(c.fetchall())
    print("用户信息查询成功！")

#删除用户信息
def delete():
    global conn
    c = conn.cursor()
    dname = input("请输入所需要删除的用户姓名：")
    c.execute("DELETE from PERSON_1720375 WHERE NAME = ?;", (dname,))
    conn.commit()
    print("用户删除成功！")
    conn.close()


create()
insert()
select()
delete()
