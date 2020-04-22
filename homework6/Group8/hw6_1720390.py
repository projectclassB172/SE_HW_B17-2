import re
# 1将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "

a = "PHP is the best programming language in the world!"
print(a.replace("PHP","Python"))

# 运行结果
# Python is the best programming language in the world!

# 2
# 编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
week = input("请输入数字1-7：")
print("今天是周{}".format(week))

# 运行结果
# 请输入数字1-7：1
# 今天是周1
#
# Process finished with exit code 0



# 3
# 给定一个字符串： Python is the
# BEST
# Programming
# Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。


a = "Python is the BEST Programming Language！"
b = r'^[a-z\s]*$'
if re.match(b, a):
    print('全为小写字母')
else:
    print("不全为小写字母")
# 运行结果
# 不全为小写字母
#
# Process finished with exit code 0



# 4
# 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
# str=input("请输入一个（含电话号码）字符串:")
# # [ ]?表示区号可以跟“ ”，?表示也可能什么都没1有
a = "我的学号是1720390电话是187-8887-6669"
num = re.findall(r'(\d{3}-\d{4}-\d{4})', a)
for i in range(len(num)):
    print(num[i], end=" ")
    # 运行结果
# 187-8887-6669



# 5
# 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
#
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
a = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
day = re.findall(r'\d{4}-\d{2}-\d{2}', a)
for i in range(len(day)):
     print("今天是", day[i], end="")
# 运行结果
# 今天是 2012-07-25
# Process finished with exit code 0

# 全部运行结果
# E:\untitled\Scripts\python.exe E:/PythonWork/untitled/1.py
# Python is the best programming language in the world!
# 请输入数字1-7：1
# 今天是周1
# 不全为小写字母
# 187-8887-6669 今天是 2012-07-25
# Process finished with exit code 0