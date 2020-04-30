"""
1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
"""
# def gcdAndCm(a,b):
#     """ gcd是最大公约数 cM最小公倍数"""
#     if a>b:
#         bigs=a
#         mins=b
#     else:
#         bigs=b
#         mins=a
#     for i in range(1,mins+1):
#         if((a%i==0) and (b%i==0)):
#             gcd=i
#     while(True):
#         if((bigs%a==0) and (bigs%b==0)):
#             cM=bigs
#             break
#         bigs=bigs+1
#     s=(gcd,cM)
#     return s
# k=gcdAndCm(46,5)
# print(k)
# help(gcdAndCm)

#结果(1, 230)
def Sum(st):
    num,word,space,other= 0,0,0,0
    for i in st:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            word+=1
        elif i.isspace():
            space+=1
        else:
            other+=1
    dict={'数字':num,'文字':word,'空格':space,'其他':other}
    return dict

str=input('请输入一个字符串S：')
l=Sum(str)
print(l)
