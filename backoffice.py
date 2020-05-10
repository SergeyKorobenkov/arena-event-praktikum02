"""
Вспомогательный блог организации боёв.
"""
import random
from gamers.settings import ArenaSet, warrior_name, things_new
from gamers.warrior import Paladin, Warrior, Thing


def create_things(*, amount_things: int) -> list:
    """
    Функция создаёт список вещей для воинов
    на основе предустановленого словаря.
    :param amount_things: По-умолчанию количество генерируемых
    вещей берётся из настроек, если не указано в параметре иное.
    :return: Список объектов классов Things.
    """

    key_things = list(things_new.keys())
    things = list()
    for th in range(0, amount_things):
        if len(key_things) < 1:
            break

        rnd_key_things = random.choice(key_things)
        if rnd_key_things in ArenaSet.THINGS_UNIQUE:
            key_things.remove(rnd_key_things)
        rnd_things = random.choice(things_new[rnd_key_things])
        # Параметры
        things_ready = Thing(
            title=rnd_things,
            life=random.randint(0, ArenaSet.THINGS_MAX_LIFE),
            attack=round(random.uniform(0.01, ArenaSet.THINGS_MAX_ATTACK), 2)
            if rnd_key_things in ArenaSet.THINGS_ATTACK else 0,
            armor=round(random.uniform(0.01, ArenaSet.THINGS_MAX_ARMOR), 2)
        )
        things.append(things_ready)

    return things


def create_persons() -> list:
    """
    Создание списка объектов персонажей для битвы на арене.
    Количество персонажей устанавливается настройками игры.
    Персонажи сразу укомплектовываются вещами.
    :return: Список персонажей, готовых к бою.
    """

    warrior = list()
    for name in random.sample(warrior_name, ArenaSet.MAX_WARRIOR):
        # Вещи.
        rnd_point = random.randint(ArenaSet.MIN_PERSON_THINGS,
                                   ArenaSet.MAX_PERSON_THINGS)
        things = create_things(amount_things=rnd_point)

        # Персонаж.
        rnd_point = random.choice([Paladin, Warrior])
        person = rnd_point(name=name)
        person.set_things(things)
        warrior.append(person)

    return warrior


def war_of_war(warriors: list):
    """
    Распорядитель игр. Управляет процессом до выявления
    победителя.
    :param warriors: Список объектов класса Person игроков.
    :return: Объект класса Person победителя.
    """

    print('\n***** НАЧАЛО БОЁВ *****\n')

    while len(warriors) > 1:
        random.shuffle(warriors)
        aggressor = warriors[0]
        defender = warriors[1]

        defender.set_life_count(aggressor.attack)
        if defender.life <= ArenaSet.RATE_DEATH:
            message = f'* BOOM! Выбыл игрок {defender.name}!\n'\
                      f'Не помогли {", ".join(defender.things_titles)}...\n'
            print(message)
            warriors.pop(1)
        else:
            warriors[1] = defender

    return warriors[0]
