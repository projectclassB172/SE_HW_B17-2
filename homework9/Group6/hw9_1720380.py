import sqlite3

class DB:
    # 建表
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

    @staticmethod
    # 获取用户需要输入的数据
    def input():
        try:
            Id = input("ID:") or None
            name = input("姓名:") or None
            phone = input("电话:") or None
            company = input("公司(可选):") or None
            address = input("地址(可选):") or None
            init = [Id, name, phone, company, address]
            return init
        except ValueError as reason:
            print("错误: " + str(reason))

    # 传入之前用户输入的内容
    def add_contacts(self, init):
        try:
            cr.execute("INSERT INTO t_adb VALUES(?,?,?,?,?)",
                           (init[0], init[1], init[2], init[3], init[4]))
            conn.commit()
            print("错误: Affected Rows 1\n")
        except sqlite3.IntegrityError as reason:
            print("错误: " + str(reason) + "\n")
        except TypeError as reason:
            print("错误: " + str(reason) + "\n")
        except sqlite3.OperationalError as reason:
            print("错误: " + str(reason))
            print("请先执行创建表操作...\n")

    @staticmethod
    def input_name():
        name = input("输入姓名:")
        return name

    def find_by_name(self, name):
        try:
            result = cr.execute("SELECT * FROM t_adb WHERE name='{}'".format(name))
            if result:
                for each in result:
                    print("ID:{} 姓名:{} 电话:{} 公司:{} 地址:{}\n"
                          .format(each[0], each[1], each[2], each[3], each[4]))
            else:
                print("INFO: {} is not in t_adb\n".format(name))
        except sqlite3.OperationalError as reason:
            print("错误: " + str(reason))
            print("请先执行创建表操作...\n")

    def delete_by_name(self, name):
        try:
            cr.execute("DELETE FROM t_adb WHERE name='{}'".format(name))
            conn.commit()
            print("结果: 1行受影响\n")
        except sqlite3.OperationalError as reason:
            print("错误: " + str(reason))
            print("请先执行创建表操作...\n")

    @staticmethod
    def show_menu():
        print("**********************************")
        print("**********个人通讯录：***********")
        print("           1.建表             ")
        print("           2.新增联系人       ")
        print("           3.按姓名查询       ")
        print("           4.删除联系人       ")
        print("           0.退出             ")
        print("**********************************")

    # 通讯录的主函数
    def main(self):
        while True:
            self.show_menu()
            try:    # try判断用户的输入是否合法，过滤非数字字符
                opt = int(input("请输入数字以实现数据库操作:"))
            except ValueError:
                print("错误: 非法字符！\n")
                continue
            if opt == 0:
                print("成功退出系统...")
                return
            elif opt == 1:
                self.create_table()
            elif opt == 2:
                self.add_contacts(self.init_data())
            elif opt == 3:
                self.find_by_name(self.input_name())
            elif opt == 4:
                self.delete_by_name(self.input_name())
            else:
                print("无此操作,请重新选择...\n")


if __name__ == "__main__":
    # 连接数据库(如果不存在则创建)
    conn = sqlite3.connect('address_book.db')
    print("数据库连接成功！")
    # 创建游标
    cr = conn.cursor()
    db=DB()#创建对象
    db.main()#调用main方法
    # 关闭数据库操作
    cr.close()
    print("数据库连接已关闭！")
