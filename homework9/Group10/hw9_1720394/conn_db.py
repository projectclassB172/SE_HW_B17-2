import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE USER
(NAME TEXT NOT NULL,
TEL CHAR(13),
COMPANY CHAR(100),
ADDRESS CHAR(50));''')
print("Table USER created successfully");

conn.commit()