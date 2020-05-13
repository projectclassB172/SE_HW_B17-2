# 游戏要求如下：
# 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
#    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。!!!!
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#    被攻击对象即受到次点数的攻击。
#    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
import random
class attribute():
    def __init__(self,name,level,maxb):
        self.name=name
        self.level=level
        self.cl=maxb
        self.maxb=maxb
class Hero(attribute):
    def __init__(self,name,level,maxb,race):
        super().__init__(name,level,maxb)
        self.race=race
        if self.race=='humanity':
            self.agility=0.4
        else :
            self.agility=0.7
    def attack(self,Monster):
        s=random.randint(0,self.level*10)
        Monster.defense(s)
    def defense(self,s):
        lm=random.random()
        if lm>self.agility:
            self.cl-=s
            if self.cl>0:
                print("Name:{}\t受到攻击:{}\tHP:{}\tLevel:{}\t".format(self.name,s,self.cl,self.level))
            else:
                print("Name:{}\t受到攻击:{}\tHP:0\t,阵亡！".format(self.name, s))
        else:
            print("Name:{}\t躲避掉攻击\tHP:{}\tLevel:{}\t".format(self.name,self.cl,self.level))
    def upgrade(self):
        self.level+=1
        self.maxb=self.maxb+10
        self.cl=self.maxb
        print("Name:{}\t获胜！\tHP:{}\tLevel:{}\t".format(self.name,self.cl,self.level))

class Monster(attribute):
    def __init__(self,name,level,maxb):
        super().__init__(name,level,maxb)
    def attack(self,Hero):
        s=random.randint(0,self.level*10)
        Hero.defense(s)
    def defense(self,s):
        self.cl=self.cl-s
        if self.cl>0:
            print("Name:{}\t受到攻击:{}\tHP:{}\tLevel:{}\t ".format(self.name,s,self.cl,self.level))
        else:
            print("Name:{}\t受到攻击:{}\tHP:0\t阵亡！\t".format(self.name, s))

class Bigmonster(attribute):
    def __init__(self,name,level,maxb):
        super().__init__(name,level,maxb)
        self.shield=3
    def attack(self, Hero):
        s = random.randint(0,self.level*10)
        Hero.defense(s)
    def defense(self,s):
        self.shield-=1
        if self.shield>=0:
                print("Name:{}\t受到攻击:{}\t盾牌-1\t当前盾牌:{}点".format(self.name, s, self.shield))
        else:
            self.cl=self.cl-s
            if self.cl>0:
                print("Name:{}\t受到攻击:{}\tHP:{}\t".format(self.name,s,self.cl))
            else:
                print("Name:{}\t受到攻击:{}\tHP:0\t阵亡!".format(self.name, s))


def main():
    a=random.random()
    if a >=0.5:
        hero=Hero("人类",1,35,'humanity')
    else:
        hero = Hero("精灵", 1, 30, 'spirit')
    m1=Monster("怪兽1",1,30)
    m2= Monster("怪兽2",2,50)
    m3=Bigmonster("BOSS",3,80)
    mo=[m1,m2,m3]
    time=1
    while True:
        print('-'*15,"第{}回合".format(time),'-'*15)
        hero.attack(mo[0])
        if mo[0].cl>0:
            mo[0].attack(hero)
        else:
            hero.upgrade()
            del mo[0]
        time+=1

        if len(mo) == 0:
            print("英雄Win!" )
            break
        elif hero.cl<=0:
            print("英雄Lose!" )
            break

if __name__=='__main__':
    main()


