money = 100
score = 0
for a in range(1,21):
    for b in range(1,34):
        for c in range(1,301):
            score = a*5 + b*3 + float(c)/3
            if score == money and a+b+c ==100:
                print('公鸡 %s 只，母鸡 %s 只,小鸡 %s 只' % (a,b,c))
            else:
                pass
#a表示公鸡  b表示母鸡  c表示小鸡
#python range() 函数可创建一个整数列表，一般用在 for 循环中。
#参数说明：
#start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
#stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)