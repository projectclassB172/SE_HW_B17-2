# 作业提交到github以下路径homework6 / group < 组号 > / hw6_ < 学号 >.py

# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "

print("第一题")
best_language = "PHP is the best programming language in the world! "
print('替换前：'+best_language)
best_language = best_language.replace('PHP',"Python")
print("替换后："+best_language)
print()

# 第一题 运行结果：
# 替换前：PHP is the best programming language in the world!
# 替换后：Python is the best programming language in the world!


# 2 编写代码，提示用户输入1 - 7
# 七个数字，分别代表周一到周日，打印输出“今天是周几”

print("第二题")
day_num = input('请输入阿拉伯数字1-7：')
dic={'1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周六','7':'周日'}
print('今天是'+dic.get(day_num))
print()

# 第二题 运行结果：
# 请输入阿拉伯数字1-7：5
# 今天是周五

# 3 给定一个字符串： Python is the BEST programming Language！
#   编写一个正则表达式用来判断该字符串是否全部为小写。
print("第三题")
import re
fyjstr = 'Python is the BEST programming Language！'
fyj = re.search('^[a-z]+$', fyjstr)
if fyj:
    print (fyj.group(), '全为小写!' )
else:
    print (fyjstr, "不全是小写！")
# 测试字符串全为小写的情况
fyjstr = 'python'
fyj = re.search('^[a-z]+$', fyjstr)
if fyj:
    print (fyj.group(), '全为小写!' )
else:
    print (fyjstr, "不全是小写！")
print()

# 第三题 运行结果：
# Python is the BEST programming Language！ 不全是小写！
# python 全为小写!

# 4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。
print("第四题")
fyj_pnum = "来电显示 186-1234-5678 上海"
result = re.search(r"(\d{3}-\d{4}-\d{4})",fyj_pnum)
print("原字符串:"+fyj_pnum)
print("读取到的电话号码："+result.group(0))
print()

# 第四题 运行结果：
# 原字符串:来电显示 186-1234-5678 上海
# 读取到的电话号码：186-1234-5678


# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
print("第五题")
fyj_strs = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
i = 0
for s in fyj_strs:
    s = s.replace('/', '-')
    s = s.replace('年', '-')
    s = s.replace('月', '-')
    fyj_result = re.search(r"\d{4}-\d{1,2}-\d{1,2}", s)
    print('原字符串：' + fyj_strs[i])
    print('提取后的日期：' + fyj_result.group(0))
    i += 1
# 第五题 运行结果：
# 原字符串：今天是2022/9/24
# 提取后的日期：2022-9-24
# 原字符串：今天是2017/09/25
# 提取后的日期：2017-09-25
# 原字符串：今天是2012-07-25
# 提取后的日期：2012-07-25
# 原字符串：今天是2020年04月25
# 提取后的日期：2020-04-25
