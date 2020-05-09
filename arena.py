import random
import copy

class Thing():

    def __init__(self, name, protection_perc, life):
        self.name            = name
        self.protection_perc = protection_perc
        self.life            = life


class Person():

    def __init__(self, name, life_amnt, attack_damage, protection):
        self.name             = name
        self.life             = life_amnt
        self.protection       = protection
        self.attack_damage    = attack_damage
        self.thingsList       = []

    def setThings(self, thing):
        self.thingsList.append(thing)

    def lifeChange(self, damage):
        self.life -= damage


class Palladin(Person):

    def __init__(self, name, life_amnt, attack_damage, protection):
        super().__init__(name, life_amnt, attack_damage, protection)
        self.life               *= 2
        self.protection         *= 2


class Warrior(Person):

    def __init__(self, name, life_amnt, attack_damage, protection):
        super().__init__(name, life_amnt, attack_damage, protection)
        self.attack_damage     *= 2

'''=================================================================================================================='''

if __name__ == '__main__':

    names = ['Locki', 'Burtlebee', 'Dmitro', 'Vasil', 'Mikola', 'Platon', 'Pankrat', 'Luboslav',
             'Viktor', 'Elisei', 'Koljan', 'Petro', 'Ermolai', 'Germogen', 'Pafnutii', 'Mitrofan',
             'Artemii', 'Ivan', 'Semen', 'Lucifer']

    max_entities = random.randint(100,200)
    things = []
    persons= []
    for i in range(max_entities):
        name    = f'thing-{i}'
        percent = random.uniform(0.01, 0.1)
        life    = random.uniform(0.2, 0.3)

        things.append(Thing(name,round(percent,3), life))

    def sortByProtection(thing):
        return thing.protection_perc
    things.sort(key=sortByProtection)


    '''================='''
    def createPers():
        def getValidName():
            name = random.choice(names)

            existingNamesList = []
            for pers in persons:
                existingNamesList.append(pers.name)
            while name in existingNamesList:
                name = random.choice(names)
            return name

        pers_type   = random.randint(0,1)
        name        = getValidName()
        life        = 1
        attack      = random.uniform(0.2, 0.3)
        protection  = random.uniform(0.09, 0.15)

        if pers_type == 0:
            return Palladin(name, life, attack, protection)
        else:
            return Warrior(name, life, attack, protection)


    for c in range(0, 10):
        persons.append(createPers())

    '''================='''
    for pers in persons:
        things_amnt = random.randint(1,4)
        for c in range(0, things_amnt):
            pers.setThings(random.choice(things))


    while len(persons) > 1:
        #print(f'длина списка бойцов = {len(persons)}')
        attack_fighter = random.choice(persons)
        defend_fighter = attack_fighter
        while attack_fighter == defend_fighter:
            defend_fighter = random.choice(persons)

        finalProtection = defend_fighter.protection
        lifedelta       = 0
        for th in defend_fighter.thingsList:
            finalProtection += (1 - finalProtection) * th.protection_perc
            lifedelta += th.life

        damage_sum = attack_fighter.attack_damage * (1 - finalProtection)
        defend_fighter.life -= damage_sum

        print(f'{attack_fighter.name} наносит удар по {defend_fighter.name} на {round(damage_sum,5)} урона.')               #' У {defend_fighter.name} осталось собственной жизни: {defend_fighter.life}. А запас жизни от вещей: {lifedelta}')

        remainDefendingLife = defend_fighter.life + lifedelta
        if remainDefendingLife <= 0:
            persons.remove(defend_fighter)


    print(f'\n\nПобедитель гигантского замеса: {persons[0].name}')



