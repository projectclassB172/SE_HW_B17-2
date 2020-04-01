total=0
for i in range(0,int(100/5),1): #i为公鸡数量
    for j in range(0,int(100/3),1):#j为母鸡数量
        if((5*i+3*j+(100-i-j)/3)==100):
            total=total+1
            print("公鸡:"+str(i)+"只 母鸡:"+str(j)+"只 小鸡:"+str((100-i-j))+"只")
print(total)
