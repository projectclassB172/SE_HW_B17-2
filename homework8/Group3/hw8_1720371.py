# 面向对象编程练习
# 编写一个打怪兽的小游戏。
# 游戏要求如下：
# 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
#    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#    被攻击对象即受到次点数的攻击。
#    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose
import random
from idlelib.multicall import r


class Hero:
    def __init__(self, name):
        self.name = name  # 名字
        self.level = 1
        self.max_life = 50 + self.level * 5  # 最大生命
        self.current_life = 50 + self.level * 5  # 当前生命

    def upgrade(self):  # 升级
        self.level += 1
        self.max_life += 10  # 升级后血量+10
        self.current_life = self.max_life
        print("恭喜{},打赢怪兽升到{}级,当前血量为{}".format(self.name, self.level, self.current_life))

    def attack(self):
        atk = random.randint(0, self.level * 10 - 1)  # 产生随机数
        print("英雄开始进攻：")
        return atk


class Human(Hero):  # 创建人类继承Hero类
    def __init__(self, name, lhx):
        super(Human, self).__init__(name)  # 继承父类
        self.lhx = 0.4  # 灵活性

    def fy(self, hurt, atk=None):  # 防御
        is_hurt = r.random()  # 产生随机数
        if self.lhx < is_hurt:  # 随机数大于灵活性，则受到伤害
            self.current_life -= hurt
            print("人类{}受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_Life))
        else:
            print("你成功躲掉这一回合的攻击！")


class Spr(Hero):  # 精灵
    def __init__(self, name):
        super(Spr, self).__init__(name)
        self.lhx = 0.8

    def fy(self, hurt, atk=None):
        is_hurt = random.random()
        if self.lhx < is_hurt:
            self.current_life -= hurt
            print("精灵{}受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_Life))
        else:
            print("你成功躲掉这一回合的攻击！")


class gs:  # 怪兽
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_life = int(level * 3)
        self.current_life = int(level * 3)

    def fy(self, hurt):
        self.current_life -= hurt
        print(f'{self.name}受到{hurt}点伤害,当前生命值{self.current_life}')

    def attack(self):
        atk = random.randint(0, self.level * 10 - 1)
        print("怪兽开始进攻".format(self.name))
        return atk


class Boss(gs):
    def __init__(self, name, level):
        super(Boss, self).__init__(name, level)
        self.shield = 5  # 设置护盾属性

    def fy(self, hurt):
        if self.shield - hurt >= 0:  # 优先扣除护盾
            self.shield -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_life}')
        else:
            if self.shield > 0:
                self.current_life -= self.shield
                self.shield = 0
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_life}')
            else:
                self.current_life -= hurt
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_life}')


def main():
    hero = Spr('师溥然')
    monster1 = gs("怪物1", 1)
    monster2 = gs("怪物2", 2)
    monster3 = Boss("终极大怪兽", 3)
    list = [monster1, monster2, monster3]
    round = 1
    while True:
        if list[0].current_life > 0:
            print(f'*************回合{round}***************')
            list[0].fy(hero.attack())
            if list[0].current_life > 0:
                hero.fy(list[0].attack())
            else:
                hero.upgrade()  # 升级
                del list[0]  # 删除死掉的怪兽
            round += 1
        if len(list) == 0:  # 怪兽数量为0，则英雄胜利
            print("你赢了！！！！！！")
            break
        if hero.current_life <= 0:
            print(f'{hero.name}You Loss')
            break


if __name__ == '__main__':  # 运行main
    main()

E:\Workspython\venv\Scripts\python.exe E:/Workspython/hero.py
*************回合1***************
英雄开始进攻：
怪物1受到0点伤害,当前生命值3
怪兽开始进攻
你成功躲掉这一回合的攻击！
*************回合2***************
英雄开始进攻：
怪物1受到4点伤害,当前生命值-1
恭喜师溥然,打赢怪兽升到2级,当前血量为65
*************回合3***************
英雄开始进攻：
怪物2受到19点伤害,当前生命值-13
恭喜师溥然,打赢怪兽升到3级,当前血量为75
*************回合4***************
英雄开始进攻：
终极大怪兽受到16点伤害,当前护盾值0,生命值4
怪兽开始进攻
你成功躲掉这一回合的攻击！
*************回合5***************
英雄开始进攻：
终极大怪兽受到16点伤害,当前护盾值0,生命值-12
恭喜师溥然,打赢怪兽升到4级,当前血量为85
你赢了！！！！！！

Process finished with exit code 0
