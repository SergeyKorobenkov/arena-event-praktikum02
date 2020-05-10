import random


class Person:
    def __init__(self, name, base_health, base_attack, base_df):
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_df = base_df
        self.name = name

    def set_things(self, things):
        for thing in things:
            self.base_health += thing.health
            self.base_attack += thing.attack
            self.base_df += thing.df_percentage

    def set_damage(self, attack_pers):
        damage = attack_pers.base_attack - attack_pers.base_attack * self.base_df
        self.base_health = (self.base_health - damage)
        print(f'({attack_pers.name} наносит удар по {self.name} на {damage:.2f} урона)')


class Thing:
    def __init__(self, name, df_percentage, attack, health):
        self.name = name
        self.df_percentage = df_percentage
        self.attack = attack
        self.health = health


class Paladin(Person):
    def __init__(self, name, base_health, base_attack, base_df):
        super().__init__(name, base_health, base_attack, base_df)
        self.base_health *= 2
        self.base_df *= 2


class Warrior(Person):
    def __init__(self, name, base_health, base_attack, base_df):
        super().__init__(name, base_health, base_attack, base_df)
        self.base_attack *= 2


class Generator:
    @staticmethod
    def generate_thing():
        name = Generator.generate_thing_name()
        df_percentage = round(random.uniform(0, 0.1), 2)
        attack = random.randint(3, 10)
        health = random.randint(40, 100)
        return Thing(name, df_percentage, attack, health)

    @staticmethod
    def generate_pers(pers):
        name = Generator.generate_person_name()
        base_df = round(random.uniform(0, 0.2), 2)
        base_attack = random.randint(5, 10)
        base_health = random.randint(60, 100)
        if pers == Warrior:
            return Warrior(name=name, base_df=base_df, base_attack=base_attack, base_health=base_health)
        elif pers == Paladin:
            return Paladin(name=name, base_df=base_df, base_attack=base_attack, base_health=base_health)

    @staticmethod
    def generate_person_name():
        person_names = ('Swift', 'Go', 'PHP', 'C++', 'Python',
                        'JavaScript', 'Java', 'C#', 'Kotlin',
                        'Rust', 'Ruby', 'Clojure', 'Crystal', 'Elixir',
                        'Haskell', 'APL', 'Perl', 'Visual Basic',
                        'SQR', 'SAS')
        return random.choice(person_names)

    @staticmethod
    def generate_thing_name():
        first_word = (
            "chunky",
            "smily"
        )
        second_word = (
            "axe",
            "bow"
        )
        return random.choice(first_word) + " " + random.choice(second_word)


class Arena:
    def __init__(self, perses):
        self.perses = perses
        self.battle_round = []

    def wear_pers(self):
        for pers in self.perses:
            thing_list = [Generator.generate_thing() for _ in range(1, random.randint(2, 4))]
            pers.set_things(thing_list)

    def battle(self):
        self.battle_round = [random.choice(self.perses) for _ in range(2)]
        while len(self.battle_round) > 1:
            attacker = random.choice(self.battle_round)
            if self.battle_round.index(attacker) == 0:
                index = 1
                defender = self.battle_round[index]
            else:
                index = 0
                defender = self.battle_round[index]
            if defender.base_health <= 0:
                self.perses.pop(self.perses.index(defender))
                self.battle_round.pop(index)
                print(f'Battle winner: {attacker.name}')
                break
            if attacker == defender:
                break
            defender.set_damage(attacker)


if __name__ == "__main__":
    pers_list = [random.choice([Generator.generate_pers(Paladin), Generator.generate_pers(Warrior)]) for _ in range(10)]
    battle_arena = Arena(pers_list)
    battle_arena.wear_pers()
    while len(battle_arena.perses) > 1:
        battle_arena.battle()
    print(f'Winner: {battle_arena.perses[0].name}')
