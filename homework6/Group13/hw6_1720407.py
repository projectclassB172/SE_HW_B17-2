# 1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))
#运行结果：Python is the best programming language in the world!

# 2.编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
s="一二三四五六七"
number=int(input("请输入1-7内数字："))
if number in range(1,8):
    print("今天为星期{}".format(s[number-1]))
# 运行结果：请输入1-7内数字：6
# 今天为星期六

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
str="python is the best programming language！"
# \s表示字符串中可以包括空格和tab，*表示不允许空串，如果允许空串，就把*换成+
str1=re.search('^[a-z\s]+$',str)
if str1:
    print(str+"全是小写")
else:
    print(str+"不全是小写")
# 运行结果：python is the best programming language！不全是小写
# （注：！不是字母）

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
str=input("请输入一个（含电话号码）字符串:")
# # [ ]?表示区号可以跟“ ”，?表示也可能什么都没有
phone=re.findall(r'\(\d{3}\)[ ]?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',str)
for i in range(len(phone)):
    print(phone[i],end=" ")
print("\n")
# 运行结果：请输入一个字符串:(147)145-147878(185) 148-159615228-143-14785633
# (147)145-1478 (185) 148-1596 228-143-1478

# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
str=input("请输入一个（含日期）字符串:")
date=re.findall(r'\d{4}\-\d{2}\-\d{2}',str)
for i in range(len(date)):
     print(date[i],end=" ")
# 运行结果：请输入一个字符串:'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'----2018-12-19。。2018-12-9
# 2012-07-25 2018-12-19