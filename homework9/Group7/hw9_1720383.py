import sqlite3
conn=sqlite3.connect('D:\\Users\\1720383\\\Phone.db')
print("打开数据库成功")
    conn.execute('''CREATE TABLE USER
    (id int primary key not null, 
    name CHAR(20) not null,
    phone CHAR(11) not null,
    company CHAR(50) not null,
    address CHAR(50));''')
    print("Table USER created successfully")
except:
    print("数据表建立成功\n")

def inputInfo(conn):
    print("请依次输入新增联系人的姓名、电话、公司、地址：")
    name= str(input("姓名："))
    tel = str(input("电话："))
    company = str(input("公司："))
    address = str(input("地址："))
    conn.execute("insert into phonelist valuesI(?,?,?,?)",(name, tel , company, address))
    conn.commit()
    print("新增联系人完成！")

try:
    name = input("请输入查询人姓名")
    cursor.execute("select id,name,phone,company,address From user WHERE name=?;",(name,))
    user = cursor.fetchone()
    print("查询结果:")
    print(user)
except:
    print("输入有误,跳过查询\n")

#删除联系人
def delperson():
    conn=sqlite3.connect('D:\\Users\\1720383\\\Phone.db')
    name=input("请输入你要删除的联系人：")
    cur=conn.execute("delete from person where name='"+name+"'")
    print("删除成功！")
    conn.commit()
    conn.close()

#打印全部数据
cursor.execute("SELECT id,name,company,address From user")
users = cursor.fetchall()
print("打印全部数据：\n")
print(users)
cursor.close()
conn.close()

if __name__ == "__main__":
    # 连接数据库(如果不存在则创建)
    conn = sqlite3.connect('address_book.db')
    print("数据库连接成功！")
    # 创建游标
    cr = conn.cursor()
    db=DB()#创建对象
    db.main()#调用main方法
    # 关闭数据库操作
    cr.close()
    print("数据库连接已关闭！")






