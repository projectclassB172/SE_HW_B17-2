# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def num(x,y):
    if x>y:
        x,y = y,x
    a = x*y
    while x!=0:
        b = y%x
        y=x
        x=b
    return (y,int(a/y))
print(num(4,21))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    letter,number,blank,other= 0,0,0,0
    for each in s:
        if each.encode().isalpha():
            letter += 1
        elif each.isdigit():
            number += 1
        elif each.isspace():
            blank += 1
        else:
            other +=1
    print("数字{}个,字母{}个,空格{}个,其他字符{}个".format(number, letter, blank, other))
count(input("请输入一个字符串："))
