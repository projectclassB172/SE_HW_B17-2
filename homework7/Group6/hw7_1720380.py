# 1.编写函数，接收两个正整数作为参数，返回一个元组，
# 其中第一个元素为最大公约数，第二个元素为最小公倍数。


def min_max_muldiv(a,b):
    L=[]
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if(a%i==0) and (b%i==0):
            L.append(i)
        continue
    n=L[-1]
    c=a              #print("%d和%d的最小公倍数是%d"%(a,b,a*b//n))
    while True:
        if c%a==0 and c%b==0:
            v=c
            break
        c+=1
    return n,v
if __name__ == '__main__':
    print(min_max_muldiv(45,55))
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，
# 字母，空格，以及其它的个数。

string = input("输入一句话：")


def count(s):
    letter = 0
    number = 0
    blank = 0
    other = 0
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


count(string)
