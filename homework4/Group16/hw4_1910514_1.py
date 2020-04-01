Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for a in range(0,20):
    for b in range(0,33):
        if(5*a+3*b+(100-a-b)/3==100):
            print("公鸡有"+str(a)+"只，"+"母鸡有"+str(b)+"只,"+"小鸡"+str(100-a-b)+"只")

            
公鸡有0只，母鸡有25只,小鸡75只
公鸡有4只，母鸡有18只,小鸡78只
公鸡有8只，母鸡有11只,小鸡81只
公鸡有12只，母鸡有4只,小鸡84只
>>> 