#运行结果：种族（精灵）
# --------------- 第1回合 ---------------
# Name:怪兽1	受到攻击:9	HP:21	Level:1
# Name:精灵	    受到攻击:9	HP:21	Level:1
# --------------- 第2回合 ---------------
# Name:怪兽1	受到攻击:10	HP:11	Level:1
# Name:精灵	    躲避掉攻击	HP:21	Level:1
# --------------- 第3回合 ---------------
# Name:怪兽1	受到攻击:2	HP:9	Level:1
# Name:精灵	    受到攻击:5	HP:16	Level:1
# --------------- 第4回合 ---------------
# Name:怪兽1	受到攻击:5	HP:4	Level:1
# Name:精灵	    受到攻击:2	HP:14	Level:1
# --------------- 第5回合 ---------------
# Name:怪兽1	受到攻击:4	HP:0	阵亡！
# Name:精灵	    获胜！	HP:40	Level:2
# --------------- 第6回合 ---------------
# Name:怪兽2	受到攻击:17	HP:33	Level:2
# Name:精灵	    躲避掉攻击	HP:40	Level:2
# --------------- 第7回合 ---------------
# Name:怪兽2	受到攻击:20	HP:13	Level:2
# Name:精灵	    受到攻击:0	HP:40	Level:2
# --------------- 第8回合 ---------------
# Name:怪兽2	受到攻击:3	HP:10	Level:2
# Name:精灵	    躲避掉攻击	HP:40	Level:2
# --------------- 第9回合 ---------------
# Name:怪兽2	受到攻击:12	HP:0	阵亡！
# Name:精灵	    获胜！	HP:50	Level:3
# --------------- 第10回合 ---------------
# Name:BOSS	受到攻击:5	盾牌-1	当前盾牌:2点
# Name:精灵	躲避掉攻击	HP:50	Level:3
# --------------- 第11回合 ---------------
# Name:BOSS	受到攻击:16	盾牌-1	当前盾牌:1点
# Name:精灵	受到攻击:19	HP:31	Level:3
# --------------- 第12回合 ---------------
# Name:BOSS	受到攻击:5	盾牌-1	当前盾牌:0点
# Name:精灵	受到攻击:3	HP:28	Level:3
# --------------- 第13回合 ---------------
# Name:BOSS	受到攻击:7	HP:73
# Name:精灵	躲避掉攻击	HP:28	Level:3
# --------------- 第14回合 ---------------
# Name:BOSS	受到攻击:1	HP:72
# Name:精灵	躲避掉攻击	HP:28	Level:3
# --------------- 第15回合 ---------------
# Name:BOSS	受到攻击:5	HP:67
# Name:精灵	躲避掉攻击	HP:28	Level:3
# --------------- 第16回合 ---------------
# Name:BOSS	受到攻击:19	HP:48
# Name:精灵	躲避掉攻击	HP:28	Level:3
# --------------- 第17回合 ---------------
# Name:BOSS	受到攻击:25	HP:23
# Name:精灵	躲避掉攻击	HP:28	Level:3
# --------------- 第18回合 ---------------
# Name:BOSS	受到攻击:30	HP:0	阵亡!
# Name:精灵	获胜！	HP:60	Level:4
# 英雄Win!

#运行结果：种族（人类）
# --------------- 第1回合 ---------------
# Name:怪兽1	受到攻击:0	HP:30	Level:1
# Name:人类	    躲避掉攻击	HP:35	Level:1
# --------------- 第2回合 ---------------
# Name:怪兽1	受到攻击:9	HP:21	Level:1
# Name:人类	    躲避掉攻击	HP:35	Level:1
# --------------- 第3回合 ---------------
# Name:怪兽1	受到攻击:1	HP:20	Level:1
# Name:人类	    躲避掉攻击	HP:35	Level:1
# --------------- 第4回合 ---------------
# Name:怪兽1	受到攻击:8	HP:12	Level:1
# Name:人类	    躲避掉攻击	HP:35	Level:1
# --------------- 第5回合 ---------------
# Name:怪兽1	受到攻击:9	HP:3	Level:1
# Name:人类	    躲避掉攻击	HP:35	Level:1
# --------------- 第6回合 ---------------
# Name:怪兽1	受到攻击:8	HP:0	阵亡！
# Name:人类	    获胜！	HP:45	Level:2
# --------------- 第7回合 ---------------
# Name:怪兽2	受到攻击:20	HP:30	Level:2
# Name:人类	    躲避掉攻击	HP:45	Level:2
# --------------- 第8回合 ---------------
# Name:怪兽2	受到攻击:4	HP:26	Level:2
# Name:人类	    受到攻击:3	HP:42	Level:2
# --------------- 第9回合 ---------------
# Name:怪兽2	受到攻击:4	HP:22	Level:2
# Name:人类	    受到攻击:11	HP:31	Level:2
# --------------- 第10回合 ---------------
# Name:怪兽2	受到攻击:16	HP:6	Level:2
# Name:人类	    躲避掉攻击	HP:31	Level:2
# --------------- 第11回合 ---------------
# Name:怪兽2	受到攻击:10	HP:0	阵亡！
# Name:人类	    获胜！	HP:55	Level:3
# --------------- 第12回合 ---------------
# Name:BOSS	受到攻击:25	盾牌-1	当前盾牌:2点
# Name:人类	躲避掉攻击	HP:55	Level:3
# --------------- 第13回合 ---------------
# Name:BOSS	受到攻击:4	盾牌-1	当前盾牌:1点
# Name:人类	躲避掉攻击	HP:55	Level:3
# --------------- 第14回合 ---------------
# Name:BOSS	受到攻击:18	盾牌-1	当前盾牌:0点
# Name:人类	躲避掉攻击	HP:55	Level:3
# --------------- 第15回合 ---------------
# Name:BOSS	受到攻击:27	HP:53
# Name:人类	躲避掉攻击	HP:55	Level:3
# --------------- 第16回合 ---------------
# Name:BOSS	受到攻击:28	HP:25
# Name:人类	受到攻击:26	HP:29	Level:3
# --------------- 第17回合 ---------------
# Name:BOSS	受到攻击:8	HP:17
# Name:人类	受到攻击:20	HP:9	Level:3
# --------------- 第18回合 ---------------
# Name:BOSS	受到攻击:24	HP:0	阵亡!
# Name:人类	获胜！	HP:65	Level:4
# 英雄Win!


