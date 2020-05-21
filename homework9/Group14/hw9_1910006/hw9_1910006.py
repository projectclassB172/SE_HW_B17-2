def createtable():
    conn.execute("create table addressbook( ID varchar(10) primary key, name text not null, tel text, company text, addr text)")

def insertuser(list_user):
    for user in list_user:
        conn.execute("insert into addressbook (name, tel, company, addr) values('%s', '%s', '%s', '%s')" % (user.name, user.tel, user.company, user.addr))
    conn.commit()
    print("新增了{}个联系人".format(len(list_user)))
    
def finduserbyname(name):
    cursor = conn.execute("select * from addressbook where name='" + name + "'")
    list_user = []
    for row in cursor:
        user = User(row[1], row[2], row[3], row[4])
        list_user.append(user)
    if len(list_user) == 0:
        print("查无此人")
    else:
        for user in list_user:
            print(user.name, user.tel, user.company, user.addr)
    cursor.close()
    return len(list_user)
    
def deleteuser(name):
    if finduserbyname(name) == 0:
        print("删除失败")
    else:
        conn.execute("delete from addressbook where name='" + name + "'")
        conn.commit()
        print("成功删除" + name)
        finduserbyname(name)
    
class User:
    def __init__(self, name, tel, company, addr):
        self.name = name
        self.tel = tel
        self.company = company
        self.addr = addr
        
import sqlite3
conn = sqlite3.connect('addressbook_admin.db')
createtable()
choice = input("\n选择联系人功能1新增2查询3删除(直接回车退出程序)：")
while choice:
    if int(choice) == 1:
        list_user = []
        user = input("\n姓名 电话 公司 地址(直接回车退回菜单)：")
        while user:
            user = user.split()    
            list_user.append(User(user[0], user[1], user[2], user[3]))
            user = input("\n姓名 电话 公司 地址(直接回车退回菜单)：")
        insertuser(list_user)
    elif int(choice) == 2:
        name = input("\n输入您要查询的联系人姓名(直接回车退回菜单)：")
        while name:
            finduserbyname(name)
            name = input("\n输入您要查询的联系人姓名(直接回车退回菜单)：")
    elif int(choice) == 3:
        name = input("\n输入您要删除的联系人姓名(直接回车退回菜单)：")
        while name:
            deleteuser(name)
            name = input("\n输入您要删除的联系人姓名(直接回车退回菜单)：")   
    choice = input("\n选择联系人功能1新增2查询3删除(直接回车退出程序)：")    
conn.close()

'''
Run Module:
选择联系人功能1新增2查询3删除(直接回车退出程序)：1

姓名 电话 公司 地址(直接回车退回菜单)：zhangsan 13013001300 PWC Shanghai

姓名 电话 公司 地址(直接回车退回菜单)：lisi 15015001500 KPMG Beijing

姓名 电话 公司 地址(直接回车退回菜单)：
新增了2个联系人

选择联系人功能1新增2查询3删除(直接回车退出程序)：2

输入您要查询的联系人姓名(直接回车退回菜单)：lisi
lisi 15015001500 KPMG Beijing

输入您要查询的联系人姓名(直接回车退回菜单)：zhangsan
zhangsan 13013001300 PWC Shanghai

输入您要查询的联系人姓名(直接回车退回菜单)：wangwu
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：

选择联系人功能1新增2查询3删除(直接回车退出程序)：3

输入您要删除的联系人姓名(直接回车退回菜单)：zhangsan
zhangsan 13013001300 PWC Shanghai
成功删除zhangsan
查无此人

输入您要删除的联系人姓名(直接回车退回菜单)：wangwu
查无此人
删除失败

输入您要删除的联系人姓名(直接回车退回菜单)：

选择联系人功能1新增2查询3删除(直接回车退出程序)：1

姓名 电话 公司 地址(直接回车退回菜单)：wangwu 18018001800 DDT Guangzhou

姓名 电话 公司 地址(直接回车退回菜单)：zhaoliu 19019001900 EY Shenzhen

姓名 电话 公司 地址(直接回车退回菜单)：
新增了2个联系人

选择联系人功能1新增2查询3删除(直接回车退出程序)：2

输入您要查询的联系人姓名(直接回车退回菜单)：zhaoliu
zhaoliu 19019001900 EY Shenzhen

输入您要查询的联系人姓名(直接回车退回菜单)：wangwu
wangwu 18018001800 DDT Guangzhou

输入您要查询的联系人姓名(直接回车退回菜单)：zhangsan
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：

选择联系人功能1新增2查询3删除(直接回车退出程序)：3

输入您要删除的联系人姓名(直接回车退回菜单)：lisi
lisi 15015001500 KPMG Beijing
成功删除lisi
查无此人

输入您要删除的联系人姓名(直接回车退回菜单)：wangwu
wangwu 18018001800 DDT Guangzhou
成功删除wangwu
查无此人

输入您要删除的联系人姓名(直接回车退回菜单)：zhaoliu
zhaoliu 19019001900 EY Shenzhen
成功删除zhaoliu
查无此人

输入您要删除的联系人姓名(直接回车退回菜单)：

选择联系人功能1新增2查询3删除(直接回车退出程序)：2

输入您要查询的联系人姓名(直接回车退回菜单)：zhangsan
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：lisi
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：wangwu
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：zhaoliu
查无此人

输入您要查询的联系人姓名(直接回车退回菜单)：

选择联系人功能1新增2查询3删除(直接回车退出程序)：

'''


