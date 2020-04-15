# 1
name=input('请输入您的姓名:')
sex=input('请输入您的性别:')
age=int(input('请输入您的年龄:'))
adict={}
adict['姓名']=name
adict['性别']=sex
adict['年龄']=age
print(adict)
# 2
print("我的名字"+adict.get('姓名')+',今年'+str(adict.get('年龄'))+'岁,性别'+adict.get('性别')+',喜欢敲代码')
# 3
height=input('请输入您的身高(cm)：')
phone=input('请输入您的联系方式：')
adict['身高']=height
adict['联系方式']=phone
print(adict)
# 4 
for key in adict:
    print(key+':'+str(adict.get(key)))
# 5. 
li = [11,22,33,22,22,44,55,77,88,99,11]
li_1=set(li)
print(li_1)
for item in li_1:
    print("the %d has found %d" %(item,li.count(item)))
# 6.
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])
# 7
s = 'python java php'
print(s[7:11])