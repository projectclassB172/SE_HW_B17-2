gj=[]
mj=[]
xj=[]
for i in range(1,20):
    for j in range(1,33):
        for k in range(3,300,3):
            if i+j+k==100 and 5*i+3*j+k//3==100:
                gj.append(i)
                mj.append(j)
                xj.append(k)
print("总共有",len(gj),"种买法")
for m in range(int(len(gj))):
    print("第"+str(m+1)+"种买法为:","公鸡"+str(gj[m]),"母鸡"+str(mj[m]),"小鸡"+str(xj[m]))

    