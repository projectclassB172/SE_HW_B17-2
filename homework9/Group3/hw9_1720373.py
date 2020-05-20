'''通讯录'''
import sqlite3
import os

db_file = 'contact.db'
if os.path.exists(db_file) == False:
    con = sqlite3.connect(db_file)
    cursor  = con.cursor()
# 创建表
    sql = '''
    create table contact (
        id int primary key, 
        name varchar(32), 
        mobile char(11), 
        company varchar(128), 
        address varchar(128)
    )
    '''
    cursor.execute(sql)
    cursor.close()
    con.close()
    print("成功创建")
#数据库
con = sqlite3.connect("contact.db")
cursor = con.cursor()
#添加
print('请输入个人信息：')
id      = int(input('ID: '))
name    = str(input('姓名: '))
mobile  = str(input('电话: '))
company = str(input('公司: '))
address = str(input('地址: '))

sql="insert into contact(id, name, mobile, company, address) values(?,?,?,?,?)"
try:
    cursor.execute(sql, (id, name, mobile, company, address))
except Exception as e:
    con.rollback()
    print("ERROR!")
    sys.exit(0)
con.commit()
print("联系人已保存成功！")
#查找
con = sqlite3.connect("contact.db")
cursor = con.cursor()

name = str(input('请输入要查找的姓名: '))
sql = "select * from contact WHERE name = ?"
arr = cursor.execute(sql, (name,))

values = cursor.fetchall()
if len(values) == 0:
    print('not found')

for item in values:
    print(item)
    print('id: %s, name: %s, mobile: %s, company: %s, address: %s' % (
        item[0],
        item[1],
        item[2],
        item[3],
        item[4]
    ))

#删除
con = sqlite3.connect("contact.db")
cursor = con.cursor()
did=int(input('请输入你要删除的id： '))

sql="delete from contact where id=?"

cursor.execute(sql,(did,))
con.commit()
print('删除成功！')

