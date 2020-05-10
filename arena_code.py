import random


class Thing:
    def __init__(self, name, protection, damage, hp):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.hp = hp


class Person:
    def __init__(self, name, hp=100, base_protection=10, base_damage=10):
        self.name = name
        self.protection = base_protection
        self.damage = base_damage
        self.hp = hp

    def setThings(self, things):
        for thing in things:
            self.hp += thing.hp
            self.damage += thing.damage
            self.protection += (100-self.protection) * (thing.protection/100)
        if self.protection > 99:
            self.protection = 99

    def receive_damage(self, attacker):
        incoming_damage = attacker.damage * (100 - self.protection) / 100
        self.hp -= incoming_damage
        print(f'{attacker.name} наносит удар по {self.name} на {round(incoming_damage, 2)} урона')


class Warrior(Person):
    def __init__(self, name, hp=100, base_protection=10, base_damage=10):
        super().__init__(name, hp, base_protection, base_damage)
        self.damage = base_damage * 2


class Paladin(Person):
    def __init__(self, name, hp=100, base_protection=10, base_damage=10):
        super().__init__(name, hp, base_protection, base_damage)
        self.hp = hp * 2
        self.protection = base_protection * 2


def create_items():
    item_list = []
    for i in range (1, 101):
        item_name = f'Item_{i}'
        item_protection = random.randint(0, 10)
        item_damage = random.randint(0, 30)
        item_hp = random.randint(0, 100)
        item = Thing(item_name, item_protection, item_damage, item_hp)
        item_list.append(item)
    return sorted(item_list, key=lambda x: x.protection)


def create_fighters():
    name_list = ['Lumpy Space Princess', 'Eric Cartman', 'Kenny', 'Mileena',
             'Mikhail Boyarsky', 'Sub Zero', 'Scorpion', 'Optimus Prime',
             'Kitana', 'Wonderwoman', 'Valentina Tereshkova', 'X Æ A-12',
             'Uwe Boll', 'Tinto Brass', "Ner'zhul", 'Cersei',
             "Jaqen H'ghar", 'Bobby B', 'Beelzebub', 'Kobe Bryant']
    class_list = [Paladin, Warrior]
    fighter_list = []

    for name in random.sample(name_list, 10):
        fighter_class = random.choice(class_list)
        fighter_hp = random.randint(100, 300)
        fighter_protection = random.randint(0, 30)
        fighter_damage = random.randint(5, 50)
        fighter = fighter_class(name, fighter_hp, fighter_protection, fighter_damage)
        fighter_list.append(fighter)
    return fighter_list


def equip_fighters(fighters, items):
    guaranteed_item_list = items[:len(fighters)]
    additional_item_list = items[len(fighters):]
    for fighter in fighters:
        items = []
        guaranteed_item = random.choice(guaranteed_item_list)
        guaranteed_item_list.remove(guaranteed_item)
        items.append(guaranteed_item)
        for qty in range(random.randint(0, 3)):
            try:
                additional_item = random.choice(additional_item_list)
                additional_item_list.remove(additional_item)
                items.append(additional_item)
            except IndexError:
                break
        fighter.setThings(items)


def start_battle(participants):
    while len(participants) > 1:
        pair = random.sample(participants, 2)
        attacker = pair[0]
        victim = pair[1]
        victim.receive_damage(attacker)
        if victim.hp <= 0:
            print(f'{victim.name} убит!')
            participants.remove(victim)
    print(f'{participants[0].name} стал Чемпионом Арены!')


def main():
    fighters = create_fighters()
    items = create_items()
    equip_fighters(fighters, items)
    start_battle(fighters)


if __name__ == "__main__":
    main()
