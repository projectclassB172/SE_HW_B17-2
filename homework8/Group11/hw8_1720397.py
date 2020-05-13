from random import randint  # 导入randint函数


# 父类——放置英雄与怪兽的共同属性
class sameAttribution:
    def __init__(self, name, grade, currentLifeValue, currentGradeMaxLifeValue):
        self.name = name  # 名字
        self.grade = grade  # 等级
        self.currentLifeValue = currentLifeValue  # 当前生命值
        self.currentGradeMaxLifeValue = currentGradeMaxLifeValue  # 当前等级的最大生命值

    def currentLifeValue(self):
        return self.currentLifeValue


class Hero(sameAttribution):
    def __init__(self, race, mobility, experienceValue):
        self.race = race  # 种族
        self.mobility = mobility  # 灵活性
        self.experienceValue = experienceValue  # 经验值(格外添加的累计经验值升等级)

    def skill(self):
        return self.skill  # 伤害值

    # 设置攻击方法，其实就是定义动作属性, subject指的是攻击对象
    # 经验值满一定的值后升一等级，3等级为满级
    def attack(self, subject):
        if self.grade == 1:
            self.skill = randint(0, 10)
            self.experienceValue += self.skill
            print('英雄的经验值：' + str(self.experienceValue))
            subject.currentLifeValue -= self.skill
            if self.experienceValue >= 40:
                self.grade += 1
        elif self.grade == 2:
            self.skill = randint(0, 20)
            self.experienceValue += self.skill
            print('英雄的经验值：' + str(self.experienceValue))
            subject.currentLifeValue -= self.skill
            if self.experienceValue >= 80:
                self.grade += 1
        elif self.grade == 3:
            self.skill = randint(0, 30)
            self.experienceValue += self.skill
            print('英雄的经验值：' + str(self.experienceValue))
            subject.currentLifeValue -= self.skill
        sc = (self.skill, subject.currentLifeValue)
        return sc

    # 防御方法
    def defence(self):
        if SmallLeviathan.currentLifeValue != 0:
            hurt = SmallLeviathan.skill
        else:
            hurt = BigLeviathan.skill
        randomValue = randint(0, 10)
        if self.race == '人类':
            if randomValue <= self.mobility:
                if Hero.currentLifeValue > 100:
                    Hero.currentLifeValue = Hero.currentLifeValue
                else:
                    Hero.currentLifeValue = Hero.currentLifeValue + hurt
                    if Hero.currentLifeValue > 100:
                        Hero.currentLifeValue = 100
            else:
                Hero.currentLifeValue = Hero.currentLifeValue
        elif self.race == '精灵':
            if randomValue <= self.mobility:
                if Hero.currentLifeValue > 100:
                    Hero.currentLifeValue = Hero.currentLifeValue
                else:
                    Hero.currentLifeValue = Hero.currentLifeValue + hurt
                    if Hero.currentLifeValue > 100:
                        Hero.currentLifeValue = 100
            else:
                Hero.currentLifeValue = Hero.currentLifeValue
        return self.currentLifeValue

    # 返回每次调用之后的剩余参数
    def __str__(self):
        return '当前生命值：%d\n' % self.currentLifeValue + \
               '等级：%d\n' % self.grade


class SmallLeviathan(sameAttribution):
    def skill(self):
        return self.skill  # 伤害值

    def attack(self, subject):  # 攻击方法
        if self.grade == 1:
            self.skill = randint(0, 15)
            subject.currentLifeValue -= self.skill
        elif self.grade == 2:
            self.skill = randint(0, 25)
            subject.currentLifeValue -= self.skill
        sc = (self.skill, subject.currentLifeValue)
        return sc

    def __str__(self):  # 返回每次调用之后的剩余参数
        return '当前生命值：%d' % self.currentLifeValue


class BigLeviathan(sameAttribution):
    def __init__(self, shield):
        self.shield = shield  # 盾牌

    def skill(self):
        return self.skill  # 伤害值

    def attack(self, subject):  # 攻击方法
        if self.grade == 3:
            self.skill = randint(0, 40)
            subject.currentLifeValue -= self.skill
        sc = (self.skill, subject.currentLifeValue)
        return sc

    def defence(self):  # 防御方法
        hurt = Hero.skill  # 获取到英雄的攻击值
        if self.grade == 3:
            if self.shield >= 0:
                print('大怪兽的盾牌保护力还剩：' + str(self.shield))
            if (hurt <= self.shield) | (self.shield > 0):
                BigLeviathan.currentLifeValue += hurt
                self.shield -= hurt
            elif self.shield <= 0:
                BigLeviathan.currentLifeValue = BigLeviathan.currentLifeValue
        return self.currentLifeValue

    def __str__(self):  # 返回每次调用之后的剩余参数
        return '当前生命值：%d' % self.currentLifeValue


