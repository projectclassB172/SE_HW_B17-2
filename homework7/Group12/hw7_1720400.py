#编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def WW(A,B):
    if A>B:
        A,B = B,A
    C = A*B
    while A!=0:
        R= B%A
        B=A
        A=R
    return (B,int(C/B))
print(WW(20,30))

#编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(words):
    num_number = char_number = space_number = other_number = 0
    for char in words:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1
    print("数字个数：%d, 字母个数：%d, 空格个数：%d, 其他字符：%d" % (num_number,char_number,space_number,other_number))
count(input("请输入一个字符串："))