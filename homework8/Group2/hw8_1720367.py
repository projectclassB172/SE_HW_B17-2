import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name
        self.max = hp
        self._hp = hp
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return '剩余HP: {} \t 当前LEVEL:{}'.format(self._hp, self.level)


class Hero(Person):
    def __init__(self, name, hp=30, level=1, race=''):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.3
        elif self.race == 'elves':
            self.agile = 0.7

    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    def upgrade(self):
        self.level += 1
        if self.level <= 3:
            self.max = self.max + 10
            self._hp = self.max
            print('你升级到{}级*****'.format(self.level), )

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('受到{}伤害'.format(hurt))
        else:
            print('没有命中')


class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)
        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('敌人受到了{}伤害'.format(hurt))


class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
        print("Boss受到{}点伤害".format(hurt))


def main():
    name = input("决定英雄取个名字：")
    race = input("请选定英雄种族：human或者elves，分别代表人类和精灵：")
    hero = Hero(name, 100, 1, race)
    monster1 = Monster("鱼人")
    monster2 = Monster("野兽", 80, 1)
    boss = Boss("城堡恶龙", 100)
    monster_list = [monster1, monster2, boss]
    print("*****游戏开始*****")
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('第{}回合'.format(r))
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
        print('*****获得胜利，游戏结束!*****')
    else:
        print("*****你的英雄死了，游戏结束*****")


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


if __name__ == '__main__':
    main()
