'''
编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
'''
"""
分析步骤：
打怪兽涉及四个对象：一个英雄，两个低级怪兽、一个大怪兽涉及类：游戏类（怪兽和英雄类）
英雄类的属性：
名字、级别、当前生命、当前等级、最大生命值、种族、灵活性
英雄的方法：
1.防御：
攻击点数m大于灵活性则防御失败，受到相应的m点攻击伤害
攻击点数m小于灵活性则攻击失败
2.攻击：
在级别范围内产生随机数
怪兽类：
属性：
名字、级别、当前生命、当前等级、最大生命值、种族、灵活性
特殊属性：
大怪兽的盾牌
怪兽的方法：
1.防御：
攻击点数m大于灵活性则防御失败，受到相应的m点攻击伤害
攻击点数m小于灵活性则攻击失败
2.攻击：
在级别范围内产生随机数
显示回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
"""
'''
编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
'''
"""
分析步骤：
打怪兽涉及四个对象：一个英雄，两个低级怪兽、一个大怪兽涉及类：游戏类（怪兽和英雄类）
英雄类的属性：
名字、级别、当前生命、当前等级、最大生命值、种族、灵活性
英雄的方法：
1.防御：
攻击点数m大于灵活性则防御失败，受到相应的m点攻击伤害
攻击点数m小于灵活性则攻击失败
2.攻击：
在级别范围内产生随机数
怪兽类：
属性：
名字、级别、当前生命、当前等级、最大生命值、种族、灵活性
特殊属性：
大怪兽的盾牌
怪兽的方法：
1.防御：
攻击点数m大于灵活性则防御失败，受到相应的m点攻击伤害
攻击点数m小于灵活性则攻击失败
2.攻击：
在级别范围内产生随机数
显示回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
"""
import random
#创建游戏父类
class Game(object):
    #名字、级别、当前生命
    def __init__(self, name, life, rank):
        self.name = name
        self. max = life
        self._life = life
        self.rank = rank

    def get_name(self):

        return self .name

    def get_life(self):
        return self._life

    def get_rank(self):
        return self.rank

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return '名字: {}\t 生命值: {}\t 等级:{}'.format(self.name, self._life, self.rank)
#创建英雄类
class Hero(Game):
    #初始化
    def __init__(self, name, life=20, rank=1, race='human'):
        super().__init__(name, life, rank)
        #种族
        self.race = race
        # 判断灵活性
        if self.race == '人类':
            self.flexibility = 0.4
        elif self.race == '精灵':
            self.flexibility = 0.8

    # 创建英雄的攻击方法
    def attack(self,Monster):
        # 攻击伤害为0到等级*10之间的随机值
        fight = random.randint(0, self.rank*10)
        Monster.defense(fight) #血量变化情况
    ##英雄的防御方法
    def defense(self, fight):
        # 躲避攻击的随机值
        luck = random.random()
        if luck > self.flexibility:
            # 血量情况
            self._life -= fight
            #输出伤害值
            print('受到{}伤害值'.format(fight))
        else:
            print('躲避攻击成功')

    # 英雄升级
    def upgrade(self):
        self.rank += 1
        self.max = self.max+5#血量上限+5
        self._life = self.max#恢复至上限
        print('升到了{}级'.format(self.rank))

class Monster(Game):#怪兽类继承Game
    def __init__(self , name , life=20, rank=1):
        super().__init__(name,life, rank)
    def attack(self,Hero):
        fight = random.randint(0, self.rank*10)
        Hero.defense(fight)
    def defense(self,fight):
        self._life -= fight#怪兽的血量变化
        print('怪兽受到{}伤害'.format(fight))

# 大怪兽类
class Boss(Game):
    def __init__(self,name,rank,life=80):
        super().__init__(name,rank,life)
        self.shield=20
    def attack(self, Hero):
        fight = random.randint(0, self.rank*10)
        Hero.defense(fight)
    def defense(self,fight):
        # 先减去护盾值
        self.shield-=fight
        if self.shield<=0:
            self._life -= fight
            print('怪兽受到{}伤害'.format(fight))
def main():
    #赋值注意要与之前的变量位置一一对应
    hero = Hero("哪吒", 50, 1, '人类')
    monster1 = Monster("龙王", 30, 1)
    monster2 = Monster("蛇精", 30, 1)
    boss = Boss("如来佛祖", 50, 2)
    monster_list = [monster1, monster2, boss]
    round=1#回合数
    # 判断当hero血量大于0且怪兽数量不为空游戏继续否则结束
    while hero.get_life() > 0 and len(monster_list) > 0:
        # 调用next_monster方法可以在怪兽死后加入下一个怪兽，调用下一个怪兽
        monster = next_monster(monster_list)
        # 判断怪兽血量
        while monster.get_life() > 0:
            print('-' *20, "Round{}".format(round), '-' * 20)
            hero.attack(monster)
            # 攻击英雄
            if monster.get_life() > 0:
                monster.attack(hero)
                if hero.get_life() <= 0:
                    break
            print(hero)
            print(monster)
            round += 1#回合数
        if monster.get_life() <= 0:#如果怪兽死亡
            monster_list.remove(monster)#移除怪兽
            print('怪兽{}惨败'.format(monster.get_name()))
            hero.upgrade()#调用uprade函数英雄升级
            monster = next_monster(monster_list)

    if hero.get_life() >0:#最后英雄没死输出胜利
        print('win,{}'.format(hero.get_name()))
    else:
        print('惨败')

def next_monster(monster_list:list):
    assert type(monster_list) is list
    if len(monster_list)>0:
        return monster_list[0]

if __name__=='__main__':
    main()


