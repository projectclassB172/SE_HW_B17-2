'''1 将给定字符串的PHP替换为Python'''
best_language = "PHP is the best programming language in the world! "
print(best_language.replace('PHP', 'Python'))
print()

'''2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”'''
number = str(input("输入1-7七个数字："))
dic = {'1' : '一', '2' : '二', '3' : '三', '4' : '四', '5' : '五', '6' : '六', '7' : '日'}
print("今天是周" + dic[number])
print()

'''3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。'''
import re 
if re.search('[^a-z]', "Python is the BEST programming Language！"):
    print("不全为小写")
else:
    print("全为小写")
print()

'''4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。'''
str = input("电话号码为：")
for tel in re.findall('\(\d{3}\)\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',str):
    print(tel,end=" ")
print("\n")

'''5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。

'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
list = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for str in list:
    time = re.findall('\d{4}-\d{2}-\d{2}',str)
    if time:
        for t in time:
            print(t)

'''
Run Module
Python is the best programming language in the world! 

输入1-7七个数字：7
今天是周日

不全为小写

电话号码为：(021)123-4567,021-765-4321,8888888888
(021)123-4567 021-765-4321 

2012-07-25

'''
