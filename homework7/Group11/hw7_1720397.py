# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def check(a, b):
    s = []
    result = [0, 0]
    for i in range(1, min(a + 1, b + 1)):
        if (a % i == 0) & (b % i == 0):
            s.append(i)
    # 存储最大公约数
    result[0] = max(s)
    # 存储最小公倍数
    result[1] = int((a * b) / max(s))
    print('最大公约数与最小公倍数：', end='')
    return tuple(result)

print('1、求最大公约数与最小公倍数')
a = int(input('输入第一个数：'))
b = int(input('输入第二个数：'))
print(check(a, b))
# 输出结果：
# 1、求最大公约数与最小公倍数
# 输入第一个数：6
# 输入第二个数：8
# 最大公约数与最小公倍数：(2, 24)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
import re
def demo(text):
    s = {}
    num = re.findall('[0-9]', text)
    s['数字'] = s.get('数字', len(num))
    letter = re.findall('[a-zA-Z]', text)
    s['字母'] = s.get('字母', len(letter))
    space = re.findall(' ', text)
    s['空格'] = s.get('空格', len(space))
    other = 0
    for ch in text:
        if (ch not in num) & (ch not in letter) & (ch not in space):
            other = other + 1
    s['其它字符'] = s.get('其它字符', other)
    return s

print('2、计算数字，字母，空格，以及其它的个数')
text = input('输入字符串：')
print(demo(text))
# 输出结果：
# 2、计算数字，字母，空格，以及其它的个数
# 输入字符串：123qweASD#$  #deQ098 GB !=-\i
# {'数字': 6, '字母': 12, '空格': 4, '其它字符': 7}



