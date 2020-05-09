from operator import attrgetter
import random
import classes
import names_lists
from time import sleep
import colorama
from colorama import Back, Style, Fore
colorama.init()


def get_things_list(number_of_things=random.randrange(100, 300),
                    names_list=names_lists.things_names_lists['Стандартный набор'], max_def_percent=10, max_attack=10, max_hp=100):
    things_list = []
    for thing in range(0, number_of_things):
        name = random.choice(names_list)
        defence_percent = random.uniform(0, max_def_percent)
        attack = random.uniform(0, max_attack)
        hp = random.uniform(0, max_hp)
        thing = classes.Thing(name, defence_percent, attack, hp)
        things_list.append(thing)

    asc_ordered_by_def_precent = sorted(
        things_list, key=attrgetter('defence_percent'))
    return asc_ordered_by_def_precent


def create_persons(person_type, num_of_persons, names_list=names_lists.persons_names_lists['Стандартный набор'], min_hp=100, max_hp=300, min_attack=5, max_attack=15, max_def_percent=15):
    persons_list = []
    persons_uniq_names_list = names_list
    for person in range(0, num_of_persons):
        name = random.choice(persons_uniq_names_list)
        persons_uniq_names_list.remove(name)
        hp = random.randrange(min_hp, max_hp)
        attack = random.randrange(min_attack, max_attack)
        defence_percent = random.randrange(0, max_def_percent)
        if person_type == 'Paladin':
            person = classes.Paladin(name, hp, attack, defence_percent)
        elif person_type == 'Warrior':
            person = classes.Warrior(name, hp, attack, defence_percent)
        persons_list.append(person)

    return persons_list


def get_persons_list(num_of_persons=10, names_list=names_lists.persons_names_lists['Стандартный набор'], min_hp=100, max_hp=300, min_attack=5, max_attack=15, max_def_percent=15):
    persons_list = []
    paladins_number = random.randrange(0, num_of_persons)
    warriors_number = num_of_persons - paladins_number

    persons_list = create_persons(
        'Paladin', paladins_number, names_list, min_hp, max_hp, min_attack, max_attack, max_def_percent) + create_persons('Warrior', warriors_number, names_list, min_hp, max_hp, min_attack, max_attack, max_def_percent)

    return persons_list


def setThings(things, persons, max_things=4):
    for person in persons:
        number_of_things_for_person = random.randrange(1, max_things)
        for _ in range(0, number_of_things_for_person):
            thing = random.choice(things)
            person.hp += thing.hp
            person.attack += thing.attack
            person.defence_percent += thing.defence_percent

    return persons


def subtract_hp(attacker, defender):
    damage = attacker.attack - attacker.attack * \
        (defender.defence_percent / 100)
    defender.hp = defender.hp - damage
    return damage


def start_game(dressed_persons, debug_mode=False, slow_mode=False):
    pair = []
    while len(dressed_persons) > 1:
        pair = random.sample(dressed_persons, 2)
        attacker_number = random.randint(0, 1)
        defender_number = 1 - attacker_number
        damage = subtract_hp(pair[attacker_number], pair[defender_number])

        print(
            f'{pair[attacker_number].name} наносит удар по {pair[defender_number].name} на {round(damage, 2)} урона')

        if debug_mode:
            print('\nАтакующий персонаж\n' +
                  f'Имя {pair[attacker_number].name} ХП {round(pair[attacker_number].hp, 2)} ' +
                  f'атака {round(pair[attacker_number].attack, 2)} защита {round(pair[attacker_number].defence_percent, 2)}\n' +
                  'Защищающийся\n' +
                  f'Имя {pair[defender_number].name} ХП {round(pair[defender_number].hp, 2)} ' +
                  f'атака {round(pair[defender_number].attack, 2)} защита {round(pair[defender_number].defence_percent, 2)}\n')

        if pair[defender_number].hp <= 0:
            dressed_persons.remove(pair[defender_number])
            if len(dressed_persons) == 9:
                print(Back.RED + '\nПервая кровь!' + Style.RESET_ALL)
            print(Fore.YELLOW +
                  f'\nПерсонаж {pair[defender_number].name} был убит {pair[attacker_number].name} :(\n' + Style.RESET_ALL)

        if slow_mode:
            sleep(1)

    print(Back.WHITE + Fore.BLACK +
          f'Персонаж {dressed_persons[0].name} остался в живых, с {round(dressed_persons[0].hp, 2)} хп! Поздравляем!' + Style.RESET_ALL)
