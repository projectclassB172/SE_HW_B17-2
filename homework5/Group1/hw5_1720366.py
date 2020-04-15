# 题目<1>
name = input("输入姓名：")
sex = input("输入性别：")
age = input("输入年龄：")
dict = {}
dict.update({"姓名": name, "性别": sex, "年龄": age})
print(dict)

# 题目<2>
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict["name"], dict["sex"], dict["age"]))

# 题目<3>
high = input("请输入您的身高：")
phone = input("请输入您的联系方式：")
dict.update({"high": high, "phone": phone})
print(dict)

# 题目<4>
for x in dict:
    print("{}:{}".format(x,dict[x]))

# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

# 题目<7>
s = 'python java php'
print("结果：", "\'"+s[7:11]+"\'")
