#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def question1(number1,number2):
   tup=()
   if number1>0 and number2>0:
      for i in range(1,min(number1,number2)+1):
         if(number1%i==0 and number2%i==0):
             lcm=i
      gcdg=(number1*number2) // lcm
   else:
       print("请输入正数")
   tup=(lcm,gcdg)
   print(tup)
question1(10,48)

#运行结果：
#(2, 240)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。以及其它的个数
def question2(strs):
    digital,alpha,space,other=0,0,0,0
    for w in strs:
        if w.isdigit():
            digital += 1
        elif w.isalpha():
            alpha += 1
        elif w.isspace():
            space += 1
        else:
            other += 1
    print("字符串中有数字"+str(digital)+"个")
    print("字符串中有字母"+str(alpha)+"个")
    print("字符串中有空格"+str(space)+"个")
    print("字符串中有其他字符"+str(other)+"个")

question2("qewwwe  232fd45  ")
#运行结果：
#字符串中有数字5个
#字符串中有字母8个
#字符串中有空格4个
#字符串中有其他字符0个
