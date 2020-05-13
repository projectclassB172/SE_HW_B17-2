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
            print(beattacked.name+ '护盾消失')
        print(beattacked.name + ' 剩余血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')

    def minus_blood(self, num):
        self.blood -= num
    def has_living(self): 
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

    def minus_blood(self, num):
        self.blood -= num

    def has_living(self): 
        if self.blood > 0:
            return True
        return False

m1 = monster(name='【小兵】' , lv=1 , maxblood=20) 
m2 = monster(name='【炮车】' , lv=2 , maxblood=30)  
m3 = monster(name='【超级兵】' , lv=3 , maxblood=50) 
mo = [m1,m2,m3]
h = hero(name='【孙膑】' , lv=3 , race='精灵',maxblood=100)  
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
        print(h.name + ' 胜利!')
    else:
        print(m.name + ' 和 ' + h.name + '均阵亡!')