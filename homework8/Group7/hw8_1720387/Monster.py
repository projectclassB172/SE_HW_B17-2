import random
from hw8_1720387.Person import Person
class Monster(Person):
    def __init__(self,name='onster', level=1, maxhp=20):
        super().__init__(name,level,maxhp)

    def attack(self,hero):
        # 根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数
        # hero被攻击对象
        if self.get_level() == 1:
            monsterHurt = random.randint(0, 10)
        elif self.get_level() == 2:
            monsterHurt = random.randint(0, 20)
        hero.defence(monsterHurt)#怪物伤害

    def defence(self, hurt):
        self.set_hp(hurt)
        print('伤害提示:怪兽:{},受到{}点伤害'.format(self.get_name(),hurt))

class Boss(Person):
    def __init__(self, name='boss', level=3, maxhp=100):
        super().__init__(name,level,maxhp)
        self._shield = 50 #防御值

    def defence(self, hurt):
        if self._shield > 0:#先进行破防
            self._shield = self._shield - hurt
            if self._shield < 0:
                self._shield = 0
        if self._shield <= 0:
            self.set_hp(hurt)
        print('伤害提示:Boss:{},受到{}点伤害'.format(self.get_name(),hurt))

    def attack(self, hero):
        hurt = random.randint(0, 20)
        hero.defence(hurt)#Boss伤害

    def __str__(self):
        return 'Name:{}\t Level:{}\t MAXHP:{}\t Shield:{}\t HP:{}'.format(self.get_name(),self.get_level(),self.get_maxhp(),self._shield,self.get_hp() )  # 注意HP为当前HP

