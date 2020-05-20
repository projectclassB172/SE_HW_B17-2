import sqlite3
conn = sqlite3.connect('addr.db')
print("Opened database successfully")
cursor = conn.cursor()
#创建数据库表
    try:
        sql='''create table USER (id int primary key, name varchar(20), number char(11), company char(20), addr char(20))'''
        con.execute(sql)
        print("USER 创建成功!\n")
    except sqlite3.OperationalError as reason:
        print("错误: 创建失败： " + str(reason) + "\n")

# cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
# last_id = cursor.fetchone()
# print(last_id[0])

try:
    _name,_phone,_company,_addr = input("请依次输入姓名，电话，公司，地址（使用空格隔开）").split()
except:
    print("错误,跳过插入\n")
else:
    try:
        cursor.execute("Select * From user limit ((select count(id) from user)-1),1")
        last_id = cursor.fetchone()
        new_id = last_id[0]+1
        cursor.execute('''INSERT INTO user (id,name,number,company,addr) VALUES (?,?,?,?,?)''',(new_id,_name,_number,_company,_addr,))
        conn.commit()
        num1=conn.total_changes
        print("{0} rows changed in table addr.".format(num1))
    except:
        print("请勿插入重复数据\n")

def select (con,cur):
      try:
        name = input("请输入要查询的人的姓名:")
        cur.execute("SELECT * From user WHERE  name='{}'".format(name))
        print("查询结果为:{}".fomat.cur.fetchall())
    except:
        print("输入有误,跳过查询\n")

 def delete(self, name):
        try:
            self.c.execute("DELETE FROM list WHERE name='%s'" % (name))
            self.conn.commit()
            print("删除成功！")
        except:
            print("请先创建数据库表!")


cursor.execute("SELECT id,name,company,address From user")
users = cursor.fetchall()
print("打印全部数据：\n")
print(users)
cursor.close()
conn.close()

if __name__ == "__main__":
    connect = ConnDB()
    connect.close()
