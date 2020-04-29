#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def NO_1(A,B):
    if A>B:
        A,B = B,A
    C = A*B
    while A!=0:
        R= B%A
        B=A
        A=R
    return (B,int(C/B))
print(NO_1(20,30))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def NO_2(words):
    number,alpha,space,other=0,0,0,0
    for w in words:
        if w.isdigit():
            number += 1
        elif w.isalpha():
            alpha += 1
        elif w.isspace():
            space += 1
        else:
            other += 1
    print("字符串中数字有"+str(number)+"个")
    print("字符串中字母有"+str(alpha)+"个")
    print("字符串中空格有"+str(space)+"个")
    print("字符串中其他字符有"+str(other)+"个")
words = input("请输入字符串：")
NO_2(words)