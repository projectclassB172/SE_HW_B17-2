# 吴吕俊 1720389

# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "

import re
string = "best_language = 'PHP is the best programming language in the world! ' "
string1 = "PHP"
string2 = re.sub(string1,'Python',string)
print(string2)
print()

# 2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

input = input('请输入1-7其中任意一个阿拉伯数字：')
input1 = {'1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周六','7':'周日'}
input2 = input1.get(input)
print("今天是"+input2)
print()

# 3 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写

import re
str = "Python is the BEST programming Language！"
str1 = re.search("^[a-z]+$", str)
if(str1):
    print (str1.group(), '该字符串全部为小写')
else:
    print (str,"该字符串不是全部为小写")
print()

# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx-xxxx或xxx-xxx-xxxx

import re
information = "(123)123-1234 123-123-1234 "
information1 = re.findall(r'(\d\d\d-\d\d\d-\d\d\d\d)',information)
#information2 = re.findall(r'(\d\d\d)\d\d\d-\d\d\d\d',information) 第一个格式输不出来
print(information1)
#print(information2)
print()

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',

import re
data = "'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'"
data1 = re.findall(r'(\d\d\d\d/\d/\d\d)',data)
data2 = re.findall(r'(\d\d\d\d/\d\d/\d\d)',data)
data3 = re.findall(r'(\d\d\d\d-\d\d-\d\d)',data)
data4 = re.findall(r'(\d\d\d\d年\d\d月\d\d)',data)
print(data1)
print(data2)
print(data3)
print(data4)
