#1.计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？

#设
公鸡 cock 
母鸡 hen 
小鸡chick
#关系式： 1.总价钱为100：5*cock+3*hen+chick/3=100；
#        2.买的鸡总共一百只：cock+hen+chick=100

#将鸡放入列表存储
chicken = []
for cock in range(1,20):
    for hen in range(1,33):
        chick=100-hen-cock
        if 5*cock+3*hen+chick/3==100:
#           准备空字典，字典新增数据，列表追加字典
            chicken_dict={}
            chicken_dict['cock']=cock
            chicken_dict['hen']=hen
            chicken_dict['chick']=chick
            chicken.append(chicken_dict)
print(f'-------鸡数量不可为0的情况-------')
#打印列表--字典内容
for i in chicken:
    print(f'{i}')
    print(f'公鸡有{i["cock"]}只，母鸡有{i["hen"]}只,小鸡有{i["chick"]}只。')

for i in chicken1:
    print(f'{i}')
    print(f'公鸡有{i["cock"]}只，母鸡有{i["hen"]}只,小鸡有{i["chick"]}只。')
