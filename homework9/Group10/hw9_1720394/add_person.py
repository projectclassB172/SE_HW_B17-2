import sqlite3

from hw9_1720394.person import Person

conn = sqlite3.connect("test.db")
list1 = []
name = input('请输入您的姓名：')
tel = input('请输入您的电话：')
company = input('请输入您的公司：')
address = input('请输入您的地址：')
per = Person(name,tel,company,address)
if per in list1:
    print('已存在该联系人！')
else:
    list1.append(per)

for per in list1:
    conn.execute("insert into USER (NAME,TEL,COMPANY,ADDRESS) values('%s', '%s', '%s', '%s')"
                 % (per.NAME, per.TEL,per.COMPANY,per.ADDRESS))
    print(f'添加成功')
conn.commit()