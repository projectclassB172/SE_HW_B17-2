import random
class Hero():
    # bh为此级别的最大血量
    def __init__(self,name,level,bh,race):
        self.name = name
        self.level = level
        # ch为当前血量
        self.ch = bh
        self.bh = bh
        self.race=race
        if self.race=='人类':
            self.flexibility=0.4
        elif self.race=='精灵':
            self.flexibility=0.7
    def attack(self,Monster):
        m=random.randint(0,self.level*10)
        Monster.defense(m)
    def defense(self,m):
        df=random.random()
        if df>self.flexibility:
            self.ch-=m
            print("{}受到了{}点攻击,当前生命值为{}".format(self.name, m,self.ch))
        else:
            print("{}躲避掉了攻击,当前生命值为{}".format(self.name,self.ch))
class Monster():
    def __init__(self,name,level,bh):
        self.name = name
        self.level = level
        self.ch = bh
        self.bh = bh
        self.shield =0
        if self.level==3:
            self.shield=100
    def attack(self,Hero):
        m=random.randint(0,self.level*10)
        Hero.defense(m)
    def defense(self,m):
        self.shield -= m
        if self.shield <= 0:
            self.ch -= m
        if self.shield > 0:
            print("{}受到了{}点攻击,盾牌减少1，当前盾牌为{}".format(self.name, m, self.shield))
        else:
            print("{}受到了{}点攻击,当前生命值为{}".format(self.name, m,self.ch))
hero = Hero("蜘蛛侠",2, 50, '精灵')
monster1 = Monster("灭霸1号", 1, 50)
monster2 = Monster("灭霸2号", 2, 70)
monster3 = Monster("终极灭霸", 3, 100)
monster = [monster1, monster2, monster3]
round = 1
while True:
    if monster[0].ch > 0:
        print('-' * 21, "Round{}".format(round), '-' * 21)
        hero.attack(monster[0])
        if monster[0].ch > 0:
            monster[0].attack(hero)
        else:
            del monster[0]
        round += 1
    if len(monster) == 0:
        print("{}Win!".format(hero.name))
        break
    if hero.ch <= 0:
        print("{}Lose!".format(hero.name))
        break