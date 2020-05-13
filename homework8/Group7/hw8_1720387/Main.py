from hw8_1720387.Hero import Hero
from hw8_1720387.Monster import Monster,Boss

def nextMonster(monsterList:list):
    #下一只怪物上场
    assert  type(monsterList) is list
    if len(monsterList) > 0:
        return monsterList[0]

if __name__ == '__main__':

    hero = Hero('张三', 1, 100, 'human')
    monster1 = Monster('青蛙', 1, 20)
    monster2 = Monster('蝙蝠', 1, 20)
    boss = Boss('琨', 3, 150)
    monsterList = [monster1, monster2, boss]
    round = 1
    while hero.get_hp()> 0 and len(monsterList) > 0:
        monster = nextMonster(monsterList)
        while monster.get_hp() > 0:
            print('*' * 20, '第{}回合-1720387'.format(round), '*' * 20)
            #英雄先手攻击
            hero.attack(monster)
            if hero.get_hp() > 0:
                # 怪物后手攻击
                monster.attack(hero)
                if hero.get_hp() < 0:
                    break
            print(hero)
            print(monster)
            round = round + 1

        if monster.get_hp() <= 0:
            monsterList.remove(monster)
            hero.upLevel()
            monster = nextMonster(monsterList)
    if hero.get_hp() > 0:
        print('英雄:{}\t获得胜利！'.format(hero.get_name()))
    else:
        print('英雄:{}\t挑战失败！'.format(hero.get_name()))

print('create by 1720387-王泽霖')

'''
运行结果：
******************** 第1回合-1720387 ********************
伤害提示:怪兽:青蛙,受到8点伤害
您成功躲避攻击！
Name:张三	 Level:1	 MAXHP:100	 HP:100
Name:青蛙	 Level:1	 MAXHP:20	 HP:12
******************** 第2回合-1720387 ********************
伤害提示:怪兽:青蛙,受到6点伤害
伤害提示:英雄:张三,受到4点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:96
Name:青蛙	 Level:1	 MAXHP:20	 HP:6
******************** 第3回合-1720387 ********************
伤害提示:怪兽:青蛙,受到9点伤害
伤害提示:英雄:张三,受到10点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:86
Name:青蛙	 Level:1	 MAXHP:20	 HP:-3
升级提示：英雄:张三,成功升级到2级！
******************** 第4回合-1720387 ********************
伤害提示:怪兽:蝙蝠,受到20点伤害
伤害提示:英雄:张三,受到6点伤害！
Name:张三	 Level:2	 MAXHP:110	 HP:104
Name:蝙蝠	 Level:1	 MAXHP:20	 HP:0
升级提示：英雄:张三,成功升级到3级！
******************** 第5回合-1720387 ********************
伤害提示:Boss:琨,受到20点伤害
伤害提示:英雄:张三,受到6点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:114
Name:琨	 Level:3	 MAXHP:150	 Shield:30	 HP:150
******************** 第6回合-1720387 ********************
伤害提示:Boss:琨,受到5点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:114
Name:琨	 Level:3	 MAXHP:150	 Shield:25	 HP:150
******************** 第7回合-1720387 ********************
伤害提示:Boss:琨,受到28点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:114
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:122
******************** 第8回合-1720387 ********************
伤害提示:Boss:琨,受到20点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:114
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:102
******************** 第9回合-1720387 ********************
伤害提示:Boss:琨,受到12点伤害
伤害提示:英雄:张三,受到20点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:94
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:90
******************** 第10回合-1720387 ********************
伤害提示:Boss:琨,受到0点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:94
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:90
******************** 第11回合-1720387 ********************
伤害提示:Boss:琨,受到14点伤害
伤害提示:英雄:张三,受到7点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:87
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:76
******************** 第12回合-1720387 ********************
伤害提示:Boss:琨,受到10点伤害
伤害提示:英雄:张三,受到19点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:68
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:66
******************** 第13回合-1720387 ********************
伤害提示:Boss:琨,受到25点伤害
伤害提示:英雄:张三,受到5点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:63
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:41
******************** 第14回合-1720387 ********************
伤害提示:Boss:琨,受到28点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:63
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:13
******************** 第15回合-1720387 ********************
伤害提示:Boss:琨,受到25点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:63
Name:琨	 Level:3	 MAXHP:150	 Shield:-3	 HP:-12
升级提示：英雄:张三,成功升级到4级！
英雄:张三	获得胜利！
create by 1720387-王泽霖

'''