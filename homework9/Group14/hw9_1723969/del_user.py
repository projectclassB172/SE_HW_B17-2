import sqlite3
from hw9_1723969.user import User

conn = sqlite3.connect("address_list.db")

print('请输入要删除的姓名！')
name = input('姓名：')
conn.execute("delete from user where name='{}'".format(name))
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1 = conn.total_changes
print("{0} rows changed in table USER.".format(num1))

# 运行结果：C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/Administrator/PycharmProjects/untitled/hw9_1723969/del_user.py
# 请输入要删除的姓名！
# 姓名：mahuateng
# Total number of rows updated : 1
# 1 rows changed in table USER.

# sqlite> select * from user;
# |suting|13301822767|阿里巴巴网络技术有限公司|上海建桥学院
# |mayun|15082194027|阿里巴巴网络技术有限公司|浙江省杭州市




