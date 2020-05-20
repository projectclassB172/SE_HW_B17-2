import sqlite3
#   连接数据库
def connection():
    conn = sqlite3.connect("C:\\Users\\JackSmith\\Desktop\\PY0515\\PhoneList.db")
    print("数据库连接成功")
    return conn

#   创建数据库表
def createTable(conn):
    try:
        conn.execute('''CREATE TABLE t_table
                (
                id       PRIMARY KEY NOT NULL ,
                name  TEXT  NOT NULL
                phone  TEXT NOT NULL,
                company TEXT ,
                address TEXT；''')
          conn.commit()
        print("t_table 创建成功")
        except sqlite3.OperationalError as reason:
            print("错误:  创建失败： " + str(reason) + "\n")


def addperson():
    id = int(input('请输入你的ID: '))
    name= str(input("请输入你的姓名："))
    phone = str(input("请输入你的电话："))
    company = str(input("请输入你的公司："))
    address = str(input("请输入你的地址："))
    conn.execute("insert into person VALUES(?,?.?,?,?)",(id,name, tel , company, address))
    conn.commit()
   conn.close()    


def searchperson():
    name = input("请输入您要查询的联系人：")
    person = conn.execute("select id,name,phone,company,address from person where name='"+name+"'")
    for i in person:
        print('id：', i[0])
        print('name：', i[1])
        print('phone：', i[2])
        print('company：', i[3])
        print('address：', i[4])
     conn.close()


def deleteperson():
    name=input("请输入你要删除的联系人：")
    person=conn.execute("delete from person where name='"+name+"'")
    print("删除成功！")
    conn.commit()
    conn.close()
