#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def demo(a,b):
	if a>b:
			a,b=b,a
	p=a*b
	while a!=0:
		r=b%a
		b=a
		a=r
	return(b,p//b)

a=int(input('a='))
b=int(input('b='))
print(demo(a,b))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def func(s):
     # num = 0
     # alpha = 0
     # space = 0
     # other = 0
     dic = {'num':0,'alpha':0,'space':0,'other':0}
     for i in s:
         if i.isdigit():
             dic['num'] += 1
         elif i.isalpha():
             dic['alpha'] += 1
         elif i.isspace():
             dic['space'] += 1
         else:
             dic['other'] += 1
     return dic
abc=input('输入字符串：')
print(func(abc))