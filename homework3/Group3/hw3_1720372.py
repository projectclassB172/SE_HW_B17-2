# 2k = -9     ---变量不能数字开头，可改为k2
#   if 2k>= 0:  ---if前方有空格导致程序编译出现错误，将空格删除并修改2k为k2
#     with = 2k +"正数"   ----变量命名格式错误，with为内置关键字不可以使用，with更改为wi即可
#                         ----- 且字符串(str)与数字(int)不能使用+进行拼接，应该将k2转换类型为字符串
#         print(with)     ----更改为print(wi)
#     else:              -----同一级别的代码，缩进必须一致。这里if与else是同一级别代码
#     print(2K+ '负数")   -----1.python对字符串的表示方法有单引号'' 双引号" " 三引号 """ """ ''' '''，但没有' "
#                         -----2.字符串(str)与数字(int)不能使用+进行拼接，应该将k2转换类型为字符串
#                         -----3.变量名字没有区分大小写以及使用数字开头，错误，将2K改为k2


#代码改正
k2 = -9
if k2 >= 0:
    wi=str(k2)+"正数"
    print(wi)
else:
    print(str(k2)+"负数")
