from Fight_monsters.role import hero_test,monster_test
def next_one(monster_List:list):
    assert  type(monster_List) is list
    if len(monster_List) > 0:
        return monster_List[0]
if __name__ == '__main__':
    hero = hero_test('hero', 'human')
    monster1 = monster_test('虾兵', 1)
    monster2 = monster_test('蟹将', 2)
    monster3 = monster_test('龙王', 3)
    monster_list = [monster1,monster2,monster3]
    round = 1
    while hero.get_nowhp() > 0 and len(monster_list) > 0:
        monster = next_one(monster_list)
        while monster.get_nowhp() > 0:
            print('回合{}:'.format(round))
            hero.attact(monster)
            if hero.get_nowhp() > 0:
                monster.attact(hero)
                if hero.get_nowhp() == 0:
                    print(hero)
                    print(monster)
                    break
            print(hero)
            print(monster)
            round += 1
        if monster.get_nowhp() <= 0:
            monster_list.remove(monster)
            hero.up_level()
            monster= next_one(monster_list)
    if hero.get_nowhp() > 0:
        print('WIN!')
    else:
        print('LOSE!')