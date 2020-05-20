import sqlite3
conn=sqlite3.connect('C:\\Users\\Administrator\\Desktop\\项目实战\\hw10_1910007\\AddressList.db')
print("连接数据库成功")
conn.execute("delete from AddressList where ID=1")
conn.commit()
num=conn.total_changes
print("有 {} 行数据被删除。".format(num)+'\n'+"{0} row changed in table AddressList.".format(num))
#print("{} row changed in table AddressList.".format(conn.total_changes))
conn.commit()
print("删除成功")
conn.close()
