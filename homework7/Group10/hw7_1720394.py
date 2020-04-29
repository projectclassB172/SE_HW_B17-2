#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def re_num(m,n):
    #x为m,n最大的参数
    #y为m,n最小的参数
    x = max(m, n)
    y = min(m, n)
    #当两个参数有余数是进入while循环
    # 最大公约数：若余数为0，y为最大公约数
    #最小公倍数：两个数的积除以最大公约数
    while x % y:
        x, y = y, x % y
    return (y,m * n // y)
m=int(input('请输入一个正整数：'))
n=int(input('请输入一个正整数：'))
a=re_num(m,n)
print(f'输入的两个正整数为：{m},{n}\n最大公约数和最小公倍数为:{a}')
#输出结果：  请输入一个正整数：3
#           请输入一个正整数：10
#           输入的两个正整数为：3,10
#           最大公约数和最小公倍数为:(1, 30)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(str):
    num,word,space,other= 0,0,0,0
    for i in str:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            word+=1
        elif i.isspace():
            space+=1
        else:
            other+=1
    print(f'输入字符串为：{str}\n'
          f'其中数字有{num}个，字母有{word}个，空格有{space}个，其它的有{other}个')
str=input('请输入一个字符串(可包含空格、字母、数字等)：')
count(str)
#输出结果：请输入一个字符串(可包含空格、字母、数字等)：akdkadbakd  baskdbakd12312313=-=-
#         输入字符串为：akdkadbakd  baskdbakd12312313=-=-
#         其中数字有8个，字母有19个，空格有2个，其它的有4个

