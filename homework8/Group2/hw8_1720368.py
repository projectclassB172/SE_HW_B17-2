import random  as  rn
class hero:
    def __init__(self, name, lv, race, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.race = race
        self.maxblood = maxblood
        self.blood = maxblood
        if self.race == 'humanity':
            self.flexibility = 0.2
        else :
            self.flexibility = 0.4
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)

    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            beattacked.minus_blood(self.att)
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name+ '的护盾被击碎了')
        print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')
        # 输出剩余血量

    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # 判断是否还有血量
        if self.blood > 0:
            return True
        return False

class monster:
    def __init__(self, name, lv, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.maxblood = maxblood
        self.blood = maxblood
        self.blood = self.maxblood + 10
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)

    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            if beattacked.flexibility < rn.random():
                beattacked.minus_blood(self.att)
            else:
                beattacked.minus_blood(0)
                print('但是' + beattacked.name + '闪避了攻击！')
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) +
                  '剩余护盾：' + str(beattacked.maxblood + 10 - beattacked.blood) + "\n")
        else:
            print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')
        # 输出剩余血量

    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # 判断是否还有血量
        if self.blood > 0:
            return True
        return False
#############################################

m1 = monster(name='【小小怪】' , lv=1 , maxblood=20)  # 创建怪物1
m2 = monster(name='【小怪】' , lv=2 , maxblood=30)  # 创建怪物2
m3 = monster(name='【BOSS】' , lv=3 , maxblood=50)  # 创建怪物3
mo = [m1,m2,m3]
h = hero(name='【天选之子】' , lv=3 , race='精灵',maxblood=100)  # 创建英雄
print(h.name + '的初始血量:' + str(h.maxblood) + '他是一个' + h.race)
for m in mo:
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
        print(m.name + ' 胜利!')
    elif h.has_living():
        print(h.name + ' 胜利~!')
    else:
        print(m.name + ' 和 ' + h.name + '均阵亡!')