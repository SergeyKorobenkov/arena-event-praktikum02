from random import choice

from world.settings import HACKATONE_MODE, WAREHOUSE_ITEMS


class PersonNameGenerator:
    def __init__(self):
        self.name_list = self.make_dict_from_file()

    def make_dict_from_file(self):
        name_list = {'male': [], 'female': []}

        with open('world/persons_name', 'r', encoding='utf-8') as namefilelist:
            gender = 'male'
            for name in namefilelist:
                if name.strip() == '@female':
                    gender = 'female'
                    continue
                name_list[gender].append(name.strip())
        return name_list

    def give_name(self):
        gender = choice(['male', 'female'])
        return gender, choice(self.name_list[gender])


class ThingsNameGenerator:
    def __init__(self):
        self.things_name = self.make_set_from_file()

    def make_set_from_file(self):
        things_name = set()
        with open('world/things_name_adj', 'r', encoding='utf-8') as f:
            adj = set()
            for line in f:
                adj.add(line.strip())
        with open('world/things_name_subj', 'r', encoding='utf-8') as f:
            subj = set()
            for line in f:
                subj.add(line.strip())
        adj = tuple(adj)
        for _ in range(len(subj)):
            things_name.add(choice(adj) + ' ' + subj.pop())

        return things_name

    def take_name(self):
        if len(self.things_name) > 1:
            return self.things_name.pop()
        else:
            return '____ИМЕНА ЗАКОНЧИЛИСЬ____'


def greetings_msg(fighters):
    s = "Поприветствуем участников битвы!\n"
    for i, f in enumerate(fighters):
        s += str(i + 1) + " "
        s += str(f) + "\n"
    s += '---'
    return s


def warehouse_storage_msg(warehouse):
    s = f'На нашем складе нашлось [{WAREHOUSE_ITEMS}]:\n'
    s += warehouse.items()
    return s


def things_to_fighters_msg(fighters):
    s = '---\nНачинаем раздачу:'
    for fighter in fighters:
        s += '\n' + fighter.name + " получает: "
        if fighter.items:
            for thing in fighter.items:
                s += thing.name + ', '
        else:
            s += 'шиш с маслом'
    return s


def mode_msg():
    if HACKATONE_MODE:
        return 'Game mode for yandex.hackatone\n==========='
    else:
        return 'Extended game mod enabled\n==========='


def make_hit_msg(attacker, deffender, def_hp, atk_dmg):
    if HACKATONE_MODE:
        atk_item = '\b'
        def_item = '\b'
    else:
        if attacker.atk_item is None:
            atk_item = 'руками'
        else:
            atk_item = attacker.atk_item.name
        if deffender.def_item is None:
            def_item = 'беззащитному телу'
        else:
            def_item = deffender.def_item.name

    return (f'{attacker.name} наносит удар {atk_item} по {def_item} '
            f'{deffender.name}[{def_hp}HP] на {atk_dmg}')


def broke_def_item_msg(deffender, item, attacker):
    return f'\n# У {deffender} вышел из строя {item} от ударов {attacker}\n'


def broke_atk_item_msg(attacker, item, deffender):
    return f'\n# У {attacker} разломался {item} о защиту {deffender}\n'


def fighter_is_dead_msg(person):
    return f'@@@\n\t[XXX]\t {person.name} падает без сил, ' \
           f'бойца тут же уносят мурлоки\n@@@'
