import sqlite3
from mail_list.contacts import contacts

conn = sqlite3.connect("mail_list.db")
name = input("请输入联系人姓名：")
cur = conn.execute("delete from contact where NAME = '"+name+"'")
conn.commit()
print('删除成功！')