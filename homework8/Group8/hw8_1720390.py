import random

class Person(object):#创建英雄和怪兽的属性值，方便你后期调用
    def __init__(self, name, hp, level):
        self.name = name #名字
        self. max = hp #最大血量
        self._hp = hp #当前血量
        self.level = level #当前等级

    def get_name(self):

        return self .name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return 'Name: {}\t HP: {}\t Level:{}'.format(self.name, self._hp, self.level)

class Hero(Person):#创建英雄类继承person类
    def __init__(self, name, hp=50, level=1, race='human'):#英雄类属性以及初始值，在函数中可以重写值该值
        super().__init__(name, hp, level)#继承父类
        self.race = race#创建一个新属性，种族
        if self.race == 'human':#判断不同种族的敏捷
            self.agile = 0.4
        elif self.race == 'god':
            self.agile = 0.7

    def attack(self,Monster): #创建英雄的攻击类
        hurt = random.randint(0, self.level*10) #攻击伤害为0到等级*10之间的随机值
        Monster.defense(hurt) #调用moster中的defense方法，此方法决定英雄对怪兽攻击时怪兽的血量变化情况

    def defense(self, hurt):#英雄的防御
        luck = random.random() #设置一个幸运值，意在有闪避怪兽攻击的可能，为随机数
        if luck > self.agile:
            self._hp -= hurt #收到怪兽攻击血量减少
            print('你受到了{}伤害'.format(hurt))#输出受到的伤害用format确定{}中的值
        else:
            print('你躲避了攻击')

    def upgrade(self):#英雄升级的方法
        self.level += 1#等级+1
        self.max = self.max+10#血量上限+10
        self._hp = self.max#恢复血量至上限
        print('你升到了{}级'.format(self.level))

class Monster(Person):#怪兽类继承person
    def __init__(self , name , hp=20, level=1):
        super().__init__(name,hp, level)#继承父类的属性值
    def attack(self,Hero):#怪兽攻击英雄的方法
        hurt = random.randint(0, self.level*10)#攻击伤害为0到等级*10之间的随机值
        Hero.defense(hurt)#调用Hero中的defense方法，此方法决定怪兽对英雄攻击时怪兽的血量变化情况
    def defense(self,hurt):
        self._hp -= hurt#怪兽的血量变化
        print('怪兽受到{}伤害'.format(hurt))

# boss级别的怪兽拥有护盾和更高的血量，具体方法同moster类
class Boss(Person):
    def __init__(self,name,level,hp=70):
        super().__init__(name,level,hp)
        self.shield=20
    def attack(self, Hero):
        hurt = random.randint(0, self.level*10)
        Hero.defense(hurt)
    def defense(self,hurt):
        self.shield-=hurt#先扣护盾值
        if self.shield<=0:
            self._hp -= hurt
            print('怪兽受到{}伤害'.format(hurt))
def main():
    #赋值注意要与之前的变量位置一一对应
    hero = Hero("钢铁侠", 50, 1, 'human')#调用hero类并且赋值
    monster1 = Monster("海拉", 30, 1)#调用Monster类并且赋值
    monster2 = Monster("小小兵", 30, 1)#调用Monster类并且赋值
    boss = Boss("灭霸", 50, 2)
    monster_list = [monster1, monster2, boss]#创建一个怪兽列表
    round=1#回合数
    while hero.get_hp() > 0 and len(monster_list) > 0:#判断当hero血量大于0且怪兽数量不为空游戏继续否则结束
        monster = next_monster(monster_list) #调用next_monster方法可以在怪兽死后加入下一个怪兽
        while monster.get_hp() > 0:#判断怪兽血量是否大于1
            print('*' * 18, "Round{}".format(round), '*' * 18)
            hero.attack(monster)#英雄攻击怪兽
            if monster.get_hp() > 0:#如果怪兽血量大于英雄则攻击英雄
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break
            print(hero)
            print(monster)
            round += 1#回合数加一
        if monster.get_hp() <= 0:#如果怪兽死亡
            monster_list.remove(monster)#移除怪兽
            print('怪兽{}死亡'.format(monster.get_name()))
            hero.upgrade()#调用uprade函数英雄升级
            monster = next_monster(monster_list)

    if hero.get_hp() >0:#最后英雄没死输出胜利
        print('win,{}'.format(hero.get_name()))
    else:
        print('you lose')

def next_monster(monster_list:list):
    assert type(monster_list) is list
    if len(monster_list)>0:
        return monster_list[0]

if __name__=='__main__':
    main()#运行main方法


    # 运行结果
# ****************** Round1 ******************
# 怪兽受到5伤害
# 你受到了4伤害
# Name: 钢铁侠	 HP: 46	 Level:1
# Name: 海拉	 HP: 25	 Level:1
# ****************** Round2 ******************
# 怪兽受到1伤害
# 你受到了8伤害
# Name: 钢铁侠	 HP: 38	 Level:1
# Name: 海拉	 HP: 24	 Level:1
# ****************** Round3 ******************
# 怪兽受到4伤害
# 你受到了10伤害
# Name: 钢铁侠	 HP: 28	 Level:1
# Name: 海拉	 HP: 20	 Level:1
# ****************** Round4 ******************
# 怪兽受到7伤害
# 你躲避了攻击
# Name: 钢铁侠	 HP: 28	 Level:1
# Name: 海拉	 HP: 13	 Level:1
# ****************** Round5 ******************
# 怪兽受到5伤害
# 你躲避了攻击
# Name: 钢铁侠	 HP: 28	 Level:1
# Name: 海拉	 HP: 8	 Level:1
# ****************** Round6 ******************
# 怪兽受到9伤害
# Name: 钢铁侠	 HP: 28	 Level:1
# Name: 海拉	 HP: -1	 Level:1
# 怪兽海拉死亡
# 你升到了2级
# ****************** Round7 ******************
# 怪兽受到14伤害
# 你受到了8伤害
# Name: 钢铁侠	 HP: 52	 Level:2
# Name: 小小兵	 HP: 16	 Level:1
# ****************** Round8 ******************
# 怪兽受到13伤害
# 你受到了1伤害
# Name: 钢铁侠	 HP: 51	 Level:2
# Name: 小小兵	 HP: 3	 Level:1
# ****************** Round9 ******************
# 怪兽受到11伤害
# Name: 钢铁侠	 HP: 51	 Level:2
# Name: 小小兵	 HP: -8	 Level:1
# 怪兽小小兵死亡
# 你升到了3级
# ****************** Round10 ******************
# 怪兽受到21伤害
# 你躲避了攻击
# Name: 钢铁侠	 HP: 70	 Level:3
# Name: 灭霸	 HP: 29	 Level:2
# ****************** Round11 ******************
# 怪兽受到18伤害
# 你躲避了攻击
# Name: 钢铁侠	 HP: 70	 Level:3
# Name: 灭霸	 HP: 11	 Level:2
# ****************** Round12 ******************
# 怪兽受到25伤害
# Name: 钢铁侠	 HP: 70	 Level:3
# Name: 灭霸	 HP: -14	 Level:2
# 怪兽灭霸死亡
# 你升到了4级
# win,钢铁侠
#
# Process finished with exit code 0
