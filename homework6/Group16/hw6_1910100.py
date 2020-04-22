#1 将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
print("题一\n替换前："+best_language+"\n替换后:"+best_language.replace('PHP','Python'))

#结果
#替换前：PHP is the best programming language in the world!
#替换后:Python is the best programming language in the world!

#2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

list=["周一","周二","周三","周四","周五","周六","周日"]
day=int(input("\n请输入1-7其中一个数，代表周一到周日:"))
if(day in range(1,8)):
   print("今天是："+list[day-1])

#结果
#请输入1-7其中一个数，代表周一到周日:2
#今天是：周二


#3 给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。

import re
str="Python is the BEST programming Language！"
flag=re.match('[a-z\s]',str)
if flag:
   print("\n"+str+"匹配结果为：全为小写")
else:
   print("\n"+str+"匹配结果为：不全为小写")

#结果
#Python is the BEST programming Language！匹配结果为：不全为小写

#4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx-xxxx或xxx-xxx-xxxx。
#输入样例1：电话号码为123-456-7899号
#输入样例2：电话号码为(123) 456-7891号
#输入样例3：电话号码为(123)asbb456-7891号
import re
str=input("\n请输入字符串，其中需要包含电话号码：")
stresult=re.findall(r'\(\d{3}\)[ ]?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', str)
for i in range(len(stresult)):
   print("\n原字符串:"+str+"  匹配后结果为: "+stresult[i])

#结果：1 2字符串中有符合电话格式的子串，可匹配成功。3不行

#5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。

#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
import re
day=input("\n请输入一个含日期的字符串，日期的格式为yyyy-mm-dd:")
dayresult=re.findall(r'\d{4}[/-年]?\d{1,2}[/-月]?\d{1,2}',day)
for i in range(len(dayresult)):
   print("\n匹配结果为： "+dayresult[i])

#结果
#匹配结果为：2017/09/25
#匹配结果为：2012-07-25
#匹配结果为：2020年04月25
