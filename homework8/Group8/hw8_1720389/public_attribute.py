import random
class public_attribute(object):
    def __init__(self, name='', level=0, maxhp=0, flexibility=0, shield=0):
        self.name = name                # 名字
        self.level = level              # 等级
        self.maxhp = maxhp              # 最大血量
        self.nowhp = maxhp              # 当前血量
        self.flexibility = flexibility  # 灵活度
        self.shield = shield            # 护盾值

    def __str__(self):  # 输出状态
        return '{}({}):{}/{}'.format(self.name,self.level,self.nowhp,self.maxhp)

    def reduce_hp(self,damage_value):   # 扣血
        self.nowhp = self.nowhp - damage_value
        if self.nowhp < 0:
            self.nowhp = 0

    def reduce_shield(self,damage_value):   # 减少护盾值
        self.shield = self.shield - damage_value

    def up_level(self):     # 升级
        if self.level < 3:
            self.level = self.level + 1
            self.maxhp = self.maxhp + 20
            self.nowhp = self.maxhp
            print('升级！')

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_maxhp(self):
        return  self.maxhp

    def get_nowhp(self):
        return self.nowhp

    def get_flexibility(self):
        return self.flexibility

    def get_shield(self):
        return self.shield

    def attact(self,target):    # 攻击
        if self.get_level() == 1:
            hurt_value = random.randint(0, 10)
        elif self.get_level() == 2:
            hurt_value = random.randint(0, 20)
        elif self.get_level() == 3:
            hurt_value = random.randint(0, 30)
        target.defense(hurt_value)

    def defense(self,hurt_value):   # 防御
        f = random.random()
        if f > self.flexibility:
            if self.shield > 0:
                self.reduce_shield(hurt_value)
                print('{}受到0点伤害'.format(self.name))
            elif self.shield <= 0:
                self.reduce_hp(hurt_value)
                if self.flexibility > 0:
                    print('你受到{}点伤害'.format(hurt_value))
                elif self.flexibility == 0:
                    print('{}受到{}点伤害'.format(self.name,hurt_value))
        elif f < self.flexibility:
            print('你成功闪避怪兽的攻击')