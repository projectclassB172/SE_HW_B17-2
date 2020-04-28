#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def xx(j,k):
     if j>k:
            j,k = k,j
     p = j*k
     while j!=0:
             r = k%j
             k = j
             j = r
     return(k,p//k)
print(xx(12,30))
#"F:\BaiduNetdiskDownload\PyCharm 2019.3.4\工程文件\venv\Scripts\python.exe" "F:/BaiduNetdiskDownload/PyCharm 2019.3.4/工程文件/hw6_1720368.py"
#(6, 60)

#Process finished with exit code 0


#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def xx(str1):
    num_number = char_number = space_number = other_number = 0
    for char in str1:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1

    print("数字个数：%d,字母个数：%d,空格个数：%d,其他字符：%d" % (num_number, char_number, space_number, other_number))
    return
xx("30jka  96$%  ^&*ss  a555")
#"F:\BaiduNetdiskDownload\PyCharm 2019.3.4\工程文件\venv\Scripts\python.exe" "F:/BaiduNetdiskDownload/PyCharm 2019.3.4/工程文件/hw6_1720368.py"
#数字个数：7,字母个数：6,空格个数：6,其他字符：5

#Process finished with exit code 0
