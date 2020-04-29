#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
#a为第一个正整数，b为第二个正整数,c为最大公约数和最小公倍数
def re_num(a,b):
    x=max(a, b)
    y=min(a, b)
    while x%y:
        x,y=y,x%y
    return (y,a*b//y)
a=int(input('输入第一个正整数：'))
b=int(input('输入第二个正整数：'))
c=re_num(a,b)
print(f'输入的两个正整数为：{a},{b}\n最大公约数和最小公倍数为:{c}')
#输出结果：
#输入第一个正整数：5
#输入第二个正整数：15
#输入的两个正整数为：5,15
#最大公约数和最小公倍数为:(5, 15)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
#num为数字，alpha为字母，space为空格，other为其他
def count(s):
    num,alpha,space,other=0,0,0,0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('数字字符数{},字母字符数{},空格字符数{},其他字符数{}'.format(num, alpha, space, other))
count(input("输入一段字符串："))
#输出结果：
#输入一段字符串：1as   !@#$
#数字字符数1,字母字符数2,空格字符数3,其他字符数4
