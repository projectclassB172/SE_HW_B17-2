#1.计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？

cock = []
hen = []
chicken = []
way = 0
for i in range(1,15):
    for j in range(1,30):
        k=3*(100-5*i-3*j)
        if i+j+k==100:
            cock.append(i)
            hen.append(j)
            chicken.append(k)
           way+=1
ways=[cock,hen,chicken]
print("共%d种，方案为：%s"%(way,ways))

