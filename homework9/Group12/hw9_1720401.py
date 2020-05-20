import sqlite3
import os
def conphonenumber():
    hcon = sqlite3.connect("phonenumber.db")
    sql = '''create table person (id int primary key, name varchar(20), number char(11), company char(20), addr char(20))'''
    c.execute(sql)
    c.close()
    hcon.close()
    print("成功创建")

def addperson(hcon,c):
    id = int(input('请输入你的ID: '))
    name = str(input('请输入你的名字: '))
    number = str(input('请输入你的手机号: '))
    company = str(input('请输入你的公司: '))
    addr = str(input('请输入你的地址: '))
    sql="insert into person(id,name,number,company,addr) values(?,?,?,?,?)"
    c.execute(sql, (id,name,number,company,addr))
    hcon.commit()
    print("保持成功")
    hcon.rollback()


def selectmail(hcon,c):
    c.execute('select * from person where name like "严%"')
    print(c.fetchall())

def delete(hcon,c):
	selectmail(hcon,c)
	did=int(input('请输入你要删除的id： '))
	sql="delete from person where id=?"
	c.execute(sql,(did,))
	hcon.commit()


def choice():
    print("欢迎使用通讯录")
    print("添加联系人请输入:1")
    print("查询联系人请输入:2")
    print("删除联系人请输入:3")
    print("退出请按5")
    Button = 9
    while (Button>5 or Button<0 ):
        Button = int(input("请输入:"))
    return Button

def main():
    if os.path.exists('phonenumber.db') == False:
        conphonenumber()
    hcon = sqlite3.connect('phonenumber.db')
    c = hcon.cursor()
    while (True):
        Button = choice()
        if (Button == 1):
            addperson(hcon,c)
        elif(Button == 2):
            selectmail(hcon,c)
        elif(Button == 3):
            delete(hcon, c)
        else:
            break
        print("结束")


    c.close()
    hcon.close()

if __name__=="__main__":
	main()

