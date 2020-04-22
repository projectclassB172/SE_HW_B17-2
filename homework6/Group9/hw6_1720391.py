#<1> 将给定字符串的PHP替换为Python

best_language = "PHP is the best programming language in the world! "
rep = best_language.replace('PHP' , 'Python')
print("替换后的字符串为：" + rep)


#<2> 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

day = input("请输入1-7之间的数字：")
date = ["今天是周一" , "今天是周二" , "今天是周三" ,  "今天是周四" ,  "今天是周五" ,  "今天是周六" ,  "今天是周日"]
for i in range(len(date)):
    if i == int(day):
        print(date[i-1])

#<3> 给定一个字符串： Python is the BEST programming Language！ 编写一个正则表达式用来判断该字符串是否全部为小写。

import re
string1 = 'Python is the BEST programming Language！'
string2 = re.match(r'[a-z] + $', string1)
if string2:
    print (string1 + '全为小写' )
else:
    print (string1 + '不全为小写')

#<4> 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。

import re
word = 'My phonenumber is 999-810-7777'
num = re.findall(r'\d{3}-\d{3}-\d{4}' , word)
print("电话号码为：" + str(num[0]))

#<5> 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'

word1 = "'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'"
word2 = re.findall(r'\d{4}-\d{2}-\d{2}', word1)
print("指定格式的日期为：" + word2[0])


'''
运行结果:
替换后的字符串为：Python is the best programming language in the world! 
请输入1-7之间的数字：3
今天是周三
Python is the BEST programming Language！不全为小写
电话号码为：999-810-7777
指定格式的日期为：2012-07-25

'''