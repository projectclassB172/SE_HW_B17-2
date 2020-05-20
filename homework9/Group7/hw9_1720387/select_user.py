import sqlite3
from hw9_1720387.User import User

def selectUserList(Name):#Name为查询条件进行查询信息
    userList = []#接受查询结果
    conn = sqlite3.connect('addressBook.db')

    result = conn.execute("SELECT ID ,Name ,Phone ,Company ,Address FROM User WHERE DeleSign = 0 AND Name = '%s' " %(Name))
    resultAll = result.fetchall()
    for user in resultAll:#获取查询到的数据
        ID = user[0]
        Name = user[1]
        Phone = user[2]
        Company = user[3]
        Address = user[4]
        userTemp = User(Name,Phone,Company,Address)
        userTemp.setID(ID)
        userList.append(userTemp)

    conn.close()
    return userList

def selectUserAll():#查询所有未被删除的用户信息
    userList = []  # 接受查询结果
    conn = sqlite3.connect('addressBook.db')

    result = conn.execute(
        "SELECT ID ,Name ,Phone ,Company ,Address FROM User WHERE DeleSign = 0 ")
    resultAll = result.fetchall()
    for user in resultAll:  # 获取查询到的数据
        ID = user[0]
        Name = user[1]
        Phone = user[2]
        Company = user[3]
        Address = user[4]
        userTemp = User(Name, Phone, Company, Address)
        userTemp.setID(ID)
        userList.append(userTemp)

    conn.close()
    return userList