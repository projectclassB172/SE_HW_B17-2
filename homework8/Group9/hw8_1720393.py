import random
class Person():
    def __init__(self,name,level,mhp):
        self.name=name
        self.level=level
        self.hp=mhp
        self.mhp=mhp
    # def intitle(self):
   #    self.name=input("请输入名字：")
class Hero(Person):
    def __init__(self,name,level,mhp,race):
        super().__init__(name,level,mhp)
        self.race=race
        if self.race=='人类':
            self.flexibility=0.4
        elif self.race=='精灵':
            self.flexibility=0.5

    # def latk(self):
    # self.atk=self.level*random.random()*10
    # def drace(self):
    #   input= input("请选择英雄的种类：1.人类  2.精灵")
    #   if input==1:
    #     print("你选择的是人类")
    #     self.flexibility=0.4
    #   else:
    #     print("你选择的是精灵")
    #     self.flexibility=0.5
    def attack(self,Monster):
        atk=random.random()*self.level*10
        Monster.defense(atk)
    def defense(self,atk):
        df=random.random()
        if df>self.flexibility:
            self.hp-=atk
            if self.hp>0:
                print("{}受到了{}点攻击,当前第{}级,生命值为{}".format(self.name,atk,self.level,self.hp))
                #print(self.name+"受到了"+atk+"点攻击,当前第"+self.level+"级,生命值为:"+self.hp)
            else:
                print("{}受到了{}点攻击,当前生命值为0,失败".format(self.name, atk))
        else:
            print("{}躲避掉了攻击,当前第{}级,生命值为{}".format(self.name,self.level,self.hp))
    def upLevel(self):
        self.level+=1
        self.mhp=self.mhp+50
        self.hp=self.mhp
        print("{}赢了怪兽升到{}级,当前生命值为{}".format(self.name,self.level,self.hp))
class Monster(Person):
    def __init__(self,name,level,mhp):
        super().__init__(name,level,mhp)
    def attack(self,Hero):
        atk=random.random()*self.level*10
        Hero.defense(atk)
    def defense(self,atk):
        self.hp-=atk
        if self.hp>0:
            print("{}受到了{}点攻击,当前生命值为{}".format(self.name,atk,self.hp))
        else:
            print("{}受到了{}点攻击,当前生命值为0,阵亡".format(self.name, atk))

class BigMonster(Person):
    def __init__(self,name,level,mhp):
        super().__init__(name,level,mhp)
        self.shield=15
    def attack(self, Hero):
        atk = random.random() * self.level * 10
        Hero.defense(atk)
    def defense(self,atk):
        self.shield-=1
        if self.shield<=0:
            self.hp-=atk
        if self.shield>0:
                print("{}受到了{}点攻击,盾牌减少1，当前盾牌为{}".format(self.name, atk, self.shield))
        else:
            if self.hp>0:
                print("{}受到了{}点攻击,当前生命值为{}".format(self.name,atk,self.hp))
            else:
                print("{}受到了{}点攻击,当前生命值为0,阵亡".format(self.name, atk))
def main():
    Hero.level=random.randint(1,3)
    hero=Hero("英雄1号",Hero.level,50,'精灵')
    m1=Monster("小小怪下士",1,30)
    m2= Monster("小小怪中士",1,30)
    m3=BigMonster("大大怪将军",3,75)
    list=[m1,m2,m3]
    round=1
    print("============================英雄打怪兽游戏开始！！！=============================")
    while True:
        if list[0].hp>0:
            print('-'*21,"第{}回合".format(round),'-'*21)
            hero.attack(list[0])
            if list[0].hp>0:
                list[0].attack(hero)
            else:
                if hero.level<3:
                    hero.upLevel()
                    del list[0]
                    round+=1
                else:
                    del list[0]
                    round += 1

        if len(list) == 0:
            print("怪兽全部死亡！！！游戏结束！！！！")
            print("{}Win!".format(hero.name))
            break
        if hero.hp<=0:
            print("{}Lose!".format(hero.name))
            break
if __name__=='__main__':
    main()