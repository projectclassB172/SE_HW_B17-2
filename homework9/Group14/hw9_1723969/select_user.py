import sqlite3
from hw9_1723969.user import User

conn = sqlite3.connect("address_list.db")
print('输入联系人的姓名！')
name = input('姓名：')
cur = conn.execute("select * from user where name='{}'".format(name))
r = cur.fetchall()
user_ls = []
for i in r:
    name = i[1]
    tel = i[2]
    company = i[3]
    address = i[4]
    user = User(name, tel, company, address)
    user_ls.append(user)
if user_ls:
    for user in user_ls:
        print(user.name, user.tel, user.company, user.address)
else:
    print('没有找到该联系人！')

# 运行结果：
# C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/Administrator/PycharmProjects/untitled/hw9_1723969/select_user.py
# 输入联系人的姓名！
# 姓名：mayun
# mayun 15082194027 阿里巴巴网络技术有限公司 浙江省杭州市
# Process finished with exit code 0

# C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/Administrator/PycharmProjects/untitled/hw9_1723969/select_user.py
# 输入联系人的姓名！
# 姓名：liuqiangdong
# 没有找到该联系人！
# Process finished with exit code 0


