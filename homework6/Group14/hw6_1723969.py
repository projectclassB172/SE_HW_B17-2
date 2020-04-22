# 1、将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
str = "PHP is the best programming language in the world!"
print('替换前：'+str)
print('替换后：'+str.replace('PHP','Python'))
# 运行结果：替换前：PHP is the best programming language in the world!
# 替换后：Python is the best programming language in the world!

# 2、编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”
weeks = ['一','二','三','四','五','六','日']
result = int(input('请输入1-7的整数：'))
if 0 < result <= 7:
    print('今天是周'+weeks[result-1])
else:
    print('请输入1-7的整数!')
# 运行结果：请输入1-7的整数：2
# 今天是周二

# 3、给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
str = 'Python is the BEST programming Language'
a = re.search(r'^[a-z]',str)
if a:
    print(str,a.group(),'全为小写')
else:
    print(str,'不全为小写')
# 运行结果：Python is the BEST programming Language 不全为小写

# 4、读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
str = '(021)887-7654 010-556-6789 (021)2055200 15182309567 856-5525252'
result = re.findall('((\d{3}\-|\(\d{3}\))(\d{3})\-(\d{4}))', str)
if result:
    for item in result:
        print(item[0])
else:
    print('no phone')
# 运行结果：(021)887-7654 010-556-6789

# 5、利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'
import re
a = ['今天是2022/9/24','今天是2017/09/25','今天是2012-07-25','今天是2020年04月25']
for b in a:
    c = re.search(r'(\d{4}\-\d{2}\-\d{2})',b)
    if c:
        print(c.group())
# 运行结果：2012-07-25