# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def no(m,n):
    if m>n:
        m,n = n,m
    p = m*n
    while m!=0:
        r = n%m
        n=m
        m=r
    return (n,int(p/n))
print(no(20,30))

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(j):
    num1,num2,num3,num4 = 0,0,0,0
    for i in j :
        if i.isdigit():
            num1 += 1
        elif i.isalpha():
            num2 += 1
        elif i.isspace():
            num3 += 1
        else:
            num4 += 1
    print('数字的个数：{}\t字母的个数：{}\t空格的个数：{}\t其他的个数：{}'.format(num1,num2,num3,num4))
count(input("请输入一个字符串："))