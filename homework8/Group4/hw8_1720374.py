#1720374�Ƶ���

import random
class Hero:
    
    def __init__(hero, name):
        hero.name = name     
        hero.level = 1       
        hero.max_hp = hero.level*20  
        hero.current_hp = hero.level*20  
    
    def attack(hero):
        atk = r.randint(0, hero.level*10-1)
        print("-->�����𹥻�!")
        return atk
    
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10  
        hero.level = hero.level +1 
        print("---->{} ����,��ǰ�ȼ� {},��ǰѪ�� {}".format(hero.name, hero.level, hero.current_hp))

class HeroHuman(Hero):
    
    def __init__(hero, name):
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.4 
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->�����ܵ� {}���˺�,��ǰѪ�� {}".format(atk, hero.current_hp))
        else:
            print("-->���񣺶�ܣ�δ����!")

class HeroSpirit(Hero):
    
    def __init__(hero, name):
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.7        
    
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("-->�����ܵ� {}���˺�,��ǰѪ�� {}".format( atk, hero.current_hp))
        else:
            print("-->���񣺶�ܣ�δ����!")
class Monster:
    def __init__(monster, name, level):
        monster.name = name      
        monster.level = level   
        monster.max_hp = int(level * 15)  
        monster.current_hp = int(level * 15)  


    def attack(monster):
        atk = r.randint(0, monster.level * 10 - 1)
        print("-->���˷��𹥻�!".format(monster.name))
        return atk

    def defense(monster, atk):
        monster.current_hp -= atk
        print("-->�����ܵ� {} ���˺�,��ǰѪ�� {}".format( atk, monster.current_hp))


class Monster_bigMonster(Monster):
    
    def __init__(Big_monster, name, level):
        super(Monster_bigMonster, Big_monster).__init__(name, level)
        Big_monster.shield = Big_monster.max_hp * 0.2  
   
    def defense(Big_monster, atk):  
        if Big_monster.shield - atk >= 0:
            Big_monster.shield = atk-Big_monster.shield
            print("-->���ߣ��ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format( atk, Big_monster.shield, Big_monster.current_hp))
        else:
            if Big_monster.shield > 0:
                Big_monster.current_hp -= Big_monster.shield
                Big_monster.shield = 0
                print("-->���ߣ��ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format( atk, Big_monster.shield, Big_monster.current_hp))
            else:
                Big_monster.current_hp -= atk
                print("-->���ߣ��ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format(Big_monster.name, atk, Big_monster.shield, Big_monster.current_hp))



def main():
    h1 = HeroHuman("����")
    m1 = Monster("����1", 1)
    m2 = Monster("����2", 2)
    m3 = Monster_bigMonster("����", 3)
    enemy = [m1, m2, m3]
    r = 1
    while True:
        print("�غ�{}��".format(r))
        enemy[0].defense(h1.attack())   
        if enemy[0].current_hp <= 0:   
            print("{} ����".format(enemy[0].name))
            h1.upgrade()
            del enemy[0]
        
        if len(enemy) == 0:      
            print("---->����Win!")
            return

        for each in enemy:       
            h1.defense(each.attack())
        if h1.current_hp <= 0:    
            print("---->����Lose!")
            return
        r += 1    

if __name__ == '__main__':
  main()