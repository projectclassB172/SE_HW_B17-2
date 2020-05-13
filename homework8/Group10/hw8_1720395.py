#面向对象编程练习
#编写一个打怪兽的小游戏。
#游戏要求如下：
#1. 游戏中角色有英雄和怪兽两种大类型。
#2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
#3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
#   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#  英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#  受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
#4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#   被攻击对象即受到次点数的攻击。
#   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
#5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#   直到英雄死亡或所有怪兽被杀死。
#6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

import random
class Attribute():
    def __init__(self, name, level, maxblood):
        self.name = name
        self.level = level
        self.blood=maxblood
        self.maxblood=maxblood
class hero(Attribute):
    def __init__(self,name,level,maxblood,race):
        super().__init__(name,level,maxblood)
        self.race=race
        if self.race=='人类':
            self.flexibility = 0.3
        elif self.race == '精灵':
            self.flexibility =0.6
    def attack(self, monster):
        att = random.randint(0, self.level*10)
        monster.defense(att)
    def defense(self,att):
        df=random.random()
        if df>self.flexibility:
            self.blood-=att
            if self.blood>0:
                print("--{}受到了{}点攻击,当前{}级,生命值：{}".format(self.name,att,self.level,self.blood))
            else:
                print("--{}受到了{}点攻击,当前生命值为0,失败".format(self.name, att))
        else:
            print("--{}躲避掉了攻击".format(self.name))
    def uplevel(self):
        self.level+=1
        self.maxblood = self.maxblood + 10
        self.blood=self.maxblood
        print("---{}升级了，目前{}级,生命值：{}".format(self.name, self.level, self.blood))
class monster(Attribute):
    def __init__(self,name,level,maxblood):
        super().__init__(name,level,maxblood)
        self.shield=0
        if self.level==3:
            self.shield=5
            print("------怪兽升级为BOSS，拥有了5点护盾")
    def attack(self,hero):
        att=random.randint(0,self.level*10)
        hero.defense(att)
    def  defense(self,att):
        self.shield-=att
        if self.shield<=0:
            self.blood-=att
        if self.shield>0:
                print("--{}受到{}伤害,盾牌减少{}，当前护盾为{}".format(self.name, att, att,self.shield))
        else:
            if self.blood>0:
                print("--{}受到{}伤害,当前生命值为{}".format(self.name,att,self.blood))
            else:
                print("--{}受到了{}伤害,当前生命值为0,死亡".format(self.name, att))
def main():
    m1 = monster("小兵" , 1 , 20)
    m2 = monster("中级兵", 2 , 30)
    m3 = monster("超级兵", 3 ,50)
    mo = [m1,m2,m3]
    h = hero("英雄", 2,80,'人类')
    round=1
    while True:
        if mo[0].blood>0:
            print('~'*15,"Round{}".format(round),'~'*15)
            h.attack(mo[0])
            if mo[0].blood>0:
                mo[0].attack(h)
            else:
                h.uplevel()
                del mo[0]
            round += 1
        if len(mo) == 0:
            print("胜利属于{}!".format(h.name))
            break
        if h.blood<=0:
            print("{}失败了!".format(h.name))
            break
if __name__=='__main__':
    main()
