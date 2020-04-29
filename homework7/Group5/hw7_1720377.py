# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def num(j, k):
    if j > k:
        j, k = k, j
    p = j * k
    while j != 0:
        r = k % j
        k = j
        j = r
    return (k, p // k)


print(num(12, 30))

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
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