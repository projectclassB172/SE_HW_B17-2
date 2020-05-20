import sqlite3
conn=sqlite3.connect('D:\\1720377\\add.db')

def creat():
    conn.execute('''
    CREATE TABLE CONTACTS(
    ID INT PRIMARY KEY,
    NAME TEXT UNIQUE NOT NULL,
    TEL CHAR(11) NOT NULL,
    COMPANY CHAR(40) NOT NULL,
    ADDRESS CHAR(80) NOT NULL
    );''')
    conn.close()
def insert(id,name,tel,company="Google公司",address="硅谷"):
    conn = sqlite3.connect('D:\\1720377\\add.db')
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)"
                 "VALUES(1,'TONY','1720377','斯塔克工业','纽约')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS) values('%s', '%s','%s', '%s','%s')" % (id,name,tel,company,address))
    conn.commit()
    num = conn.total_changes
    print("{0} user表中更改的行数.".format(num))
    print("插入成功")
def select(name):
    conn = sqlite3.connect('D:\\1720377\\add.db')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT ID,NAME,TEL,COMPANY,ADDRESS "
                             "from CONTACTS "
                             "where NAME='"+name+"' ")
    row=cursor1.fetchone()
    if row is None:
        print("并没有{}".format(name))
    else:
        print("ID=", row[0])
        print("NAME=", row[1])
        print("TEL=", row[2])
        print("COMPANY=", row[3])
        print("ADDRESS=", row[4])
    cursor1.close()
    conn.close()
def delete(id):
    conn = sqlite3.connect('D:\\1720377\\add.db')
    conn.execute("delete from CONTACTS where ID="+id)
    conn.commit()
    num = conn.total_changes
    if num==0:
        print("通讯录中无id为{}的联系人".format(id))
    else:
        print("已更新行数 :{}".format(num))
        print("成功删除id="+id+"的联系人")
    conn.close()
def fun():
    print('-'*15,"通讯录",'-'*15)
    print("1.新增联系人")
    print("2.按姓名查询联系人信息")
    print("3.删除联系人")
    i=int(input("请根据功能输入对应的数字:"))
    return i
def main():
    while(True):
        i =fun()
        if(i==1):
            creat()
            print('-' * 15, "新增联系人", '-' * 15)
            id1=int(input("请输入id:"))
            name1=input("请输入新增联系人名字：")
            tel1 = input("请输入新增联系人电话：")
            insert(id=id1,name=name1,tel=tel1)
        elif(i==2):
            print('-' * 15, "按姓名查询联系人详细信息", '-' * 15)
            name=input("请输入你要查询的联系人名字:")
            select(name)
        elif(i==3):
            print('-' * 15, "删除联系人", '-' * 15)
            id=input("请输入删除联系人的id：")
            delete(id)
if __name__=='__main__':
    main()
