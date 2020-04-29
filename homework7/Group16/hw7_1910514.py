#1
print("#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数")
def fun(num1, num2):  # 定义一个函数, 两个形参
    if num1 < num2:  # 判读两个整数的大小,目的为了将大的数作为除数,小的作为被除数
        num1, num2 = num2, num1  # 如果if条件满足,则进行值的交换
        x = num1 * num2  # 计算出两个整数的乘积,方便后面计算最小公倍数
        y = num1 % num2  # 对2个整数进行取余数
        while y != 0:  # 判断余数是否为0, 如果不为0,则进入循环
            num1 = num2  # 重新进行赋值,进行下次计算
            num2 = y
            y = num1 % num2  # 对重新赋值后的两个整数取余数
            x /= num2   # 得出最小公倍数
        return (num2,int(x))
print(fun(6, 9))
#运行结果
#(3, 18)

#2
print("#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数")
def count(str1):
    num_number = char_number = space_number = other_number = 0
    for char in str1:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1
    print("数字个数：%d, 字母个数：%d, 空格个数：%d, 其他字符：%d" % (num_number,char_number,space_number,other_number))
count(input("请输入一个字符串："))
#运行结果
#请输入一个字符串：zwy ^_^ 666
#数字个数：3, 字母个数：3, 空格个数：2, 其他字符：3


