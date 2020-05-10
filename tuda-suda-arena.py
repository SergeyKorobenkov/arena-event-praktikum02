import random

class Thing:
    def __init__(self, name, armor_boost, attack_boost, hp_boost):
        self.name = name
        self.armor_boost = armor_boost
        self.attack_boost = attack_boost
        self.hp_boost = hp_boost

class Person:
    def __init__(self, name, base_hp, base_attack, base_armor):
        self.name = name
        self.hp = base_hp
        self.attack = base_attack
        self.armor = base_armor
        self.kills = []
        self.iswinner = False

    def setThings(self, things):
        self.things = things
        hp_boost, attack_boost, armor_boost = (0, 0, 0)
        #вычисляем общий бонус статов
        for thing in self.things:
            hp_boost += thing.hp_boost
            attack_boost += thing.attack_boost
            armor_boost += thing.armor_boost

        self.armor += armor_boost
        self.hp *= 1 + hp_boost
        self.attack *= 1 + attack_boost

    def attackedBy(self, other):
        damage = other.attack - other.attack*self.armor
        print(f'{other.name} наносит удар по {self.name} на {damage:.2f} урона')
        self.hp -= damage

    def addKill(self, name):
        self.kills.append(name)

    def isalive(self):
        if self.hp <= 0:
            print(f'{self.name} был убит.')
            return False
        return True

    def showMe(self):
        print(f'Name: {self.name}\n\t'
              f'Class: {self.__class__.__name__}\n\t'
              f'HP: {self.hp:.2f}\n\t'
              f'Armor: {self.armor*100:.2f}%\n\t'
              f'Attack: {self.attack:.2f}\n\tItems:')
        for item in self.things:
                print(f'\t\tName: {item.name}\n\t\t'
                f'HP: +{item.hp_boost*100:.2f}%\n\t\t'
                f'Armor: +{item.armor_boost*100:.2f}%\n\t\t'
                f'Attack: +{item.attack_boost*100:.2f}%\n')


class Paladin(Person):
    def __init__(self, name, base_hp, base_attack, base_armor):
        super().__init__(name, base_hp, base_attack, base_armor)
        self.hp *= 2
        self.armor *= 2


class Warrior(Person):
    def __init__(self, name, base_hp, base_attack, base_armor):
        super().__init__(name, base_hp, base_attack, base_armor)
        self.attack *= 2


class Arena:
    def __init__(self, name_pool):
        self.items = self.items_setup()
        self.contenders = self.contenders_setup(name_pool)

    def items_setup(self):
        items = []
        for i in range(40):
            #логнормальное распределение дает высокий шанс получить вещь со средними значениями,
            #и низкий шанс дать вещь с очень высокими либо низкими значениями
            armor_value = normalize(random.lognormvariate(0, 0.5), 0.01, 0.1)  #нормализация случайных значений до промежутка [0.01, 0.1]
            hp_value = normalize(random.lognormvariate(0, 0.5), 0.1, 0.3)
            attack_value = normalize(random.lognormvariate(0, 0.5), 0.05, 0.2)

            items.append(Thing(f'item_{i+1}', armor_value, hp_value, attack_value))

        return items

    def contenders_setup(self, name_pool):
        contenders = []
        for _ in range(10):
            name = random.choice(name_pool)
            name_pool.remove(name)
            armor_value = normalize(random.lognormvariate(0, 1), 0.15, 0.4, 0, 10)
            hp_value = normalize(random.lognormvariate(0, 1), 75, 150, 0, 10)
            attack_value = normalize(random.lognormvariate(0, 1), 15, 35, 0, 10)

            contender = random.choice((Warrior, Paladin))(name, hp_value, attack_value, armor_value)

            contender_items = []
            for i in range(random.randint(1, 4)):
                new_item = random.choice(self.items)
                contender_items.append(new_item)
                self.items.remove(new_item)

            contender.setThings(contender_items)
            contenders.append(contender)
        
        return contenders

    def battle_loop(self):
        remaining = self.contenders.copy()
        round_counter = 0
        while len(remaining) > 1:
            round_counter += 1

            print(f'----РАУНД {round_counter}----')

            attacker, defender = random.sample(remaining, 2)

            print(f'{attacker.name} атакует {defender.name}')
            defender.attackedBy(attacker)

            if not defender.isalive():
                attacker.addKill(defender.name)
                remaining.remove(defender)

        print(f'\nБитва завершилась в {round_counter} раундов')
        print('Победитель:')
        remaining[0].iswinner = True
        remaining[0].showMe()

    def print_contenders(self, verbose = False):
        if not verbose:
            for c in self.contenders:
                print(f'Name: {c.name}\nClass: {c.__class__.__name__}\n')
        else: 
            for c in self.contenders:
                c.showMe()

    def print_scoreboard(self):
        sorted_contenders = sorted(self.contenders, key=lambda c: len(c.kills), reverse=True)
        print('-------------РЕЗУЛЬТАТЫ-------------')
        print('         Имя          |Убийства|  Жертвы')
        print('------------------------------------')
        for c in sorted_contenders:
            print(f'{f"**{c.name}**" if c.iswinner else c.name:22}|{len(c.kills):7} | {", ".join(c.kills)}')


def normalize(value, scale_min, scale_max, range_min = 0.2, range_max = 2.5):
    return (value - range_min) / (range_max - range_min) * (scale_max - scale_min) + scale_min


if __name__ == '__main__':
    name_pool = ['Genji', 'Zarya', 'Zeratul', 'Raynor', 'Trall', 'Arthas', 'Commander Shepard', 
                'Garrus Vakarian', 'Ghost', 'Hulk Hogan','Jinx', 'Pudge', 'Techies', 'Jett', 
                'Борис', 'Тетсуо', 'Меченый', 'Сидорович', 'Gordon Freeman', 'Link']

    arena = Arena(name_pool)
    arena.print_contenders()
    arena.battle_loop()
    arena.print_scoreboard()
