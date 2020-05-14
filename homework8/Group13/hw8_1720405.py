import random


class attribute:
    def __init__(self, name, level, HP, maxHP, ):
        self.name = name
        self.level = level
        self.HP = HP
        self.maxHP = maxHP

    def attack(self, attacker, victim):
        hurt = random.randint(0, attacker.level * 10)
        victim.HP -= hurt
        if victim.HP > 0:
            print("%s受到的伤害%d，当前生命%d" % (victim.name, hurt, victim.HP))
        else:
            print("%s受到的伤害%d，当前生命0，%s死亡" % (victim.name, hurt, victim.name))


class Hero(attribute):
    def setFlexibility(self, flexibility):
        self.flexibility = flexibility

    def defense(self):
        if random.uniform(0, 1) < self.flexibility:
            print("%s闪避成功,当前生命值%d" % (self.name, self.HP))
            return False
        else:
            return True


class boss(attribute):
    def Shield(self, shield):
        self.shield = shield

    def defense(self, hero, monster):
        if monster.shield > 0:
            hurt = random.randint(0, hero.level * 10)
            monster.shield -= hurt
            if monster.shield < 0:
                monster.HP += monster.shield
                monster.shield = 0
            print("%s受到攻击%d,剩余防御值%d，剩余生命%d" % (monster.name, hurt, monster.shield, monster.HP))
            return False
        else:
            return True


def main():
    hero2 = Hero("人类", 2, 200, 400)
    monster1 = attribute("怪兽1", 1, 50, 50)
    monster2 = attribute("怪兽2", 2, 50, 50)
    monster3 = boss("怪兽boss", 3, 180, 150)
    hero2.setFlexibility(0.4)
    monster3.Shield(50)
    allmo = [monster1, monster2, monster3]
    i = 0
    number = 1
    while hero2.HP > 0 and allmo[i].HP > 0:
        print("第%d回合" % number)
        number += 1
        print("--%s攻击--" % allmo[i].name)
        if hero2.defense():
            allmo[i].attack(allmo[i], hero2)
        if hero2.HP <= 0:
            print("%s胜利" % allmo[i].name)
            break
        print("--%s攻击--" % hero2.name)
        if i < 2:
            hero2.attack(hero2, allmo[i])
            if allmo[i].HP <= 0:
                i += 1
        elif i >= 2:
            if allmo[i].defense(hero2, allmo[i]):
                hero2.attack(hero2, allmo[i])
                if allmo[i].HP <= 0:
                    print("%s胜利" % hero2.name)
                    break
        print()


main()