1.
a = "PHP is the best programming language in the world! "
newa=a.replace("PHP","Python")
print(newa)

2.
input = input("请输入1-7数字：")
print("今天是周{}".format(input))


3.
import re

string = 'Python is the BEST programming Language！'
if re.search('[a-z]+$', string):
    print(string+'全是小写')
else:
    print(string+'不全是小写')

4.
import re
phone = input("请输入一个字符串")
r = re.search(r'\d{3}-\d{3}-\d{4}',phone)
print('读取到的电话号码:'+ r.group(0))

5.
import re
string2 = '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'
day = re.compile(r'\d[4]-\d[2]-\d[2]',string2)
print(day)