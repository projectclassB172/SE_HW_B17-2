import random
class Property():
    def __init__(self,name,level,ml):
        #cl��ʾ��ǰ����ֵ��ml��ʾ�������ֵ
        self.name=name
        self.level=level
        self.cl=ml
        self.ml=ml
class Hero(Property):
    def __init__(self,name,level,ml,race):
        super().__init__(name,level,ml)
        self.race=race
        if self.race=='human':
            self.agillity=0.4
        elif self.race=='elf':
            self.agillity=0.7
    def attack(self,Monster):
        m=random.randint(0,self.level*10)
        Monster.defense(m)
    def defense(self,m):
        df=random.random()
        if df>self.agillity:
            self.cl-=m
            if self.cl>0:
                print("{}�ܵ���{}�㹥��,��ǰ��{}��,����ֵΪ{}".format(self.name,m,self.level,self.cl))
            else:
                print("{}�ܵ���{}�㹥��,��ǰ����ֵΪ0,ʧ��".format(self.name, m))
        else:
            print("{}��ܵ��˹���,��ǰ��{}��,����ֵΪ{}".format(self.name,self.level,self.cl))
    def upgrade(self):
        self.level+=1
        self.ml=self.ml+10
        self.cl=self.ml
        print("{}Ӯ�˹�������{}��,��ǰ����ֵΪ{}".format(self.name,self.level,self.cl))
class Monster(Property):
    def __init__(self,name,level,ml):
        super().__init__(name,level,ml)
    def attack(self,Hero):
        m=random.randint(0,self.level*10)
        Hero.defense(m)
    def defense(self,m):
        self.cl-=m
        if self.cl>0:
            print("{}�ܵ���{}�㹥��,��ǰ����ֵΪ{}".format(self.name,m,self.cl))
        else:
            print("{}�ܵ���{}�㹥��,��ǰ����ֵΪ0,����".format(self.name, m))
s1 = monster(name='��һ�����ޡ�' , lv=1 , maxblood=20)  # ������ֻ����
s2 = monster(name='���������ޡ�' , lv=2 , maxblood=30)
s3 = monster(name='���������ޡ�' , lv=3 , maxblood=50)
s4 = [s1,s2,s3]
h = hero(name='��ƤƤϺ��' , lv=3 , race='����',maxblood=100)  # ����Ӣ��
print(h.name + '�ĳ�ʼѪ��:' + str(h.maxblood) + '(' + h.race + ')')
for m in s4:
    print(h.name + '������Ѫ����' + str(h.blood))
    if m.lv == 3:
        print(m.name + '�ĵȼ��ﵽ�������������10�㻤��')
        print(m.name + '�ĳ�ʼѪ��:' + str(m.maxblood) + '  ���ܣ�' + str(10))
    else:
        print(m.name + '�ĳ�ʼѪ��:' + str(m.maxblood))

    print('-------------------------------------')
    while m.has_living() and h.has_living():
        print(m.name + ' �� ' + h.name + ' ����˺�:')
        m.attack(h)
        print(h.name + ' �� ' + m.name + ' ����˺�:')
        h.attack(m)

    if m.has_living():
        print(m.name + ' Ӯ����ʤ��!')
    elif h.has_living():
        print(h.name + ' Ӯ����ʤ��!')
    else:
        print('ƽ�֣�')