print("齐天大圣三打白骨精")
import random
class a:
    def __init__(self, name):
        self.name = name
        self.lv = 1
        self.max_hp = 100
        self.now_hp = 100

    def attack(self):
        hurt = random.randint(0,self.lv*10-1)
        print(f'{self.name}进行攻击!')
        return hurt

    def upgrade(self):
        self.max_hp += 10
        self.now_hp = self.max_hp
        self.lv += 1
        print(f'{self.name}升级,当前等级{self.lv},当前生命值{self.now_hp}')

class Human(a):
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.agile= 0.4

    def defense(self, hurt):
        is_hurt = random.random()
        if self.agile < is_hurt:
            self.now_hp -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前生命值 {self.now_hp}')
        else:
            print(f'{self.name}躲避攻击！')
            print(f'{self.name}当前生命值 {self.now_hp}')

class Hero(a):
    def __init__(self, name):
        super(Hero, self).__init__(name)
        self.agile = 0.6

    def defense(self, hurt):
        is_hurt = random.random()
        if self.agile < is_hurt:
            self.now_hp -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前生命值{self.now_hp}')
        else:
            print(f'{self.name}躲避攻击！')
            print(f'{self.name}当前生命值 {self.now_hp}')

class Monster:
    def __init__(self, name, lv):
        self.name = name
        self.lv = lv
        self.max_hp = int(lv * 10)
        self.now_hp = int(lv * 10)

    def attack(self):
        hurt = random.randint(0, self.lv*10-1)
        print(f'{self.name}进行攻击!')
        return hurt

    def defense(self, hurt):
        self.now_hp -= hurt
        print(f'{self.name}受到{hurt}点伤害,当前生命值{self.now_hp}')

class Boss(Monster):
    def __init__(self, name, lv):
        super(Boss, self).__init__(name, lv)
        self.shield = int(self.max_hp * 1.0)

    def defense(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.now_hp}')
        else:
            if self.shield > 0:
                self.now_hp -= self.shield
                self.shield = 0
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.now_hp}')
            else:
                self.now_hp -= hurt
                print(f'{self.name}受到{hurt}点伤害,当前护盾值{self.shield},生命值{self.now_hp}')


def main():
    hero = Hero('齐天大圣')
    monster1 = Monster("白骨精1", 1)
    monster2 = Monster("白骨精2", 2)
    monster3 = Boss("白骨精3", 3)
    monster_list = [monster1, monster2, monster3]
    round = 1
    while True:
        if monster_list[0].now_hp > 0:
            print(f'Round{round}')
            monster_list[0].defense(hero.attack())
            if monster_list[0].now_hp > 0:
                hero.defense(monster_list[0].attack())
            else:
                hero.upgrade()
                del monster_list[0]
            round+=1
        if len(monster_list) == 0:
            print(f'{hero.name}You Win!')
            break
        if hero.now_hp<=0:
            print(f'{hero.name}You Loss')
            break

if __name__ == '__main__':
    main()