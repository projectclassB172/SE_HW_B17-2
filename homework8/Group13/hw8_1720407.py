import random
class Property():
    def __init__(self,name,level,ml):
        #cl表示当前生命值，ml表示最大生命值
        self.name=name
        self.level=level
        self.cl=ml
        self.ml=ml
class Hero(Property):
    def __init__(self,name,level,ml,race):
        super().__init__(name,level,ml)
        self.race=race
        if self.race=='human':
            self.agillity=0.4
        elif self.race=='elf':
            self.agillity=0.7
    def attack(self,Monster):
        m=random.randint(0,self.level*10)
        Monster.defense(m)
    def defense(self,m):
        df=random.random()
        if df>self.agillity:
            self.cl-=m
            if self.cl>0:
                print("{}受到了{}点攻击,当前第{}级,生命值为{}".format(self.name,m,self.level,self.cl))
            else:
                print("{}受到了{}点攻击,当前生命值为0,失败".format(self.name, m))
        else:
            print("{}躲避掉了攻击,当前第{}级,生命值为{}".format(self.name,self.level,self.cl))
    def upgrade(self):
        self.level+=1
        self.ml=self.ml+10
        self.cl=self.ml
        print("{}赢了怪兽升到{}级,当前生命值为{}".format(self.name,self.level,self.cl))
class Monster(Property):
    def __init__(self,name,level,ml):
        super().__init__(name,level,ml)
    def attack(self,Hero):
        m=random.randint(0,self.level*10)
        Hero.defense(m)
    def defense(self,m):
        self.cl-=m
        if self.cl>0:
            print("{}受到了{}点攻击,当前生命值为{}".format(self.name,m,self.cl))
        else:
            print("{}受到了{}点攻击,当前生命值为0,阵亡".format(self.name, m))
# 大怪兽
class Bigms(Property):
    def __init__(self,name,level,ml):
        super().__init__(name,level,ml)
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
                print("{}受到了{}点攻击,盾牌减少1，当前盾牌为{}".format(self.name, m, self.shield))
        else:
            if self.cl>0:
                print("{}受到了{}点攻击,当前生命值为{}".format(self.name,m,self.cl))
            else:
                print("{}受到了{}点攻击,当前生命值为0,阵亡".format(self.name, m))
def main():
    hero_level=random.randint(1,3)
    hero=Hero("奥特曼",hero_level,30,'elf')
    m1=Monster("怪兽1号",1,30)
    m2= Monster("怪兽2号",2,40)
    bm=Bigms("终极怪兽",3,70)
    list=[m1,m2,bm]
    round=1
    while True:
        if list[0].cl>0:
            print('-'*21,"Round{}".format(round),'-'*21)
            hero.attack(list[0])
            if list[0].cl>0:
                list[0].attack(hero)
            else:
                hero.upgrade()
                del list[0]
            round+=1
        if len(list) == 0:
            print("{}Win!".format(hero.name))
            break
        if hero.cl<=0:
            print("{}Lose!".format(hero.name))
            break
if __name__=='__main__':
    main()

# 运行结果
# --------------------- Round1 ---------------------
# 怪兽1号受到了4点攻击,当前生命值为26
# 奥特曼受到了0点攻击,当前第1级,生命值为30
# --------------------- Round2 ---------------------
# 怪兽1号受到了0点攻击,当前生命值为26
# 奥特曼躲避掉了攻击,当前第1级,生命值为30
# --------------------- Round3 ---------------------
# 怪兽1号受到了0点攻击,当前生命值为26
# 奥特曼躲避掉了攻击,当前第1级,生命值为30
# --------------------- Round4 ---------------------
# 怪兽1号受到了10点攻击,当前生命值为16
# 奥特曼受到了6点攻击,当前第1级,生命值为24
# --------------------- Round5 ---------------------
# 怪兽1号受到了8点攻击,当前生命值为8
# 奥特曼躲避掉了攻击,当前第1级,生命值为24
# --------------------- Round6 ---------------------
# 怪兽1号受到了0点攻击,当前生命值为8
# 奥特曼受到了7点攻击,当前第1级,生命值为17
# --------------------- Round7 ---------------------
# 怪兽1号受到了2点攻击,当前生命值为6
# 奥特曼受到了6点攻击,当前第1级,生命值为11
# --------------------- Round8 ---------------------
# 怪兽1号受到了0点攻击,当前生命值为6
# 奥特曼受到了1点攻击,当前第1级,生命值为10
# --------------------- Round9 ---------------------
# 怪兽1号受到了8点攻击,当前生命值为0,阵亡
# 奥特曼赢了怪兽升到2级,当前生命值为40
# --------------------- Round10 ---------------------
# 怪兽2号受到了15点攻击,当前生命值为25
# 奥特曼躲避掉了攻击,当前第2级,生命值为40
# --------------------- Round11 ---------------------
# 怪兽2号受到了0点攻击,当前生命值为25
# 奥特曼躲避掉了攻击,当前第2级,生命值为40
# --------------------- Round12 ---------------------
# 怪兽2号受到了20点攻击,当前生命值为5
# 奥特曼躲避掉了攻击,当前第2级,生命值为40
# --------------------- Round13 ---------------------
# 怪兽2号受到了12点攻击,当前生命值为0,阵亡
# 奥特曼赢了怪兽升到3级,当前生命值为50
# --------------------- Round14 ---------------------
# 终极怪兽受到了3点攻击,盾牌减少1，当前盾牌为4
# 奥特曼受到了8点攻击,当前第3级,生命值为42
# --------------------- Round15 ---------------------
# 终极怪兽受到了26点攻击,盾牌减少1，当前盾牌为3
# 奥特曼躲避掉了攻击,当前第3级,生命值为42
# --------------------- Round16 ---------------------
# 终极怪兽受到了4点攻击,盾牌减少1，当前盾牌为2
# 奥特曼躲避掉了攻击,当前第3级,生命值为42
# --------------------- Round17 ---------------------
# 终极怪兽受到了17点攻击,盾牌减少1，当前盾牌为1
# 奥特曼受到了5点攻击,当前第3级,生命值为37
# --------------------- Round18 ---------------------
# 终极怪兽受到了26点攻击,当前生命值为44
# 奥特曼躲避掉了攻击,当前第3级,生命值为37
# --------------------- Round19 ---------------------
# 终极怪兽受到了22点攻击,当前生命值为22
# 奥特曼躲避掉了攻击,当前第3级,生命值为37
# --------------------- Round20 ---------------------
# 终极怪兽受到了16点攻击,当前生命值为6
# 奥特曼受到了18点攻击,当前第3级,生命值为19
# --------------------- Round21 ---------------------
# 终极怪兽受到了3点攻击,当前生命值为3
# 奥特曼躲避掉了攻击,当前第3级,生命值为19
# --------------------- Round22 ---------------------
# 终极怪兽受到了24点攻击,当前生命值为0,阵亡
# 奥特曼赢了怪兽升到4级,当前生命值为60
# 奥特曼Win!