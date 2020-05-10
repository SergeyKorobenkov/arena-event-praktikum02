"""Модуль содержит классы для мини-игры "Арена"."""

import random as rnd


class Things:
    """
    Класс описывает объекты вещей персонажа.

    Класс содержит в себе следующие параметры -
    название, процент защиты, атаку и жизнь.
    """

    THING_DEF_MAX = 0.1  # максимальный процент защиты для одной вещи.

    def __init__(self, name, defence_pct, attack_damage, hitpoints):
        """
        Инициализирует экземпляр класса, экземпляр описывает один предмет.

        :param name: строка - имя предмета.
        :param defence_pct: float - процент защиты, который добавит персонажу
                            этот предмет.
        :param attack_damage: int - единицы атаки, которые предмет добавит
                              персонажу.
        :param hitpoints: int - количество hitpoint, которые предмет добавит
                              персонажу.
        """
        self.name = name
        self.hitpoints = hitpoints
        self.attack_damage = attack_damage
        # макс.процент защиты для одной вещи не должен превышать THING_DEF_MAX
        if defence_pct > self.THING_DEF_MAX:
            self.defence_pct = self.THING_DEF_MAX
        else:
            self.defence_pct = defence_pct


class Person:
    """
    Класс описывает базового персонажа.

    Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    Параметры передаются через конструктор.
    """

    # Согласно ТЗ, финальная защита складывается из базовой защиты и вещей
    # персонажа, при этом вещей может быть не более 4-х, а процент защиты
    # у одной вещи не более 0.1. Исходя из того, что стопроцентная защита
    # соответствует неуязвивому персонажу, а значит, не должна достигаться,
    # начальный процент защиты любого персонажа не должен превышать
    # 1 - (4 * 0.1) = 0.6. Т.к. существует персонаж с двойной защитой
    # относительно базового, то следует, что процент защиты рядового персонажа
    # не должен превышать 0.3
    BASE_DEFENCE_MAX = 0.29  # максимальная базовая защита рядового персонажа

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints):
        """
        Инициализирует экземпляр базового персонажа.

        :param name: строка - имя персонажа.
        :param base_defence_pct: float - процент защиты без использования
                                 предметов.
        :param base_attack_damage: int - сила атаки без использования
                                   предметов.
        :param hitpoints: int - количество 'жизни' без использования предметов.
        """
        self.name = name
        self.hitpoints = hitpoints
        self.things = []
        self.attack_damage = base_attack_damage
        # начальный процент защиты не должен превышать BASE_DEFENCE_MAX
        if base_defence_pct > self.BASE_DEFENCE_MAX:
            self.defence_pct = self.BASE_DEFENCE_MAX
        else:
            self.defence_pct = base_defence_pct

    def setThings(self, things):
        """
        Метод устанавливает список вещей персонажа.

        Метод заполняет атрибут things[] обекта класса Person, располагая при
        этом вещи в порядке возрастания значения Things.defence_pct.
        :param things: спсок из объектов класса Things.
        :return:
        """
        self.things = sorted(things, key=lambda items: items.defence_pct)

    def getDressed(self):
        """
        Метод 'одевает' персонаж, используя вещи из списка things[].

        Метод рассчитывает финальные значения hitpoints, атаки
        и процента защиты персонажа с учетом вещей из списка things[].
        :return:
        """
        for thing in self.things:
            self.defence_pct += thing.defence_pct
            self.attack_damage += thing.attack_damage
            self.hitpoints += thing.hitpoints

    def letsFight(self, attacker):
        """
        Метод для определения последствий атаки.

        Метод вычисляет количество получаемого урона после атаки.
        :param attacker: атакующий, объект класса Person или его
                         классов-наследников.
        :return: строка, содержащая количество урона в hitpoints.
        """
        damage = \
            attacker.attack_damage - attacker.attack_damage * self.defence_pct
        self.hitpoints -= damage

        return (f"{attacker.name} наносит удар по {self.name} "
                f"на {damage} урона")


class Paladin(Person):
    """
    Класс описывает персонажа 'Паладин'.

    Класс наследуется от персонажа, при этом количество присвоенных жизней
    и процент защиты умножается на def_factor=2 в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints,
                 def_factor=2.0):
        """
        Инициализирует экземпляр персонажа 'Паладин'.

        :param name: строка - имя персонажа.
        :param base_defence_pct: float - процент защиты без использования
                                 предметов.
        :param base_attack_damage: int - сила атаки без использования
                                   предметов.
        :param hitpoints: int - количество 'жизни' без использования предметов.
        :param def_factor: float - множитель для процента защиты, по умолчанию
                           равен 2.
        """
        super().__init__(name, base_defence_pct, base_attack_damage, hitpoints)
        self.defence_pct = self.defence_pct * def_factor


class Warrior(Person):
    """
    Класс описывает персонажа 'Воин'.

    Класс наследуется от персонажа, при этом атака умножается на att_factor=2
    в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints,
                 att_factor=2):
        """
        Инициализирует экземпляр персонажа 'Воин'.

        :param name: строка - имя персонажа.
        :param base_defence_pct: float - процент защиты без использования
                                 предметов.
        :param base_attack_damage: int - сила атаки без использования
                                   предметов.
        :param hitpoints: int - количество 'жизни' без использования предметов.
        :param att_factor: int - множитель для единиц атаки, по умолчанию
                           равен 2.
        """
        super().__init__(name, base_defence_pct, base_attack_damage, hitpoints)
        self.attack_damage = self.attack_damage * att_factor


