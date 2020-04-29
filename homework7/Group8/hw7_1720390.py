# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def fun(x, y):
    min1 = min(x, y)
    max1 = max(x, y)
    ji = x * y
    while min1 != 0:
        yushu = max1 % min1
        max1 = min1
        min1 = yushu
    g = int(ji/max1)
    return max1, g
print(fun(7, 17))

# (1, 119)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def fun(x):
    no = 0
    abc = 0
    space = 0
    else_a = 0
    list_a = list(x)
    for s in list_a:
        if s.isdigit():#判断数字部分个数
            no += 1
        elif s.isalpha():#判断字母部分个数
            abc += 1
        elif s.isspace():#判断空格部分个数
            space += 1
        else:
            else_a += 1
    print("数字个数：", no)
    print("字母个数：", abc)
    print("空格个数：", space)
    print("其他个数：", else_a)

    # 数字的个数： 3
    # 字母的个数： 4
    # 空格的个数： 2
    # 其他的个数： 3
    #在声明使用过程中要先把变量初始化，也可以用过字典来实现，将字典的key值作为计数
fun(' qwer%%$123 ')