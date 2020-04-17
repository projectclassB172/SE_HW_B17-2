"""
有6道题（通过字典来操作）：
1. 某比赛需要获取你的个人信息，设计一个程序，
运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，
2、数据存储完了，然后输出个人介绍，格式如下:
我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
4, 平台为了保护你的隐私，需要你删除你的联系方式；
5, 你为了取得更好的成绩， 你添加了自己的擅长技能，至少需要 3 项。
6、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
"""
# 第一题
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {}
dic.update({"name": name, "gender": gender, "age": age})
print(dic)
# 第二题
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["name"], dic["gender"], dic["age"]))
# 第三题
high = input("请输入您的身高：")
mobil_phone = input("请输入您的联系方式：")
dic.update({"high": high, "mobil_phone": mobil_phone})
print(dic)
# 第四题
del dic["mobil_phone"]
print(dic)
# 第五题
dic.update({"skill1": "精通python语言", "skill2": "c语言","skill3": "软件工程"})
print(dic)
# 第六题
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))