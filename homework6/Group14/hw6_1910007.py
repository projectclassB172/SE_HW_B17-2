'''XiaC'''
##第一题
sentence = "PHP is the best programming language in the world! "
word=sentence.replace("PHP","Python")
print(word)

##第二题
input = input("请输入1-7数字：")
print("今天是周{}".format(input))


##第三题
import re

string = 'Python is the BEST programming Language！'
write = '[a-z]+$'
if re.match(write, string):
    print('该字符全是小写')
else:
    print('该字符不全是小写 ')




##第四题
import re
print('读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。')

text = input('请输入电话号码：')

tel = re.findall(r'\(\d{3}\)\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',text)
print("55:"+tel)
re.purge()



##第五题
import re


m=input()
dd = re.findall(r'\d{4}-\d{2}-\d{2}', m)
for i in range(0, len(dd)):
    print('获取的日期为：' + dd[i], end='\n')
if str(dd) == '[]':
    print('没有日期可获取')
print('\n')