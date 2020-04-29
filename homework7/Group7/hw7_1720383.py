#编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def XX(A,B):
    if A>B:
        A,B = B,A
    p = A*B
    while A!=0:
        R= B%A
        B=A
        A=R
    return (B,int(p/B))
print(XX(20,30))

#编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def XX(A):
    num1 = 0
    num 2= 0
    num 3= 0
    num 4= 0
    for char in A:
    if char.isdigit():
      num1 += 1
        elif char.isalpha():
            num2 += 1
        elif i.isspace():
            num3 += 1
        else:
            num4 += 1
 print("数字个数：%d,字母个数：%d,空格个数：%d,其他字符：%d" % (num 1,  num 2,  num 3,  num 4))
    return