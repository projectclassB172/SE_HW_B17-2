#1.
name =input("请输入你的姓名：")
gender=input("请输入你的性别：")
age=input("请输入你的年龄：")
dict={}
dict.update({"姓名":name,"性别":gender,"年龄":age})
#2.
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict["姓名"],dict["年龄"],dict["性别"]))
#3.
height=input("请输入你的身高：")
phone=input("请输入你的联系方式：")
dict.update({"身高":height,"联系方式":phone})
#4.
for i in dict:
    print(str(i)+":"+str(dict[i]))
#5.
li=[11,22,33,22,22,44,55,77,88,99,11]
li2=list(set(li))
lenli2= len(li2)
print("列表为:",li,"去重后的列表长度为：",lenli2)
#6.
lili=[1,2,3,4,5,6,7,8,9]
print("列表为:",lili,"切片后的结果为：",lili[2:9:3])
#7.
s='python java php'
print("字符串为：",s,"切片后的结果为:",s[7:11:1])