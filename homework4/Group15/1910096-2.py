#a鸡头（屁股），b鸡脚，x鸡，y兔
a = 30
b = 90
for x in range(1, a):
    y = a - x
    if 2 * x + 4 * y == b:
        print("鸡有" + str(x) + "只，兔有" + str(y) + "只。")