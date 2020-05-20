import sqlite3

from hw9_1723969.user import User

conn = sqlite3.connect("address_list.db")
list_user = []
user1 = User('suting', 13301822767, '阿里巴巴网络技术有限公司','上海建桥学院')
list_user.append(user1)
user1 = User('mahuateng', 15182309567, '腾讯科技有限公司', '深圳市南山区')
list_user.append(user1)
print('请输入要添加的联系人信息！')
name = input('姓名：')
tel = input('电话：')
company = input('公司：')
address = input('地址：')
user1 = User(name,tel,company,address)
if user1 in list_user:
    print('已有该联系人！')
else:
    list_user.append(user1)
    for user1 in list_user:
        conn.execute("insert into user (name,tel,company,address) values('%s', '%s', '%s', '%s')" %
        (user1.name, user1.tel, user1.company, user1.address))
conn.commit()

# 运行结果：C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/Administrator/PycharmProjects/untitled/hw9_1723969/add_user.py
# 请输入要添加的联系人信息！
# 姓名：mayun
# 电话：15082194027
# 公司：阿里巴巴网络技术有限公司
# 地址：浙江省杭州市
# Process finished with exit code 0

# C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/Administrator/PycharmProjects/untitled/hw9_1723969/add_user.py
# 请输入要添加的联系人信息！
# 姓名：mayun
# 电话：15082194027
# 公司：阿里巴巴网络技术有限公司
# 地址：浙江省杭州市
# 已有该联系人！
# Process finished with exit code 0

# sqlite> select * from user;
# |suting|13301822767|阿里巴巴网络技术有限公司|上海建桥学院
# |mahuateng|15182309567|腾讯科技有限公司|深圳市南山区
# |mayun|15082194027|阿里巴巴网络技术有限公司|浙江省杭州市