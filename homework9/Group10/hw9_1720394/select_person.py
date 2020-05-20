import sqlite3

from hw9_1720394.person import Person
conn = sqlite3.connect("test.db")
per_name=input('请输入需要查询的名字：')
# 也可以使用cur = conn.execute("select * from USER where NAME = 'gaolin'")直接指定查询对象
cur = conn.execute("select * from USER where NAME = '%s'" %(per_name))
r = cur.fetchall()
per_ls = []
for i in r:
    # print (i)
    NAME = i[0]
    TEL = i[1]
    COMPANY = i[2]
    ADDRESS = i[3]
    person = Person(NAME,TEL,COMPANY,ADDRESS)
    per_ls.append(person)

for per in per_ls:
    print(per.NAME, per.TEL,per.COMPANY,per.ADDRESS)

#输出结果：
# 请输入需要查询的名字：gaolin
# gaolin 123-1324-1234 腾讯 深圳