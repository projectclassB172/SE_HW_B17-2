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
s1 = monster(name='【一级怪兽】' , lv=1 , maxblood=20)  # 创建三只怪物
s2 = monster(name='【二级怪兽】' , lv=2 , maxblood=30)
s3 = monster(name='【三级怪兽】' , lv=3 , maxblood=50)
s4 = [s1,s2,s3]
h = hero(name='【皮皮虾】' , lv=3 , race='精灵',maxblood=100)  # 创建英雄
print(h.name + '的初始血量:' + str(h.maxblood) + '(' + h.race + ')')
for m in s4:
    print(h.name + '的现有血量：' + str(h.blood))
    if m.lv == 3:
        print(m.name + '的等级达到了三级他获得了10点护盾')
        print(m.name + '的初始血量:' + str(m.maxblood) + '  护盾：' + str(10))
    else:
        print(m.name + '的初始血量:' + str(m.maxblood))

    print('-------------------------------------')
    while m.has_living() and h.has_living():
        print(m.name + ' 对 ' + h.name + ' 造成伤害:')
        m.attack(h)
        print(h.name + ' 对 ' + m.name + ' 造成伤害:')
        h.attack(m)

    if m.has_living():
        print(m.name + ' 赢得了胜利!')
    elif h.has_living():
        print(h.name + ' 赢得了胜利!')
    else:
        print('平局！')