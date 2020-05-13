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
        return 'Name:{}\tHP:{}\tLevel:{}\t'.format(self.name, self.hp, self.level)

class Hero(Person):
    def __init__(self, name, hp=20, level=1, race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'elves':
            self.fexibility = 0.8
        elif self.race == 'human':
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
            print('Boss用盾牌抵御了{}伤害'.format(m))
        else:
            self.hp -= m
            print('Boss受到{}点伤害'.format(m))

if __name__=='__main__':
    hero = Hero('英雄', 20, 1, 'human')
    monster1 = Monster('渣渣1')
    monster2 = Monster('渣渣2', 60, 2)
    boss = Boss('Boss', 100)
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


'''
Run Module

--------------------round 1--------------------

渣渣1受到2点伤害
英雄受到1点伤害
Name:英雄	HP:19	Level:1	
Name:渣渣1	HP:18	Level:1	

渣渣1受到7点伤害
英雄受到4点伤害
Name:英雄	HP:15	Level:1	
Name:渣渣1	HP:11	Level:1	

渣渣1受到10点伤害
英雄受到5点伤害
Name:英雄	HP:10	Level:1	
Name:渣渣1	HP:1	Level:1	

渣渣1受到9点伤害
渣渣1败
英雄升到2级,血槽加到60

--------------------round 2--------------------

渣渣2受到19点伤害
英雄受到13点伤害
Name:英雄	HP:47	Level:2	
Name:渣渣2	HP:41	Level:2	

渣渣2受到3点伤害
英雄躲掉了攻击
Name:英雄	HP:47	Level:2	
Name:渣渣2	HP:38	Level:2	

渣渣2受到4点伤害
英雄受到9点伤害
Name:英雄	HP:38	Level:2	
Name:渣渣2	HP:34	Level:2	

渣渣2受到18点伤害
英雄受到4点伤害
Name:英雄	HP:34	Level:2	
Name:渣渣2	HP:16	Level:2	

渣渣2受到2点伤害
英雄躲掉了攻击
Name:英雄	HP:34	Level:2	
Name:渣渣2	HP:14	Level:2	

渣渣2受到7点伤害
英雄受到20点伤害
Name:英雄	HP:14	Level:2	
Name:渣渣2	HP:7	Level:2	

渣渣2受到11点伤害
渣渣2败
英雄升到3级,血槽加到100

--------------------round 3--------------------

Boss用盾牌抵御了28伤害
英雄躲掉了攻击
Name:英雄	HP:100	Level:3	
Name:Boss	HP:100	Level:3	

Boss用盾牌抵御了28伤害
英雄受到0点伤害
Name:英雄	HP:100	Level:3	
Name:Boss	HP:100	Level:3	

Boss受到15点伤害
英雄受到16点伤害
Name:英雄	HP:84	Level:3	
Name:Boss	HP:85	Level:3	

Boss受到26点伤害
英雄躲掉了攻击
Name:英雄	HP:84	Level:3	
Name:Boss	HP:59	Level:3	

Boss受到22点伤害
英雄受到9点伤害
Name:英雄	HP:75	Level:3	
Name:Boss	HP:37	Level:3	

Boss受到24点伤害
英雄躲掉了攻击
Name:英雄	HP:75	Level:3	
Name:Boss	HP:13	Level:3	

Boss受到17点伤害
Boss败
英雄胜
'''
        
'''
Run Module

--------------------round 1--------------------

渣渣1受到8点伤害
英雄受到7点伤害
Name:英雄	HP:13	Level:1	
Name:渣渣1	HP:12	Level:1	

渣渣1受到6点伤害
英雄躲掉了攻击
Name:英雄	HP:13	Level:1	
Name:渣渣1	HP:6	Level:1	

渣渣1受到8点伤害
渣渣1败
英雄升到2级,血槽加到60

--------------------round 2--------------------

渣渣2受到12点伤害
英雄受到13点伤害
Name:英雄	HP:47	Level:2	
Name:渣渣2	HP:48	Level:2	

渣渣2受到13点伤害
英雄受到16点伤害
Name:英雄	HP:31	Level:2	
Name:渣渣2	HP:35	Level:2	

渣渣2受到11点伤害
英雄受到13点伤害
Name:英雄	HP:18	Level:2	
Name:渣渣2	HP:24	Level:2	

渣渣2受到7点伤害
英雄受到20点伤害
Name:英雄	HP:-2	Level:2	
Name:渣渣2	HP:17	Level:2	

英雄败
'''        

        
        
        
    
