#编写程序，计算百钱买百鸡问题。
# 假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
#1720397-李如丹

#存在为0的情况
S = 0
for S1 in range(0,21):
    for S2 in range(0,34):
        S3 = 100 - S1 - S2
        if 3 * S2 + 5 * S1 + S3 / 3.0 == 100:
            # S = str(S1 + S2 + S3)
            S = S + 1
            print("公鸡"+str(S1)+"只,母鸡"+str(S2)+"只,小鸡"+str(S3)+"只\n")
print("如果存在为0的情况则有" + str(S) + "种买法！\n")

#不存在为0的情况
S = 0
for S1 in range(1,21):
    for S2 in range(1,34):
        S3 = 100 - S1 - S2
        if 3 * S2 + 5 * S1 + S3 / 3.0 == 100:
            # S = str(S1 + S2 + S3)
            S = S + 1
            print("公鸡"+str(S1)+"只,母鸡"+str(S2)+"只,小鸡"+str(S3)+"只\n")
print("如果不存在为0的情况则有" + str(S) + "种买法！\n")