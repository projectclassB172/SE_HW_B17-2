#游戏要求如下： 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
# 攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
# 例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
# 英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。   受到攻击时，根据灵活性，可以躲避掉对方的攻击。
# 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
# 怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
# 所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。   被攻击对象即受到次点数的攻击。
# 大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，   直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.maxLife = 250 + 50 * self.level
        self.nowLife = self.level*120
    def attack(self):
        atk = random.randint(0, 10*self.level )
        return atk
    def upgrade(hero):
        hero.nowLife= hero.nowLife+10
        hero.level = hero.level +1
        print("{} 【成功升级】,【当前等级】 {},【当前血量】 {}".format(hero.name, hero.level, hero.nowLife))
class HeroHuman(Hero):
    def __init__(self, name):
        super(HeroHuman, self).__init__(name)
        self.avd = 0.4
    def defense(self, atk):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.nowLife -= atk
            print("rl英雄：受到 {}点伤害,当前血量 {}".format(atk, self.nowLife))
        else:
            print("rl英雄：闪避")
class HeroJl(Hero):
    def __init__(self, name):
        super(HeroJl, self).__init__(name)
        self.avd = 0.7
    def defense(self, atk):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.nowLife -= atk
            print("jl英雄：受到 {}点伤害,当前血量 {}".format( atk, self.nowLife))
        else:
            print("jl英雄：闪避")
class Monster:
    def attack(monster):
        attack = 3+random.randint(0, 5*monster.level )
        print("怪兽攻击".format(monster.name))
        return attack
    def __init__(monster, name, level):
        monster.name = name
        monster.level = level
        monster.maxLife = int(level * 15)
        monster.nowLife = int(level * 15)
    def defense(monster, attack):
        monster.nowLife -= attack
        print("怪兽完全体：受到 {} 点伤害,当前血量 {}".format(attack, monster.nowLife))
class BM(Monster):
    def __init__(Bm, name, level):
        super(BM, Bm).__init__(name, level)
        Bm.shield = 5  # 护盾
    def defense(Bm, attack):
        if Bm.shield - attack >= 0:
            Bm.shield = attack-Bm.shield
            print("大怪兽究极体：受到 {}点伤害,当前护盾值 {} ,血量 {}".format( attack, Bm.shield, Bm.nowLife))
        else:
            if Bm.shield > 0:
                Bm.nowLife -= Bm.shield
                Bm.shield = 0
                print("大怪兽究极体：受到 {}点伤害,当前护盾值 {} ,血量 {}".format(attack, Bm.shield, Bm.nowLife))
            else:
                Bm.nowLife -= attack
                print("大怪兽究极体{}：受到 {}点伤害,当前护盾值 {} ,血量 {}".format(Bm.name, attack, Bm.shield, Bm.nowLife))
def main():
    A = HeroHuman("人类")
    B = HeroJl("精灵")
    C = Monster("怪兽幼年体", 1)
    D = Monster("怪兽完全体", 2)
    E = BM("", 3)
    list = [C, D, E]
    while True:
        print("-------------------------------------------------------------")
        list[0].defense(A.attack())
        if list[0].nowLife <= 0:
            print("{} 阵亡".format(list[0].name))
            A.upgrade()
            del list[0]
        if len(list) == 0:
            print("【英雄】：Win!")
            return
        for each in list:
            A.defense(each.attack())
        if A.nowLife <= 0:
            print("【英雄】：Lose!")
            return
if __name__ == '__main__':
  main()

