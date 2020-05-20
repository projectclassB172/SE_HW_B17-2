from hw9_1720387.User import User
from hw9_1720387.delete_user import deleteUserByName, updateUserByName, deleteUserByID, updateUserByID
from hw9_1720387.insert_user import insertUser, insertUserList
from hw9_1720387.conn_db import createDatebase
from hw9_1720387.select_user import selectUserList, selectUserAll


def printUserList(userList):
    if len(userList)<=0:
        print("查询结果:为空!")
    else:
        for user in userList:
            print('查询结果:{}'.format(user.__str__()))

if __name__ == '__main__':
    userList = []#用户列表
    print('1、创建数据库表')
    createDatebase()#链接并创建数据库addressBook.db和User表

    user0 = User('小明',1234567890,'上海建桥学院','上海市浦东新区南汇新城沪城环路1111号')
    user1 = User('张三',1234567890,'上海建桥学院','上海市浦东新区南汇新城沪城环路1111号')
    user2 = User('李四',1234567890,'上海建桥学院','上海市浦东新区南汇新城沪城环路1111号')
    user3 = User('王五',1234567890,'上海建桥学院','上海市浦东新区南汇新城沪城环路1111号')
    user4 = User('王泽霖', 1234567890, '上海建桥学院', '上海市浦东新区南汇新城沪城环路1111号')
    userList.append(user1)
    userList.append(user2)
    userList.append(user3)
    userList.append(user4)

    print('2、新增联系人')
    print('*插入一个用户:')
    insertUser(user0)#插入一个用户
    print('*插入用户列表:')
    insertUserList(userList) #插入用户列表

    print('3、按姓名查询联系人详细信息')
    print('*查询用户信息:')
    selectUserList = selectUserList('张三')#输入查询条件
    printUserList(selectUserList)#打印

    print('4、删除联系人通过姓名')
    deleteUserByName('王泽霖')
    # updateUserByName('王泽霖')

    print('5、删除联系人通过ID')
    deleteUserByID(1)
    # updateUserByID(1)

    print('6、查询所有未被删除的用户信息')
    selectUserList = selectUserAll()  # 输入查询条件
    printUserList(selectUserList)  # 打印
'''
运行结果:
C:\Users\LingAlReis\PycharmProjects\Demo\venv\Scripts\python.exe C:/Users/LingAlReis/PycharmProjects/Demo/hw9_1720387/Main.py
1、创建数据库表
*创建&打开数据库addressBook.db成功!
*创建表格结果:创建User表格成功！
2、新增联系人
*插入一个用户:
插入结果:姓名:小明	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号	这条数据插入成功！
*插入用户列表:
插入结果:姓名:张三	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号	这条数据插入成功！
插入结果:姓名:李四	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号	这条数据插入成功！
插入结果:姓名:王五	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号	这条数据插入成功！
插入结果:姓名:王泽霖	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号	这条数据插入成功！
3、按姓名查询联系人详细信息
*查询用户信息:
查询结果:ID:2	姓名:张三	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号
4、删除联系人通过姓名
删除结果:姓名为:王泽霖	的对象删除成功！
5、删除联系人通过ID
删除结果:ID为:1	的对象删除成功！
6、查询所有未被删除的用户信息
查询结果:ID:2	姓名:张三	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号
查询结果:ID:3	姓名:李四	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号
查询结果:ID:4	姓名:王五	电话:1234567890	公司:上海建桥学院	地址:上海市浦东新区南汇新城沪城环路1111号

Process finished with exit code 0

'''
