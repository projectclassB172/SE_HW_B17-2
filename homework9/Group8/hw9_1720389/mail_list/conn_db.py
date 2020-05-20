import sqlite3
conn = sqlite3.connect('mail_list.db')
conn.execute('''CREATE TABLE contact (ID varchar(10) primary key, NAME TEXT NOT NULL, tel TEXT NOT NULL, gongsi TEXT NOT NULL,adr TEXT NOT NULL);''')
print("Table USER created successfully")
conn.commit()

