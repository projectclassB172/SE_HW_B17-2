题目<1>
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

题目<2>
week = int(input('请输入数字1-7！'))
dateweek = ['周一','周二','周三','周四','周五','周六','周日']
print(f'{dateweek[num-1]}')

题目<3>
import re
language = 'Python is the BEST programming Language！'
result = re.search('^[a-z]+$', language)
if result:
    print ('全都是小写' )
else:
    print ('不全是小写')

题目<4>
text = input("请输入一个字符串：")
result = re.search(r'([(]\d{3}[)]|\d{3})-(\d{3})-(\d{4})',text)
print('电话号码是： '+ result.group(0))

题目<5>
day = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
dateday = re.compile(r'\d{4}-\d{2}-\d{2}')
dateday = dateday.findall(day)
print("".join(dateday))