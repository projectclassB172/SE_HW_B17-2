#<1> 编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def num_1(x , y):
    for i in range(1, min(x , y) + 1):
        if (x % i == 0 and y % i == 0):
            gys = i
    gbs = (x * y) // gys
    return(gys , gbs)
print(num_1(6,15))


#<2> 编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def num_2(x):
    digital = alpha = space = other = 0
    for i in x:
        if i.isdigit():
            digital += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other +=1
    print('数字个数：' + str(digital))
    print('字母个数：' + str(alpha))
    print('空格个数：' + str(space))
    print('其他字符个数：' + str(other))
num_2('Hello,world!  123')

'''
运行结果：
(3, 30)
数字个数：3
字母个数：10
空格个数：2
其他字符个数：2
'''