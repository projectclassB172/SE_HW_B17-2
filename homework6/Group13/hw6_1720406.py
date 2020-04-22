# 作业提交到github以下路径homework6 / group < 组号 > / hw6_ < 学号 >.py

# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "

print("第一题")
best_language = "PHP is the best programming language in the world! "
print("替换后 "+best_language.replace("PHP", "Python"))

#运行结果：
# 第一题
# 替换后 Python is the best programming language in the world!

# 2 编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”

print("第二题")
num = int(input('输入阿拉伯数字1-7：'))
list = ['周一','周二','周三','周四','周五','周六','周日']
print(f'今天是 {list[num-1]}')

#运行结果：第二题
#输入阿拉伯数字1-7：6
#今天是 周六


# 3 给定一个字符串： Python is the BEST programming Language！
#   编写一个正则表达式用来判断该字符串是否全部为小写。

import re
print("第三题")
str = 'Python is the BEST programming Language！'
result = re.search('^[a-z]+$', str)
if result:
    print ('该字符串全为小写!' )
else:
    print ('该字符串不全是小写！')

#运行结果：
#第三题
#该字符串不全是小写！


# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。

print("第四题")
tel = input(" 请正确输入一个包含电话格式的字符串：")
result_2 = re.search(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})',tel)
print('读取到的电话号码： '+ result_2.group(0))

#运行结果：
#第四题
#请正确输入一个包含电话格式的字符串：123-123-12334
#读取到的电话号码： 123-123-1233


# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
print("第五题")
str_2 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
res = re.compile(r'\d{4}-\d{2}-\d{2}')
res = res.findall(str_2)
print("".join(res))

#运行结果：
# 第五题
#2012-07-25