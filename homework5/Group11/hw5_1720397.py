# hw5——1720397

# 输入 姓名、性别、年龄 ，将数据存储为一个字典
S1 = input("请输入姓名：")
S2 = input("请输入性别：")
S3 = input("请输入年龄：")
SDict = {'姓名' : S1 , '性别' : S2 , '年龄' : S3}
# print(SDict)

# 输出个人介绍——我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print("我的名字" + SDict['姓名'] + "，今年" + SDict['年龄'] + "岁，性别" + SDict['性别'] + "，喜欢敲代码")

# 提醒用户输入身高、联系方式，把数据添加到1中创建的字典
S4 = input("请输入身高：")
S5 = input("请输入联系方式：")
SDict['身高'] =  S4
SDict['联系方式'] = S5

# 循环输出完成后的字典中的所有信息
for Key , Value in SDict.items():
    print(Key + "：" + Value)

# 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
li = [11,22,33,22,22,44,55,77,88,99,11]
S6 = set(li)
li = list(S6)
S6 = dict()
for s in li:
    S6[s] = S6.get(s, 0) + 1
print(S6)

# li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1,2,3,4,5,6,7,8,9]
li = li[2 : 9 : 3]
print(li)

# s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
s = s.split()
s = s[1:2]
s = ','.join(s)
print(s)