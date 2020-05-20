conn = sqlite3.connect("test.db")
per_name=input('请输入需要查询的名字：')

cur = conn.execute("select * from USER where NAME = '%s'" %(per_name))
r = cur.fetchall()
per_ls = []
for i in r:
    # print (i)
    NAME = i[0]
    ID = i[1]
    TEL = i[2]
    ADDRESS = i[3]
    person = Person(NAME,ID,TEL,ADDRESS)
    per_ls.append(person)

for per in per_ls:

    print(per.NAME, per.ID,per.TEL,per.ADDRESS)
'''
查都不会，删库跑路
'''