# 最终调用所有的类对象的属性进行动作，最终的命令执行以上的函数及各种方法
def main():
    h = sameAttribution('迪迦奥特曼', 2, 100, 100)
    h1 = Hero('精灵', 4, 0)
    l1 = SmallLeviathan('怪兽1', 1, 30, 30)
    l2 = SmallLeviathan('怪兽2', 2, 40, 40)
    l3 = sameAttribution('怪兽3', 3, 50, 50)
    l4 = BigLeviathan(20)
    at_round = 1
    count = 0
    while (l1.currentLifeValue > 0) & (h.currentLifeValue > 0):
        print('===第%d回合===' % at_round)
        h1.grade = h.grade
        h1.attack(l1)  # 英雄攻击怪兽(包含怪兽防御，虽然没有)
        if l1.currentLifeValue > 0:
            sc = l1.attack(h)
            SmallLeviathan.skill = sc[0]  # 返回的怪兽的伤害值, 怪兽攻击英雄
            Hero.currentLifeValue = sc[1]  # 返回的英雄的当前生命值
            Hero.currentLifeValue = h1.defence()  # 英雄对怪兽进行防御
            h.currentLifeValue = Hero.currentLifeValue
        print(l1.name + '的', end='')
        print(l1)
        print(h.name + '的', end='')
        print(h1)
        at_round += 1
        count += 1
    while (l2.currentLifeValue > 0) & (h.currentLifeValue > 0):
        print('===第%d回合===' % at_round)
        h1.grade = h.grade
        h1.attack(l2)  # 英雄攻击怪兽(包含怪兽防御，虽然没有)
        if l2.currentLifeValue > 0:
            sc = l2.attack(h)  # 返回的怪兽的伤害值, 怪兽攻击英雄
            SmallLeviathan.skill = sc[0]  # 返回的怪兽的伤害值, 怪兽攻击英雄
            Hero.currentLifeValue = sc[1]  # 返回的英雄的当前生命值
            Hero.currentLifeValue = h1.defence()  # 英雄对怪兽进行防御
            h.currentLifeValue = Hero.currentLifeValue  # 返回的英雄的当前生命值
        print(l2.name + '的', end='')
        print(l2)
        print(h.name + '的', end='')
        print(h1)
        at_round += 1
        count += 1
    while (l3.currentLifeValue > 0) & (h.currentLifeValue > 0):
        print('===第%d回合===' % at_round)
        h1.grade = h.grade
        l4.grade = l3.grade
        sc1 = h1.attack(l3)  # 英雄攻击怪兽
        Hero.skill = sc1[0]  # 返回的英雄的伤害值, 英雄攻击怪兽
        BigLeviathan.currentLifeValue = sc1[1]  # 返回的怪兽的当前生命值
        BigLeviathan.currentLifeValue = l4.defence()  # 大怪兽对英雄进行防御, 并返回生命值
        l3.currentLifeValue = BigLeviathan.currentLifeValue  # 返回的大怪兽的当前生命值
        if l3.currentLifeValue > 0:
            sc = l4.attack(h)  # 返回的怪兽的伤害值, 怪兽攻击英雄
            SmallLeviathan.skill = sc[0]  # 返回的怪兽的伤害值, 怪兽攻击英雄
            Hero.currentLifeValue = sc[1]  # 返回的英雄的当前生命值
            Hero.currentLifeValue = h1.defence()  # 英雄对怪兽进行防御
            h.currentLifeValue = Hero.currentLifeValue  # 返回的英雄的当前生命值
        print(l3.name + '的', end='')
        print(l4)
        print(h.name + '的', end='')
        print(h1)
        at_round += 1
        count += 1
    print('战斗共进行了%d个回合' % count)
    if h1.currentLifeValue > 0:
        print('最终恭喜奥特曼取得胜利！')
    else:
        print('最终恭喜怪兽取得胜利')


if __name__ == '__main__':
    main()

# 结果：
# ===第1回合===
# 英雄的经验值：12
# 怪兽1的当前生命值：18
# 迪迦奥特曼的当前生命值：100
# 等级：2
#
# ===第2回合===
# 英雄的经验值：21
# 怪兽1的当前生命值：9
# 迪迦奥特曼的当前生命值：98
# 等级：2
#
# ===第3回合===
# 英雄的经验值：34
# 怪兽1的当前生命值：-4
# 迪迦奥特曼的当前生命值：98
# 等级：2
#
# ===第4回合===
# 英雄的经验值：36
# 怪兽2的当前生命值：38
# 迪迦奥特曼的当前生命值：73
# 等级：2
#
# ===第5回合===
# 英雄的经验值：51
# 怪兽2的当前生命值：23
# 迪迦奥特曼的当前生命值：70
# 等级：2
#
# ===第6回合===
# 英雄的经验值：52
# 怪兽2的当前生命值：22
# 迪迦奥特曼的当前生命值：70
# 等级：2
#
# ===第7回合===
# 英雄的经验值：61
# 怪兽2的当前生命值：13
# 迪迦奥特曼的当前生命值：70
# 等级：2
#
# ===第8回合===
# 英雄的经验值：79
# 怪兽2的当前生命值：-5
# 迪迦奥特曼的当前生命值：70
# 等级：2
#
# ===第9回合===
# 英雄的经验值：95
# 大怪兽的盾牌保护力还剩：20
# 怪兽3的当前生命值：50
# 迪迦奥特曼的当前生命值：65
# 等级：3
#
# ===第10回合===
# 英雄的经验值：99
# 大怪兽的盾牌保护力还剩：4
# 怪兽3的当前生命值：50
# 迪迦奥特曼的当前生命值：65
# 等级：3
#
# ===第11回合===
# 英雄的经验值：106
# 大怪兽的盾牌保护力还剩：0
# 怪兽3的当前生命值：43
# 迪迦奥特曼的当前生命值：29
# 等级：3
#
# ===第12回合===
# 英雄的经验值：117
# 大怪兽的盾牌保护力还剩：0
# 怪兽3的当前生命值：32
# 迪迦奥特曼的当前生命值：29
# 等级：3
#
# ===第13回合===
# 英雄的经验值：131
# 大怪兽的盾牌保护力还剩：0
# 怪兽3的当前生命值：18
# 迪迦奥特曼的当前生命值：21
# 等级：3
#
# ===第14回合===
# 英雄的经验值：146
# 大怪兽的盾牌保护力还剩：0
# 怪兽3的当前生命值：3
# 迪迦奥特曼的当前生命值：-19
# 等级：3
#
# 战斗共进行了14个回合
# 最终恭喜怪兽取得胜利
