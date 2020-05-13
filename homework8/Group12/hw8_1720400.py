import random  as  rd
class hero:
    def __init__(self, name, lv, race, maxblood ):
        self.name = name
        self.lv = lv # 英雄级别
        self.race = race
        self.maxblood = maxblood
        self.blood = maxblood
        if self.race == 'humanity':
            self.flexibility = 0.3
        else :
            self.flexibility = 0.4
        if self.lv == 1:
            self.att = rd.randint(0, 10)
        elif self.lv == 2:
            self.att = rd.randint(0, 20)
        elif self.lv == 3:
            self.att = rd.randint(0, 30)

    def attack(self, attacked):
        if attacked.has_living():
            if self.lv == 1:
                self.att = rd.randint(0, 10)
            elif self.lv == 2:
                self.att = rd.randint(0, 20)
            elif self.lv == 3:
                self.att = rd.randint(0, 30)
            print(self.att)
            attacked.minus_blood(self.att)
        if attacked.blood <= (attacked.maxblood + 10) & attacked.lv == 3:
            print(attacked.name+ '护盾被打消失')
        print(attacked.name + ' 被攻击后剩余血量:\n' + str(attacked.blood) + "\n")
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
        self.lv = lv # 小兵的级别
        self.maxblood = maxblood
        self.blood = maxblood
        self.blood = self.maxblood + 10
        if self.lv == 1:
            self.att = rd.randint(0, 10)
        elif self.lv == 2:
            self.att = rd.randint(0, 20)
        elif self.lv == 3:
            self.att = rd.randint(0, 30)

    def attack(self, attacked):
        if attacked.has_living():
            if self.lv == 1:
                self.att = rd.randint(0, 10)
            elif self.lv == 2:
                self.att = rd.randint(0, 20)
            elif self.lv == 3:
                self.att = rd.randint(0, 30)
                print(self.att)
            if attacked.flexibility < rd.random():
                attacked.minus_blood(self.att)
            else:
               attacked.minus_blood(0)
                print('但是' + attacked.name + '巧妙躲过了攻击！')
        if attacked.blood <= (attacked.maxblood + 10) & attacked.lv == 3:
            print(attacked.name + ' 被攻击后剩余血量:\n' + str(attacked.blood) +
                  '剩余护盾：' + str(attacked.maxblood + 10 - attacked.blood) + "\n")
        else:
            print(attacked.name + '被攻击后剩余血量:\n' + str(attacked.blood) + "\n")
        print('---------------------')

    def minus_blood(self, num):
        self.blood -= num

    def has_living(self): 
        if self.blood > 0:
            return True
        return False

#小兵的种类以及血量的设置
m1 = monster(name='【小兵】' , lv=1 , maxblood=15) 
m2 = monster(name='【炮车】' , lv=2 , maxblood=30)  
m3 = monster(name='【超级兵】' , lv=3 , maxblood=100) 
mo = [m1,m2,m3]
#英雄的血量和护盾设置
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
