
'''


1 将给定字符串的PHP替换为Python      

best_language = "PHP is the best programming language in the world! "
'''
best_language = "PHP is the best programming language in the world! "
word=best_language.replace("PHP","Python")

print(word)

'''
Python is the best programming language in the world! 
'''
'''
 

2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

'''
week=input("请输入1—7之内的数! ")

def case1():
    print('星期一')
def case2():
    print('星期二')
def case3():
    print('星期三')
def case4():
    print('星期四')
def case5():
    print('星期五')
def case6():
    print('星期六')
def case7():
    print('星期日')
def default():
    print('你在乱输什么东东')
'''
自制switch
'''
switch = {'1': case1,               
          '2': case2,                
          '3': case3,
          '4': case4,               
          '5': case5,
          '6': case6,
          '7': case7,
          
          
          }
'''
根据获取得到的输入值，开始‘switch’
'''
switch.get(week,default)()
print(week)

'''
3 给定一个字符串： Python is the BEST programming Language！

编写一个正则表达式用来判断该字符串是否全部为小写。
'''
import re
word='Python is the BEST programming Language！'


word2=re.search(r"[a-z]",word)
if word2!="":
    print("有小写")
    print(word2)
else:
    print("没有小写")
    

'''
有小写
<re.Match object; span=(1, 2), match='y'>
'''

'''
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：

（xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
import re
word=input("请输入您的个人信息\n")

phone = re.search(r"(\d{3}-\d{3}-\d{4})",word)
if phone=="":
    phone=re.search(r"(\d{3}-\d{4})",word)
    
print(phone)
'''
请输入您的个人信息
123-4567-555-4444-44444-44444
None
请输入您的个人信息
567-555-4444-44444-44444
<re.Match object; span=(0, 12), match='567-555-4444'>

'''
'''
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。

'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''

import re
date1='今天是2022/9/24'
date2='今天是2017/09/25'
date3= '今天是2012-07-25'
date=date1+date2+date3
print(date)
dates = re.search(r"(\d{4}-\d{2}-\d{2})",date)

print(dates.groups())

