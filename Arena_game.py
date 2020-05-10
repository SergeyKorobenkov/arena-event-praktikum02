from data import sorted_things, sorted_persons
import random

class Things:
    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life
        # print(f"Создан новый артефакт {name}")



    # def show(self):
        # print(f"Название: {self.name}, Процент защиты: {self.protection}, атака: {self.attack}, жизнь: {self.life}")


class Person:
    def __init__(self, name, lives, attack, protection):
        self.name = name
        self.lives = lives
        self.protection = protection
        self.thingsList = self.setThings()
        self.attack = attack
        # print(f"Создан новый персонаж {name}")
        # print(self.thingsList)

    def setThings(self):
        for things in sorted_things:
            list_things = list(sorted_things.keys())
            quantity = random.randint(1, 4)
            # global random_things
            random_things = random.sample(list_things, quantity)
        return random_things

# armour = Things(name='Броня', protection='0.2', attack='0.03', life='0.33')

    def things_value(self):
        attack_sum = self.attack
        for thing in self.thingsList:
            # for item in thing:
                # if item.keys() is not 'name':
            attack_sum = attack_sum + float(thing.attack)
        return attack_sum



    # def show(self):
        # print(f'Имя: {self.name}, количество жизней: {self.lives}, базовая атака: {self.attack}, базовый процент защиты: {self.protection}')



class Paladin(Person):
   def __init__(self, name, lives, attack, protection):
       lives = int(lives) * 2
       protection = float(protection) * 2
       Person.__init__(self, name, lives, attack, protection)



class Warrior(Person):
   def __init__(self, name, lives, attack, protection):
    #    attack = float(attack) * 2 + 
       Person.__init__(self, name, lives, attack, protection)

bear = Warrior(name='Медведь', lives=3, attack='0.3', protection='0.32')
print(bear.things_value())
print(bear.attack)


# class Game(Things, Person):

#     def setPerson():
#         global random_persons
#         random_persons=[]
#         for person in sorted_persons:
#             list_persons = list(sorted_persons.keys())
#             random_persons = random.sample(list_persons, 2)
#             return random_persons


#     def give_things_to_person():
#         pass

    # role = ['Attacker', 'Defender']
    # role_random = random.choice(role)
    # if role_random == 'Defender':
    #     def attack_damage:
    #         pass



# armour = Things(name='Броня', protection='0.2', attack='0.03', life='0.33')
# bear = Warrior(name='Медведь', lives=3, attack='0.3', protection='0.32')
# horse = Paladin(name='Лошадь', lives=4, attack='0.11', protection='0.25')
# tiger = Warrior(name='Тигр', lives=5, attack='0.16', protection='0.11')
# monkey = Paladin(name='Обезьяна', lives=5, attack='0.61', protection='0.41')
# rabbit= Paladin(name='Кролик', lives=4, attack='0.31', protection='0.41')
# snake = Warrior(name='Змея', lives=6, attack='0.22', protection='0.31')
# hat = Things(name='Шляпа', protection='0.3', attack='0.03', life='0.33')
# snikers = Things(name='Сникерс', protection='0.3', attack='0.02', life='0.43')
# armour = Things(name='Броня', protection='0.2', attack='0.03', life='0.33')
# armour.show()
# bear.show()
# horse.show()
# tiger.show()
# monkey.show()
# rabbit.show()
# snake.show()
# hat.show()
# snikers.show()

