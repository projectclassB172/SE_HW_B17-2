#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def d1(m,n):
    if m>n:
        m,n=n,m
    p = m*n
    while m != 0:
        r = n%m
        n=m
        m=r
    return (n,p//n)
print(d1(4,6))
# (2, 12)
   

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def d2(str):
    number=0
    letter=0
    blank=0
    other=0
    for i in range(0,len(str)):
        if 48 <= ord(str[i]) <=57:
            number += 1
        elif(65< ord(str[i])<=90) or (97<=ord(str[i])<=122):
            letter += 1
        elif ord(str[i]) ==32:
            blank += 1
        else:
            other += 1
    print("该字符串数字%d个，字母%d个，空格%d个，其他的%d个." % (number,letter,blank,other))

string = input("请输入一个字符串：")
d2(string)
# 请输入一个字符串：aa123  ##$%^
# 该字符串数字3个，字母2个，空格2个，其他的5个.
            
            
