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
                if hero.get_hp() <= 0:
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
伤害提示:怪兽:青蛙,受到3点伤害
伤害提示:英雄:张三,受到3点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:97
Name:青蛙	 Level:1	 MAXHP:20	 HP:17
******************** 第2回合-1720387 ********************
伤害提示:怪兽:青蛙,受到5点伤害
伤害提示:英雄:张三,受到3点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:94
Name:青蛙	 Level:1	 MAXHP:20	 HP:12
******************** 第3回合-1720387 ********************
伤害提示:怪兽:青蛙,受到5点伤害
伤害提示:英雄:张三,受到3点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:91
Name:青蛙	 Level:1	 MAXHP:20	 HP:7
******************** 第4回合-1720387 ********************
伤害提示:怪兽:青蛙,受到5点伤害
您成功躲避攻击！
Name:张三	 Level:1	 MAXHP:100	 HP:91
Name:青蛙	 Level:1	 MAXHP:20	 HP:2
******************** 第5回合-1720387 ********************
伤害提示:怪兽:青蛙,受到7点伤害
伤害提示:英雄:张三,受到2点伤害！
Name:张三	 Level:1	 MAXHP:100	 HP:89
Name:青蛙	 Level:1	 MAXHP:20	 HP:-5
升级提示：英雄:张三,成功升级到2级！
******************** 第6回合-1720387 ********************
伤害提示:怪兽:蝙蝠,受到8点伤害
伤害提示:英雄:张三,受到7点伤害！
Name:张三	 Level:2	 MAXHP:110	 HP:103
Name:蝙蝠	 Level:1	 MAXHP:20	 HP:12
******************** 第7回合-1720387 ********************
伤害提示:怪兽:蝙蝠,受到16点伤害
伤害提示:英雄:张三,受到0点伤害！
Name:张三	 Level:2	 MAXHP:110	 HP:103
Name:蝙蝠	 Level:1	 MAXHP:20	 HP:-4
升级提示：英雄:张三,成功升级到3级！
******************** 第8回合-1720387 ********************
伤害提示:Boss:琨,受到22点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:120
Name:琨	 Level:3	 MAXHP:150	 Shield:28	 HP:150
******************** 第9回合-1720387 ********************
伤害提示:Boss:琨,受到26点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:120
Name:琨	 Level:3	 MAXHP:150	 Shield:2	 HP:150
******************** 第10回合-1720387 ********************
伤害提示:Boss:琨,受到22点伤害
伤害提示:英雄:张三,受到5点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:115
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:128
******************** 第11回合-1720387 ********************
伤害提示:Boss:琨,受到13点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:115
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:115
******************** 第12回合-1720387 ********************
伤害提示:Boss:琨,受到10点伤害
伤害提示:英雄:张三,受到0点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:115
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:105
******************** 第13回合-1720387 ********************
伤害提示:Boss:琨,受到1点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:115
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:104
******************** 第14回合-1720387 ********************
伤害提示:Boss:琨,受到0点伤害
伤害提示:英雄:张三,受到8点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:107
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:104
******************** 第15回合-1720387 ********************
伤害提示:Boss:琨,受到4点伤害
伤害提示:英雄:张三,受到13点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:94
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:100
******************** 第16回合-1720387 ********************
伤害提示:Boss:琨,受到8点伤害
伤害提示:英雄:张三,受到13点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:81
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:92
******************** 第17回合-1720387 ********************
伤害提示:Boss:琨,受到21点伤害
伤害提示:英雄:张三,受到15点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:66
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:71
******************** 第18回合-1720387 ********************
伤害提示:Boss:琨,受到22点伤害
伤害提示:英雄:张三,受到6点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:60
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:49
******************** 第19回合-1720387 ********************
伤害提示:Boss:琨,受到1点伤害
您成功躲避攻击！
Name:张三	 Level:3	 MAXHP:120	 HP:60
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:48
******************** 第20回合-1720387 ********************
伤害提示:Boss:琨,受到6点伤害
伤害提示:英雄:张三,受到1点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:59
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:42
******************** 第21回合-1720387 ********************
伤害提示:Boss:琨,受到9点伤害
伤害提示:英雄:张三,受到10点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:49
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:33
******************** 第22回合-1720387 ********************
伤害提示:Boss:琨,受到5点伤害
伤害提示:英雄:张三,受到1点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:48
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:28
******************** 第23回合-1720387 ********************
伤害提示:Boss:琨,受到24点伤害
伤害提示:英雄:张三,受到12点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:36
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:4
******************** 第24回合-1720387 ********************
伤害提示:Boss:琨,受到18点伤害
伤害提示:英雄:张三,受到20点伤害！
Name:张三	 Level:3	 MAXHP:120	 HP:16
Name:琨	 Level:3	 MAXHP:150	 Shield:0	 HP:-14
升级提示：英雄:张三,成功升级到4级！
英雄:张三	获得胜利！
create by 1720387-王泽霖
'''