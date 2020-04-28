#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def cs(x, y):
    if x > y:
        x, y = y, x
    p = x * y
    while x != 0:
        r = y % x
        y = x
        x = r
    return (y, int(p/y))
print(cs(3, 70))

#运行结果:(1, 210)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    digit,alpha,space,other = 0,0,0,0
    for i in s:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('数字的个数：{}\t字母的个数：{}\t空格的个数：{}\t其他的个数：{}'.format(digit,alpha,space,other))
count(input("请输入字符串："))
#运行结果:
请输入字符串：asdf   #$%2^5
数字的个数：2	字母的个数：4	空格的个数：3	其他的个数：4