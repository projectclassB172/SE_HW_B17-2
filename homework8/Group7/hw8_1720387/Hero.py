import random
from hw8_1720387.Person import Person
class Hero(Person):
    def __init__(self,name='hero', level=1, maxhp=100, race='human'):#设置英雄初始化
        super().__init__(name,level,maxhp)
        # 定义种族，和灵活度
        self._race = race
        if self._race == 'human':#人类
            self._flex = 0.4
        elif self._race == 'elves':#精灵
            self._flex = 0.8

    def get_race(self):  # 获取种族
        return self._race

    def get_flex(self):  # 获取灵活度
        return self._flex

    def defence(self, hurt):
        #根据灵活性，可以躲避掉对方的攻击。
        luck = random.random()
        if luck >= self.get_flex():
            self.set_hp(hurt)
            print('伤害提示:英雄:{},受到{}点伤害！'.format(self.get_name(),hurt))
        else:
            print('您成功躲避攻击！')

    def attack(self,monster):
        #根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数
        #monster被攻击对象
        if self.get_level() == 1:
            heroHurt = random.randint(0,10)
        elif self.get_level() ==2:
            heroHurt = random.randint(0, 20)
        elif self.get_level() ==3:
            heroHurt = random.randint(0, 30)
        monster.defence(heroHurt)#英雄伤害

    def upLevel(self):
        #升级，最大生命加点，回复生命
        self.set_level(1)#升一级
        self.set_maxhp(10)#注意最大生命必须先于回复生命
        self.reply_hp()
        print('升级提示：英雄:{},成功升级到{}级！'.format(self.get_name(),self.get_level()))

