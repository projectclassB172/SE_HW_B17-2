#2.鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

#设兔子为i，则鸡为（30-i）只

#列示：总脚数：i*4+(30-i)*2=90

for i in range(1,30):

    if i*4+(30-i)*2==90:

        print(f'兔子有{i}只，鸡有{30-i}')