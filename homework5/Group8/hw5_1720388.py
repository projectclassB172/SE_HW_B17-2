#1720388李东鸿

user = {'姓名':'','性别':'','年龄':''}
user['姓名'] = input('请输入你的姓名：')
user['性别'] = input('请输入你的性别：')
user['年龄'] = int(input('请输入你的年龄：'))
print(f"我的名字{user['姓名']}，今年{user['年龄']}岁，性别{user['性别']},喜欢敲代码")
user['身高']=input('请输入你的身高：')
user['联系方式']=input('请输入你的联系方式：')
for key in user:
    print(key+':',user[key])
li = [11,22,33,22,22,44,55,77,88,99,11]
lq = list(set(li))
lq.sort(key=li.index)
print(lq)
set1 = set(lq)
dict1 = {}
for item in set1:
    dict1.update({item:lq.count(item)})
print(dict1)
li = [1,2,3,4,5,6,7,8,9]
liq = li[2:9:3]
print(liq)
s = 'python java php'
print(s[7:11])
