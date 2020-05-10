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
        self.final_health = health
        self.final_attack = base_attack
        self.final_protection = base_defence

    def show_equipment(self):
        """Показать экипировку."""
        for eq in self._equipment:
            print(
                f'{eq.name: <25}'               #название 
                f'ATK: {eq.attack:<3} '         #атака 
                f'DEF: {eq.defence:<3} '        #защита 
                f'HP: {eq.health:<3}'           #здоровье 
            )
        
    def show_stats(self):
        """Показать характеристики."""
        print(
            f'{self.name :<10}'                 #имя
            f'{type(self).__name__:<15}'        #класс
            f'ATK: {self.final_attack:<3} '     #атака
            f'DEF: {self.final_protection:<3} ' #защита
            f'HP: {self.final_health:<3}'       #здоровье 
            )

    def get_damage(self, amount):
        """Получить урон.
        
        amount (int): количество.
        """
        self.final_health -= amount

    def _equip_sum(self):
        """Пересчитать характеристики персонажа"""
        __hp = 0
        __atk = 0
        __def = 0
        for item in self._equipment:
            __hp += item.health
            __atk += item.attack
            __def += item.defence
            if __def > 99:
                __def = 99
        self.final_health = self._health + __hp
        self.final_attack = self._attack + __atk 
        self.final_protection = self._defence + __def

    def set_things(self, things):
        """Надеть вещи.
        
        things (list): вещи
        """
        for thing in things:
            self._equipment.append(thing)
        self._equip_sum()

    def take_things(self):
        """Забрать первую вещь"""
        __item = None
        if self._equipment:
            __item = self._equipment.pop(0)
        self._equip_sum()
        return __item

    def have_things(self):
        "Есть ли вещи."
        if len(self._equipment) > 0:
            return True
        else:
            return False

    @property
    def alive(self):
        """Статус жизни."""
        if self.final_health > 0:
            return True
        else:
            return False


class Paladin(Person):
    """Класс паладина.
    
    Здоровье *2
    Защита *2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._health = health * 2
        self._defence = base_defence * 2
        self.final_health = self._health
        self.final_defence = self._defence


class Warrior(Person):
    """Класс война.
    
    Урон *2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._attack = base_attack * 2
        self.final_attack = self._attack
        

class Assassin(Person):
    """Класс ассасина.
    
    Урон *4
    Защита /2
    """
    def __init__(self, name, health, base_attack, base_defence):
        super().__init__(name, health, base_attack, base_defence)
        self._attack = base_attack * 4
        self._health = health // 2
        self.final_attack = self._attack
        self.final_health = self._health


class Arena:
    """Класс арена"""
    def __init__(self):
        self._characters = []
        self._equipment = []

    def items_gen(self, def_limit=10, limit=50):
        """Генерация предметов.
    
        def_limit (int): верхний предел для защиты,
        limit (int): верхний предел для здоровья/атаки.
        """
        items_names = ['Life Ring', 'Ring of Favor', 'Ring of Steel Protection',
            'Flame Stoneplate Ring', 'Thunder Stoneplate Ring', 'Calamity Ring',
            'Magic Stoneplate Ring', 'Dark Stoneplate Ring', 'Fleshbite Ring',
            'Speckled Stoneplate Ring', 'Bloodbite Ring', 'Young Dragon Ring', 
            'Poisonbite Ring', 'Cursebite Ring', 'Wood Grain Ring', 'Wolf Ring',
            'Priestess Ring', 'Red Tearstone Ring', 'Blue Tearstone Ring', 
            'Leo Ring', 'Ring of Sacrifice' 
        ]
        random.seed()
        for i in range(30):
            rand_name = random.choice(items_names)
            rand_def = random.randint(1, def_limit)
            rand_atk = random.randint(1, limit)
            rand_hp = random.randint(1, limit)
            self._equipment.append(Thing(rand_name, rand_hp, rand_atk, rand_def))
        self._equipment = sorted(self._equipment, 
                                    key=lambda x: x.defence, reverse=True)
        
    def chars_gen(self, atk_limit=100, hp_limit=1000):
        """Генерация персонажей.
        
        atk_limit (int): верхний предел атаки,
        hp_limit (int): верхний предел здоровья.
        """
        char_names = [
            'Mesald', 'Aldfred', 'Antol', 'Waruwulf', 'Mark',
            'Padon', 'Kimcome', 'Sagar', 'Gar', 'Lau',
            'Eka', 'Warddic', 'Seankim', 'Aregel', 'Cwencar',
            'Docan', 'Lege', 'Wise', 'Grimand', 'Leofuha'
        ]
        random.seed()
        rand_names = random.sample(char_names, 10)
        for i in range(10):
            rand_class = random.choice(Person.__subclasses__())
            def_limit = 25 if rand_class is Paladin else 50
            rand_def = random.randint(1, def_limit)
            rand_atk = random.randint(50, 100)
            rand_hp = random.randint(500, 1000)
            char = rand_class(rand_names[i], rand_hp, rand_atk, rand_def)
            self._characters.append(char)
        
    def equip(self):
        """Экипировка персонажей."""
        for char in self._characters:
            items_amount = random.randint(1, 4)
            char.set_things(random.sample(self._equipment, items_amount))

    def show_participants(self):
        """Показать данные участников"""
        for char in self._characters:
            char.show_stats()

    def fight(self, detailed=True):
        """Битва на арене.
        
        detailed (bool): показывать детали боя.
        """
        print('-------НАЧАЛО БИТВЫ----------------------------')
        round = 1
        random.seed()
        while len(self._characters) > 1:
            print(f'------ {round} РАУНД ---------------------------')
            attacker, defencer = random.sample(self._characters, 2)
            if detailed:
                attacker.show_stats()
                print('-------ПРОТИВ---------------------------------')
                defencer.show_stats()
                print('----------------------------------------------')
            defence = defencer.final_protection
            attack = attacker.final_attack
            damage = attack - attack * defence // 100
            defencer.get_damage(damage)
            print(f'{attacker.name} наносит {damage} урона {defencer.name}.')
            break_item =  random.randint(0, 100) < 70
            find_item = random.randint(0, 100) < 50
            if break_item and defencer.have_things():
                thing = defencer.take_things()
                print(f'{defencer.name} теряет предмет "{thing.name}".')
                if find_item:
                    lis_thing = []
                    lis_thing.append(thing)
                    attacker.set_things(lis_thing)
                    print(f'{attacker.name} находит предмет "{thing.name}".')
            if not defencer.alive:
                self._characters.remove(defencer)
                print(f'{defencer.name} убит.', end='\n')
            round += 1
            print()
        print(f'Победитель арены: {self._characters[0].name}.')


arena = Arena()
arena.items_gen()
arena.chars_gen()
arena.equip()
arena.fight()



