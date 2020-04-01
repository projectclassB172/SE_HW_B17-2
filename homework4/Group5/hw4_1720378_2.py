#设a为头，b为脚，x为鸡的个数，y为兔的个数。
a = 30
b = 90
for x in range(1, a):
    y = a - x
    if 2 * x + 4 * y == b:
        print("鸡有" + str(x) + "只，兔有" + str(y) + "只。")