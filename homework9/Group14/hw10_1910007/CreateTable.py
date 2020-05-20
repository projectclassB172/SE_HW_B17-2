import sqlite3
conn=sqlite3.connect('C:\\Users\\Administrator\\Desktop\\项目实战\\hw10_1910007\\AddressList.db')
print('打开数据库成功');
conn.execute("""CREATE TABLE AddressList
	(ID      INT        PRIMARY KEY NOT NULL,
	 NAME    TEXT       NOT NULL,
	 TEL     CHAR(20)   NOT NULL,
	 CO      TEXT       NOT NULL,
	 ADDRESS TEXT       NOT NULL,
	 XIACHAO TEXT
	 );""")
print("AddressList表成功建立");
conn.close()