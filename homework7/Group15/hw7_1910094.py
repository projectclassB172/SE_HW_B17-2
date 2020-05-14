def func(x,y):
    m=min(x,y)
    a_list=[]
    cj=x*y
    for i in range(1,m+1):
        a_list.append(i)
    a_list.reverse()
    for j in a_list:
        if x%j==0 and y%j==0:
            break
    k=int(cj/j)
    return j,k
print(func(18,24))

def func(x,y):
    m1=min(x,y)
    m2=max(x,y)
    cj=x*y
    while m1!=0:
        c=m2%m1
        m2=m1
        m1=c
    gbs=int(cj/m2)
    return m2,gbs
print(func(24,18))

def func(s):
    list_a=list(s)
    dict_a={"数字个数:":0,"字母个数:":0,"空格个数:":0,"其它个数:":0}
    for i in list_a:
        if i>='0' and i<='9':
            dict_a["数字个数:"]+=1
        elif i>='a' and i<='z' or i>='A' and i<='Z':
            dict_a["字母个数:"]+=1
        elif i==' ':
            dict_a["空格个数:"]+=1
        else:
            dict_a["其它个数:"]+=1
    print(dict_a)
func(' 152Rlun{}()@#$fgh369 ')
# 结果：{'数字个数:': 6, '字母个数:': 7, '空格个数:': 2, '其它个数:': 7}
