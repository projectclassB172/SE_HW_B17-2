#1、
def SH(A,B):
    if A>B:
        A,B = B,A
    C = A*B
    while A!=0:
        R= B%A
        B=A
        A=R
    return (B,int(C/B))
print(SH(20,30))

#2、
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
count(input("请输入字符串："))