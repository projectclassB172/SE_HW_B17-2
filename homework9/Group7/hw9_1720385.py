# -*-code:gbk-*-
'''
	build on sqlite3 database
'''
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
		tels char(11),
		other varchar(50)
	)
	"""
    hcur.execute(stable)
    hcur.close()
    hcon.close()


def AddInfo(hcon, hcur):
    id = int(input('please input ID: '))
    name = str(input('please input Name: '))
    telf = str(input('please input Tel 1: '))
    tels = str(input('please input Tel 2: '))
    other = str(input('please input other: '))
    sql = "insert into contract(id,name,telf,tels,other) values(?,?,?,?,?)"
    try:
        hcur.execute(sql, (id, name, telf, tels, other))
        hcon.commit()
    except:
        hcon.rollback()


def DeleteInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('please input id of delete: '))
    sql = "delete from contract where id=?"
    try:
        hcur.execute(sql, (did,))
        hcon.commit()
    except:
        hcon.rollback()


def UpdateInfo(hcon, hcur):
    SelectInfo(hcon, hcur)
    did = int(input('please input id of update: '))

    sqlname = "update contract set name=? where id=?"
    name = str(input('please input Name: '))
    try:
        hcur.execute(sqlname, (name, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqltelf = "update contract set telf=? where id=?"
    telf = str(input('please input Tel 1: '))
    try:
        hcur.execute(sqltelf, (telf, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqltels = "update contract set tels=? where id=?"
    tels = str(input('please input Tel 2: '))
    try:
        hcur.execute(sqltels, (tels, did))
        hcon.commit()
    except:
        hcon.rollback()

    sqlothers = "update contract set other=? where id=?"
    other = str(input('please input other: '))
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
    print('1.diaplay')
    print('2.add')
    print('3.update')
    print('4.delete')
    print('5.cls')
    print('0.exit')
    sel = 9
    while (sel > 5 or sel < 0):
        sel = int(input('please choice: '))
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
        print('-------------------------')
    hcur.close()
    hcon.close()


if __name__ == "__main__":
    main()