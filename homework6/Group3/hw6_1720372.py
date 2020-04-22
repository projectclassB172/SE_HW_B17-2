#1 将给定字符串的PHP替换为Python
print('第一题：')
best_language = " PHP is the best programming language in the world! "

best_language2 = str(best_language.strip())  # 去掉两端空格
if best_language2.find("PHP") != 1:
    best_language3 = best_language2.replace("PHP", "Python")
    print(f'修改后为：'+best_language3)
else:
    print("你要找的字符不存在")

#2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
print('第二题：')
i= int(input("请输入数字："))
if 0<i<=7:
    print('今天是周'+str(i));
else :
    print('请输入1-7的数字')

print('用列表实现：')
num =int(input('请输入1-7之间的数字：'))
list1=['周一','周二','周三','周四','周五','周末','周日']
str1='今天是{}'.format(list1[num-1]) #字符串的格式化输出format()方法
print(str1)

#3 给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
print('第三题：')
import re
string = 'Python is the BEST programming Language！'
res = '[a-z]+$'
if re.match(res, string):#re.search和re.match都可以，两者区别在于后者默认以开始符（^）开始
    print('该字符全是小写')
else:
    print('该字符不全是小写')

#4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。
print('第四题：')
import re
str=input("输入一个字符串:")
tel=re.search(r'[(]\d{3}[)]|\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',str)
print('电话号码为： '+ tel.group(0))

#5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
print('第五题：')
str='今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date=re.findall(r'\d{4}\-\d{2}\-\d{2}',str)
for n in range(len(date)):
     print(f'指定日期为：'+date[n],end=" ")

