import re
# 1 将给定字符串的PHP替换为Python
# best_language = "PHP is the best programming language in the world! "
print('------------将给定字符串的PHP替换为Python--------------')
best_language = "PHP is the best programming language in the world! "
def checkFilter(keywords,s1):
    return re.sub(keywords,'Python',s1)
keywords=('PHP')
print(checkFilter(keywords,best_language))
#输出结果：Python is the best programming language in the world!

# 2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
print('根据所给数字输出“今天是周几”')
data =int(input('请输入1-7之间的数字代表周一到周日：'))
list1 = ['周一','周二','周三','周四','周五','周六','周日']
print(f'今天是{list1[data-1]}')
#输出结果：请输入1-7之间的数字代表周一到周日：2
#         今天是周二

# 3 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
print('------------判断字符串是否全为小写--------------')
s2 = "Python is the BEST programming Language！"
result=re.search('^[a-z]+$',s2)
#也可以使用re.match()
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
#re.search匹配整个字符串，直到找到一个匹配。
#若匹配失败re.search返回值为none可作于判断条件使用
if result:
    print(f'字符全为小写')
else:
    print(f'不全为小写')
#输出结果：不全为小写

# 4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx-xxxx或xxx-xxx-xxxx。
print('-----------读取电话号码------------')
print(f'电话号码格式：（xxx） xxx-xxxx或xxx-xxx-xxxx')
s3 =input("请按正确的电话号码格式随意输入一个字符串，我们将读取其中的电话号码：")
tel = re.compile(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})')
tel = tel.findall(s3)   #输出之后为列表嵌套元组的形式
for i in tel:
    print(f'{i[0]}-{i[1]}-{i[2]}')
#输出结果：请按正确的电话号码格式随意输入一个字符串，我们将读取其中的电话号码：akudkabdakd(123)-123-1234
#          (123)-123-1234
# 请按正确的电话号码格式随意输入一个字符串，我们将读取其中的电话号码：bkajbfkafkad123-123-1234
# 123-123-1234

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
print('---------------------读取日期-------------------')
s4 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.compile(r'\d{4}-\d{2}-\d{2}')
date = date.findall(s4)
print("".join(date))
#输出结果：2012-07-25