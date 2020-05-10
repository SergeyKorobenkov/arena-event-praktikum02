import random

class Things:
    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life


class Person:
    list_of_persons = []
    def __init__(self, name, HitPoints , attack_damage, protection):
        self.name = name
        self.HitPoints  = HitPoints 
        self.attack_damage = attack_damage
        self.protection = protection
        self.finalProtection = protection
        Person.list_of_persons.append(self)

    def setThings(self, *things):
        for thing in things:
            self.finalProtection += thing.protection

    def life_leastening(self, attacker):
        damage = attacker.attack_damage - self.attack_damage * (self.finalProtection / 100)
        self.HitPoints -= damage
        if self.HitPoints <= 0:
            Person.list_of_persons.remove(self)
        return f'{attacker.name} наносит удар по {self.name} на {round(damage, 2)} урона'


class Paladin(Person):
    def __init__(self, name, HitPoints, attack_damage, protection):
        super().__init__(name, 2 * HitPoints, attack_damage, 2 * protection)


class Warrior(Person):
    def __init__(self, name, HitPoints, attack_damage, protection):
        super().__init__(name, HitPoints, 2 * attack_damage, protection)


hat = Things('hat', 5, 5, 2)
trousers = Things('trousers', 7, 3, 5)
boots = Things('boots', 8, 1, 4)
shirt = Things('shirt', 9, 4, 1)
coat = Things('coat', 10, 3, 2)

list_of_names = ['JAMES', 'JOHN', 'ROBERT', 'MICHAEL', 'WILLIAM', 'DAVID',
                 'RICHARD', 'CHARLES', 'JOSEPH', 'THOMAS', 'CHRISTOPHER',
                 'DANIEL', 'PAUL', 'MARK', 'DONALD', 'GEORGE',  'KENNETH',
                 'STEVEN', 'EDWARD', 'BRIAN']

person1 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person2 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person3 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person4 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person5 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person6 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person7 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person8 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person9 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))
person10 = Person(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))

warrior = Warrior(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 50))

paladin = Paladin(random.choice(list_of_names), random.randint(1, 10), random.randint(1, 10), random.randint(1, 49))

person1.setThings(hat)
person2.setThings(coat)
person3.setThings(hat, coat)
person4.setThings(hat, trousers)
person5.setThings(hat, coat, trousers)
person6.setThings(coat, trousers)
person7.setThings(hat, boots)
person8.setThings(boots, shirt)
person9.setThings(hat, coat, trousers, boots)
person10.setThings(coat)

paladin.setThings(coat, boots, shirt)

while len(Person.list_of_persons) > 1:
    [attacker, defender] = random.sample(Person.list_of_persons, 2)
    print(defender.life_leastening(attacker))

