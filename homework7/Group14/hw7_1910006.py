'''1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。'''
def gygb(x,y):
    a,b=x,y
    while b!=0:
        a, b=b, a%b
    return (a,int(x*y/a))
print(gygb(int(input("输入第一个正整数：")),int(input("输入第二个正整数："))))
print()

'''2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。'''
def count(string):
    d,a,sp,o = 0,0,0,0
    for s in string:
        if s.isdigit():
            d = d + 1
        elif s.isalpha():
            a = a + 1
        elif s.isspace():
            sp = sp + 1
        else:
            o = o + 1
    print("数字个数:"+str(d)+" 字母个数:"+str(a)+" 空格个数:"+str(sp)+" 其它个数:"+str(o))
count(input("输入字符串："))

'''
Run Module
输入第一个正整数：6
输入第二个正整数：9
(3, 18)

输入字符串：967ykhu  *&5pwt %$#^
数字个数:4 字母个数:7 空格个数:3 其它个数:6
'''
