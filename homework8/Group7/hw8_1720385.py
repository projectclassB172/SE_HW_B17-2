from random import randint  # 导入randint函数


class Ultraman(object):  # 定义类（爸爸、祖宗.......



    def __init__(self, name, hp, mp):  # 标准格式，init顾名思义（括号里面是定义对象的属性）
        self._name = name  # 固定格式，其中下划线表示属性受保护，不能随便改。要改就得用装饰器
        self._hp = hp  # 定义奥特曼的名字、血量、魔法量
        self._mp = mp

    @property  # 访问器包装起来方便调用和增加其他功能而不改动本身
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter  # 修改器，只要修属性改变量就得用
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, monster):  # 设置攻击方法，其实就是定义动作属性
        monster.hp -= randint(0, 25)

    def huge_attack(self, monster):  # 另一种动作属性，大招
        if self._mp >= 50:
            self._mp -= 50
            injury = monster.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            monster.hp -= injury
        else:
            self.attack(monster)  # 回合制，下一轮调用monster对象进行动作

    def magic_attack(self, monsters):  # 另一种动作属性
        if self._mp >= 20:
            self._mp -= 20
        for monster in monsters:  # 定义多个静态属性monster
            monster.hp -= randint(1, 15)

    def __str__(self):  # 返回每次调用之后的剩余参数（血量、魔法量、名字）
        return '%s奥特曼\n' % self._name + \
               '生命值：%d\n' % self._hp + \
               '魔法值：%d\n' % self._mp


class Monster(object):  # 定义另一个类（怪兽）

    def __init__(self, name, hp):  # 固定起手式
        self._name = name
        self._hp = hp

    @property  # 继续包装器
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter  # 继续修改器
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, ultraman):  # 定义动态属性（攻击）
        ultraman.hp -= randint(0, 15)

    def __str__(self):
        return '%s小怪兽\n' % self.name + \
               '生命值：%d\n' % self.hp


def main():  # 最终调用所有的类对象的属性进行动作，最终的命令执行以上的函数及各种方法
    u = Ultraman('杰哥', 600, 300)
    m1 = Monster('牛头1', 300, )
    m2 = Monster('牛头2', 180)
    m3 = Monster('牛头3', 260)
    ms = [m1, m2, m3]
    at_round = 1
    while u.hp > 0 and m1.hp > 0:  # 设定while循环直到要求的条件将其打破
        print('===第%d回合===' % at_round)
        u.attack(m1)
        if m1.hp > 0:
            m1.attack(u)
        print(m1)
        print(u)
        at_round += 1
    if u.hp > 0:
        print('%s奥特曼胜利！' % u.name)
    else:
        print('%s怪兽胜利' % m1.name)


if __name__ == '__main__':
    main()