if __name__ == "__main__":

    # Создаем вещи: name, defence_pct, attack_damage, hitpoints
    things_list = [
        ['Крылатая рогатка', 0.01, 11, 30],
        ['Нож Сириуса Блэка', 0.02, 12, 35],
        ['Вопящие носки', 0.03, 9, 23],
        ['Самовяжущие спицы', 0.04, 11, 18],
        ['Зеркало Сириуса', 0.05, 6, 17],
        ['Проявитель врагов', 0.05, 2, 27],
        ['Остроконечная шляпа', 0.06, 5, 47],
        ['Меч Гриффиндора', 0.07, 14, 39],
        ['Взрывающиеся хлопушки', 0.08, 7, 14],
        ['Измеритель угроз', 0.09, 10, 20]
    ]

    # Сортируем по проценту защиты, по возрастанию, как указано в ТЗ.
    things_list.sort(key=lambda thing: thing[1])

    # Создаем список имен персонажей
    pers_name_list = [
        'Karlsson', 'Aladdin', 'Jafar', 'Mickey Mouse',
        'Goofy', 'Bugs Bunny', 'Shrek', 'Scrat',
        'Panch Bob', 'Tom', 'Winnie-the-Pooh', 'Pikachu',
        'Scooby-Doo', 'Jerry', 'Pluto', 'Snoopy',
        'Donald Duck', 'Sonic', 'Simba', 'Pumbaa'
    ]

    # Создаем список типов персонажей
    pers_type_list = ['Paladin', 'Warrior']

    rnd.seed()

    # Создаем 10 персонажей
    pers_list = []
    temp_pers_name_list = list(pers_name_list)
    for i in range(10):
        # Выберем случайное имя из списка имен.
        pers_name = rnd.choice(temp_pers_name_list)
        # Создадим персонажа случайного типа из списка типов pers_type_list
        # и случайными параметрами в эмпирически выбранных диапазонах.
        pers_list.append(eval(rnd.choice(pers_type_list))
                         (name=pers_name,
                          base_defence_pct=rnd.uniform(0.1, 0.29),
                          base_attack_damage=rnd.randint(10, 20),
                          hitpoints=rnd.randint(200, 300))
                         )
        # Удалим использованное имя из временного списка, для исключения
        # участия в бою персонажей с одинаковыми именами.
        temp_pers_name_list.remove(pers_name)

    # Раздаём вещи персонажам.
    for pers in pers_list:
        # Создадим список, который заполним вещами и передадим персонажу.
        pers_things_list = []
        # Скопируем список вещей во временный список, из которого будем
        # удалять уже выбранные вещи.
        temp_things_list = list(things_list)
        # Каждому персонажу выдаем случайно от 1 до 4-х вещей.
        for i in range(rnd.randint(1, 4)):
            next_thing = rnd.choice(temp_things_list)
            pers_things_list.append(Things(next_thing[0], next_thing[1],
                                           next_thing[2], next_thing[3]))
            # Удалим уже выбранную вещь из последующего выбора для этого
            # персонажа, чтобы у персонажа не было двух одинаковых вещей.
            temp_things_list.remove(next_thing)

        pers.setThings(pers_things_list)
        #  Применяем вещи для каждого персонажа.
        pers.getDressed()

    # В бой!
    # Битва до тех пор, пока не останется единственный победитель.
    while len(pers_list) > 1:
        # Случайно выбираем защищающегося персонажа.
        defensive_pers = rnd.choice(pers_list)
        # На время боя убираем из списка защищающегося, чтобы исключить бой
        # с самим собой.
        pers_list.remove(defensive_pers)
        # Случайно выбираем атакующего персонажа.
        offensive_pers = rnd.choice(pers_list)

        print(defensive_pers.letsFight(offensive_pers))
        # Если hitpoints персонажа не исчерпаны - возвращаем его на арену,
        # иначе - сообщаем о победе атакующего.
        if defensive_pers.hitpoints > 0:
            pers_list.append(defensive_pers)
        else:
            print(f"{defensive_pers.name} повержен!")
        # Если остался один, то он - победитель.
        if len(pers_list) == 1:
            print(f"{offensive_pers.name} - победитель!")
