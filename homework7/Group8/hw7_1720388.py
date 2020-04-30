# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def num(x,y):
    if x>y:
        x,y = y,x
       p = m*n
    while m!=0:
        r = y%x
        y=x
        x=r
    return (y,int(p/y))
print(num(10,20))
# 运行结果：(5, 20)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，
# 字母，空格，以及其它的个数。

string = input("输入一句话：")


def num(x):
    a = b = c = d = 0
    for i in x:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print('数字个数：' + str(a))
    print('字母个数：' + str(b))
    print('空格个数：' + str(c))
    print('其他字符个数：' + str(d))
num(input("请输入一个字符串："))
