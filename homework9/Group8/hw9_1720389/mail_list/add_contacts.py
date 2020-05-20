import sqlite3
from mail_list.contacts import contacts

conn = sqlite3.connect("mail_list.db")
list_contact = []
contact1 = contacts('zhangsan', '11111111111', 'aaa', 'aaaaaa')
list_contact.append(contact1)
contact1 = contacts('lisi', '22222222222', 'bbb', 'bbbbbb')
list_contact.append(contact1)
for contact1 in list_contact:
    conn.execute("insert into contact (NAME, tel, gongsi, adr) values('%s', '%s', '%s', '%s')" % (contact1.name, contact1.tel, contact1.gongsi, contact1.adr))
print('插入成功！')
conn.commit()