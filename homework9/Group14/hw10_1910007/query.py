import sqlite3
conn=sqlite3.connect('C:\\Users\\Administrator\\Desktop\\项目实战\\hw10_1910007\\AddressList.db')
print("连接数据库成功")
cursor=conn.execute("SELECT ID,NAME,TEL,CO,ADDRESS from AddressList where NAME='XIA'")
for row in cursor:
	print("ID=",row[0])
	print("NAME=",row[1])
	print("TEL=",row[2])
	print("CO=",row[3])
	print("ADDRESS=",row[4])
cursor.close()
conn.close()