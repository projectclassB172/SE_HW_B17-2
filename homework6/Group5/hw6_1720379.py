import re
"""
1 将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
"""
best_language = "PHP is the best programming language in the world! "
print(best_language.replace('PHP','Python'))


"""
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
"""
number=input('输入1-7七个数字，分别代表周一到周日：')
#print(type(number))
if number=='1':
    print('今天是周一')
elif number=='2':
    print('今天是周二')
elif number == '3':
    print('今天是周三')
elif number == '4':
    print('今天是周5')
elif number=='5':
    print('今天是周五')
elif number=='6':
    print('今天是周六')
else:
    print('今天是周日')

"""
3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
"""

str=" Python is the BEST programming Language！"
s=re.match('[a-z]+$',str)
if s:
    print('全部是小写')
else:
    print('不全是小写')


""""
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。
"""
tels=input("enter your tel like this way (xxx-xxxx or xxx-xxx-xxxx):")
tell=re.search(r"(\d{3}-\d{4}-\d{4})",tels)
if tell=='\n':
    tell=re.search(r"(\d{3}-\d{4})",tels)
print(tell)

"""
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
"""

str = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
ymd = re.compile(r'\d{4}-\d{2}-\d{2}')
ymd = ymd.findall(str)
print("".join(ymd))