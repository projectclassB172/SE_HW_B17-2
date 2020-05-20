import sqlite3

from hw9_1720394.person import Person

conn = sqlite3.connect("test.db")
per_name=input('请输入需要删除的联系人姓名：')
#或者可以使用conn.execute("delete from USER where NAME='gaolin'")来删除对象
conn.execute("delete from USER where NAME = '%s'" %(per_name))
conn.commit()
print("Total number of rows updated :", conn.total_changes)
num1=conn.total_changes
print(f"{num1} rows changed in table USER.")
#输出结果：
# 请输入需要删除的联系人姓名：gaolin
# Total number of rows updated : 1
# 1 rows changed in table USER.