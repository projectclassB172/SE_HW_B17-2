# Course:项目实战
# Sno:1720397
# Name:李如丹

# 1 将给定字符串的PHP替换为Python
# eg:best_language = "PHP is the best programming language in the world! "
print('===1、将给定字符串的PHP替换为Python===')
S = ('PHP', )
best_language = "PHP is the best programming language in the world! "
print('原句为：' + best_language)
for s in S:
    if s in best_language:
        best_language = best_language.replace(s, 'Python')
print('转换后为：' + str(best_language) + '\n')
# 输出结果
# ===1、将给定字符串的PHP替换为Python===
# 原句为：PHP is the best programming language in the world!
# 转换后为：Python is the best programming language in the world!

# 2 编写代码，提示用户输入1 - 7七个数字，分别代表周一到周日，打印输出“今天是周几”(实在没读懂题目，两种意思都往下写了)
# print('===2、提示用户输入1 - 7七个数字，分别代表周一到周日，打印输出“今天是周几”===')
# # 输入七个数字，逐一确定是周几
S = input('日期_请输入1 - 7七个数字：')
num = ('1', '2', '3', '4', '5', '6', '7')
wDict = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '日'}
for s in S:
    if s not in num:
        print('仅输入包含1-7的数字！')
        break
    elif S.count('')-1 != 7:
        print('请输入七个1-7范围内的数字！')
        break
    else:
        print('你输入的是' + s)
        print('今天是周' + str(wDict[s]))
# 输出结果
# ===2、提示用户输入1 - 7七个数字，分别代表周一到周日，打印输出“今天是周几”===
# 日期_请输入1 - 7七个数字：4567123
# 你输入的是4
# 今天是周四
# 你输入的是5
# 今天是周五
# 你输入的是6
# 今天是周六
# 你输入的是7
# 今天是周日
# 你输入的是1
# 今天是周一
# 你输入的是2
# 今天是周二
# 你输入的是3
# 今天是周三

# 只需输入一个数字输出周几
digits = int(input('\n' + '请输入1-7的数字：'))
num = (1, 2, 3, 4, 5, 6, 7)
wDict = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '日'}
if digits not in range(1, 8):
    print('仅输入1-7的数字！' + '\n')
else:
    print('今天是周' + str(wDict[digits]) + '\n')
# 输出结果
# 请输入1-7的数字：3
# 今天是周三

# 3 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
print('===3、编写一个正则表达式用来判断该字符串是否全部为小写===')
S = r'Python is the BEST programming Language！'
print('输入：' + S)
# 除了识别字母大小写，允许有其他字符出现
s = re.search('^[^A-Z]+$', S)
if s:
    print('输入全为小写！\n')
else:
    print('输入不全为小写！\n')
# 输出结果
# ===3、编写一个正则表达式用来判断该字符串是否全部为小写===
# 输入：Python is the BEST programming Language！
# 输入不全为小写！

# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
print('===4、要求使用正则表达式来读取其中的电话号码===')
S = input('输入一串带电话号码的字符串：')
number = re.findall(r'\(\d{3}\)\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', S)
for i in range(0, len(number)):
    print(number[i], end='\n')
if str(number) == '[]':
    print('没有电话号码可获取')
print('\n')
re.purge()
# 输出结果
# ===4、要求使用正则表达式来读取其中的电话号码===
# 输入一串带电话号码的字符串：1231231daf(183)170-336343hjkfbskj
# (183)170-3363

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '2020-04-22', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
print('===5、利用正则表达式从不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd===')
S = input('输入一串带日期的字符串：')
sDate = re.findall(r'\d{4}-\d{2}-\d{2}', S)
for i in range(0, len(sDate)):
    print('获取的日期为：' + sDate[i], end='\n')
if str(sDate) == '[]':
    print('没有日期可获取')
print('\n')
# 输出结果
# ===5、利用正则表达式从不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd===
# 输入一串带日期的字符串：'今天是2022/9/24', '2020-04-22', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'
# 获取的日期为：2020-04-22
# 获取的日期为：2012-07-25
