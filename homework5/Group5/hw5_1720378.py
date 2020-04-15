#<1> 某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典
name = input("请输入你的姓名：")
gender = input("请输入你的性别：")
age = input("请输入你的年龄：")
dict = {}
dict['姓名']=name
dict['性别']=gender
dict['年龄']=age
print(dict)
# 2、数据存储完了，然后输出个人介绍，格式如下:
# 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print("我的名字"+dict.get('姓名')+',今年'+str(dict.get('年龄'))+'岁,性别'+dict.get('性别')+',喜欢敲代码')
# 3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
height=input('请输入您的身高：')
tel=input('请输入您的联系方式：')
dict['身高']=height
dict['联系方式']=tel
print(dict)
# 4 用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
# 姓名 ： xxx
# 性别： xxx
# 年龄： xx
# 身高： xx
# 联系方式：xx
for key in dict:
    print(key+':'+str(dict.get(key)))
# 5. 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
li = [11,22,33,22,22,44,55,77,88,99,11]
l1=list(set(li))
l1.sort(key=li.index)
print(l1)
# 6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])
# 7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
print(s[7:11])