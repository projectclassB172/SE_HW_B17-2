count=0
for i in range(20):
    for j in range(33):
            if(i*5+j*3+(100-i-j)/3==100):
                print('公鸡数'+str(i),'母鸡数'+str(j),'小鸡数'+str(100-i-j))
                count=count+1
print('有'+str(count)+'种买法')

'''
Run Module
公鸡数0 母鸡数25 小鸡数75
公鸡数4 母鸡数18 小鸡数78
公鸡数8 母鸡数11 小鸡数81
公鸡数12 母鸡数4 小鸡数84
有4种买法
'''
