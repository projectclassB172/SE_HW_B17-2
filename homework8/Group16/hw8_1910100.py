import random
class hero(object):
    def __init__(self, name,race,level):
        self.name = name
        self.race = race
        self.level=level
        self.hp=100
        self.maxhp=150
        if(self.name=="human"):
            self.alige=0.2
        else:
            self.alige=0.4
        if self.level == 1:
            self.attack = random.randint(0, 10)
        elif self.level == 2:
            self.attack = random.randint(0, 20)
        elif self.level == 3:
            self.attack = random.randint(0, 30)
    def miss(self):
        if(random.random()<self.alige):
            return 1
        else:
            return 0
    def damage(self,attack):
        if(self.miss()):
            attack=0
            print("英雄"+self.name+"闪避成功，攻击miss!")
        self.hp=self.hp-int(attack)
        print("英雄："+self.name+"受到"+str(attack)+"点伤害，剩余hp:"+str(self.hp))
        if (self.hp <= 0):
            print("英雄" + self.name + "死掉了！")
class monster(object):
    def __init__(self,level,name):
        self.name=name
        self.level=level
        self.hp=100
        self.maxhp=150
        self.sheld = level == 3 and 30 or 0
    def attack(self):
        if(self.level!=3):
            return random.randint(1,self.level*5)
        else:
            i=random.randint(1,self.level*5)
            i+=5
            return i
    def damage(self,damage):
        self.sheld=int(self.sheld)-int(damage)
        if(int(self.sheld)<=0):
            self.hp-=damage
            print("怪兽:"+self.name+"收到了"+str(damage)+"点伤害，剩余HP:"+str(self.hp))
        if(self.hp<=0):
            print("怪兽"+self.name+"死掉了！")

def fun1():
    i = 1
    a=hero(input("英雄的名字为："),input("你的种族是:人类（human） 或者 精灵（elf）"),2)
    m1=monster(1,"史莱姆")
    m2=monster(2,"火焰史莱姆")
    m3=monster(3,"钢铁火焰史莱姆")
    print(a.alige)
    while((m1.hp>0 or m2.hp>0 or m3.hp>0)or a.hp>0):
        print("____________回合"+str(i)+",英雄发起进攻！____________")
        m1.damage(a.attack)
        m2.damage(a.attack)
        m3.damage(a.attack)
        if(m1.hp<=0 and m2.hp<=0 and m3.hp<=0):
            break
        print("怪兽发起进攻")
        if (a.hp <= 0):
            break
        a.damage(m1.attack())
        if(a.hp<=0):
            break
        a.damage(m2.attack())
        if (a.hp <= 0):
            break
        a.damage(m3.attack())
        if (a.hp <= 0):
            break
        i=i+1
        print("\n")
    print("----------------战斗结果--------------------------")
    if(m1.hp>0 or m2.hp>0 or m3.hp>0):
        print("怪兽的胜利！")
    else:
        print("英雄的胜利！")
fun1()
