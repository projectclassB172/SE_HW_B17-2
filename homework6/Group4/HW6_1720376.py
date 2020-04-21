'''1 将给定字符串的PHP替换为Python      
best_language = "PHP is the best programming language in the world! "

import re
best_language = "PHP is the best programming language in the world! "
p = re.compile('PHP')
replace = p.sub("Python",best_language)
print(replace)


 
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

n = int(input())
if 0<n<=7:
    print('今天是周'+str(n));
else :
    print('请输入1-7的数字')



3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。

import re
string  = 'Python is the BEST programming Language！'
reg = r'^[a-z\s]*$'
if re.match(reg, string):
    print('yes')
else:
    print('no')
 
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。

import re
tel = input('输入一串数据，自动判断手机号')
m = re.findall(r"1\d{10}",tel)
if m:
    print(m)
else:
    print('没有匹配到手机号')

''这里使用的匹配规则是   1开头的十一位数字''

5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
import re
from datetime import datetime
date = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
dates = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",date)
for item in date_all:
    print (item)


