# 设计相应函数
import sqlite3

conn = sqlite3.connect('D:\\Program Files (x86)\\Python\\Project\\db\\hw9_1720397.db')
print("Open database successfully")


# 1、创建数据库表
def createTable():
    conn.execute('''CREATE TABLE SatanUSER
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    PHONE INT NOT NULL,
    COMPANY TEXT NOT NULL,
    ADDRESS TEXT NOT NULL);''')
    conn.commit()
    print("Create SatanUSER successfully")


# 2、新增联系人
def insertUser():
    conn.execute("INSERT INTO SatanUSER(ID, NAME, PHONE, COMPANY, ADDRESS) \
             VALUES(001, 'Satan', 18317053363, '致一公司', '中国');")
    conn.execute("INSERT INTO SatanUSER(ID, NAME, PHONE, COMPANY, ADDRESS) \
             VALUES(002, '迪迦奥特曼', 18317053363, '致一公司', '法国');")
    conn.execute("INSERT INTO SatanUSER(ID, NAME, PHONE, COMPANY, ADDRESS) \
             VALUES(003, 'Satan', 12345678901, '可爱多公司', '澳大利亚');")
    conn.commit()


def insertUser1(ID, NAME, PHONE, COMPANY, ADDRESS):
    conn.execute("INSERT INTO SatanUSER(ID, NAME, PHONE, COMPANY, ADDRESS) \
             VALUES('%s', '%s', '%s', '%s', '%s');" % (ID, NAME, PHONE, COMPANY, ADDRESS))
    conn.commit()
    print("Insert users successfully")


# 3、按姓名查询联系人详细信息；(包含同名情况)
def selectInformation2():
    conn.execute("SELECT * FROM SatanUSER;")
    row = conn.total_changes
    return row


def selectInformation():
    cursor = conn.execute("SELECT * FROM SatanUSER;")
    row = cursor.fetchall()
    num = row.__len__()
    if not row:
        print('Sorry, this is none!')
    else:
        for i in range(0, num):
            print(row[i], end='\n')
        print("Select all information successfully")
    cursor.close()


def selectInformation1(NAME):
    cursor = conn.execute("SELECT * FROM SatanUSER WHERE NAME = '%s';" % NAME)
    row = cursor.fetchall()
    num1 = row.__len__()
    if not row:
        print('Sorry, this is none!')
    else:
        for i in range(0, num1):
            print(row[i])
        print("Select information through the name successfully")
    cursor.close()


# 4、删除联系人；
def backspaceUser():
    conn.execute("DELETE FROM SatanUSER")
    conn.commit()
    print("Delete all users successfully")


def backspaceUser1(ID):
    conn.execute("DELETE FROM SatanUSER WHERE ID = " + ID)
    conn.commit()
    print("Delete user who id is %s successfully" % ID)


def main():
    createTable()
    insertUser()
    while 1:
        S = input('输入Y/N确定是否需要新增通讯录用户信息：')
        if S == 'Y':
            row = selectInformation2()
            print('ID：' + str(row + 1))
            ID = row + 1
            NAME = input('NAME：')
            PHONE = input('PHONE：')
            COMPANY = input('COMPANY：')
            ADDRESS = input('ADDRESS：')
            insertUser1(ID, NAME, PHONE, COMPANY, ADDRESS)
        else:
            break
    while 1:
        S1 = input('输入1：查询所有联系人信息，'
                   '输入2：按姓名查询联系人信息，'
                   '输入3：不查询：')
        if S1 == '1':
            selectInformation()
        elif S1 == '2':
            NAME = input('NAME：')
            selectInformation1(NAME)
        else:
            break
    while 1:
        S2 = input('输入1：删除所有联系人信息，'
                   '输入2：按ID删除联系人信息，'
                   '输入3：查询所有联系人信息，'
                   '输入4：不操作：')
        if S2 == '1':
            backspaceUser()
        elif S2 == '2':
            ID = input('ID：')
            backspaceUser1(ID)
        elif S2 == '3':
            selectInformation()
        else:
            break
    conn.close()


if __name__ == '__main__':
    main()
# 结果：
# "D:\Program Files (x86)\Python\Python\python.exe" "D:/Program Files (x86)/Python/Project/HW/hw9_1720397.py"
# Open database successfully
# Create SatanUSER successfully
# 输入Y/N确定是否需要新增通讯录用户信息：Y
# ID：4
# NAME：LiRudan
# PHONE：18317053363
# COMPANY：喜羊羊公司
# ADDRESS：中国广东
# Insert users successfully
# 输入Y/N确定是否需要新增通讯录用户信息：N
# 输入1：查询所有联系人信息，输入2：按姓名查询联系人信息，输入3：不查询：1
# (1, 'Satan', 18317053363, '致一公司', '中国')
# (2, '迪迦奥特曼', 18317053363, '致一公司', '法国')
# (3, 'Satan', 12345678901, '可爱多公司', '澳大利亚')
# (4, 'LiRudan', 18317053363, '喜羊羊公司', '中国广东')
# Select all information successfully
# 输入1：查询所有联系人信息，输入2：按姓名查询联系人信息，输入3：不查询：2
# NAME：Satan
# (1, 'Satan', 18317053363, '致一公司', '中国')
# (3, 'Satan', 12345678901, '可爱多公司', '澳大利亚')
# Select information through the name successfully
# 输入1：查询所有联系人信息，输入2：按姓名查询联系人信息，输入3：不查询：2
# NAME：LiRudan
# (4, 'LiRudan', 18317053363, '喜羊羊公司', '中国广东')
# Select information through the name successfully
# 输入1：查询所有联系人信息，输入2：按姓名查询联系人信息，输入3：不查询：3
# 输入1：删除所有联系人信息，输入2：按ID删除联系人信息，输入3：查询所有联系人信息，输入4：不操作：2
# ID：3
# Delete user who id is 3 successfully
# 输入1：删除所有联系人信息，输入2：按ID删除联系人信息，输入3：查询所有联系人信息，输入4：不操作：3
# (1, 'Satan', 18317053363, '致一公司', '中国')
# (2, '迪迦奥特曼', 18317053363, '致一公司', '法国')
# (4, 'LiRudan', 18317053363, '喜羊羊公司', '中国广东')
# Select all information successfully
# 输入1：删除所有联系人信息，输入2：按ID删除联系人信息，输入3：查询所有联系人信息，输入4：不操作：4
#
# Process finished with exit code 0


