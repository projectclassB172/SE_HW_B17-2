#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def reserve(num1, num2):
    if num1>num2:
        num3 = num1
        num1 = num2
        num2 = num3
    mingbs = num1 * num2
    while num1!=0:
        num4 = num2 % num1
        num2 = num1
        num1 = num4
    maxgys = int(mingbs/num2)
    print('最大公因数为{}\n最小公倍数为{}\n'.format(num2, maxgys))
number1 = input("请输入第一个整数：\n")
num1 = int(number1)
number2 = input("请输入第二个整数：\n")
num2 = int(number2)
result = reserve(num1,num2)
#运行结果
#请输入第一个整数：
#2
#请输入第二个整数：
#3
#最大公因数为1
#最小公倍数为6

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def static(str):
    numbers = 0
    letters = 0
    spaces = 0
    others = 0
    for i in str:
        if i.isdigit():
            numbers += 1
        elif i.isalpha():
            letters += 1
        elif i.isspace():
            spaces += 1
        else:
            others += 1
    print('数字的个数为{}\n字母的个数为{}\n空格的个数为{}\n其他的个数为{}\n'.format(numbers, letters, spaces, others))
str = input("请输入字符串：")
static(str)
#运行结果
#请输入字符串：123abc   ,,,
#数字的个数为3
#字母的个数为3
#空格的个数为3
#其他的个数为3