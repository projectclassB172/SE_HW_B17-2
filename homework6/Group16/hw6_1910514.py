#1.
print('No.1：将给定字符串的PHP替换为Python')
words=('PHP')
str = "best_language = PHP is the best programming language in the world!"
if words in str:
    str=str.replace(words,'Python')
else:
    pass
print('答案：替换后：'+str)
#运行结果
# 答案：替换后：best_language = Python is the best programming language in the world!

#2.
print('No.2：提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几')
weeks=['一','二','三','四','五','六','日']
answer=int(input('请输入1-7的整数：'))
print('答案：'+'今天是星期'+weeks[answer-1])
#运行结果
#请输入1-7的整数：1
#答案：今天是星期一

#3.
print('No.3：给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写')
import re
s = ' Python is the BEST programming Language！'
#判断s是否都是小写字母：s.islower()；
if s.islower():
    print('答案：'+s+'->是全为小写')
else:
    print('答案：'+s+'->不是全为小写')
#运行结果
#答案： Python is the BEST programming Language！->不是全为小写

#4.
print('No.4：读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。')
text = input('请输入电话号码：')
m = re.findall('((\d{3}\-|\(\d{3}\) )(\d{3})\-(\d{4}))',text)
if m:
    for item in m:
        print ('答案：'+item[0])
else:
    print('答案：'+'not match')
#运行结果
#请输入电话号码：zwy(123) 123-1234
#答案：(123) 123-1234

#5.
print('No.5：利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。')
import re
str="'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',"
s=re.findall(r'\d\d\d\d-\d\d-\d\d',str)
print('答案：符合指定日期格式的日期为：'+s[0])
#运行结果
#答案：符合指定日期格式的日期为：2012-07-25