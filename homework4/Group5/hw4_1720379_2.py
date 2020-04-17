
i = 30#设i为头，
j = 90#j为脚
for x in range(1, i):#x为鸡数，
    y = i - x #y为兔数
    if 2 * x + 4 * y == j:
        print("鸡有" + str(x) + "只，兔有" + str(y) + "只。")