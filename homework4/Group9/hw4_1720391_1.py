sum = 0
for rooster in range(0,20):
    for hen in range(0,33):
        for chicken in range(0,100):
            if rooster*5 + hen*3 + chicken*(1/3) == 100:
                if rooster + hen + chicken == 100:
                    print("公鸡的个数："+str(rooster),"母鸡的个数："+str(hen),"小鸡的个数："+str(chicken))
                    sum += 1

print("共" + str(sum) + "种买法")


'''
运行结果:
公鸡的个数：0 母鸡的个数：25 小鸡的个数：75
公鸡的个数：4 母鸡的个数：18 小鸡的个数：78
公鸡的个数：8 母鸡的个数：11 小鸡的个数：81
公鸡的个数：12 母鸡的个数：4 小鸡的个数：84
共4种买法

'''