import sqlite3
def deleteUserByName(Name):#删除一个姓名为Name对象
    conn = sqlite3.connect('addressBook.db')
    conn.execute("DELETE FROM User WHERE NAME = '%s'" %(Name))
    conn.commit()  # 注意一定要commit
    print('删除结果:姓名为:{}\t的对象删除成功！'.format(Name))
    conn.close()

def updateUserByName(Name):#形式上删除
    conn = sqlite3.connect('addressBook.db')
    conn.execute("UPDATE User SET DeleSign = 1 WHERE NAME = '%s'" % (Name))
    conn.commit()  # 注意一定要commit
    print('删除结果:姓名为:{}\t的对象删除成功！'.format(Name))
    conn.close()

def deleteUserByID(ID):#删除一个姓名为Name对象
    conn = sqlite3.connect('addressBook.db')
    conn.execute("DELETE FROM User WHERE ID = '%s'" %(ID))
    conn.commit()  # 注意一定要commit
    print('删除结果:ID为:{}\t的对象删除成功！'.format(ID))
    conn.close()

def updateUserByID(ID):#形式上删除
    conn = sqlite3.connect('addressBook.db')
    conn.execute("UPDATE User SET DeleSign = 1 WHERE ID = '%s'" %(ID))
    conn.commit()  # 注意一定要commit
    print('删除结果:ID为:{}\t的对象删除成功！'.format(ID))
    conn.close()