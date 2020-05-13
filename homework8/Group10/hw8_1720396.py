import random
class Property():
    def __init__(self,name,level,ml,mp):
        self.name=name
        self.level=level
        self.cl=ml
        self.ml=ml
        self.mp=mp
class Hero(Property):
    def __init__(self,name,level,ml,mp,race):
        super().__init__(name,level,ml,mp)
        self.race=race
        if self.race=='human':
            self.agillity=0.5
        elif self.race=='elf':
            self.agillity=0.7
    def attack(self,Monster):
        m=random.randint(0,self.level*10)
        Monster.defense(m)
    def huge_attack(self,Monster):
        if self.mp >= 50:
            self.mp -= 50
            injury = Monster.ml * 1 // 2
            if injury >= 50:
                injury = injury
            else:
                injury = 50
            Monster.ml -= injury
            return True
        else:
            self.attack(Monster)
            return False
    def defense(self,m):
        df=random.random()
        if df>self.agillity:
            self.cl-=m
            if self.cl>0:
                print("{}被攻击了{}点伤害,当前第{}级,生命值为{},魔法值{}".format(self.name,m,self.level,self.cl,self.mp))
            else:
                print("{}被攻击了{}点伤害,当前生命值为0,失败".format(self.name, m))
        else:
            print("{}躲避掉了攻击,当前第{}级,生命值为{},魔法值{}".format(self.name,self.level,self.cl,self.mp))
    def upgrade(self):
        self.level+=1
        self.ml=self.ml+10
        self.cl=self.ml
        self.mp=self.mp+20
        print("{}赢了怪兽升到{}级,当前生命值为{},魔法值{}".format(self.name,self.level,self.cl,self.mp))
class Monster(Property):
    def __init__(self,name,level,ml,mp):
        super().__init__(name,level,ml,mp)
    def attack(self,Hero):
        m=random.randint(0,self.level*10)
        Hero.defense(m)
    def defense(self,m):
        self.cl-=m
        if self.cl>0:
            print("{}被攻击了{}点伤害,当前生命值为{}".format(self.name,m,self.cl,self.mp))
        else:
            print("{}被攻击了{}点伤害,当前生命值为0,阵亡".format(self.name, m))
# 大怪兽
class Bigms(Property):
    def __init__(self,name,level,ml,mp):
        super().__init__(name,level,ml,mp)
        # shield为盾牌
        self.shield=5
    def attack(self, Hero):
        m = random.randint(0,self.level*10)
        Hero.defense(m)
    def defense(self,m):
        self.shield-=1
        if self.shield<=0:
            self.cl-=m
        if self.shield>0:
                print("{}被攻击了{}点伤害,盾牌减少1，当前盾牌为{}".format(self.name, m, self.shield))
        else:
            if self.cl>0:
                print("{}被攻击了{}点伤害,当前生命值为{}".format(self.name,m,self.cl,self.mp))
            else:
                print("{}被攻击了{}点伤害,当前生命值为0,阵亡".format(self.name, m))

def main():
    hero_level=random.randint(1,3)
    hero=Hero("圣斗士",hero_level,50,60,'elf')
    m1=Monster("初级怪兽",1,30,30)
    m2= Monster("中级怪兽",2,50,50)
    bm=Bigms("究极怪兽",3,80,80)
    gs=[m1,m2,bm]
    round=1

    while True:
        if gs[0].cl>0:
            print('-'*21,"Round{}".format(round),'-'*21)
            hero.attack(gs[0])
            if gs[0].cl>0:
                gs[0].attack(hero)
            else:
                hero.upgrade()
                del gs[0]
            round+=1
        if len(gs) == 0:
            print("{}胜利!".format(hero.name))
            break
        if hero.cl<=0:
            print("{}失败!".format(hero.name))
            break
if __name__=='__main__':
    main()

'''
初级怪兽被攻击了4点伤害,当前生命值为26
圣斗士躲避掉了攻击,当前第3级,生命值为50,魔法值60
--------------------- Round2 ---------------------
初级怪兽被攻击了30点伤害,当前生命值为0,阵亡
圣斗士赢了怪兽升到4级,当前生命值为60,魔法值80
--------------------- Round3 ---------------------
中级怪兽被攻击了34点伤害,当前生命值为16
圣斗士被攻击了13点伤害,当前第4级,生命值为47,魔法值80
--------------------- Round4 ---------------------
中级怪兽被攻击了35点伤害,当前生命值为0,阵亡
圣斗士赢了怪兽升到5级,当前生命值为70,魔法值100
--------------------- Round5 ---------------------
究极怪兽被攻击了11点伤害,盾牌减少1，当前盾牌为4
圣斗士躲避掉了攻击,当前第5级,生命值为70,魔法值100
--------------------- Round6 ---------------------
究极怪兽被攻击了7点伤害,盾牌减少1，当前盾牌为3
圣斗士躲避掉了攻击,当前第5级,生命值为70,魔法值100
--------------------- Round7 ---------------------
究极怪兽被攻击了49点伤害,盾牌减少1，当前盾牌为2
圣斗士躲避掉了攻击,当前第5级,生命值为70,魔法值100
--------------------- Round8 ---------------------
究极怪兽被攻击了20点伤害,盾牌减少1，当前盾牌为1
圣斗士躲避掉了攻击,当前第5级,生命值为70,魔法值100
--------------------- Round9 ---------------------
究极怪兽被攻击了36点伤害,当前生命值为44
圣斗士被攻击了13点伤害,当前第5级,生命值为57,魔法值100
--------------------- Round10 ---------------------
究极怪兽被攻击了4点伤害,当前生命值为40
圣斗士被攻击了9点伤害,当前第5级,生命值为48,魔法值100
--------------------- Round11 ---------------------
究极怪兽被攻击了37点伤害,当前生命值为3
圣斗士躲避掉了攻击,当前第5级,生命值为48,魔法值100
--------------------- Round12 ---------------------
究极怪兽被攻击了18点伤害,当前生命值为0,阵亡
圣斗士赢了怪兽升到6级,当前生命值为80,魔法值120
圣斗士胜利!
'''