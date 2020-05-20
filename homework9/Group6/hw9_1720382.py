# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 创建数据库表；
# 新增联系人；
# 按姓名查询联系人详细信息；
# 删除联系人；
# 修改联系人数据
import sqlite3
###
#   建立连接
###
def connection():
    conn = sqlite3.connect("C:\\Users\\JackSmith\\Desktop\\PY0515\\PhoneList.db")
    print("Opened database successfully")
    return conn
###
#   创建数据库表
###
def createTable(conn):
    try:
        conn.execute('''CREATE TABLE PHONELIST(
                NAME TEXT PRIMARY KEY NOT NULL ,
                TEL TEXT NOT NULL,
                COMPANY TEXT VARCHAR(20) ,
                ADDRESS TEXT
            )''')
        print("Table PHONEList created successfully")
    except sqlite3.OperationalError as reason:
        print("错误:创建失败： " + str(reason) + "\n")
###
#   新建联系人
###
def inputInfo(conn):
    print("请依次输入新增联系人的姓名、电话、公司、地址：")
    name= str(input("姓名："))
    tel = str(input("电话："))
    company = str(input("公司："))
    address = str(input("地址："))
    conn.execute("INSERT INTO  PHONEList VALUES(?,?,?,?)",(name, tel , company, address))
    conn.commit()
    print("新增联系人成功！！！")
###
#   按姓名查询联系人详细信息
###
def search(conn):
    print('按姓名查询联系人详细信息')
    name = input("请输入您要查询的联系人的姓名：")
    friend = conn.execute("SELECT * FROM PHONELIST WHERE NAME ='"+str(name)+"'")
    for i in friend:
        print('姓名：', i[0])
        print('联系方式：', i[1])
        print('公司：', i[2])
        print('地址：', i[3])
        if i is not None:
            print('联系人查询成功')
        else:
            print('联系人不存在！！')
###
#   删除联系人
###
def delete(conn):
    print("1 代表 按照名字删除数据")
    print("2 代表 按照电话删除数据")
    print("3 代表 按照公司删除数据")
    print("4 代表 按照地址删除数据")
    print("其他任意数字 代表 取消")
    flag = int(input("请输入一个数字代表你要删除数据的方式："))
    kind = ""
    if flag == 1:
        kind = "NAME"
        s = input("请输入您要删除的联系人姓名：")
        conn.execute("DELETE FROM PHONELIST WHERE "+kind+" = '"+str(s)+"'")
        print("删除数据 successfully")
    elif flag == 2:
        kind = "TEL"
        s = input("请输入您要删除的联系人电话：")
        conn.execute("DELETE FROM PHONELIST WHERE " + kind + " = '" + str(s) + "'")
        print("删除数据 successfully")
    elif flag == 3:
        kind = "COMPANY"
        s = input("请输入您要删除的联系人的公司名称：")
        conn.execute("DELETE FROM PHONELIST WHERE " + kind + " = '" + str(s) + "'")
        print("删除数据 successfully")
    elif flag == 4:
        kind == "ADDRESS"
        s = input("请输入您要删除的联系人的地址：")
        conn.execute("DELETE FROM PHONELIST WHERE " + kind + " = '" + str(s) + "'")
        print("删除数据 successfully")
    else:
        print("取消删除")
###
#   修改联系人数据
###
def update(conn):
    print("1 代表 修改名字数据")
    print("2 代表 修改电话数据")
    print("3 代表 修改公司数据")
    print("4 代表 修改地址数据")
    print("其他任意数字 代表 取消")
    flag = int(input("请输入一个数字代表你要修改数据的方式："))
    kind = ""
    if flag == 1:
        kind = "NAME"
        s = input("请输入您要修改的联系人姓名：")
        new = input("请输入新的联系人名字：")
        conn.execute("UPDATE PHONELIST SET "+kind+" = '"+str(new)+"' WHERE NAME = '"+str(s)+"'")
        print("修改数据 successfully")
        person = conn.execute("SELECT * FROM PHONELIST WHERE NAME ='"+str(new)+"'")
        for p in person:
            print('姓名：', p[0])
            print('联系方式：', p[1])
            print('公司：', p[2])
            print('地址：', p[3])
        conn.commit()
    elif flag == 2:
        kind = "TEL"
        s = input("请输入您要修改的联系人姓名：")
        new = input("请输入新的联系人电话：")
        conn.execute("UPDATE PHONELIST SET "+kind+" = '"+str(new)+"' WHERE NAME = '"+str(s)+"'")
        print("修改数据 successfully")
        person = conn.execute("SELECT * FROM PHONELIST WHERE NAME ='"+str(s)+"'")
        for p in person:
            print('姓名：', p[0])
            print('联系方式：', p[1])
            print('公司：', p[2])
            print('地址：', p[3])
        conn.commit()
    elif flag == 3:
        kind = "COMPANY"
        s = input("请输入您要修改的联系人姓名：")
        new = input("请输入新的公司名称：")
        conn.execute("UPDATE PHONELIST SET " + kind + " = '" + str(new) + "' WHERE NAME = '" + str(s) + "'")
        print("修改数据 successfully")
        person = conn.execute("SELECT * FROM PHONELIST WHERE NAME ='"+str(s)+"'")
        for p in person:
            print('姓名：', p[0])
            print('联系方式：', p[1])
            print('公司：', p[2])
            print('地址：', p[3])
        conn.commit()
    elif flag == 4:
        kind = "ADDRESS"
        s = input("请输入您要修改的联系人姓名：")
        new = input("请输入新的地址名称：")
        conn.execute("UPDATE PHONELIST SET " + kind + " = '" + str(new) + "' WHERE NAME = '" + str(s) + "'")
        print("修改数据 successfully")
        person = conn.execute("SELECT * FROM PHONELIST WHERE NAME ='" + str(s) + "'")
        for p in person:
            print('姓名：', p[0])
            print('联系方式：', p[1])
            print('公司：', p[2])
            print('地址：', p[3])
        conn.commit()
    else:
        print("取消修改")
