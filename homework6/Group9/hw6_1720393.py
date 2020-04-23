#1 将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
input = input("请输入1-7数字：")
print("今天是周{}".format(input))

#3 给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s= "Python is the BEST programming Language！"
a=r'^[a-z\s]*$'
if re.match(a,s):
    print("全是小写")
else:
    print("不是全是小写")

#4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。
str="sa185-235-4567fu"
b=r'\d{3}-\d{3}-\d{4}'
c=r'\d{3}-\d{4}'
print (re.findall(b,str))
print(re.findall(c,str))


#5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
str="今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25"
pattern1=re.compile(r'\d{4}/\d{1,2}/\d{2}')
pattern2=re.compile(r'\d{4}-\d{1,2}-\d{2}')
pattern3=re.compile(r'\d{4}年\d{1,2}月\d{2}')
#print( re.findall(pattern1,str))
print(re.findall(pattern2,str))
#print(re.findall(pattern3,str))

