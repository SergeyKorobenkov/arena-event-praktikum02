import random


class Thing:
    def __init__(self, name, defence, damage, HP):
        self.name = name
        self.defence = defence
        self.damage = damage
        self.HP = HP


class Person:
    def __init__(self, name, HP, damage, defence):
        self.name = name
        self.defence = defence
        self.damage = damage
        self.HP = HP


class Paladin(Person):
    def __init__(self, name, HP, damage, defence):
        HP = HP * 2
        damage = damage * 2
        Person.__init__(self, name, HP, damage, defence)


class Warrior(Person):
    def __init__(self, name, HP, damage, defence):
        defence = defence * 2
        Person.__init__(self, name, HP, damage, defence)


class Game:
    def __init__(self):
        self.person_records = []
        self.thing_records = []

    def add_person_record(self, record):
        self.person_records.append(record)

    def add_thing_record(self, record):
        self.thing_records.append(record)

    def setThings(self):
        n = 0
        for person in self.person_records:
            quantity = random.randint(1, 4)
            random_things = random.sample(self.thing_records, quantity)
            sum_defence = 0
            sum_HP = 0
            sum_damage = 0
            for thing in random_things:
                sum_defence = sum_defence + thing.defence
                sum_HP = sum_HP + thing.HP
                sum_damage = sum_damage + thing.damage
            self.person_records[n].defence = self.person_records[n].defence + sum_defence
            self.person_records[n].HP = self.person_records[n].HP + sum_HP
            self.person_records[n].damage = self.person_records[n].damage + sum_damage
            n += 1

    def setPerson(self):
        random_persons = random.sample(self.person_records, 2)
        attacker_index = random.randint(0, 1)
        defender_index = abs(attacker_index - 1)
        print(
            f'Начинается рауд игрока {random_persons[attacker_index].name} против игрока {random_persons[defender_index].name}')
        while random_persons[defender_index].HP > 0 and random_persons[attacker_index].HP > 0:
            damage_amount = round(
                (random_persons[attacker_index].damage - random_persons[attacker_index].damage * random_persons[defender_index].defence), 2)
            random_persons[defender_index].HP = round(
                (random_persons[defender_index].HP - damage_amount), 2)
            print(
                f'{random_persons[attacker_index].name} наносит удар по игроку {random_persons[defender_index].name} на {damage_amount} урона')
            attacker_index = defender_index
            defender_index = abs(attacker_index - 1)
        print(f"{random_persons[attacker_index].name} Выбывает из игры")
        self.person_records.remove(random_persons[attacker_index])

    def battle(self):
        while len(self.person_records) > 1:
            game.setPerson()
        print(f"{self.person_records[0].name} Побеждает всех!")


game = Game()
game.add_thing_record(Thing(name='Молот', defence=0.02, damage=0.02, HP=0.13))
game.add_thing_record(Thing(name='Броня', defence=0.01, damage=0.03, HP=0.31))
game.add_thing_record(Thing(name='Шляпа', defence=0.03, damage=0.04, HP=0.21))
game.add_thing_record(Thing(name='Меч', defence=0.04, damage=0.02, HP=0.12))
game.add_thing_record(Thing(name='Шлем', defence=0.06, damage=0.01, HP=0.30))
game.add_person_record(Warrior(name='Лошадь', HP=5, damage=0.04, defence=0.25))
game.add_person_record(Warrior(name='Морж', HP=5, damage=0.02, defence=0.31))
game.add_person_record(Warrior(name='Кролик', HP=3, damage=0.01, defence=0.21))
game.add_person_record(Warrior(name='Сова', HP=2, damage=0.02, defence=0.27))
game.add_person_record(Warrior(name='Лиса', HP=2, damage=0.05, defence=0.41))
game.add_person_record(Paladin(name='Медведь', HP=3, damage=0.3, defence=0.32))
game.add_person_record(Paladin(name='Тигр', HP=5, damage=0.06, defence=0.11))
game.add_person_record(Paladin(name='Змея', HP=2, damage=0.02, defence=0.31))
game.add_person_record(Paladin(name='Лев', HP=6, damage=0.03, defence=0.01))
game.add_person_record(Paladin(name='Акула', HP=4, damage=0.03, defence=0.12))


game.battle()