def information():
    print("=========个人通信录小程序==========")
    print("1  新增联系人")
    print("2  按姓名查询联系人详细信息")
    print("3  删除联系人")
    print("4  修改联系人数据")
    print("0  程序结束")
    print("==================================")

conn = connection()
createTable(conn)
while True:
    information()
    flag = int(input("请输入您需要的操作数字："))
    if flag == 1:
        inputInfo(conn)
    elif flag == 2:
        search(conn)
    elif flag == 3:
        delete(conn)
    elif flag == 4:
        update(conn)
    else:
        print("结束程序")
        break
# 运行结果
# C:\Users\JackSmith\Desktop\PY0515\venv\Scripts\python.exe C:/Users/JackSmith/Desktop/PY0515/hw9_1720392.py
# Opened database successfully
# Table PHONEList created successfully
# =========个人通信录小程序==========
# 1  新增联系人
# 2  按姓名查询联系人详细信息
# 3  删除联系人
# 4  修改联系人数据
# 0  程序结束
# ==================================
# 请输入您需要的操作数字：1
# 请依次输入新增联系人的姓名、电话、公司、地址：
# 姓名：樊崟杰
# 电话：1720392
# 公司：Tencent
# 地址：深圳
# 新增联系人成功！！！
# =========个人通信录小程序==========
# 1  新增联系人
# 2  按姓名查询联系人详细信息
# 3  删除联系人
# 4  修改联系人数据
# 0  程序结束
# ==================================
# 请输入您需要的操作数字：2
# 按姓名查询联系人详细信息
# 请输入您要查询的联系人的姓名：樊崟杰
# 姓名： 樊崟杰
# 联系方式： 1720392
# 公司： Tencent
# 地址： 深圳
# 联系人查询成功
# =========个人通信录小程序==========
# 1  新增联系人
# 2  按姓名查询联系人详细信息
# 3  删除联系人
# 4  修改联系人数据
# 0  程序结束
# ==================================
# 请输入您需要的操作数字：4
# 1 代表 修改名字数据
# 2 代表 修改电话数据
# 3 代表 修改公司数据
# 4 代表 修改地址数据
# 其他任意数字 代表 取消
# 请输入一个数字代表你要修改数据的方式：4
# 请输入您要修改的联系人姓名：樊崟杰
# 请输入新的地址名称：浙江
# 修改数据 successfully
# 姓名： 樊崟杰
# 联系方式： 1720392
# 公司： Tencent
# 地址： 浙江
# =========个人通信录小程序==========
# 1  新增联系人
# 2  按姓名查询联系人详细信息
# 3  删除联系人
# 4  修改联系人数据
# 0  程序结束
# ==================================
# 请输入您需要的操作数字：3
# 1 代表 按照名字删除数据
# 2 代表 按照电话删除数据
# 3 代表 按照公司删除数据
# 4 代表 按照地址删除数据
# 其他任意数字 代表 取消
# 请输入一个数字代表你要删除数据的方式：1
# 请输入您要删除的联系人姓名：樊崟杰
# 删除数据 successfully
# =========个人通信录小程序==========
# 1  新增联系人
# 2  按姓名查询联系人详细信息
# 3  删除联系人
# 4  修改联系人数据
# 0  程序结束
# ==================================
# 请输入您需要的操作数字：0
# 结束程序
#
# Process finished with exit code 0
