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
class Hero:
    def __init__(self, name):
        self.name = name     # 名字
        self.level = 1       # 等级
        self.max_hp = 20  # 最大生命
        self.current_hp = 20  # 当前生命

    def attack(self):
        #等级1伤害在[0,10)范围内随机产生一个数作为攻击力
        #等级2伤害在[0,20)范围内随机产生一个数作为攻击力
        #以此类推
        hurt = random.randint(0,self.level*10-1)
        print(f'{self.name}进行攻击!')
        return hurt

    def upgrade(self):
        #杀怪奖励回复生命并多10点生命，等级加一
        self.max_hp += 10
        self.current_hp = self.max_hp
        self.level += 1
        print(f'{self.name}升级,当前等级{self.level},当前生命值{self.current_hp}')

#种族为人类，继承英雄的基础属性，为不同种族添加灵活性，人类为0.4，精灵0.6
class Human(Hero):
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.agile= 0.4

    def defense(self, hurt):
        is_hurt = random.random()
        if self.agile < is_hurt:
            self.current_hp -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前生命值 {self.current_hp}')
        else:
            print("躲避攻击！")
            print(f'{self.name}当前生命值 {self.current_hp}')

#种族为人类，继承英雄的基础属性，为不同种族添加灵活性，人类为0.4，精灵0.6
class Elves(Hero):
    def __init__(self, name):
        super(Elves, self).__init__(name)
        self.agile = 0.6

    def defense(self, hurt):
        is_hurt = random.random()
        if self.agile < is_hurt:
            self.current_hp -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前生命值{self.current_hp}')
        else:
            print("躲避攻击！")
            print(f'{self.name}当前生命值 {self.current_hp}')

#定义怪物类，定义攻击与被攻击的函数
class Monster:
    def __init__(self, name, level):
        self.name = name      # 名字
        self.level = level    # 等级
        self.max_hp = int(level * 15)  # 最大生命，采用怪物等级去换算生命值的方法
        self.current_hp = int(level * 15)  # 当前生命，采用怪物等级去换算生命值的方法

    def attack(self):
        #攻击原理与英雄一样
        hurt = random.randint(0, self.level*10-1)
        print(f'{self.name}进行攻击!')
        return hurt

    def defense(self, hurt):
        self.current_hp -= hurt
        print(f'{self.name}受到{hurt}点伤害,当前生命值{self.current_hp}')

#首领怪物继承了怪物类中所有属性，增加了额外的盾牌属性
# 收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
class Boss(Monster):
    def __init__(self, name, level):
        super(Boss, self).__init__(name, level)
        #设置盾牌的防御值为生命的百分之五十
        self.shield = int(self.max_hp * 0.5)

    def defense(self, hurt):
        #考虑减去受到伤害还有无护盾的情况
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_hp}')
        #伤害超出护盾值
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_hp}')
            else:
                self.current_hp -= hurt
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.current_hp}')


def main():
    #调用英雄种类是精灵的类
    hero = Elves('大侠')
    monster1 = Monster("怪物1", 1)
    monster2 = Monster("怪物2", 2)
    boss = Boss("首领", 3)
    #将怪物放到列表中，杀死一个怪物就使用del方法删除
    monster_list = [monster1, monster2, boss]
    round = 1
    while True:
        if monster_list[0].current_hp > 0:
            print(f'---------回合{round}-----------')
            #英雄对怪物发起攻击
            monster_list[0].defense(hero.attack())
            if monster_list[0].current_hp > 0:
                #怪物还活着，英雄受到攻击
                hero.defense(monster_list[0].attack())
            else:
                #怪物死了，英雄升级
                hero.upgrade()
                #删除死掉的怪物
                del monster_list[0]
            round+=1
        #没有怪物，列表长度为0，胜利
        if len(monster_list) == 0:
            print(f'{hero.name}You Win!')
            break
        #英雄生命值为0或者小于0英雄死亡
        if hero.current_hp<=0:
            print(f'{hero.name}You Loss')
            break

if __name__ == '__main__':
    main()
'''
---------回合1-----------
大侠进行攻击!
怪物1受到2点伤害,当前生命值13
怪物1进行攻击!
大侠受到5点伤害,当前生命值15
---------回合2-----------
大侠进行攻击!
怪物1受到4点伤害,当前生命值9
怪物1进行攻击!
大侠受到7点伤害,当前生命值8
---------回合3-----------
大侠进行攻击!
怪物1受到5点伤害,当前生命值4
怪物1进行攻击!
躲避攻击！
大侠当前生命值 8
---------回合4-----------
大侠进行攻击!
怪物1受到4点伤害,当前生命值0
大侠升级,当前等级2,当前生命值30
---------回合5-----------
大侠进行攻击!
怪物2受到3点伤害,当前生命值27
怪物2进行攻击!
躲避攻击！
大侠当前生命值 30
---------回合6-----------
大侠进行攻击!
怪物2受到12点伤害,当前生命值15
怪物2进行攻击!
大侠受到7点伤害,当前生命值23
---------回合7-----------
大侠进行攻击!
怪物2受到12点伤害,当前生命值3
怪物2进行攻击!
躲避攻击！
大侠当前生命值 23
---------回合8-----------
大侠进行攻击!
怪物2受到11点伤害,当前生命值-8
大侠升级,当前等级3,当前生命值40
---------回合9-----------
大侠进行攻击!
首领受到4点伤害,当前护盾值18,生命值45
首领进行攻击!
躲避攻击！
大侠当前生命值 40
---------回合10-----------
大侠进行攻击!
首领受到25点伤害,当前护盾值0,生命值27
首领进行攻击!
躲避攻击！
大侠当前生命值 40
---------回合11-----------
大侠进行攻击!
首领受到14点伤害,当前护盾值0,生命值13
首领进行攻击!
躲避攻击！
大侠当前生命值 40
---------回合12-----------
大侠进行攻击!
首领受到28点伤害,当前护盾值0,生命值-15
大侠升级,当前等级4,当前生命值50
大侠You Win!
'''