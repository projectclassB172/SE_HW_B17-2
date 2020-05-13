class Person(object):#定义超类
    def __init__(self, name='', level=1, maxhp=100):  # 标准格式，init顾名思义（括号里面是定义对象的属性）
        self._name = name  # 定义名字、级别、最大血量、当前血量
        self._level = level
        self._maxhp = maxhp
        self._hp = maxhp #当前生命值为最大生命

    def get_name(self):#获取名字
        return self._name

    def get_level(self):  # 获取level
        return self._level

    def get_maxhp(self):#获取最大hp
        return self._maxhp

    def get_hp(self):#获取当前hp
        return self._hp

    def set_level(self,upLevel):  # 升一级
        self._level = self._level + upLevel

    def set_maxhp(self,upMaxhp):  # 设置最大生命值
        self._maxhp = self._maxhp + upMaxhp

    def set_hp(self,hurt):  # 设置hp-受到伤害
        self._hp = self._hp - hurt

    def reply_hp(self):  # 回复生命值为最大生命
        self._hp = self._maxhp

    def attack(self,object):  # 设置攻击方法，其实就是定义动作属性，monster攻击对象
        pass
        # raise NotImplementedError('请实现attack方法')#返回伤害值

    def defence(self, hurt):  # 设置防御方法，其实就是定义动作属性，hurt伤害值
        pass
        # raise NotImplementedError('请实现defence方法')

    def __str__(self): #打印人物情况name、level、hp
        return 'Name:{}\t Level:{}\t MAXHP:{}\t HP:{}'.format(self._name,self._level,self._maxhp,self._hp)#注意HP为当前HP


