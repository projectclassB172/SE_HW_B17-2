import sqlite3
from sqlite3 import OperationalError
# 采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 链接并创建数据库addressBook.db和User表
def createDatebase():#创建数据库addressBook.db和User表
    conn = sqlite3.connect('addressBook.db')
    print("*创建&打开数据库addressBook.db成功!")
    try:# 创建User表
        conn.execute('''CREATE TABLE User
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           Name TEXT NOT NULL,
           Phone CHAR(11) NOT NULL,
           Company TEXT NOT NULL,
           Address TEXT NOT NULL,
           DeleSign INT DEFAULT 0);''')
        # 注意异常：OperationalError:table Hero already exists
        print("*创建表格结果:创建User表格成功！")
    except OperationalError:#异常处理
        print("*创建表格结果:User表格已经存在！")
    conn.close()#关闭连接
