# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
print('1 将给定字符串的PHP替换为Python')
best_language = 'PHP is the best programming language in the world!'
print('实际结果:'+best_language.replace("PHP", "Python"))
print('理论结果:Python is the best programming language in the world! ')

# 2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
print('2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”')
input0 = input("请输入1-7数字：")
print("今天是周{}".format(input0))

# 3 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
print('3 编写一个正则表达式用来判断该字符串是否全部为小写')
string = 'Python is the BEST programming Language！'
temp = re.search('^[a-z]+$',string)
if temp:
    print('实际结果:'+string + '全部为小写')
else:
    print('实际结果:'+string  + '不全部为小写')
print('理论结果:Python is the BEST programming Language！不全部为小写')

# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx-xxxx或xxx-xxx-xxxx。
print('4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：')
import re
#通过正则表达式从字符串中获取日期，
phone_list = ['我的学号是1720387电话是176-176-1761']
# 正则表达式
regex = "((\d{3}\-|\(\d{3}\))(\d{3})\-(\d{4}))"
# 根据正则表达式列表进行日期截取
for phone in phone_list:
    temp = re.search(regex,phone)
    if temp:
        print('读取其中的电话号码:' + temp[0])
    else:
        print('没有获取到有效电话号码')

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'
print('5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd')
import re
#通过正则表达式从字符串中获取日期，
str_list = ['今天是2022/9/24','今天是2017/09/25','今天是2012-07-25','今天是2020年04月25']
# 正则表达式
# regex = "(\d{4}\-\d{2}\-\d{2})"
regex_list = ['(\d{4}\-\d{2}\-\d{2})','(\d{4}\/\d{2}\/\d{2})',]
# 将年月日转换
# 根据正则表达式列表进行日期截取
for regex in regex_list:
    for str in str_list:
        temp = re.search(regex,str)
        if temp:
            print('日期输出:' + temp.group(0))
        else:
            print('没有获取到有效日期')

# 运行结果：
# 1 将给定字符串的PHP替换为Python
# 实际结果:Python is the best programming language in the world!
# 理论结果:Python is the best programming language in the world!
# 2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
# 请输入1-7数字：1
# 今天是周1
# 3 编写一个正则表达式用来判断该字符串是否全部为小写
# 实际结果:Python is the BEST programming Language！不全部为小写
# 理论结果:Python is the BEST programming Language！不全部为小写
# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# 读取其中的电话号码:176-176-1761
# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd
# 没有获取到有效日期
# 没有获取到有效日期
# 日期输出:2012-07-25
# 没有获取到有效日期
# 没有获取到有效日期
# 日期输出:2017/09/25
# 没有获取到有效日期
# 没有获取到有效日期
