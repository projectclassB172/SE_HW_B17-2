#1720374黄德鑫

import sqlite3

class DB:
    
    def create_table(self):
        try:
            cr.execute('''CREATE TABLE t_adb
                (id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL ,
                company TEXT,
                address TEXT);''')
            conn.commit()
            print("t_adb 创建成功!\n")
        except sqlite3.OperationalError as reason:
            print("错误: t_adb 创建失败： " + str(reason) + "\n")


def addperson(hcon,c):

    id = int(input('请输入你的ID: '))
    name = str(input('请输入你的名字: '))
    number = str(input('请输入你的手机号: '))
    company = str(input('请输入你的公司: '))
    addr = str(input('请输入你的地址: '))
    sql="insert into person(id,name,number,company,addr) values(?,?,?,?,?)"
    c.execute(sql, (id,name,number,company,addr))
    hcon.commit()
    print("保持成功")
    hcon.rollback()



def delete(hcon,c):
	selectmail(hcon,c)
	did=int(input('请输入你要删除的id： '))
	sql="delete from person where id=?"
	c.execute(sql,(did,))
	hcon.commit()


def choice():
    print("添加联系人请输入:1")
    print("查询联系人请输入:2")
    print("删除联系人请输入:3")
    print("退出请按4")
    Button = 6
    while (Button>5 or Button<0 ):
        Button = int(input("请输入:"))
    return Button

def main():
    if os.path.exists('phonenumber.db') == False:
        conphonenumber()
    hcon = sqlite3.connect('phonenumber.db')
    c = hcon.cursor()
    while (True):
        Button = choice()
        if (Button == 1):
            addperson(hcon,c)
        elif(Button == 2):
            selectmail(hcon,c)
        elif(Button == 3):
            delete(hcon, c)
        else:
            break
        print("结束")


    c.close()
    hcon.close()

if __name__=="__main__":
	main()