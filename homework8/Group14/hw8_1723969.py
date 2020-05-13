import random

class Person(object):
    def __init__(self, name, hp, level):
        self.name = name    # 名称
        self.max = hp       # 血槽
        self._hp = hp       # 血量
        self.level = level  # 等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return 'NAME:{}\t HP: {} \t LEVEL:{}'.format(self.name, self._hp, self.level)

class Hero(Person):  #  英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
    def __init__(self, name, hp=30, level=1, race=''):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':    # 人类
            self.agile = 0.4
        elif self.race == 'elves':  # 精灵
            self.agile = 0.8

    def attack(self, monster):  # 攻击技能
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    def defence(self, hurt):  #  受到攻击时，根据灵活性，可以躲避掉对方的攻击
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('你受到了{}点伤害'.format(hurt))
        else:
            print('你躲避了攻击！')

    def upgrade(self):  #  升级英雄
        self.level += 1  #  升级等级到下一级
        if self.level <= 3:
            self.max = self.max + 10  #  更新血槽，血槽加10点
            self._hp = self.max
            print('-'*10, '你升级到{}级'.format(self.level), '-'*10)

class Monster(Person):  #怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero): #  不同等级具有不同的攻击点数
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)
        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('怪兽受到了{}点伤害'.format(hurt))

class Boss(Person):  #  大怪兽具有一个额外的盾牌属性。
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 40  #盾牌

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):  #  收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
        print("Boss受到{}点伤害".format(hurt))

def main():
    name = input("请为您的英雄取一个昵称：")
    race = input("请选定英雄种族：human或者elves，分别代表人类和精灵：")
    hero = Hero(name,100,1,race)
    monster1 = Monster("僵尸")
    monster2 = Monster("吸血鬼",80,1)
    boss = Boss("阎王", 100)
    monster_list = [monster1, monster2, boss]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*10, '第{}回合'.format(r), '*'*10)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break
            print(hero)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_hp() > 0:
        print('You win，{}!'.format(hero.get_name()))
    else:
        print("You lose!")

def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

if __name__ == '__main__':
    main()
