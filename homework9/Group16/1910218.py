import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

c = conn.cursor()
c.execute('''CREATE TABLE LIST
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE           INT     NOT NULL,
       ADDRESS        CHAR(50));''')
print("Table created successfully")

c.execute("INSERT INTO LIST (ID,NAME,PHONE,ADDRESS) \
      VALUES (1, '张三', 137137137137, 'SHANGHAI')")

c.execute("INSERT INTO LIST (ID,NAME,PHONE,ADDRESS) \
      VALUES (2, '李四', 12345678910, 'BEIJING')")

c.execute("INSERT INTO LIST (ID,NAME,PHONE,ADDRESS) \
      VALUES (3, '王五', 10987654321, 'SHENGZHENG')")

cursor = c.execute("SELECT ID,NAME,PHONE,ADDRESS  from LIST")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("PHONE = ", row[2])
   print ("ADDRESS = ", row[3], "\n")

c.execute("DELETE from LIST where ID=2;")

cursor = c.execute("SELECT ID,NAME,PHONE,ADDRESS  from LIST")
print("-------------删除后------------")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("PHONE = ", row[2])
   print ("ADDRESS = ", row[3], "\n")
conn.commit()
conn.close()