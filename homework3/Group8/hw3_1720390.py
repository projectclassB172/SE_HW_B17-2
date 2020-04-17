# 变量不能以数字开头
k = -9
# if语句缩进相同，且with不能作为变量
if k>= 0:
    with1 = k +"正数"
    print(with1)
else:
    # print语句中+一个字符串需要在变量钱定义类型
    print(str(k)+ "负数")