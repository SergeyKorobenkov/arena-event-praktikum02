from random import sample, randint
from operator import attrgetter


class Item:
    def __init__(self, name, def_perc, atk):
        self.name = name
        self.def_perc = def_perc
        self.atk = atk


class Weapon(Item):
    def __init__(self, name, def_perc, atk):
        super().__init__(name, def_perc, atk)
        self.cls = 'weapon'


class Armor(Item):
    def __init__(self, name, def_perc, atk):
        super().__init__(name, def_perc, atk)
        self.cls = 'armor'


class Thing:
    dict_names = {'Sword': Weapon("Slave's shortsword", 0.03, 5),
                  'Spear': Weapon("Slave's spear", 0.02, 5),
                  'Morgenstern': Weapon("Slave's morgenstern", 0, 5),
                  'Club': Weapon("Slave club", 0, 3),
                  'Chain Male': Armor("Slave's Chain Male", 0.09, 0),
                  'Breast Plate': Armor("Slave's Breast Plate", 0.09, 0),
                  'Hard Leather Armor': Armor("Hard Leather Armor", 0.05, 0),
                  'Shield': Armor('Wooden Shield', 0.04, 2)
                  }

    def __init__(self, amount):
        self.amount = amount

    def randomize(self):
        random_things = []
        while self.amount > 0:
            random_things.append(sample(
                list(self.dict_names.values()), 1)[0])
            self.amount -= 1
        random_things = sorted(random_things, key=attrgetter('def_perc'))
        return random_things


class Person:
    def __init__(self, name, hp, base_attack, base_def_perc):
        self.name = name
        self.hp = hp
        self.base_atk = base_attack
        self.base_def_perc = base_def_perc
        self.stack = []
        self.equipment = []
        self.status = ['Naked', 'Weaponless']
        self.items_count = 0
        self.finalProtection = self.base_def_perc
        self.atk = self.base_atk

    def set_things(self, obj):
        while self.items_count > 0:
            self.stack.append(obj)
            self.items_count -= 1

    def equipping(self):
        for item in self.stack:
            if self.status[0] == 'Naked' and item.cls == 'armor':
                self.status[0] = f'{item.name} equipped'
            elif self.status[1] == 'Weaponless' and item.cls == 'weapon':
                self.status[1] = f'{item.name} equipped'
            self.atk += item.atk
            self.finalProtection += item.def_perc
            self.equipment.append(item)
            self.stack.remove(item)

    def taking_damage(self, person):
        damage = int(person.atk * (1 - self.finalProtection))
        self.hp -= damage
        return damage

    def attacking(self):
        return self.atk


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_def_perc):
        super().__init__(name, hp, base_attack, base_def_perc)
        self.hp *= 2
        self.base_def_perc *= 2


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_def_perc):
        super().__init__(name, hp, base_attack, base_def_perc)
        self.base_atk *= 2


class Arena:
    items_amount = randint(10, 40)
    gladiators_amount = 10
    gladiators_names = ['Maximillian The Last', 'Gurv of The Northern Winds',
                        'Huvert THe Bravest', 'Baven From The East',
                        'Brut The Traitor', 'Vurd From The Far-Away Galaxy',
                        'Norbert The Judge', 'Nuby From The East',
                        'John The Saint', 'Fafnir From The Wild Tribes',
                        'Billy The Stranger', 'Goldberg From The Bloody Hell',
                        'Boris The Russian', 'Wultberg From The Void',
                        'Choiji The Fat', 'Gwin From The Ancient City',
                        'Michael The Archangel', 'Dave The Barbarian',
                        'Caesar The Killed', 'Unknown From The Nowhere']

    def __init__(self):
        self.free_items = Thing(self.items_amount).randomize()
        self.fighters = []
        self.fighters_choose()

        for fighter in self.fighters:
            fighter.items_count = self.items_amount // 10
        for fighter in self.fighters:
            while fighter.items_count > 0:
                idx = randint(0, len(self.free_items)-1)
                fighter.set_things(self.free_items.pop(idx))
                fighter.equipping()
        print('Добро пожаловать на Арену! Сегодня у нас будут сражаться: ' +
              ', \n'.join(fighter.name for fighter in self.fighters) + '!')
        print('Let the game begin!')
        while len(self.fighters) > 1 :
            self.battle(sample(self.fighters, 2))
        print(f'Победитель сегодняшнего турнира: {self.fighters[0].name}!')

    def fighters_choose(self):
        id_name = sample([j for j in range(0, len(self.gladiators_names))],
                         self.gladiators_amount)
        for i in range(0, self.gladiators_amount):
            if id_name[i] % 2 == 0:
                self.fighters.append(
                    Paladin(self.gladiators_names[id_name[i]], 30, 1, 0.01)
                )
            else:
                self.fighters.append(
                    Warrior(self.gladiators_names[id_name[i]], 30, 1, 0.01)
                )

    def battle(self, pair):
        attack = pair[0]
        defencive = pair[1]
        damage = defencive.taking_damage(attack)
        print(f'{attack.name} наносит удар по {defencive.name} на {damage} '
              f'урона')
        if defencive.hp <= 0:
            text = ['Очередной кусок мяса под именем', 'К сожалению,',
                    'Подобно зайцу, убегающему от волка ', 'Наконец-то!',
                    'С прискорбием сообщаю Вам', f'Для {attack.name} было '
                                                 f'легко сделать всё'
                                                 f'возможное, чтобы']
            print(f'{text[randint(0, len(text))]} {defencive.name} '
                  f'был повержен.')
            self.fighters.remove(defencive)


test1 = Arena()
