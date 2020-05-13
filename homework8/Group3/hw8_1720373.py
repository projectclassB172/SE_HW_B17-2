'''面向对象编程练习
编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose'''
import random as s
class hero:#定义英雄类
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
            print(beattacked.name+ '护盾已失效！')
        print(beattacked.name + ' 的血量:\n' + str(beattacked.blood) + "\n")
        print('---------------------')
    def minus_blood(user, num):
        user.blood -= num
    def __init__(user, name, lv, race, maxblood ): #名字，等级（max=3），种族，血量
        user.name = name
        user.lv = lv
        user.race = race
        user.maxblood = maxblood
        user.blood = maxblood
        if user.race == 'humanity':
            user.flexibility = 0.2#灵活度
        else :
            user.flexibility = 0.4
        if user.lv == 1:
            user.att = s.randint(0, 10)
        elif user.lv == 2:
            user.att = s.randint(0, 20)
        elif user.lv == 3:
            user.att = s.randint(0, 30)

    def has_living(user):  # 判断是否还有血量
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
                print('但是' + beattacked.name + '闪避了攻击！')
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
'''5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。'''
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