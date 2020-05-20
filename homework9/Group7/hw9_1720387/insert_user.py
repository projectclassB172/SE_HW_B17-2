import sqlite3
def insertUser(user):#插入一个对象user
    conn = sqlite3.connect('addressBook.db')
    conn.execute("INSERT INTO User(Name,Phone,Company,Address) "
                 "VALUES ('%s','%s','%s','%s')" % (
                 user.getName(), user.getPhone(), user.getCompany(), user.getAddress()))
    conn.commit()  # 注意一定要commit
    print('插入结果:姓名:{}\t电话:{}\t公司:{}\t地址:{}\t这条数据插入成功！'.format(user.getName(), user.getPhone(), user.getCompany(),user.getAddress()))
    conn.close()

def insertUserList(userList):#插入列表userList
    conn = sqlite3.connect('addressBook.db')
    for user in userList:
        conn.execute("INSERT INTO User(Name,Phone,Company,Address) "
                     "VALUES ('%s','%s','%s','%s')" % (
                     user.getName(), user.getPhone(), user.getCompany(), user.getAddress()))
        conn.commit()  # 注意一定要commit
        print('插入结果:姓名:{}\t电话:{}\t公司:{}\t地址:{}\t这条数据插入成功！'.format(user.getName(),user.getPhone(),user.getCompany(),user.getAddress()))
    conn.close()