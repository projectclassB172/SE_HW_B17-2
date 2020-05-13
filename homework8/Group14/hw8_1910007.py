import random

class Person():
    def __init__(self, name, hp, level):
        self.name = name 
        self.max = hp 
        self.hp = hp 
        self.level = level 

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getLevel(self):
        return self.level

    def attack():
        raise NotImplementedError

    def defense():
        raise NotImplementedError

    def __str__(self):
        return '姓名:{}\t血量:{}\t等级:{}\t'.format(self.name, self.hp, self.level)

class Hero(Person):
    def __init__(self, name, hp=20, level=1, race='人族'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'elves':
            self.fexibility = 0.8
        elif self.race == '人族':
            self.fexibility = 0.4
            
    def attack(self, monster):
        if self.level == 1:
            m = random.randint(0,10)
        elif self.level == 2:
            m = random.randint(0,20)
        elif self.level == 3:
            m = random.randint(0,30)
        monster.defense(m)
        
    def defense(self, m):
        if random.random() >= self.fexibility:
            self.hp -= m
            print('英雄受到{}点伤害'.format(m))
        else:
            print('英雄躲掉了攻击')

    def upgrade(self):
        if self.level < 3:
            self.level += 1
            self.max += 40
            self.hp = self.max
            print('英雄升到{}级,血槽加到{}'.format(self.level,self.max))
        else:
            print("英雄胜")

class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            m = random.randint(0,10)
        elif self.level == 2:
            m = random.randint(0,20)
        hero.defense(m)

    def defense(self, m):
        self.hp -= m
        print('{}受到{}点伤害'.format(self.name,m))

class Boss(Person):
    def __init__(self, name, hp=100):
        super().__init__(name, hp, 3)
        self.shield = 30

    def attack(self, hero):
        m = random.randint(0,30)
        hero.defense(m)

    def defense(self, m):
        if self.shield > 0:
            self.shield -= m
            print('老怪用盾牌抵御了{}伤害'.format(m))
        else:
            self.hp -= m
            print('老怪受到{}点伤害'.format(m))

if __name__=='__main__':
    hero = Hero('英雄', 20, 1, '人族')
    monster1 = Monster('3狼')
    monster2 = Monster('石头人', 60, 2)
    boss = Boss('老怪', 100)
    monsterlist = [monster1, monster2, boss]
    round = 1
    for monster in monsterlist:
        print('\n'+'-'*20+'round {}'.format(round)+'-'*20+'\n')
        while hero.getHp() > 0:
            hero.attack(monster)
            if monster.getHp() > 0:
                monster.attack(hero)
                print(hero.__str__())
                print(monster.__str__()+'\n')
            else:
                print(str(monster.getName())+'败')
                hero.upgrade()
                round += 1
                break

        else:
            print('英雄败')
            break