#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def re_num(m,n):
    x = max(m, n)
    y = min(m, n)
    while x % y:
        x, y = y, x % y
    return (y,m * n // y)
m=int(input('请输入一个正整数：'))
n=int(input('请输入一个正整数：'))
a=re_num(m,n)
print(f'输入的两个正整数为：{m},{n}\n最大公约数和最小公倍数为:{a}')
#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def fn(word):
    count_num = 0
    count_letter = 0
    count_space = 0
    count_other = 0
    for s in word:
        if s.isdigit():
            count_num += 1
        elif s.isalpha():
            count_letter += 1
        elif s.isspace():
            count_space += 1
        else:
            count_other += 1
    print('数字有{}个'.format(count_num))
    print('字母有{}个'.format(count_letter))
    print('空格有{}个'.format(count_space))
    print('其他有{}个'.format(count_other))
    return count_num, count_letter, count_space, count_other

word = input("请输入一段话：")
print(fn(word))


#请输入一个正整数：12
#请输入一个正整数：30
#输入的两个正整数为：12,30
#最大公约数和最小公倍数为:(6, 60)
#请输入一段话：c b a! @123
#数字有3个
#字母有3个
#空格有3个
#其他有2个
#(3, 3, 3, 2)