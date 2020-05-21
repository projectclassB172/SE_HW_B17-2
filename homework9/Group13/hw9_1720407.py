# 1.编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# 2.采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# 设计相应的函数完成以下数据库操作：
# 1.创建数据库表；
# 2.新增联系人；
# 3.按姓名查询联系人详细信息；
# 4.删除联系人；
import sqlite3
conn=sqlite3.connect('D:\\temp\\zy\\addressList.db')
# print("created database addressList.db successfully")

def t_creat():
    conn.execute('''
    CREATE TABLE CONTACTS(
    ID INT PRIMARY KEY,
    NAME TEXT UNIQUE NOT NULL,
    TEL CHAR(11) NOT NULL,
    COMPANY CHAR(50) NOT NULL,
    ADDRESS CHAR(100) NOT NULL
    );''')
    print("Table CONTACTS created successfully!")
    conn.close()
def t_insert(id,name,tel,company="微软上海分公司",address="上海市静安区"):
    conn = sqlite3.connect('D:\\temp\\zy\\addressList.db')
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)"
                 "VALUES(1,'张雅','1478522','阿里巴巴上海分公司','上海市静安区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)"
                 "VALUES(2,'bz','1452366','阿里巴巴上海分公司','上海市静安区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)\
                   VALUES(3,'严格格','14785363','腾讯上海分公司','上海市宝山区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)\
                   VALUES(4,'肖肖羽','14239955','百度上海分公司','上海市宝山区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)\
                   VALUES(5,'婷婷苏','14852366',' 美团上海分公司','上海市静安区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS)\
                   VALUES(6,'丹丹李','14782366','滴滴上海分公司','上海市浦东新区')")
    conn.execute("INSERT INTO CONTACTS(ID,NAME,TEL,COMPANY,ADDRESS) values('%s', '%s','%s', '%s','%s')" % (id,name,tel,company,address))
    conn.commit()
    num = conn.total_changes
    print("{0} rows changed in table CONTACTS.".format(num))
    print("Insert operation successfully")
def t_select(name):
    conn = sqlite3.connect('D:\\temp\\zy\\addressList.db')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT ID,NAME,TEL,COMPANY,ADDRESS "
                             "from CONTACTS "
                             "where NAME='"+name+"' ")
    row=cursor1.fetchone()
    if row is None:
        print("对不起,没有{}联系人".format(name))
    else:
        print("ID=", row[0])
        print("NAME=", row[1])
        print("TEL=", row[2])
        print("COMPANY=", row[3])
        print("ADDRESS=", row[4])
    cursor1.close()
    conn.close()
def t_delete(id):
    conn = sqlite3.connect('D:\\temp\\zy\\addressList.db')
    conn.execute("delete from CONTACTS where ID="+id)
    conn.commit()
    # USER表中更新的行数
    num = conn.total_changes
    if num==0:
        print("通讯录中无id为{}的联系人".format(id))
    else:
        print("Total number of rows updated :{}".format(num))
        print("成功删除id="+id+"的联系人")
    conn.close()
def main():
    print('-'*25,"通讯录",'-'*25)
    i=1
    for i in range(1, 5):
        if i == 1:
            print('-' * 22, "创建数据库表", '-' * 22)
            t_creat()
        elif i == 2:
            print('-' * 23, "新增联系人", '-' * 23)
            id1=int(input("请输入6以上的整数id:"))
            name1=input("请输入您要插入的联系人名字：")
            tel1 = input("请输入您要插入的联系人电话：")
            t_insert(id=id1,name=name1,tel=tel1)
        elif i == 3:
            print('-' * 17, "按姓名查询联系人详细信息", '-' * 17)
            name=input("请输入你要查询的联系人名字:")
            t_select(name)
        elif i==4:
            print('-' * 23, "删除联系人", '-' * 23)
            id=input("请输入您要删除联系人的id：")
            t_delete(id)
if __name__=='__main__':
    main()

#运行结果
# ------------------------- 通讯录 -------------------------
# ---------------------- 创建数据库表 ----------------------
# Table CONTACTS created successfully!
# ----------------------- 新增联系人 -----------------------
# 请输入6以上的整数id:7
# 请输入您要插入的联系人名字：如意
# 请输入您要插入的联系人电话：147852369
# 7 rows changed in table USER.
# Insert operation successfully
# ----------------- 按姓名查询联系人详细信息 -----------------
# 请输入你要查询的联系人名字:如意
# ID= 7
# NAME= 如意
# TEL= 147852369
# COMPANY= 微软上海分公司
# ADDRESS= 上海市静安区
# ----------------------- 删除联系人 -----------------------
# 请输入您要删除联系人的id：7
# Total number of rows updated :1
# 成功删除id=7的联系人
