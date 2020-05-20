import sqlite3
class Person:
    def __init__(self,name,phone,company,addr):
        self.name=name
        self.phone=phone
        self.company=company
        self.addr=addr
def createdb():
    conn=sqlite3.connect('D:\\1910100.db')
    conn.execute("create table person(NAME text not null,PHONE text,COMPANY text,addr text);")
    conn.commit()
    conn.close()

def add_person():
    conn=sqlite3.connect('D:\\1910100.db')
    list_person=[]
    person1=Person('zhangsan','13912345678','micosoft','shanghai')
    list_person.append(person1)
    person2=Person('lisi','13812345678','google','zhejiang')
    list_person.append(person2)
    person3=Person('wangwu','1331273655','baidui','chongqing')
    list_person.append(person3)
    for newperson in list_person:
        conn.execute("insert into person(name,phone,company,addr) values('%s','%s','%s','%s');" %(newperson.name,newperson.phone,newperson.company,newperson.addr))
    conn.commit()
    conn.close()

def query():
    conn=sqlite3.connect('D:\\1910100.db')
    name=input("请输入想要查询的姓名：")
    cur=conn.execute("select name,phone,company,addr from person where name='"+name+"'")
    #r=cur.fetchall()
    #li_person=[]
    for i in cur:
        print(i)
        name=i[0]
        phone=i[1]
        company=i[2]
        addr=i[3]
        person2=Person(name,phone,company,addr)
        print('查到了！')
    conn.close()
def delperson():
    conn=sqlite3.connect('D:\\1910100.db')
    name=input("请输入你要删除的联系人：")
    cur=conn.execute("delete from person where name='"+name+"'")
    print("删除成功！")
    conn.commit()
    conn.close()
createdb()
add_person()
query()
delperson()
print("再次查询zhangsan")
query()
print("已经查询不到了")

#————————————————运行结果——————————————————
#请输入想要查询的姓名：zhangsan
#('zhangsan', '13912345678', 'micosoft', 'shanghai')
#查到了！
#请输入你要删除的联系人：zhangsan
#删除成功！
#再次查询zhangsan
#请输入想要查询的姓名：zhangsan
#已经查询不到了
