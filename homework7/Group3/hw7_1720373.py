#编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
m = int(input("请输入m的值："))
n = int(input("请输入n的值："))
def demo(m,n):#定义一个函数，其中包含两个形参
    if m>n:#判读两个整数的大小,目的为了将大的数作为除数,小的作为被除数
            m,n = n,m
    p = m*n# 最小公倍数  =  两个整数的乘积 /  最大公约数
    while m!=0:
            r = n%m #对两个数进行取余
            n = m # 重新进行赋值,进行下次计算
            m = r
    return(n,p//n)#有两个反斜杠，只输出整数
print(demo(m,n))

#编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def demo2(s):
    al_num = 0
    spance_num = 0
    digit_num = 0
    others_num = 0
    for i in s:
        if i.isdigit():    # isdigit 判断有没有数字
            digit_num += 1
        elif i.isspace():   # isspace 判断有没有空格
            spance_num += 1
        elif i.isalpha():    #isalpha 判断有没有字符
            al_num += 1
        else:
            others_num += 1
        return (al_num,spance_num,digit_num,others_num)

r = demo2("sza shi xxmddxm 092321")
print(r)