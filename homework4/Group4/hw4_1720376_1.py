n=0
for x in range(100):  #range随机
    for y in range(100):
        z=100-x-y
        if(z % 3 == 0) and (x * 5 + y * 3 + z / 3 == 100):
            s = "公鸡:%d; 母鸡:%d; 小鸡:%d" %(x, y, z)
            print (s)
            n=n+1
print("一共有"+str(n)+"种买法")
