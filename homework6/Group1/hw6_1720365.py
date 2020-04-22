# 1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

# 2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
data = int(input('输入1-7：'))
list = ['周一','周二','周三','周四','周五','周六','周日']
print(f'今天是 {list[data-1]}')

# 3.给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s="python is the best programming language！"
# \s表示字符串中可以包括空格和tab，*表示不允许空串，如果允许空串，就把*换成+
result=re.search('^[a-z]+$',s)
if result:
    print(s+"全是小写")
else:
    print(s+"不全是小写")

# 4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
s=input(f"请输入一个格式为：（xxx） xxx-xxxx或xxx-xxx-xxxx的电话号码:")
# # [ ]?表示区号可以跟“ ”，?表示也可能什么都没有
tel=re.compile(r'\(\d{3}\)[ ]?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}')
tel = tel.findall(s)   #输出之后为列表嵌套元组的形式
for i in range(len(tel)):
    print(tel[i],end=" ")
print("\n")
# 5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
s=input("请输入一个格式为yyyy - mm - dd的日期:")
date=re.findall(r'\d{4}\-\d{2}\-\d{2}',s)
for i in range(len(date)):
    print("".join(date))
