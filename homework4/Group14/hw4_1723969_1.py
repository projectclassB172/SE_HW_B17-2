sum=0
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            if x*5+y*3+z/3==100 and x+y+z==100:
                sum=sum+1
                print(x,y,z)
print("一共有"+str(sum)+"种买法")
