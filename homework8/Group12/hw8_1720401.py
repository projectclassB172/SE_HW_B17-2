import random as s
class hero:
    def attack(user, beattacked):
        if beattacked.has_living():
            if user.lv == 1:
                user.att = s.randint(0, 10)
            elif user.lv == 2:
                user.att = s.randint(0, 20)
            elif user.lv == 3:
                user.att = s.randint(0, 30)
            print(user.att)
            beattacked.minus_blood(user.att)
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name+ '的护盾破碎！')
        print(beattacked.name + ' 的血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')
    def minus_blood(user, num):
        user.blood -= num
    def __init__(user, name, lv, race, maxblood ): 
        user.name = name
        user.lv = lv
        user.race = race
        user.maxblood = maxblood
        user.blood = maxblood
        if user.race == 'humanity':
            user.flexibility = 0.2
        else :
            user.flexibility = 0.4
        if user.lv == 1:
            user.att = s.randint(0, 10)
        elif user.lv == 2:
            user.att = s.randint(0, 20)
        elif user.lv == 3:
            user.att = s.randint(0, 30)

    def has_living(user):  
        if user.blood > 0:
            return True
        return False

class monster:
    def __init__(user, name, lv, maxblood ):
        user.name = name
        user.lv = lv # max_lv = 3
        user.maxblood = maxblood
        user.blood = maxblood
        user.blood = user.maxblood + 10
        if user.lv == 1:
            user.att = s.randint(0, 10)
        elif user.lv == 2:
            user.att = s.randint(0, 20)
        elif user.lv == 3:
            user.att = s.randint(0, 30)

    def attack(user, beattacked):
        if beattacked.has_living():
            if user.lv == 1:
                user.att = s.randint(0, 10)
            elif user.lv == 2:
                user.att = s.randint(0, 20)
            elif user.lv == 3:
                user.att = s.randint(0, 30)
            print(user.att)
            if beattacked.flexibility < s.random():
                beattacked.minus_blood(user.att)
            else:
                beattacked.minus_blood(0)
                print(beattacked.name + '躲避了攻击！')
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name + ' 血量:\n' + str(beattacked.blood) +
                  '护盾余值：' + str(beattacked.maxblood + 10 - beattacked.blood) + "\n")
        else:
            print(beattacked.name + ' 血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')

    def minus_blood(user, num):
        user.blood -= num

    def has_living(user):
        if user.blood > 0:
            return True
        return False
s1 = monster(name='【巴达兽】' , lv=1 , maxblood=20) 
s2 = monster(name='【天使兽】' , lv=2 , maxblood=30)
s3 = monster(name='【神圣天使兽】' , lv=3 , maxblood=50)
s4 = [s1,s2,s3]
h = hero(name='【高石岳】' , lv=3 , race='精灵',maxblood=100) 
print(h.name + '的初始血量:' + str(h.maxblood) + '(' + h.race + ')')
for m in s4:
    print(h.name + '的现有血量：' + str(h.blood))
    if m.lv == 3:
        print(m.name + '的等级达到了三级获得10点护盾')
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
        print('平局！')