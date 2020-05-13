import random
import time


class hero(object):
    def __init__(self, name,race):
        self.__name = name
        self.__race = race
        self.__fx=race=="human" and 0.2 or 0.4
        self.__lv=1
        self.curhp=100
        self.maxhp=100
        self.__def =  self.__lv*5

    def attack(self):
        return random.randint(1,self.__lv*10)

    def protest(self, atk):
        return (atk - self.__def) > 0 and atk - self.__def or 0

    def level_up(self):
        self.__lv+=1

    def shanbi(self):
        if (random.random() < self.__fx):
            return 1
        else:
            return 0

    def reducehp(self,atk):
        if(self.shanbi()==1):
            atk=0
            print("英雄闪避成功")
        self.curhp -= atk
        print(self.__name + "(" + str(self.curhp) + "/"+str(self.maxhp)+")")





class monster(object):
    def __init__(self,lv):
        self.__name = "怪物-lv"+str(lv)
        self.__fx = 0.2
        self.curhp = 100
        self.__maxhp = 100
        self.__exhp = lv==3 and 30 or 0
        self.__def = lv*3
        self.__lv=lv

    def attack(self):
        return random.randint(1,self.__lv*10)

    def shanbi(self):
        if(random.random() < self.__fx):
            return 1
        else:
            return 0


    def protest(self, atk):
        return (atk - self.__def) > 0 and atk - self.__def or 0

    def reducehp(self,atk):
        if(self.shanbi()==1):
            atk=0
            print("怪物闪避成功")
        if(self.__exhp <= 0):
            self.curhp -= atk
            print(self.__name + "(" + str( self.curhp )+ ")"+ "(" + str( self.__exhp )+ ")")

        else:
            self.__exhp -= atk
            print(self.__name + "(" +str( self.curhp )+ ")"+ "(" + str( self.__exhp )+ ")")



a=hero(input("你的名字是："),input("你的种族是:human or elf"))
no1=monster(1);
no2=monster(2);
no3=monster(3);
while(a.curhp>0 and no1.curhp>0):
    no1.reducehp(a.attack())
    a.reducehp(no1.attack())
if(a.curhp>0 and no1.curhp<=0):
    print("【【【【【英雄第一次胜利】】】】】】")
    time.sleep(3)
    a.maxhp+=20
    a.curhp=a.maxhp
    while (a.curhp > 0 and no2.curhp > 0):
        no2.reducehp(a.attack())
        a.reducehp(no2.attack())

    if (a.curhp > 0 and no3.curhp <= 0):
        print("【【【【【英雄第二次胜利】】】】】】")
        time.sleep(3)
        a.maxhp += 20
        a.curhp = a.maxhp
        while (a.curhp > 0 and no3.curhp > 0):
            no3.reducehp(a.attack())
            a.reducehp(no2.attack())
        if (a.curhp > 0 and no3.curhp <= 0):
            print("【【【【【WIN】】】】】】")
        else:
            print("【【【【【LOSE】】】】】】")
    else:
        print("【【【【【LOSE】】】】】】")
else:
    print("【【【【【LOSE】】】】】】")
