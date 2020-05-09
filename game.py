import funcs
import sys
import names_lists


if len(sys.argv) == 1 or sys.argv[1] == 'quickgame':
    things = funcs.get_things_list()
    persons = funcs.get_persons_list()
    dressed_persons = funcs.setThings(things, persons)
    funcs.start_game(dressed_persons)
elif sys.argv[1] == 'custom':
    print('Включить отображение дополнительной информации (y/n)')
    debug_mode = input()
    if debug_mode == 'y':
        debug_mode == True
    else:
        debug_mode = False
    print('Включить медленный режим (y/n)')
    slow_mode = input()
    if slow_mode == 'y':
        slow_mode == True
    else:
        slow_mode = False
    print('Задайте количество сгенерированных вещей')
    number_of_things = int(input())
    space = ' '
    print(f'Какой пул имен для вещей будем использовать?\n' +
          f'{space.join(names_lists.things_names_lists.keys())}\n' +
          f'Введите номер пула (1 - {len(names_lists.things_names_lists)})')
    things_names_list = list(names_lists.things_names_lists.values())[
        int(input()) - 1]
    print('Задайте максимальный процент защиты для вещей')
    things_max_def_percent = int(input())
    print('Задайте максимальную атаку для вещей')
    things_max_attack = int(input())
    print('Задайте максимальное ХП для вещей')
    things_max_hp = int(input())

    print('Задайте количество сгенерированных персонажей')
    num_of_persons = int(input())
    
    print(f'Какой пул имен для персонажей будем использовать?\n' +
          f'{space.join(names_lists.persons_names_lists.keys())}\n' +
          f'Введите номер пула (1 - {len(names_lists.persons_names_lists)})')
    persons_names_list = list(names_lists.persons_names_lists.values())[
        int(input()) - 1]
    print('Задайте минимальное ХП для персонажей')
    persons_min_hp = int(input())
    print('Задайте максимальное ХП для персонажей')
    persons_max_hp = int(input())
    print('Задайте минимальную атаку для персонажей')
    persons_min_attack = int(input())
    print('Задайте максимальную атаку для персонажей')
    persons_max_attack = int(input())
    print('Задайте максимальный процент защиты для персонажей')
    persons_max_def_percent = int(input())

    things = funcs.get_things_list(
        number_of_things, things_names_list, things_max_def_percent, things_max_attack, things_max_hp)
    persons = funcs.get_persons_list(num_of_persons, persons_names_list,
                                     persons_min_hp, persons_max_hp, persons_min_attack, persons_max_attack, persons_max_def_percent)
    dressed_persons = funcs.setThings(things, persons)

    funcs.start_game(dressed_persons, debug_mode=debug_mode,
                     slow_mode=slow_mode)
