#1 将给定字符串的PHP替换为Python      
#best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
p = re.compile('PHP')
replace = p.sub("Python",best_language)
print(replace)

#2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

d =int(input('请输入1-7之间的数字：'))
list = ['周一','周二','周三','周四','周五','周六','周日']
print(f'今天是{list1[d-1]}')

#3 给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。

import re
text  = 'Python is the BEST programming Language！'
result = re.search('^[a-z]+$', str)
if result:
    print ('该字符串全部为小写!' )
else:
    print ('该字符串有大写！')
 
#4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。

tel = input(" 请输入一个符合电话格式的字符串：")
r = re.search(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})',tel)
print('读取到的电话号码： '+ r.group(0))


#5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',

day = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
r = re.compile(r'\d{4}-\d{2}-\d{2}')
r = res.findall(day)
print("".join(r))