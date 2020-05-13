import random as rn             # 引入随机数
# 定义精灵
class Sprite:
    def __init__(self,name):
        self.blood = 100         # 假设初始血量为：100
        self.power = 5           # 假设基础攻击能力：5
        self.name = name
        self.huo = 0.4
        self.zhongzu = 1
        self.dengji = 1

    def attack(self, monster):
        # 假设每一次攻击的伤害 服从随机分布（0,10）      
        minus = rn.randrange(self.power - 5, self.power + 5)
        print(minus)
        if monster.has_living():
            monster.minus_blood(minus)
        print(monster.name + ' 剩余血量:\n' + str(monster.blood)+ "\n")
        # 输出剩余血量

    def duobi():
        # 假设每一次攻击的伤害 服从随机分布（0,10）
        minus = rn.randrange(self.huo - 0.4, self.huo + 0.6)

    def minus_blood(self,num):
        self.blood -= num

    def has_living(self):         #判断是否还有血量
        if self.blood > 0:
            return True
        return False

m = Sprite('怪兽*哥斯拉')
x = Sprite('怪兽*小斯拉')
y = Sprite('怪兽*大斯拉')
h = Sprite('迪迦*奥特曼')
print(m.name + ' 的初始血量：120')
print(x.name + ' 的初始血量：100')
print(y.name + ' 的初始血量：100')
print(h.name + ' 的初始血量：100')

while m.has_living() and h.has_living() and x.has_living() and y.has_living():
    print(m.name + ' 对 ' + h.name + ' 造成伤害:' )
    m.attack(h)
    print(x.name + ' 对 ' + h.name + ' 造成伤害:' )
    m.attack(h)
    print(y.name + ' 对 ' + h.name + ' 造成伤害:' )
    m.attack(h)
    print(h.name + ' 对 ' + m.name + ' 造成伤害:')
    h.attack(m)

if m.has_living():
    print(m.name + ' 胜利~!')
elif h.has_living():
    print(h.name + ' 胜利~!')
elif x.has_living():
    print(m.name + ' 胜利~!')
elif y.has_living():
    print(m.name + ' 胜利~!')

