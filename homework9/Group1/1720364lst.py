import sqlite3
conn = sqlite3.connect('addr.db')
print("Opened database successfully")
cursor = conn.cursor()
#创建数据库表
try:
    conn.execute('''CREATE TABLE USER
    (id INT PRIMARY KEY NOT NULL,
    name CHAR(20) NOT NULL,
    phone CHAR(11) NOT NULL,
    company CHAR(50) NOT NULL,
    address CHAR(50));''')
    print("Table USER created successfully")
except:
    print("数据表已存在\n")


# cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
# last_id = cursor.fetchone()
# print(last_id[0])
#新增联系人；
try:
    _name,_phone,_company,_address = input("请依次输入姓名，电话，公司，地址（使用空格隔开）").split()
except:
    print("输入有误,跳过插入\n")
else:
    try:
        cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
        last_id = cursor.fetchone()
        new_id = last_id[0]+1
        cursor.execute('''INSERT INTO user (id,name,phone,company,address) VALUES (?,?,?,?,?)''',(new_id,_name,_phone,_company,_address,))
        conn.commit()
        num1=conn.total_changes
        print("{0} rows changed in table addr.".format(num1))
    except:
        print("请勿插入重复数据\n")




#按姓名查询联系人详细信息
try:
    name = input("请输入要查询的人的姓名")
    cursor.execute("SELECT id,name,phone,company,address From user WHERE name=?;",(name,))
    user = cursor.fetchone()
    print("查询结果为:")
    print(user)
except:
    print("输入有误,跳过查询\n")



'''
删除联系人
'''
try:
    id1 = input("请输入要删除的id:")
    id1 = int(id1)
    conn.execute("delete from user where ID=?;",(id1,))
    conn.commit()
    print("删除成功")
except:
    print("删除失败")

#打印全部数据
cursor.execute("SELECT id,name,company,address From user")
users = cursor.fetchall()
print("打印全部数据：\n")
print(users)
cursor.close()
conn.close()









