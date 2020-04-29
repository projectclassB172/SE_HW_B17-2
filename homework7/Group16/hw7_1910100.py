#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def fun(x,y):
   if x>y:
       x,y=y,x
   z=x*y
   while x!=0:
       k=y%x
       y=x
       x=k
   return(y,int(z/y))

i=3
j=7
a=fun(i,j)
print(a)
#运行函数，结果为：(5, 10)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def fun2(str):
    num,alpha,space,other=0,0,0,0
    for ch in str:
        if ch.isdigit():
            num+=1
        elif ch.isalpha():
            alpha+=1
        elif ch.isspace():
            space+=1
        else:
            other+=1
    print("\n字符串中数字{}个，字母{}个，空格{}个,其他字符{}个".format(num,alpha,space,other))
str=input('请输入字符串')
fun2(str)
#运行结果
#请输入字符串123fsa`1

#字符串中数字4个，字母3个，空格0个,其他字符1个
#——————————————————————————————————————————————————
#请输入字符串asdf  2323 )(* 223

#字符串中数字7个，字母4个，空格4个,其他字符3个