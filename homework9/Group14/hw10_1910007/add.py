import sqlite3
conn=sqlite3.connect('C:\\Users\\Administrator\\Desktop\\项目实战\\hw10_1910007\\AddressList.db')
print("连接数据库成功")
conn.execute("INSERT INTO AddressList(ID,NAME,TEL,CO,ADDRESS,XIACHAO)\
VALUES(1,'XIA','10086','Oracle','The Fifth Street','myself')")

conn.commit()
num=conn.total_changes
print("{} rows changed in table AddressList.".format(num))


