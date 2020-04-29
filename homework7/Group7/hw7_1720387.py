# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
print('1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。')
def getGCDAndLCM(x,y):
    if x>y:
        x,y=y,x#判断x与y的大小，如果x>y 互换数据
    temp0 = x * y
    while x!=0:
        temp1 = y % x#对y去模
        y = x
        x= temp1
    return (y,temp0//y)
# 测试getGCDAndLCM
x = int(input('请输入第一个正整数:'))
if isinstance(x,int) and x > 0:#判断x为正整数
    y = int(input('请输入第二个正整数:'))
    if isinstance(y,int) and y > 0:#判断y为正整数
        print('元组:', getGCDAndLCM(x, y))
    elif y <= 0:
        print('请输入一个正数')
elif x <= 0:
    print('请输入一个正数')

'''
结果
1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
请输入第一个正整数:12
请输入第二个正整数:30
元组: (6, 60)
'''

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
print('2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。')
def getWordCount(str):
    dic = {'number': 0, 'alpha': 0, 'space': 0, 'other': 0}
    for i in str:
        if i.isdigit():#判断为number数字，然后计数+1
            dic['number'] += 1
        elif i.isalpha():#判断为alpha字母，然后计数+1
            dic['alpha'] += 1
        elif i.isspace():#判断为space空格，然后计数+1
            dic['space'] += 1
        else:#判断为other其它，然后计数+1
            dic['other'] += 1
    return dic

str = input('请输入字符串:')
title = {'number': '数字', 'alpha': '字母', 'space': '空格', 'other': '其它'}
dict = getWordCount(str)
for key in getWordCount(str).keys():#字典的遍历
    print(title[key]+key+':',getWordCount(str)[key])

'''
2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
请输入字符串:123456789  abc  /*-+
数字number: 9
字母alpha: 3
空格space: 4
其它other: 4
'''