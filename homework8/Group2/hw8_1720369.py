Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random as r

#英雄
class Hero:
    #属性
    def __init__(hero, name):
        hero.name = name     
    # 等级
        hero.level = 1
        hero.max_hp = hero.level*60  #最大生命值
        hero.current_hp = hero.level*60  # 当前生命值
    #攻击
    def attack(hero):
        atk = r.randint(0, hero.level*10)
        print("-->英雄发动攻击回合!")
        return atk
    #升级
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10 
        hero.level = hero.level +1  #等级
        print("---->{} 升级,当前等级 {},当前血量 {}".format(hero.name, hero.level, hero.current_hp))
# 人类
  class HeroHuman(Hero):
    # 属性
    def __init__(hero, name):
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.5        # 灵活性
    #防御
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_人类：受到 {}点伤害,当前血量 {}".format(atk, hero.current_hp))
        else:
            print("-->英雄_人类：miss!")

# 精灵
class HeroSpirit(Hero):
    # 属性
    def __init__(hero, name):
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.8
    # 防御
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->英雄_精灵：受到 {}点伤害,当前血量 {}".format( atk, hero.current_hp))
        else:
            print("-->英雄_精灵：miss!")


#怪兽
class Monster:
    #属性
    def __init__(monster, name, level):
        monster.name = name 
        monster.level = level
        monster.max_hp = int(level * 20)
        monster.current_hp = int(level * 20)


    # 攻击
    def attack(monster):
        atk = r.randint(0, monster.level * 10)
        print("-->怪兽发动攻击回合!".format(monster.name))
        return atk

        # 防御
    def defense(monster, atk):
        monster.current_hp -= atk
        print("-->怪兽受到 {} 点伤害,当前血量 {}".format( atk, monster.current_hp))

# boss
class Monster_bigMonster(Monster):
    # 属性
    def __init__(Monster_Boss, name, level):
        super(Monster_bigMonster, Monster_Boss).__init__(name, level)
        Monster_Boss.shield = Monster_Boss.max_hp * 0.5
    # 防御
    def defense(Monster_Boss, atk):
        if Monster_Boss.shield - atk >= 0:
            Monster_Boss.shield = atk-Monster_Boss.shield
            print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Monster_Boss.shield, Monster_Boss.current_hp))
        else:
            if Monster_Boss.shield > 0:
                Monster_Boss.current_hp -= Monster_Boss.shield
                Monster_Boss.shield = 0
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, Monster_Boss.shield, Monster_Boss.current_hp))
            else:
                Monster_Boss.current_hp -= atk
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format(Monster_Boss.name, atk, Monster_Boss.shield, Monster_Boss.current_hp))


#主函数
def main():
    hero = HeroHuman("人类")
    m1 = Monster("怪兽1", 1)
    m2 = Monster("怪兽2", 2)
    m3 = Monster_bigMonster("boss", 3)
    MonsterNum = [m1, m2, m3]
    r = 1
    while True:
        print("回合{}：".format(r))
        MonsterNum[0].defense(hero.attack()) 
        if MonsterNum[0].current_hp <= 0: 
            print("{} 阵亡".format(MonsterNum[0].name))
            hero.upgrade()
            del MonsterNum[0]
        if len(MonsterNum) == 0:      # 怪兽消灭完毕  英雄胜利
            print("---->英雄：你胜利了!")
            return

        for each in MonsterNum:
            hero.defense(each.attack())
        if hero.current_hp <= 0:    #血量为0时失败
            print("---->英雄：您已死!")
            return
        r += 1    # 回合数加1

if __name__ == '__main__':
  main()
