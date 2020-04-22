#1
#将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "
string='"best_language = "PHP is the best programming language in the world! "'
print(string.replace("PHP","Python"))
#2
#编写代码，提示用户输入1 - 7
#七个数字，分别代表周一到周日，打印输出“今天是周几”
cus_input = input("请输入范围1-7的数字：")
print("今天是周{}".format(cus_input))
#3
#给定一个字符串： Python is the
#BEST
#programming
#Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
import re
string = 'Python is the BEST programming Language！'
reg = r'^[a-z\s]*$'
if re.match(reg, string):
    print('全部为小写')
else:
    print('不全为小写')
#4
#读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
m=re.search('\d{3}-\d{3}-\d{4}','我的电话号码是：123-123-1234')
if m is not None:
    print(m.group())
#5
#利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。

#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
input = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.compile(r'\d{4}-\d{2}-\d{2}')
date = date.findall(input)
print("".join(date))