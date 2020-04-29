# 作业提交到github路径: <repository>hw6/group<组号>/， 文件命名格式： hw6_<学号>.py.
# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def calc(a,b):
    temp = 2
    if a>0 and b>0:
        while True:
            if a%temp == 0 and b%temp == 0:
                maxY= temp
                break
            else:
                if temp > max(a,b):
                    maxY = 1
                    break
                temp += 1
        if maxY == 1:
            minB = a*b
        else:
            if max(a,b)%min(a,b)==0:
                minB = max(a,b)
        return (maxY,minB)

    else:
        print('抱歉！您输入的不是两个正整数！')
print(calc(3,7))
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。以及其它的个数

def TJ(words):
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
    print("字符串中有数字"+str(number)+"个")
    print("字符串中有字母"+str(alpha)+"个")
    print("字符串中有空格"+str(space)+"个")
    print("字符串中有其他字符"+str(other)+"个")
words = input("请输入要统计的句子：")
TJ(words)


# 程序运行结果
# 请输入要统计的句子：hello! my,tel 110
# 字符串中有数字3个
# 字符串中有字母10个
# 字符串中有空格2个
# 字符串中有其他字符2个
