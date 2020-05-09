import random


class Thing:
    """Класс предмет.
    
    name (str): название,
    health (int): добавка к здоровью,
    attack (int): добавкак атаке,
    defence (int): добавка к защите.
    """
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.health = health


class Person:
    """Базовый класса персонажа.
    
    name (str): имя,
    health (int): базовое здоровье,
    base_attack (int): базовая атака,
    base_defence (int): базовая защита.
    """
    def __init__(self, name, health, base_attack, base_defence):
        self._equipment = []
        self.name = name
        self._health = health
        self._attack = base_attack
        self._defence = base_defence
        self.final_health = self._health
        self.final_attack = self._attack
        self.final_protection = self._defence

    def show_equipment(self):
        """Показать экипировку."""
        for eq in self._equipment:
            print(f'{eq.name: <25} ATK:{eq.attack:<3}' 
                    f' DEF:{eq.defence:<3} HP:{eq.health:<3}')
        
    def show_stats(self):
        """Показать характеристики."""
        print(f'{self.name:<10} ATK:{self.final_attack:<3}'
                f' DEF:{self.final_protection:<3} HP:{self.final_health:<3}')

    @property
    def alive(self):
        """Статус жизни."""
        if self.final_health > 0:
            return True
        else:
            return False

    def setThings(self, things):
        """Надеть вещи.
        
        things (list): вещи
        """
        self._equipment = things
        for item in things:
            self.final_health += item.health
            self.final_attack += item.attack
            self.final_protection += item.defence
            if self.final_protection > 99:
                self.final_protection = 99
    
    def get_damage(self, amount):
        """Получить урон.
        
        amount (int): количество.
        """
        self.final_health -= amount


class Paladin(Person):
    """Класс паладина.
    
    Здоровье *2
    Защита *2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._health = health * 2
        self._defence = base_defence * 2


class Warrior(Person):
    """Класс Война.
    
    Урон *2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._attack = base_attack * 2
        

class Assassin(Person):
    """Класс паладина.
    
    Урон *4
    Защита /2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._attack = base_attack * 4
        self._health = health // 2


def items_gen(def_limit=10, limit=50):
    """Генерация предметов.
    
    def_limit (int): верхний предел для защиты,
    limit (int): верхний предел для здоровья/атаки.
    """
    random.seed()
    equipment = []
    items_names = ['Life Ring', 'Ring of Favor', 'Ring of Steel Protection',
        'Flame Stoneplate Ring', 'Thunder Stoneplate Ring', 'Calamity Ring',
        'Magic Stoneplate Ring', 'Dark Stoneplate Ring', 'Fleshbite Ring',
        'Speckled Stoneplate Ring', 'Bloodbite Ring', 'Young Dragon Ring', 
        'Poisonbite Ring', 'Cursebite Ring', 'Wood Grain Ring', 'Wolf Ring',
        'Priestess Ring', 'Red Tearstone Ring', 'Blue Tearstone Ring', 
        'Leo Ring', 'Ring of Sacrifice' 
    ]
    for i in range(30):
        rand_name = random.choice(items_names)
        rand_def = random.randint(1, def_limit)
        rand_atk = random.randint(1, limit)
        rand_health = random.randint(1, limit)
        equipment.append(Thing(rand_name, rand_health, rand_atk, rand_def))
    equipment = sorted(equipment, key=lambda item: item.defence, reverse=True)
    return equipment

def chars_gen():
    """Генерация персонажей."""
    random.seed()
    char_names = [
        'Mesald', 'Aldfred', 'Antol', 'Waruwulf', 'Mark',
        'Padon', 'Kimcome', 'Sagar', 'Gar', 'Lau',
        'Eka', 'Warddic', 'Seankim', 'Aregel', 'Cwencar',
        'Docan', 'Lege', 'Wise', 'Grimand', 'Leofuha'
    ]
    characters = []
    rand_names = random.sample(char_names, 10)
    for i in range(10):
        rand_class = random.choice(Person.__subclasses__())
        def_limit = 99 if rand_class is Warrior else 49
        rand_defence = random.randint(1, def_limit)
        rand_attack = random.randint(1, 100)
        rand_health = random.randint(100, 1000)
        char = rand_class(rand_names[i], rand_health, rand_attack, rand_defence)
        characters.append(char)
    return characters

def equip(chars, items):
    """Экипировка персонажей.
    
    chars : персонажи,
    items (list) : список предметов.
    """
    random.seed()
    for char in chars:
        items_amount = random.randint(1, 4)
        char.setThings(random.sample(items, items_amount))
        
def fight_arena(characters):
    """Битва на арене.
    
    characters : персонажи.
    """
    while len(characters) > 1:
        attack_char, defence_char = random.sample(characters, 2)
        attack_char.show_stats()
        print('--ПРОТИВ--')
        defence_char.show_stats()
        defence = defence_char.final_protection
        attack = attack_char.final_attack
        damage = attack - attack // defence
        defence_char.get_damage(damage)
        print(f'{attack_char.name} наносит {damage} урона {defence_char.name}.')
        print()
        if not defence_char.alive:
            characters.remove(defence_char)
            print(f'{defence_char.name} убит.', end='\n\n')
    print(f'Победитель арены: {characters[0].name}.')


equipment = items_gen()
characters = chars_gen()
equip(characters, equipment)
fight_arena(characters)
