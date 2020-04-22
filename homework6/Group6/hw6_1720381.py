##第一题
best_language = "PHP is the best programming language in the world! "


best_language = "PHP is the best programming language in the world! "

word=best_language.replace("PHP","Python")

print(word)

##第二题
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))


##第三题
print('第三题：')

import re

string = 'Python is the BEST programming Language！'

res = '[a-z]+$'

if re.match(res, string):

    print('该字符全是小写')

else:

    print('该字符不全是小写')


##第四题
print('第四题：读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。')

text = input('请输入电话号码：')

m = re.findall('((\d{3}\-|\(\d{3}\) )(\d{3})\-(\d{4}))',text)


##第五题
if m:

    for item in m:

        print ('答案：'+item[0])

else:

    print('答案：'+'not match')


str = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'

ymd = re.compile(r'\d{4}-\d{2}-\d{2}')

ymd = ymd.findall(str)

print("".join(ymd))


