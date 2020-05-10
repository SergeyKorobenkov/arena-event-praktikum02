from collections import OrderedDict
import random
# from Arena_game import Paladin, Warrior

THINGS = {
    'object1':{
        'name': 'object1',
        'protection': '0.17',
        'attack': '0.12',
        'life': 3
    },
    'object2':{
        'name': 'object2',
        'protection': '0.06',
        'attack': '0.312',
        'life': 4
    },
    'object3':{
        'name': 'object3',
        'protection': '0.11',
        'attack': '0.154',
        'life': 5
    },
    'object4':{
        'name': 'object4',
        'protection': '0.42',
        'attack': '0.13',
        'life': 6
    },
    'object5':{
        'name': 'object5',
        'protection': '0.35',
        's,
        'life': 2
    },
    'object6':{
        'name': 'object6',
        'protection': '0.45',
        'attack': '0.15',
        'life': 3
    }
}

sorted_things = OrderedDict(sorted(THINGS.items(), key=lambda x: x[1]['protection'], reverse=True))

PERSONS ={
    'person1':{
        'name': 'person1',
        'protection': '0.02',
        'attack': '0.12',
        'lives': 3
    },
    'person2':{
        'name': 'person2',
        'protection': '0.06',
        'attack': '0.312',
        'lives': 4
    },
    'person3':{
        'name': 'person3',
        'protection': '0.07',
        'attack': '0.154',
        'lives': 5
    },
    'person4':{
        'name': 'person4',
        'protection': '0.04',
        'attack': '0.13',
        'lives': 6
    },
    'person5':{
        'name': 'person5',
        'protection': '0.9',
        'attack': '0.24',
        'lives': 2
    },
    'person6':{
        'name': 'person6',
        'protection': '0.45',
        'attack': '0.15',
        'lives': 3
    }
}

sorted_persons = OrderedDict(sorted(PERSONS.items(), key=lambda x: x[1]['attack'], reverse=True))


# class Person:
#     def __init__(self, name, lives, attack, protection):
#         self.name = name
#         self.lives = lives
#         self.attack = attack
#         self.protection = protection
#         print(f"Создан новый персонаж {name}")

#     def setPerson():
#         for person in PERSONS:
#             list_persons = list(PERSONS.keys())
#             random_persons = random.sample(list_persons, 2)
#             return random_persons

#     def show(self):
#         print(f'Имя: {self.name}, количество жизней: {self.lives}, базовая атака: {self.attack}, базовый процент защиты: {self.protection}')


# class Paladin(Person):
#    def __init__(self, name, lives, attack, protection):
#        lives = int(lives) * 2
#        protection = float(protection) * 2
#        Person.__init__(self, name, lives, attack, protection)


# class A():
#     def __init__(self, data=''):
#        self.data = data

#     def __str__(self):
#        return str(self.data)

# def make_dict():
#     for person in PERSONS:
#         d = {}
#         for value in PERSONS.values():
#             for items in a:
#                 a = {}
#             asds = Paladin(a)
#             a[value].append(asds)
            

#         d[person].append(a)
        # elem = Paladin(value())
    # print(d)
# d[elem] = 'person1'

# a ={'name': 'person6',
#     'protection': '0.45',
#     'attack': '0.15',
#     'lives': 3}


# print(d[elem])
# print(PERSONS[values].values())
# make_dict()

# d = ('тигр', 'лев', 'волк', 'лиса')
# a = [b() for er in PERSONS.values()]
# objs = [Paladin(a) for i in d]
# for obj in objs:
#     other_object.add(obj)

# objs[0].do_sth()

# def setPerson():
#     random_persons=[]
#     for person in sorted_persons:
#         list_persons = list(sorted_persons.keys())
#         random_persons = random.sample(list_persons, 2)
#         return random_persons


# def setThings():
#     for things in sorted_things:
#         list_things = list(sorted_things.keys())
#         quantity = random.randint(1, 4)
#         global random_things
#         random_things = random.sample(list_things, quantity)
#         return random_things

# print(setPerson())
# print(setThings())
# print(setThings())