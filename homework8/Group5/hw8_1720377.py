import random
class Attribute():
    def __init__(self, name, lv, maxblood):
        self.name = name
        self.lv = lv
        self.blood=maxblood
        self.maxblood=maxblood
class hero(Attribute):
    def __init__(self,name,lv,maxblood,race):
        super().__init__(name,lv,maxblood)
        self.race=race
        if self.race=='人类':
            self.flexibility = 0.3
        elif self.race == '精灵':
            self.flexibility =0.4
    def attack(self, monster):
        att = random.randint(0, self.lv*10)
        monster.defense(att)
    def defense(self,att):
        df=random.random()
        if df>self.flexibility:
            self.blood-=att
            if self.blood>0:
                print("{}受到了{}点攻击,当前第{}级,生命值为{}".format(self.name,att,self.lv,self.blood))
            else:
                print("{}受到了{}点攻击,当前生命值为0,失败".format(self.name, att))
        else:
            print("{}躲避掉了攻击,当前第{}级,生命值为{}".format(self.name,self.lv,self.blood))
    def uplevel(self):
        self.lv+=1
        self.maxblood = self.maxblood + 10
        self.blood=self.maxblood
        print("{}赢了怪兽升到{}级,当前生命值为{}".format(self.name, self.lv, self.blood))
class monster(Attribute):
    def __init__(self,name,lv,maxblood):
        super().__init__(name,lv,maxblood)
        self.shield=0
        if self.lv==3:
            self.shield=10
            print("怪兽升级为BOSS，拥有了10点护盾")
    def attack(self,hero):
        att=random.randint(0,self.lv*10)
        hero.defense(att)
    def  defense(self,att):
        self.shield-=att
        if self.shield<=0:
            self.blood-=att
        if self.shield>0:
                print("{}受到{}伤害,盾牌减少{}，当前护盾为{}".format(self.name, att, att,self.shield))
        else:
            if self.blood>0:
                print("{}受到{}伤害,当前生命值为{}".format(self.name,att,self.blood))
            else:
                print("{}受到了{}伤害,当前生命值为0,死亡".format(self.name, att))
def main():
    m1 = monster("【先锋卫】" , 1 , 20)
    m2 = monster("【黑矮星】", 2 , 30)
    m3 = monster("【灭霸】", 3 ,50)
    mo = [m1,m2,m3]
    h = hero("【钢铁侠】", 2,80,'人类')
    round=1
    while True:
        if mo[0].blood>0:
            print('~'*11,"Round{}".format(round),'~'*11)
            h.attack(mo[0])
            if mo[0].blood>0:
                mo[0].attack(h)
            else:
                h.uplevel()
                del mo[0]
            round += 1
        if len(mo) == 0:
            print("胜利属于{}!".format(h.name))
            break
        if h.blood<=0:
            print("{}失败了!".format(h.name))
            break
if __name__=='__main__':
    main()