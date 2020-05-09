import random

NAME_POOL = ['Genji', 'Zarya', 'Zeratul', 'Raynor', 'Trall', 'Arthas', 'Commander Shepard', 'Garrus Vakarian', 'Ghost', 'Hulk Hogan',
             'Jinx', 'Pudge', 'Techies', 'Jett', 'Борис', 'Тетсуо', 'Меченый', 'Сидорович', 'Gordon Freeman', 'Link']

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
        self.isalive = True
        self.kills = []

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
        if self.hp <= 0:
            self.isalive = False
            print(f'{self.name} был убит.')

    def addKill(self, name):
        self.kills.append(name)


class Paladin(Person):
    def __init__(self, name, base_hp, base_attack, base_armor):
        super().__init__(name, base_hp, base_attack, base_armor)
        self.hp *= 2
        self.armor *= 2


class Warrior(Person):
    def __init__(self, name, base_hp, base_attack, base_armor):
        super().__init__(name, base_hp, base_attack, base_armor)
        self.attack *= 2


def normalize(value, scale_min, scale_max, range_min = 0.2, range_max = 2.5):
    return (value - range_min) / (range_max - range_min) * (scale_max - scale_min) + scale_min


def items_setup():
    items = []
    for i in range(40):
        #логнормальное распределение дает высокий шанс получить вещь со средними значениями,
        #и низкий шанс дать вещь с очень высокими либо низкими значениями
        armor_value = normalize(random.lognormvariate(0, 0.5), 0.01, 0.1)  #нормализация случайных значений до промежутка [0.01, 0.1]
        hp_value = normalize(random.lognormvariate(0, 0.5), 0.1, 0.3)
        attack_value = normalize(random.lognormvariate(0, 0.5), 0.05, 0.2)

        items.append(Thing(f'item_{i+1}', armor_value, hp_value, attack_value))

    return items


def contenders_setup():
    contenders = []
    items = items_setup()
    for _ in range(10):
        name = random.choice(NAME_POOL)
        NAME_POOL.remove(name)
        armor_value = normalize(random.lognormvariate(0, 1), 0.15, 0.4, 0, 10)
        hp_value = normalize(random.lognormvariate(0, 1), 75, 150, 0, 10)
        attack_value = normalize(random.lognormvariate(0, 1), 15, 35, 0, 10)

        contender = random.choice((Warrior, Paladin))(name, hp_value, attack_value, armor_value)

        contender_items = []
        for i in range(random.randint(1, 4)):
            new_item = random.choice(items)
            contender_items.append(new_item)
            items.remove(new_item)

        contender.setThings(contender_items)
        contenders.append(contender)
    
    return contenders


def print_contenders(contenders, verbose = False):
    if not verbose:
        for c in contenders:
            print(f'Name: {c.name}\nClass: {c.__class__.__name__}\n')
    else: 
        for c in contenders:
            print(f'Name: {c.name}\n\tClass: {c.__class__.__name__}\n\tHP: {c.hp:.2f}\n\tArmor: {c.armor*100:.2f}%\n\tAttack: {c.attack:.2f}\n\tItems:')
            for item in c.things:
                print(f'\t\tName: {item.name}\n\t\tHP: +{item.hp_boost*100:.2f}%\n\t\tArmor: +{item.armor_boost*100:.2f}%\n\t\tAttack: +{item.attack_boost*100:.2f}%\n')


def battle_loop(contenders):
    remaining = contenders.copy()
    round_counter = 0
    while len(remaining) > 1:
        round_counter += 1

        print(f'----РАУНД {round_counter}----')

        attacker = random.choice(remaining)
        defender = random.choice(remaining)
        while attacker == defender:
            defender = random.choice(remaining)

        print(f'{attacker.name} атакует {defender.name}')
        defender.attackedBy(attacker)

        if not defender.isalive:
            attacker.addKill(defender.name)
            remaining.remove(defender)

    print(f'\nБитва завершилась в {round_counter} раундов')
    print('Победитель:')
    print_contenders(remaining, verbose=True)
    return contenders


def print_scoreboard(contenders):
    contenders = sorted(contenders, key=lambda c: len(c.kills), reverse=True)
    print('-------------РЕЗУЛЬТАТЫ-------------')
    print('       Имя        |Убийства|  Жертвы')
    print('------------------------------------')
    for c in contenders:
        print(f'{c.name:18}|{len(c.kills):7} | {", ".join(c.kills)}')


if __name__ == '__main__':
    contenders = contenders_setup()
    print_contenders(contenders, verbose=True)
    result = battle_loop(contenders)
    print_scoreboard(result)
