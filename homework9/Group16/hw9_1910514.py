import sqlite3
conn=sqlite3.connect('D:\\software\\zwy\\test.db')

class Linkman:
    def __init__(self,name,tel,company,address):
        self.name=name
        self.tel=tel
        self.company=company
        self.address=address
def conn_db():
    conn=sqlite3.connect('D:\\software\\zwy\\test.db')
    conn.execute("create table linkman( ID varchar(10) primary key, name text not null,tel text ,company text ,address text)")
    conn.commit()
    conn.close()

def add_linkman():
    conn=sqlite3.connect('D:\\software\\zwy\\test.db')
    list_man = []
    man1 = Linkman('zhangwenya',18888888888,'家里蹲公司','上海建桥学院')
    list_man.append(man1)
    man1 = Linkman('zhangsan',18822222222,'家里蹲公司','上海建桥学院')
    list_man.append(man1)
    man1 = Linkman('zhangsi',18888887777,'家里蹲公司','上海建桥学院')
    list_man.append(man1)
    print('请输入新的联系人信息:')
    name = input('姓名:')
    tel = input('电话:')
    company = input('公司:')
    address = input('地址:')
    man1 = Linkman(name,tel,company,address)
    if man1 in list_man:
        print('已有该联系人！')
    else:
        list_man.append(man1)
        for man1 in list_man:
            conn.execute("insert into linkman (name,tel,company,address) values('%s', '%s', '%s', '%s')" % (new_man.name, new_man.tel, new_man.company, new_man.address))
    conn.commit()
    conn.close()

def query_linkman():
    conn=sqlite3.connect('D:\\software\\zwy\\test.db')
    print('请输入需要查询的联系人的姓名:')
    name = input('姓名:')
    cur = conn.execute("select * from student")
    r = cur.fetchall()
    linkman_ls = []
    for i in r:
        name = i[1]
        tel = i[2]
        company = i[3]
        address = i[4]
        linkman = Linkman(name, tel, company, address)
        linkman_ls.append(linkman)
    if linkman_ls:
        for man in linkman_ls:
            print(man.name,man.tel,man.company,man.address)
    else:
        print('没有找到该联系人！')
    conn.close()

def del_linkman():
    conn=sqlite3.connect('D:\\software\\zwy\\test.db')
    print('请输入需要删除的姓名:')
    name = input('姓名:')
    cur=conn.execute("delete from person where name='"+name+"'")
    man_num=conn.total_changes
    if man_num!=0:
        print("删除成功！")
    else:
        print("联系人不存在！")
    conn.commit()
    conn.close()


#运行结果:
#请输入新的联系人信息:
#姓名:zhangdaniu
#电话:18822221111
#公司:家里蹲公司
#地址:纽约市
#请输入需要查询的联系人的姓名:
#姓名:zhangwenya
#zhangwenya,18888888888,家里蹲公司,上海建桥学院
#请输入需要删除的联系人：
#姓名:zhangdaniu
#删除成功！
