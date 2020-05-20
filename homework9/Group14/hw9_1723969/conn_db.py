import sqlite3
conn = sqlite3.connect('address_list.db')
conn.execute("create table user( ID varchar(10) primary key, name text not null, tel text ,company text ,address test)")
conn.commit()
