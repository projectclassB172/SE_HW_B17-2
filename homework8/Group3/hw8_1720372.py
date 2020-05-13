import random

class game():
    def person(self):
        self.HP = HP =100
        self.D_HP = D_HP =80
        self.powe = powe = 0
        self.D_powe = D_powe = 0
        self.experience = ex = 0
        self.leve = le = 1
        self.Dmiss = Dmiss = 1
        global race
    def fight(self):
        self.person()
        self.pickhero()
        ex = self.experience
        le = self.leve
        dm = self.Dmiss
        mi = self.miss
        print("开始战斗")
        while (self.HP > 0 and self.D_HP > 0):
            self.D_powe = random.randint(1, 10)
            self.powe = random.randint(1, 10)
            self.Dmiss = random.uniform(0, 1)
            self.HP = self.HP - self.D_powe
            self.D_HP = self.D_HP - self.powe
            print("怪兽的命中率是：",self.Dmiss)
            print("怪兽攻击力是", self.D_powe)
            print("英雄的攻击力是", self.powe)
            ex = ex+0.1
            print("你的经验",ex)
            if(self.miss>self.Dmiss):
                self.D_powe= 0
                print("你躲开了攻击")
            else:
                print("你没有躲开，被怪兽攻击了")
                self.D_powe = random.randint(1, 10)
            if (self.HP > 0 or self.D_HP > 0):
                print("怪兽被攻击，怪兽剩下：", self.D_HP)
                print("英雄被攻击，英雄剩下：", self.HP)
            elif (self.D_HP <= 0 or self.HP <= 0):
                print("战斗结束")
            if (ex>1):
                le = le+1
                self.D_HP=120
                self.HP=100
                print("你升级了",le)
                print("开始打第二阶段的怪兽，怪兽百分百命中")
                print("你的生命值：",self.HP)
                print("怪兽的生命值：",self.D_HP)
                break
        while (self.HP > 0 and self.D_HP > 0):
            self.D_powe = random.randint(10, 20)
            self.powe = random.randint(10, 20)
            self.HP = self.HP - self.D_powe
            self.D_HP = self.D_HP - self.powe
            print("boss攻击力是", self.D_powe)
            print("英雄的攻击力是", self.powe)
            print("boss被攻击，boss剩下：", self.D_HP)
            print("英雄被攻击，英雄剩下：", self.HP)
            if(self.D_HP <= 0 or self.HP <= 0):
                print("战斗结束")
                break
        if (self.HP > self.D_HP):
            print("英雄胜利")
        else :
            print("怪兽胜利")
    def pickhero(self):
        self.person()
        n = self.leve
        race = int(input("请选择你的种族：1精灵,2人类："))
        if race != 1:
            self.miss = 0.3
            print("你是人类")
            print("灵活性是：", self.miss)
        elif race != 2:
            self.miss = 0.5
            print("你是精灵")
            print("灵活性是：", self.miss)
        print("你的等级是：",n)

if __name__ == '__main__':
    game().fight()