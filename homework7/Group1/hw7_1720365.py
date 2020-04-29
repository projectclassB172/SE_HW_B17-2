# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def func(m,n):
     if m>n:
             m,n = n,m
     p = m*n
     while m!=0:
        r = n%m
        n = m
        m = r
     return(n,p//n)

print(func(17,65))
# 结果：(1, 1105)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数
import re
def func(str11):
    digital = 0
    letter = 0
    blank = 0
    other = 0
    for i in str11:
        if re.match('[\d]',i) != None:
            digital += 1
        elif re.match('[A-Za-z]',i) != None:
            letter += 1
        elif re.match('\s',i) != None:
            blank += 1
        else:
            other += 1
    print('字符串中[数字]{}个、[字母]{}个、[空格]{}个 、[其他]{}个'.format(digital, letter, blank, other))
str = input("请输入一串包含空格、字母、数字、符合的字符：")
func(str)
# 请输入一串包含空格、字母、数字、符合的字符：1720365_lhf ';o
# 字符串中[数字]7个、[字母]4个、[空格]1个 、[其他]3个