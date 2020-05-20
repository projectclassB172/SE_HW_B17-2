import sqlite3
import os


def CreateDB():
    hcon = sqlite3.connect('I2FContract.db')
    hcur = hcon.cursor()
    stable = """
	create table contract
	(
		id int(10) primary key,
		name varchar(20) not null,
		telf char(11) not null,
		tels varchar(11),
		other varchar(50)
	)
	"""
    hcur.execute(stable)
    hcur.close()
    hcon.close()




def AddInfo(hcon, hcur):
    id = int(input('请输入id: '))
    name = str(input('请输入名字: '))
    telf = str(input('请输入电话: '))
    tels = str(input('请输入公司: '))
    other = str(input('请输入地址: '))
    sql = "insert into contract(id,name,telf,tels,other) values(?,?,?,?,?)"
    try:
        hcur.execute(sql, (id, name, telf, tels, other))
        hcon.commit()
    except:
        hcon.rollback()


def DeleteInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('请输入id: '))
    sql = "delete from contract where id=?"
    try:
        hcur.execute(sql, (did,))
        hcon.commit()
    except:
        hcon.rollback()


def UpdateInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('请输入id: '))

    sqlname = "update contract set name=? where id=?"
    name = str(input('请输入名字: '))
    try:
        hcur.execute(sqlname, (name, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqltelf = "update contract set telf=? where id=?"
    telf = str(input('请输入电话: '))
    try:
        hcur.execute(sqltelf, (telf, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqltels = "update contract set tels=? where id=?"
    tels = str(input('请输入公司: '))
    try:
        hcur.execute(sqltels, (tels, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqlothers = "update contract set other=? where id=?"
    other = str(input('请输入地址: '))
    try:
        hcur.execute(sqlothers, (other, did))
        hcon.commit()
    except:
        hcon.rollback()


def SelectInfo(hcon, hcur):
    hcur.execute("select * from contract")
    result = hcur.fetchall()
    print(result)


def Meau():
    print('1.查询显示')
    print('2.添加')
    print('3.更新')
    print('4.删除')
    print('5.cls')
    print('0.退出')
    sel = 9
    while (sel > 5 or sel < 0):
        sel = int(input('请选择: '))
    return sel


def main():
    if os.path.exists('I2FContract.db') == False:
        CreateDB()
    hcon = sqlite3.connect('I2FContract.db')
    hcur = hcon.cursor()
    while (True):
        sel = Meau()
        if (sel == 1):
            SelectInfo(hcon, hcur)
        elif (sel == 2):
            AddInfo(hcon, hcur)
        elif (sel == 3):
            UpdateInfo(hcon, hcur)
        elif (sel == 4):
            DeleteInfo(hcon, hcur)
        elif (sel == 5):
            os.system('cls')
        else:
            break
        print('设置成功！')
    hcur.close()
    hcon.close()


if __name__ == "__main__":
    main()


#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 2
#请输入id: 10
#请输入名字: 彭月煜
#请输入电话: 123456
#请输入公司: 建桥
#请输入地址: 上海
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 1
#[(10, '彭月煜', '123456', '建桥', '上海')]
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 3
#[(10, '彭月煜', '123456', '建桥', '上海')]
#请输入id: 10
#请输入名字: 彭月煜
#请输入电话: 12345678
#请输入公司: 上海建桥
#请输入地址: 上海
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 1
#[(10, '彭月煜', '12345678', '上海建桥', '上海')]
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 2
#请输入id: 20
#请输入名字: 皮皮
#请输入电话: 12345
#请输入公司: 建桥
#请输入地址: 上海
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 1
#[(10, '彭月煜', '12345678', '上海建桥', '上海'), (20, '皮皮', '12345', '建桥', '上海')]
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 4
#[(10, '彭月煜', '12345678', '上海建桥', '上海'), (20, '皮皮', '12345', '建桥', '上海')]
#请输入id: 20
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出
#请选择: 1
#[(10, '彭月煜', '12345678', '上海建桥', '上海')]
#设置成功！
#1.查询显示
#2.添加
#3.更新
#4.删除
#5.cls
#0.退出