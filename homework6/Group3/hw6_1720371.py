# 1.将给定字符串的PHP替换为Python
#a="PHP is the best programming language in the world! "
#a.replace('PHP','python')
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","python"))

# 2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
number =int(input('请输入1-7之间的数字分别代表周一到周日：'))
list1=["一","二","三","四","五","六","七"]
if number in range(1,8):
    print("今天为星期{}".format(list1[number-1]))

# 3 给定一个字符串： Python is the BEST programming Language！
# 编写一个正则表达式用来判断该字符串是否全部为小写。
import re
str = 'Python is the BEST programming Language'
b = re.search('^[b-z\s]+$',str)
if b:
    print(str,b.group(),'全为小写')
else:
    print(str,'不全为小写')

# 4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
# （xxx） xxx-xxxx或xxx-xxx-xxxx。
import re
phoneLines = open(r"D:\github\1720371\data.txt","r")    
for phoneLine in phoneLines:       
      phoneLine = phoneLine.strip('\n')       
      if re.findall("(\d{3})\-(\d{3})\-(\d{4})", phoneLine):            
            print phoneLine        
     if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phoneLine):            
             print phoneLine

# 5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
# '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
c= '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
date = re.compile(r'\d{4}-\d{2}-\d{2}')
date = date.findall(c)
print("".join(date))