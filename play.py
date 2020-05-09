from random import choice, sample

from world import things, units
from world.settings import NUM_FIGHTERS, WAREHOUSE_ITEMS
from world.texts import (fighter_is_dead_msg, greetings_msg, mode_msg,
                         things_to_fighters_msg, warehouse_storage_msg)

'''
Игра запускается функцией play
Настройки находятся в файле world/settings.py
play() поддерживат две опции:
start_comment=True - Для отображения дополнительных стартовых комментов
interactive=True - Для интерактивного режима игры
'''


def prepare_to_fight(fighters, warehouse, start_comment):
    warehouse.generate_things(WAREHOUSE_ITEMS)
    if start_comment: print(warehouse_storage_msg(warehouse))
    while True:
        item = warehouse.take_item()
        if item:
            status = None
            while not status:
                status = choice(fighters).setThings(item)
        else:
            break
    if start_comment: print(things_to_fighters_msg(fighters))


def fight(players):
    if len(players) < 1:
        return f'\n### А где бойцы?'
    if len(players) == 1:
        return f'\n### Нет противников для {players[0].name}!'
    print('\nReady? Steady. Fight!\n')
    while len(players) > 1:
        fp = sample(players, 2)  # fp - fight players
        fp[0] - fp[1]
        if fp[0].hp <= 0:
            print(fighter_is_dead_msg(fp[0]))
            players.remove(fp[0])

    return f'\n\n====\nОднозначный победитель - {players[0].name}'


def make_bet(num_fighters) -> int:
    print(f'Делайте ставку на победителя!')

    return int(input(f'Введите число от 1 до {num_fighters}: '))-1


def play(start_comment=False, interactive=False):
    print(mode_msg())
    fighters = units.generatePersons(NUM_FIGHTERS)
    if start_comment: print(greetings_msg(fighters))
    if interactive:
        if not start_comment: print(greetings_msg(fighters))
        bet = fighters[make_bet(len(fighters))]
    warehouse = things.Warehouse()
    prepare_to_fight(fighters, warehouse, start_comment=start_comment)
    print(fight(fighters))
    if interactive:
        if fighters[0] == bet:
            print('\nПоздравляем Ваша ставка выйграла! Получите награду!')
        else:
            print(f'\n А Вы ставили на жалкую клячу {bet.name}.'
                  f'\n Штош. Ожидайте коллекторов.')


play(True, True)
