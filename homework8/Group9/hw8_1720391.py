import random as r

#英雄（大类）精灵、人类
class Hero:
    #属性，这里使用__init__方法，在创建Hero对象时默认被调用
    def __init__(hero, name):
        hero.name = name     # 名字
        hero.level = 1       # 等级
        hero.max_hp = hero.level*20  # 最大生命
        hero.current_hp = hero.level*20  # 当前生命
    #攻击
    def attack(hero):
        atk = r.randint(0, hero.level*10-1)
        print("-->英雄发起攻击!")
        return atk
    #升级
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10  #当前血量
        hero.level = hero.level +1  #等级
        print("---->{} 升级,当前等级 {},当前血量 {}".format(hero.name, hero.level, hero.current_hp))
# 人类(英雄分支1)
class HeroHuman(Hero):
    # 属性
    def __init__(hero, name):
        super(HeroHuman, hero).__init__(name)#继承
        hero.avd = 0.4        # 灵活性
    #防御
    def defense(hero, atk):
        is_hurt = r.random()#产生随机数，如果小于0.4则躲避，大于则命中
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_人类：受到 {}点伤害,当前血量 {}".format(atk, hero.current_hp))
        else:
            print("-->英雄_人类：躲避，未命中!")

# 精灵(英雄分支2)
class HeroSpirit(Hero):
    # 属性
    def __init__(hero, name):
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.7        # 灵活性
    # 防御
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_精灵：受到 {}点伤害,当前血量 {}".format( atk, hero.current_hp))
        else:
            print("-->英雄_精灵：躲避，未命中!")


#怪兽（大类）,包含怪兽和大怪兽
class Monster:
    #属性
    def __init__(monster, name, level):
        monster.name = name      # 名字
        monster.level = level    # 等级
        monster.max_hp = int(level * 15)  # 最大生命
        monster.current_hp = int(level * 15)  # 当前生命
        # 攻击

    def attack(monster):
        atk = r.randint(0, monster.level * 10 - 1)
        print("-->怪兽发起攻击!".format(monster.name))
        return atk

        # 防御
    def defense(monster, atk):
        monster.current_hp -= atk
        print("-->怪兽受到 {} 点伤害,当前血量 {}".format( atk, monster.current_hp))

# 大怪兽,拥有护盾属性并重写防御方法
class Monster_bigMonster(Monster):
    # 属性
    def __init__(Big_monster, name, level):
        super(Monster_bigMonster, Big_monster).__init__(name, level)
        Big_monster.shield = Big_monster.max_hp * 0.2  # 护盾
    # 防御
    def defense(Big_monster, atk):   # 重写防御方法，受到攻击优先扣除护盾
        if Big_monster.shield - atk >= 0:
            Big_monster.shield = atk-Big_monster.shield
            print("-->大怪兽：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Big_monster.shield, Big_monster.current_hp))
        else:
            if Big_monster.shield > 0:
                Big_monster.current_hp -= Big_monster.shield
                Big_monster.shield = 0
                print("-->大怪兽：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Big_monster.shield, Big_monster.current_hp))
            else:
                Big_monster.current_hp -= atk
                print("-->大怪兽：受到 {}点伤害,当前护盾值 {} 血量 {}".format(Big_monster.name, atk, Big_monster.shield, Big_monster.current_hp))


#主方法
def main():
    #生成一个英雄，两个低等级怪兽，一个大怪兽
    h1 = HeroHuman("人类")
    m1 = Monster("怪兽1", 1)
    m2 = Monster("怪兽2", 2)
    m3 = Monster_bigMonster("大怪兽", 3)
    enemy = [m1, m2, m3]
    r = 1
    while True:
        print("回合{}：".format(r))
        enemy[0].defense(h1.attack())   # 英雄先攻击第一个怪兽，直到一方死亡
        if enemy[0].current_hp <= 0:   # 如果怪兽阵亡，从列表中删除这个怪兽，英雄升级
            print("{} 阵亡".format(enemy[0].name))
            h1.upgrade()
            del enemy[0]
        # 判断英雄成功还是失败
        if len(enemy) == 0:      # 英雄胜利的条件是怪兽数量为0
            print("---->英雄：Win!")
            return

        for each in enemy:       # 英雄攻击完后，怪兽依次攻击英雄
            h1.defense(each.attack())
        if h1.current_hp <= 0:    # 失败
            print("---->英雄：Lose!")
            return
        r += 1    # 回合数

#python程序入口
if __name__ == '__main__':
  main()

