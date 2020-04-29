# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def num(x,y):
    if x>y:
        x,y = y,x
    m = x*y
    while x!=0:
        n = y%x
        y=x
        x=n
    return (y,int(m/y))
x=int(input(' 输入第一个正整数：'))
y=int(input(' 输入第二个正整数：'))

print(f'最大公约数和最小公约数是：{num(x,y)}')
# D:\workpython\venv\Scripts\python.exe D:/workpython/hw7_1720372.py
# 输入第一个正整数：4
# 输入第二个正整数：20
# 最大公约数和最小公约数是：(4, 20)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def num(str1):
    a = b = c = d = 0
    for i in str1:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("数字{}个，字母{}个，空格{}个，其他字符{}个".format(a,b,c,d))
num(input("请输入一个字符串："))

# 请输入一个字符串：sjbs13563  hdjkjk
# 数字5个，字母10个，空格2个，其他字符0个

# 进程已结束,退出代码0

