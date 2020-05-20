import sqlite3
#建一个数据库
def create_sql():
    sql = sqlite3.connect("user_data.db")#数据库命名
    sql.execute("""create table if not exists
        %s(
        %s integer primary key autoincrement,
        %s varchar(30),
        %s varchar(30),
        %s varchar(30),
        %s vachar(30))"""
                % ('user',
                   'id',#id
                   'name',#姓名
                   'number',#电话
                   'firm',#公司
                   'site'#地址
                   ))
    sql.close()#关闭数据库
create_sql()
import sqlite3
#数据库增加数据
def add_data():
    name = input("请输入您的姓名：")
    number = input("请输入您的电话：")
    firm = input('请输入您的公司：')
    site = input('请输入您的地址：')
    sql = sqlite3.connect("user_data.db")
    sql.execute("insert into user(name,number,firm,site) values(?,?,?,?)",
                (name, number, firm, site))
    sql.commit()
    print("添加成功")
    sql.close()
#这里插入了读取到的四个参数name,number，firm,site
def showalldata():
    select_name = input("请输入您的姓名：")
    sql = sqlite3.connect("user_data.db")
    data = sql.execute("select * from user where name = '%s'" %(select_name))
    sql.commit()
    print(data)
    sql.close()
#根据列name查询数据
def drop():
    print('根据id删除')
    sql = sqlite3.connect("user_data.db")
    data = sql.execute("select * from user").fetchall()
    print('所有联系人:' + str(data))
    while 1:
        id = input('请输入你要删除联系人的id:')
        sql.execute("DELETE FROM user WHERE id = %s" % id)
        sql.commit()
        print('删除完成')
        data = sql.execute("select * from user")
        print(data.fetchall())
        sql.close()
        break
#根据id删除数据

print("""
1:新增联系人
2:查询联系人信息
3.删除联系人信息
0:退出
""")
while 1:
    option = None
    cho = input('选择您想要的进行的操作:')
    if cho == '1':
        add_data()
    elif cho == '2':
        data = showalldata()
    elif cho == '3':
        drop()
    elif cho == '0':
        break
    else:
        "输入错误"