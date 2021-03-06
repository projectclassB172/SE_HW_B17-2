#   编写程序，计算百鸡百钱的问题
#   假设公鸡5元一只，母鸡3元一只，小鸡一元三只
#   现在有100块钱，问有多少种买法？
#
#   公鸡 a 只 母鸡 b 只 小鸡 100-a-b 只
#   5*a + 3*b + (100-a-b)/3 = 100
#   假设有多少种买法变量为 n
n = 0
a = 0
b = 0
for a in range(0,int(100/5),1):
    for b in  range(0,int(100/3+1),1):
        if(5*a+3*b+(100-a-b)/3==100):
            print("公鸡有"+str(a)+"只"+" 母鸡有"+str(b)+"只"+" 小鸡有"+str((100-a-b))+"只")
            n += 1

print("一共有"+str(n)+"种买法")

#   程序执行结果
#   公鸡有0只 母鸡有25只 小鸡有75只
#   公鸡有4只 母鸡有18只 小鸡有78只
#   公鸡有8只 母鸡有11只 小鸡有81只
#   公鸡有12只 母鸡有4只 小鸡有84只
#   一共有4种买法