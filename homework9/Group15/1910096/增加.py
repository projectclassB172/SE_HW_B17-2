conn = sqlite3.connect("test.db")
list1 = []
name = input('请输入您的姓名：')
ids = input('请输入您的id：')
tel = input('请输入您的电话号码：')
address = input('请输入您的地址：')
per = Person(name,ids,tel,address)
if per in list1:
    print('此用户已存在！')
else:
    list1.append(per)

for per in list1:
    conn.execute("insert into USER (NAME,ID,TEL,ADDRESS) values('%s', '%s', '%s', '%s')"
                 % (per.NAME, per.ID,per.TEL,per.ADDRESS))
    print(f'注册成功')
