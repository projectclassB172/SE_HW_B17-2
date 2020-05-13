from Fight_monsters.public_attribute import public_attribute
class hero_test(public_attribute):
    def __init__(self, name='', race=''):
        if race == 'human':  # 人类
            super().__init__(name, 1, 80, 0.4, 0)
        elif race == 'spirit':  # 精灵
            super().__init__(name, 1, 60, 0.6, 0)

class monster_test(public_attribute):
    def  __init__(self,name='',level=0):
        if level == 1:
            maxhp = 30
            defense = 0
            #super().__init__(name, 1, 100, 0, 0)
        elif level == 2:
            maxhp = 60
            defense = 0
            #super().__init__(name, 2, 150, 0, 0)
        elif level == 3:
            maxhp = 100
            defense = 30
        super().__init__(name, 3, maxhp, 0, defense)