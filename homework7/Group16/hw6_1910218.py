
def twosum(x,y):
    for i in range(x,y):
        if(i%23==0):
            print(i)

def shuixian(x):
    for i in range(100,x):
        if(((i%10)**3+(i//100)**3+(i//10%10)**3)==i):
            print(i)

def sore():
    d={"60-69":0,"70-79":0,"80-89":0,"90分以上":0}
    for i in range(0,20):
        x=random.randint(0,100)
        if(x>90):
            d["90分以上"]=d["90分以上"]+1
        elif(x>79):
            d["80-89"]=d["80-89"]+1
        elif(x>69):
            d["70-79"]= d["70-79"]+1
        elif (x > 59):
            d["60-69"]=d["60-69"]+1
    for c in d:
        print(c,d[c])

def feibo(x):
    a, b = 0, 1
    while x > 0:
        a, b = b, a + b
        x -= 1
        print(a)

def mima(p):
    if len(p)<6:
        print("错误")
    if not re.search('[a-z]', p):
        print("错误")
        return
    elif not re.search('[0-9]', p):
        print("错误")
        return
    elif not re.search('[A-Z]', p):
        print("错误")
        return
    elif not re.search('[$#@]', p):
        print("错误")
        return
    print("正确")

twosum(100,300)
shuixian(200)
sore()
feibo(10)
mima(" AB123cd#")