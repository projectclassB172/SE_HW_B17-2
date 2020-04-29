# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

'''def demo(m,n):
    p = m*n
    while m%n != 0:
        m,n = n,m%n
    return(n,p//n)
print(demo(7,100))'''

#输出结果： (1, 700)


#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
str = input("请输入一个字符串：")
num = 0
alp = 0
null = 0
num_else = 0
for s in str:
    if s >= '0' and s <= '9':
        num += 1
    elif (s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z'):
        alp += 1
    elif s == ' ':
        null += 1
    else:
        num_else += 1
print("数字的个数：",num)
print("字母的个数：",alp)
print("空格的个数：",null)
print("其他的个数：",num_else)

'''请输入一个字符串：aasd  123  --
数字的个数： 3
字母的个数： 4
空格的个数： 4
其他的个数： 2'''
