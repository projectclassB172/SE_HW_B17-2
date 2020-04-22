#1
best_language = "PHP is the best programming language in the world! "
print("第一题：")
print(best_language.replace("PHP","Python"))

#2
print("第二题：")
cus_input = input("请输入1-7数字：")
print("今天是周{}".format(cus_input))

#3
print("第三题：")
import re
s1='Python is the BEST programming Language！'
an=re.search('^[a-z]+$',s1)
if an:
    print('s1:', an.group(), '全为小写')
else:
    print( 's1', "不全是小写！")
#4
print("第四题：")
s = "Phone number is (0215)123-1234 , 056-234-4567 , 074-457-9878 , (020)475-7542"
result = re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', s)
for each in result:
    print(each[0], each[1], each[2], sep="-")
#5
print("第五题：")
import re
data='今天是2022/9/24'
patten_1 = re.compile('(\d{4}[-/]\d{1,2}[-/]\d{1,2})')
date = patten_1.findall(data)[0]
print(date)
'''运行结果
第一题：
Python is the best programming language in the world! 
第二题：
请输入1-7数字：3
今天是周3
第三题：
s1 不全是小写！
第四题：
056-234-4567
074-457-9878
(020)-475-7542
第五题：
2022/9/24'''

