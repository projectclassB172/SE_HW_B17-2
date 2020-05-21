import sqlite3
conn=sqlite3.connect('D:\\1720377\\add.db')
def creat():
    try:
        conn.execute('''
        CREATE TABLE CONTACTS(
        ID INT PRIMARY KEY,
        NAME TEXT NOT NULL,
        TEL CHAR(11) NOT NULL,
        COMPANY CHAR(40) NOT NULL,
        ADDRESS CHAR(80) NOT NULL
        );''')
        print("成功创建CONTACTS数据表\n")
    except:
        print("CONTACTS数据表已存在\n")
    conn.close()
def f():
    if not hasattr(f,'x'):
        f.x=1
    else:
        f.x+=1
    return f.x
def insert(name,tel,company="Google公司",address="硅谷"):
    conn = sqlite3.connect('D:\\1720377\\add.db')
    id=int(f())
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS) values('%s', '%s','%s', '%s','%s')" % (id, name, tel, company, address))
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
def delete(name):
    conn = sqlite3.connect('D:\\1720377\\add.db')
    conn.execute("delete from CONTACTS where NAME='"+name+"'")
    conn.commit()
    num = conn.total_changes
    if num==0:
        print("通讯录中无名字为{}的联系人".format(name))
    else:
        print("已更新行数 :{}".format(num))
        print("成功删除名字为"+name+"的联系人")
    conn.close()
def fun():
    print('-'*15,"通讯录",'-'*15)
    print("1.新增联系人")
    print("2.按姓名查询联系人信息")
    print("3.删除联系人")
    i=int(input("请根据功能输入对应的数字:"))
    return i
def main():
    a = 0
    b = 0
    c = 0
    while(True):
        i =fun()
        if(i==1):
            a=1
            creat()
            print('-' * 15, "新增联系人", '-' * 15)
            name1=input("请输入新增联系人名字：")
            tel1 = input("请输入新增联系人电话：")
            insert(name=name1,tel=tel1)
        elif(i==2):
            b = 2
            print('-' * 15, "按姓名查询联系人详细信息", '-' * 15)
            name=input("请输入你要查询的联系人名字:")
            select(name)
        elif(i==3):
            c = 3
            print('-' * 15, "删除联系人", '-' * 15)
            name=input("请输入删除联系人的名字：")
            delete(name)
        if a==1 and b==2 and c==3:
            print("通讯录功能已完成")
            break
if __name__=='__main__':
    main()

#运行结果：
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:1
# 成功创建CONTACTS数据表
#
# --------------- 新增联系人 ---------------
# 请输入新增联系人名字：hjy
# 请输入新增联系人电话：147
# 1 user表中更改的行数.
# 插入成功
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:2
# --------------- 按姓名查询联系人详细信息 ---------------
# 请输入你要查询的联系人名字:hjy
# ID= 1
# NAME= hjy
# TEL= 147
# COMPANY= Google公司
# ADDRESS= 硅谷
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:1
# CONTACTS数据表已存在
#
# --------------- 新增联系人 ---------------
# 请输入新增联系人名字：zy
# 请输入新增联系人电话：789
# 1 user表中更改的行数.
# 插入成功
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:2
# --------------- 按姓名查询联系人详细信息 ---------------
# 请输入你要查询的联系人名字:zy
# ID= 2
# NAME= zy
# TEL= 789
# COMPANY= Google公司
# ADDRESS= 硅谷
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:1
# CONTACTS数据表已存在
#
# --------------- 新增联系人 ---------------
# 请输入新增联系人名字：yu
# 请输入新增联系人电话：753
# 1 user表中更改的行数.
# 插入成功
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:2
# --------------- 按姓名查询联系人详细信息 ---------------
# 请输入你要查询的联系人名字:yu
# ID= 3
# NAME= yu
# TEL= 753
# COMPANY= Google公司
# ADDRESS= 硅谷
# --------------- 通讯录 ---------------
# 1.新增联系人
# 2.按姓名查询联系人信息
# 3.删除联系人
# 请根据功能输入对应的数字:3
# --------------- 删除联系人 ---------------
# 请输入删除联系人的名字：3
# 通讯录中无名字为3的联系人
# 通讯录功能已完成

