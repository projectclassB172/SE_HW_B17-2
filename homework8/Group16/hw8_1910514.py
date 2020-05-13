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

    def attack(self,target):
        raise NotImplementedError


    def __str__(self):
        return 'Name:{}\t HP:{}\t Level:{}'.format(self.name,self._hp,self.level)

class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='human'):
        super().__init__(name,hp,level)
        self.race=race
        if self.race=='human':
            self.agile=0.4
        elif self.race=='elves':
            self.agile=0.8
    def attack(self,monster):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        monster.defence(hurt)

    def defence(self,hurt):
        luck=random.random()
        if luck>=self.agile:
            self._hp -=hurt
            print('你受到{}点攻击!'.format(hurt))
        else:
            print('你躲避了攻击')

    def upgrade(self):
        self.level +=1
        self.max = self.max+ 10
        self.hp=self.max
        print('-'*10,'你升级到{}'.format(self.level))

class Monster(Person):
    def __init__(self,name,hp=20,level=1):
        super().__init__(name,hp,level)

    def attack(self,hero):
        if self.level==1:
            hurt=random.randint(0,10)
        if self.level==2:
            hurt=random.randint(0,20)

        hero.defence(hurt)

    def defence(self,hurt):
        self._hp -= hurt
        print('怪兽受到{}点伤害'.format(hurt))

class Boss(Person):
    def __init__(self,name,hp):
        super().__init__(name,hp,3)
        self.shield=30
    def attack(self,hero):
        hurt=random.randint(0,30)
        hero.defence(hurt)

    def defence(self,hurt):
        self.shield-=hurt
        if self.shield<=0:
            self._hp-=hurt
            print('Boss受到{}点攻击!'.format(hurt))
def main():
    hero = Hero('张三疯',100,1,'human')
    monster1 = Monster('虾兵')
    monster2 = Monster('蟹将',80,1)
    boss = Boss('龙王',100)
    monster_list = [monster1,monster2,boss]
    round = 1
    while hero.get_hp()>0 and len(monster_list)>0:
        monster=next_monster(monster_list)
        while monster.get_hp()>0:
            print('*'*20,'round {}'.format(round),'*'*20)
            hero.attack(monster)
            if monster.get_hp()>0:
                monster.attack(hero)
                if hero.get_hp()<=0:
                    break

            print(hero)
            print(monster)
            round+=1
        if monster.get_hp()<=0:
            monster_list.remove(monster)
            hero.upgrade()
            monster=next_monster(monster_list)

    if hero.get_hp()>0:
        print('You win,{}'.format(hero.get_name()))
    else:
        print('You lose')
def next_monster(monster_list:list):
    assert type(monster_list) is list
    if len(monster_list)>0:
        return monster_list[0]

if __name__=='__main__':
    main()


#运行结果
'''
******************** round 1 ********************
怪兽受到10点伤害
你受到4点攻击!
Name:张三疯	 HP:96	 Level:1
Name:虾兵	 HP:10	 Level:1
******************** round 2 ********************
怪兽受到6点伤害
你受到4点攻击!
Name:张三疯	 HP:92	 Level:1
Name:虾兵	 HP:4	 Level:1
******************** round 3 ********************
怪兽受到1点伤害
你受到0点攻击!
Name:张三疯	 HP:92	 Level:1
Name:虾兵	 HP:3	 Level:1
******************** round 4 ********************
怪兽受到4点伤害
Name:张三疯	 HP:92	 Level:1
Name:虾兵	 HP:-1	 Level:1
---------- 你升级到2
******************** round 5 ********************
怪兽受到13点伤害
你躲避了攻击
Name:张三疯	 HP:92	 Level:2
Name:蟹将	 HP:67	 Level:1
******************** round 6 ********************
怪兽受到14点伤害
你受到10点攻击!
Name:张三疯	 HP:82	 Level:2
Name:蟹将	 HP:53	 Level:1
******************** round 7 ********************
怪兽受到7点伤害
你受到8点攻击!
Name:张三疯	 HP:74	 Level:2
Name:蟹将	 HP:46	 Level:1
******************** round 8 ********************
怪兽受到19点伤害
你受到4点攻击!
Name:张三疯	 HP:70	 Level:2
Name:蟹将	 HP:27	 Level:1
******************** round 9 ********************
怪兽受到12点伤害
你躲避了攻击
Name:张三疯	 HP:70	 Level:2
Name:蟹将	 HP:15	 Level:1
******************** round 10 ********************
怪兽受到13点伤害
你受到4点攻击!
Name:张三疯	 HP:66	 Level:2
Name:蟹将	 HP:2	 Level:1
******************** round 11 ********************
怪兽受到1点伤害
你受到6点攻击!
Name:张三疯	 HP:60	 Level:2
Name:蟹将	 HP:1	 Level:1
******************** round 12 ********************
怪兽受到2点伤害
Name:张三疯	 HP:60	 Level:2
Name:蟹将	 HP:-1	 Level:1
---------- 你升级到3
******************** round 13 ********************
你躲避了攻击
Name:张三疯	 HP:60	 Level:3
Name:龙王	 HP:100	 Level:3
******************** round 14 ********************
你受到1点攻击!
Name:张三疯	 HP:59	 Level:3
Name:龙王	 HP:100	 Level:3
******************** round 15 ********************
你躲避了攻击
Name:张三疯	 HP:59	 Level:3
Name:龙王	 HP:100	 Level:3
******************** round 16 ********************
你躲避了攻击
Name:张三疯	 HP:59	 Level:3
Name:龙王	 HP:100	 Level:3
******************** round 17 ********************
Boss受到19点攻击!
你受到8点攻击!
Name:张三疯	 HP:51	 Level:3
Name:龙王	 HP:81	 Level:3
******************** round 18 ********************
Boss受到27点攻击!
你躲避了攻击
Name:张三疯	 HP:51	 Level:3
Name:龙王	 HP:54	 Level:3
******************** round 19 ********************
Boss受到22点攻击!
你躲避了攻击
Name:张三疯	 HP:51	 Level:3
Name:龙王	 HP:32	 Level:3
******************** round 20 ********************
Boss受到25点攻击!
你躲避了攻击
Name:张三疯	 HP:51	 Level:3
Name:龙王	 HP:7	 Level:3
******************** round 21 ********************
Boss受到18点攻击!
Name:张三疯	 HP:51	 Level:3
Name:龙王	 HP:-11	 Level:3
---------- 你升级到4
You win,张三疯

进程已结束,退出代码0
'''