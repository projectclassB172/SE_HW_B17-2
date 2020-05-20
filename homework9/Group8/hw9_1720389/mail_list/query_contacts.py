import sqlite3
from mail_list.contacts import contacts

conn = sqlite3.connect("mail_list.db")
name = input("请输入联系人姓名：")
cur = conn.execute("select * from contact where NAME='"+name+"'")

r = cur.fetchall()
list_contact = []

for i in r:
    name = i[1]
    tel = i[2]
    gongsi = i[3]
    adr = i[4]
    contact = contacts(name, tel, gongsi, adr)
    list_contact.append(contact)
for contact in list_contact:
    print(contact.name,contact.tel,contact.gongsi,contact.adr)