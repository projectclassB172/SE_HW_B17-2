# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def getnum(m,n):
    if m>n:
        m,n = n,m
    p = m*n
    while m!=0:
        r = n%m
        n=m
        m=r
    return (n,int(p/n))
print(getnum(20,30))
# 运行结果：(10, 60)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    num,alpha,space,other = 0,0,0,0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('数字的个数：{}\t字母的个数：{}\t空格的个数：{}\t其他的个数：{}'.format(num,alpha,space,other))
count(input("请输入一个字符串："))
# 运行结果：
# 请输入一个字符串：148ach11 * &^
# 数字的个数：5	字母的个数：3	空格的个数：2	其他的个数：3