
conn = sqlite3.connect('test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE USER
(NAME CHAR(10) NOT NULL,
ID NUMBER,
ADDRESS CHAR(13),
ADDRESS CHAR(50));''')
print("终于创建成功了");

conn.commit()
