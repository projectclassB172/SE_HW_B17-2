#面向对象编程练习
#编写一个打怪兽的小游戏。
#游戏要求如下： 
#1. 游戏中角色有英雄和怪兽两种大类型。
#2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
#3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#  攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。 
#   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#  英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
#4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#   被攻击对象即受到次点数的攻击。 
#   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
#5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#  直到英雄死亡或所有怪兽被杀死。
#6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

import random as r

#英雄函数，分别是精灵和人类
class Hero:
    #属性
    def __init__(hero, name):
        hero.name = name     # 英雄名字
        hero.level = 1       # 英雄等级
        hero.max_hp = hero.level*60  # 英雄最大生命
        hero.current_hp = hero.level*60  # 英雄当前生命
    #攻击函数
    def attack(hero):
        atk = r.randint(0, hero.level*10)
        print("-->英雄发动攻击回合!")
        return atk
    #升级函数
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10  #当前血量
        hero.level = hero.level +1  #等级
        print("---->{} 升级,当前等级 {},当前血量 {}".format(hero.name, hero.level, hero.current_hp))
# 人类分支
class HeroHuman(Hero):
    # 属性函数
    def __init__(hero, name):
        super(HeroHuman, hero).__init__(name)#继承
        hero.avd = 0.5        # 灵活性
    #防御函数
    def defense(hero, atk):
        is_hurt = r.random()#产生随机数，如果小于0.4则躲避，大于则命中
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_人类：受到 {}点伤害,当前血量 {}".format(atk, hero.current_hp))
        else:
            print("-->英雄_人类：miss!")

# 精灵分支
class HeroSpirit(Hero):
    # 属性函数
    def __init__(hero, name):
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.8        # 灵活性
    # 防御函数
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_精灵：受到 {}点伤害,当前血量 {}".format( atk, hero.current_hp))
        else:
            print("-->英雄_精灵：miss!")


#怪兽函数
class Monster:
    #属性
    def __init__(monster, name, level):
        monster.name = name      # 怪兽名字
        monster.level = level    # 怪兽等级
        monster.max_hp = int(level * 20)  # 怪兽最大生命
        monster.current_hp = int(level * 20)  # 怪兽当前生命


    # 攻击函数
    def attack(monster):
        atk = r.randint(0, monster.level * 10)
        print("-->怪兽发动攻击回合!".format(monster.name))
        return atk

        # 防御
    def defense(monster, atk):
        monster.current_hp -= atk
        print("-->怪兽受到 {} 点伤害,当前血量 {}".format( atk, monster.current_hp))

# 怪兽boss函数
class Monster_bigMonster(Monster):
    # 属性函数
    def __init__(Monster_Boss, name, level):
        super(Monster_bigMonster, Monster_Boss).__init__(name, level)
        Monster_Boss.shield = Monster_Boss.max_hp * 0.5  # 护盾值
    # 防御函数
    def defense(Monster_Boss, atk):   # 受到攻击优先扣除护盾
        if Monster_Boss.shield - atk >= 0:
            Monster_Boss.shield = atk-Monster_Boss.shield
            print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Monster_Boss.shield, Monster_Boss.current_hp))
        else:
            if Monster_Boss.shield > 0:
                Monster_Boss.current_hp -= Monster_Boss.shield
                Monster_Boss.shield = 0
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Monster_Boss.shield, Monster_Boss.current_hp))
            else:
                Monster_Boss.current_hp -= atk
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format(Monster_Boss.name, atk, Monster_Boss.shield, Monster_Boss.current_hp))


#主方法函数
def main():
    #生成一个英雄，两个低等级怪兽，一个大怪兽
    hero = HeroHuman("人类")
    m1 = Monster("小怪兽1", 1)
    m2 = Monster("小怪兽2", 2)
    m3 = Monster_bigMonster("怪兽boss", 3)
    MonsterNum = [m1, m2, m3]
    r = 1
    while True:
        print("回合{}：".format(r))
        MonsterNum[0].defense(hero.attack())   # 英雄轮番攻击怪兽1,2和大怪兽
        if MonsterNum[0].current_hp <= 0:   # 如果怪兽阵亡，则删除怪兽，并且英雄会升级
            print("{} 阵亡".format(MonsterNum[0].name))
            hero.upgrade()
            del MonsterNum[0]
        if len(MonsterNum) == 0:      # 英雄胜利的条件是怪兽数量为0
            print("---->英雄：成功歼灭所有怪兽，赢得胜利!")
            return

        for each in MonsterNum:       # 轮流攻击机制
            hero.defense(each.attack())
        if hero.current_hp <= 0:    # 失败条件：英雄血条为0
            print("---->英雄：您已英勇就义，请尝试重新开局!")
            return
        r += 1    # 回合数加1

if __name__ == '__main__':
  main()


回合1：
-->英雄发动攻击回合!
-->怪兽受到 3 点伤害,当前血量 17
-->怪兽发动攻击回合!
-->英雄_人类：受到 0点伤害,当前血量 60
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 8点伤害,当前血量 52
回合2：
-->英雄发动攻击回合!
-->怪兽受到 2 点伤害,当前血量 15
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 8点伤害,当前血量 44
回合3：
-->英雄发动攻击回合!
-->怪兽受到 10 点伤害,当前血量 5
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：miss!
回合4：
-->英雄发动攻击回合!
-->怪兽受到 0 点伤害,当前血量 5
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 6点伤害,当前血量 38
-->怪兽发动攻击回合!
-->英雄_人类：受到 17点伤害,当前血量 21
回合5：
-->英雄发动攻击回合!
-->怪兽受到 6 点伤害,当前血量 -1
小怪兽1 阵亡
---->人类 升级,当前等级 2,当前血量 31
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 1点伤害,当前血量 30
回合6：
-->英雄发动攻击回合!
-->怪兽受到 8 点伤害,当前血量 32
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 15点伤害,当前血量 15
回合7：
-->英雄发动攻击回合!
-->怪兽受到 20 点伤害,当前血量 12
-->怪兽发动攻击回合!
-->英雄_人类：miss!
-->怪兽发动攻击回合!
-->英雄_人类：受到 1点伤害,当前血量 14
回合8：
-->英雄发动攻击回合!
-->怪兽受到 17 点伤害,当前血量 -5
小怪兽2 阵亡
---->人类 升级,当前等级 3,当前血量 24
-->怪兽发动攻击回合!
-->英雄_人类：受到 3点伤害,当前血量 21
回合9：
-->英雄发动攻击回合!
-->怪兽boss：受到 26点伤害,当前护盾值 -4.0 血量 60
-->怪兽发动攻击回合!
-->英雄_人类：miss!
回合10：
-->英雄发动攻击回合!
-->怪兽boss：受到 怪兽boss点伤害,当前护盾值 21 血量 -4.0
-->怪兽发动攻击回合!
-->英雄_人类：miss!
回合11：
-->英雄发动攻击回合!
-->怪兽boss：受到 怪兽boss点伤害,当前护盾值 12 血量 -4.0
-->怪兽发动攻击回合!
-->英雄_人类：受到 15点伤害,当前血量 6
回合12：
-->英雄发动攻击回合!
-->怪兽boss：受到 怪兽boss点伤害,当前护盾值 14 血量 -4.0
-->怪兽发动攻击回合!
-->英雄_人类：miss!
回合13：
-->英雄发动攻击回合!
-->怪兽boss：受到 怪兽boss点伤害,当前护盾值 18 血量 -4.0
怪兽boss 阵亡
---->人类 升级,当前等级 4,当前血量 16
---->英雄：成功歼灭所有怪兽，赢得胜利!



