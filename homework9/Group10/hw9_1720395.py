import sqlite3


def CreateDB():
    ccon = sqlite3.connect('D:\\staff.db')
    print("打开数据库成功")
    stable = """
   create table contract
   (
      CREATE TABLE USER 
    (PHONENUMBER INT PRIMARY KEY NOT NULL, 
    NAME  TEXT NOT NULL ,
    ADDRESS  TEXT ,
    COMPANY CHAR(50))
   )
   """
    ccon.close()


def inputInfo(conn):
    conn = sqlite3.connect('D:\\staff.db')
    print("请依次输入新增联系人的id、姓名、电话、公司、地址：")
    id = int(input('请输入id: '))
    name= str(input("姓名："))
    Telephone = str(input('请输入电话: '))
    company = str(input('请输入公司: '))
    add = str(input('请输入地址: '))
    conn.execute("INSERT INTO  PHONEList VALUES(?,?,?,?,?)",(id,name,Telephone,company,add))
    conn.commit()
    print("新增联系人成功！！！")

def SelectInfo(ccon):
    conn=sqlite3.connect('D:\\staff.db')
    name=input("请输入想要查询的id：")
    cur=conn.execute("id,name,Telephone,company,add from person where id='"+id+"'")
    for i in cur:
        print(i)
        id = i[0]
        name=i[1]
        Telephone=i[2]
        company=i[3]
        add=i[4]
        person2=Person(id,name,Telephone,company,add)
        print('查到了')
    conn.close()


def SelectInfo(ccon)
    conn = sqlite3.connect('D:\\staff.db')
    did = int(input("请输入要删除的id:"))
    sql = "delete from contract where id=?"
    try:
        conn.execute("delete from user where ID=?;", (id1,))
        conn.commit()
        print("删除成功")
    except:
        print("删除失败")


def Meau():
    print("欢迎使用数据库")
    print('1.查询')
    print('2.添加')
    print('3.更新')
    print('0.退出')
    sel = 9
    while (sel > 3 or sel < 0):
        sel = int(input('请选择: '))
    return sel


def main():
    if os.path.exists('D:\\staff.db') == False:
        CreateDB()
    ccon = sqlite3.connect('D:\\staff.db')
    while (True):
        sel = Meau()
        if (sel == 1):
            SelectInfo(ccon, ccur)
        elif (sel == 2):
            AddInfo(ccon, ccur)
        elif (sel == 3):
            UpdateInfo(ccon, ccur)
        else:
            break
        print('设置成功！')
    ccon.close()


if __name__ == "__main__":
    main()

