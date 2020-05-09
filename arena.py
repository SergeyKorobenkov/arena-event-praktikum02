

class Thing:
    def __init__(self, thing_name: str, protection_thing=0.1, thing_attack=1,
                 thing_life=20
                 ):
        self.thing_name = thing_name
        self.protection_thing = protection_thing
        self.thing_attack = thing_attack
        self.thing_life = thing_life


class Person:
    def __init__(self, name, hp = 1, person_attack=1, protection_person=100):
        self.name = name
        self.hp = hp
        self.person_attack = person_attack
        self.protection_person = protection_person

    def setThings(self, *things):
        raise NotImplementedError    
    
    def attack(self):
        raise NotImplementedError

class Paladin(Person):
    def __init__(self, name, hp = 1, person_attack=1, protection_person=100):
        super().__init__(name, hp * 2, person_attack, protection_person * 2)
    


class Warrior:
    def __init__(self, name, hp = 1, person_attack=1, protection_person=100):
        super().__init__(name, hp, person_attack * 2, protection_person)



