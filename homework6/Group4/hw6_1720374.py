#1720374黄德鑫

# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
print('替换前：'+best_language)
best_language = best_language.replace('PHP',"Python")
print("替换后："+best_language)

# 2 编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”

number=input('输入1-7七个数字，分别代表周一到周日：')
#print(type(number))
if number=='1':
    print('今天是周一')
elif number=='2':
    print('今天是周二')
elif number == '3':
    print('今天是周三')
elif number == '4':
    print('今天是周四')
elif number=='5':
    print('今天是周五')
elif number=='6':
    print('今天是周六')
else:
    print('今天是周日')

# 3 给定一个字符串： Python is the BEST programming Language！
#   编写一个正则表达式用来判断该字符串是否全部为小写。

 import re
 s1 = 'Python is the BEST programming Language'
 an = re.search('^[a-z]+$', s1)
 if an:
 print ('s1:', an.group(), '全为小写')
 else:
 print (s1,"不全为小写！")

# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。

 import re
 str = "(021) 887 7654 010-556-6789 (025) 845-3362 05718472048 837922740"
 m = re.findall('((\d{3}\-|\(\d{3}\) )(\d{3})\-(\d{4}))', str)
 if m:
 for item in m:
 print (item[0])
 else:
 print('not match')

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',

str = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
ymd = re.compile(r'\d{4}-\d{2}-\d{2}')
ymd = ymd.findall(str)
print("".join(ymd))