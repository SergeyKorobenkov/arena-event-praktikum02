'''
Мини-игра "Арена".
'''
from random import randint, choice, sample
import requests

class Thing:
    '''
    Характеристики предмета.
    Показатель защиты хранится в десятичном виде, но поддерживается инициализация через проценты.
    '''
    def __init__(self, name, damage=0, defence=0, hp_bonus=0):
        if defence >= 1:
            defence /= 100
        assert defence >= 0 and defence <= 0.1, \
            "Показатель защиты предмета должен быть в интервале [0, 10]%"
        self.name = name
        self.damage = damage
        self.defence = defence
        self.hp_bonus = hp_bonus

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Person:
    '''
    Характеристики персонажа и взаимодействие с ними.
    Показатель защиты хранится в десятичном виде, но поддерживается инициализация через проценты.
    '''
    def __init__(self, name, base_damage=1, base_defence=0, base_hp=100):
        if base_defence >= 1:
            base_defence /= 100
        assert base_defence >= 0 and base_defence < 0.5, \
            "Базовая защита персонажа должна быть в интервале [0, 50)%"
        self.name = name
        self.base_damage = self.damage = base_damage
        self.base_defence = self.defence = base_defence
        self.base_hp = self.hp = base_hp
        self.things = []
        
    def set_thing(self, thing):
        '''
        Добавление предмета и расчёт новых характеристик.
        '''
        self.damage += thing.damage

        #Формула убывающей полезности. Новое значение стремится к 1, но никогда его не достигнет.
        self.defence += (1 - self.defence) * thing.defence
        assert self.defence < 1, "Самоликвидация вашей системы запущена. Осталось 30 секунд..."

        self.hp += thing.hp_bonus
        self.things.append(thing)

    def set_things(self, things):
        for thing in things:
            self.set_thing(thing)
    
    def del_thing(self, thing):
        '''
        Удаление предмета и возврат старых характеристик.
        '''
        self.damage -= thing.damage
        self.defence = (self.defence - thing.defence) / (1 - thing.defence) #things.defence != 1
        self.hp -= thing.hp_bonus
        self.things.remove(thing)

    def del_things(self, things):
        for thing in things:
            self.del_thing(thing)

    def receive_damage(self, damage):
        '''
        Персонаж получает урон.
        '''
        self.hp -= (1 - self.defence) * damage
    
    def hit(self, other):
        '''
        Персонаж наносит урон.
        '''
        other.receive_damage(self.damage)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
            
class Paladin(Person):
    '''
    Здоровье и базовая защита увеличены в 2 раза.
    '''
    def __init__(self, name, base_damage=1, base_defence=0, base_hp=100):
        super().__init__(name, base_damage, base_defence, base_hp)
        self.base_defence *= 2
        self.defence *= 2
        self.base_hp *= 2
        self.hp *= 2

class Warrior(Person):
    '''
    Урон увеличен в 2 раза.
    '''
    def __init__(self, name, base_damage=1, base_defence=0, base_hp=100):
        super().__init__(name, base_damage, base_defence, base_hp)
        self.base_damage *= 2
        self.damage *= 2

class Arena:
    '''
    Регистрация участников, выдача снаряжения и правила проведения боёв.
    При auto_setup=False необходимо вручную выполнить методы: init_things,
    init_persons и set_random_equipment для правильной подготовки арены.
    '''
    def __init__(self, num_things=0, num_persons=2, auto_setup=True):
        assert num_persons >= 2, "Арена - не подходящее место для самоубийства."
        self.num_things = num_things
        self.num_persons = num_persons
        self.things = []
        self.persons = []
        if auto_setup:
            self.init_things()
            self.init_persons()
            self.set_random_equipment()
    
    def init_things(self, names=None):
        '''
        Создание предметов с именами из списка names или с именами по умолчанию.
        '''
        names = names or []
        if len(names) < self.num_things:
            for i in range(self.num_things - len(names)):
                names.append(f'Unknown artifact {i+1}')
        else:
            names = sample(names, self.num_things)

        self.things = []
        for i in range(self.num_things):
            self.things.append(Thing(
                    name=names[i],
                    damage=randint(1, 10),
                    defence=randint(1, 10),
                    hp_bonus=randint(1, 10)
                ))
    
    def init_persons(self, names=None):
        '''
        Создание персонажей случайного класса с именами из списка names или с именами по умолчанию.
        '''
        names = names or []
        if len(names) < self.num_persons:
            for i in range(self.num_persons - len(names)):
                names.append(f'Nameless hero {i+1}')
        else:
            names = sample(names, self.num_persons)

        person_classes ={
            'Paladin' : Paladin,
            'Warrior' : Warrior,
        }
        self.persons = []
        for i in range(self.num_persons):
            person = choice(tuple(person_classes.keys()))
            self.persons.append(person_classes[person](
                    name=f'({person}) {names[i]}',
                    base_damage=randint(1, 80),
                    base_defence=randint(1, 20),
                    base_hp=randint(75, 100)
                ))

    def set_random_equipment(self):
        '''
        Случайным образом раздаем предметы участникам (максимум по 4 на человека).
        Если их больше, чем бойцы могут унести, то берём только нужное количество.
        '''
        if self.num_things > 4 * self.num_persons:
            things = sample(self.things, 4 * self.num_persons)
        else:
            things = self.things[::]
        persons = self.persons[::]
        while things and persons:
            person = choice(persons)
            if len(person.things) == 4:
                persons.remove(person)
                continue
            person.set_thing(things.pop())
    
    def fight(self):
        '''
        Из списка участников случайным образом выбирается пара, 
        которая наносит друг другу по удару и возвращается в исходную позицию.
        Бой идёт до тех пор, пока не останется один участник.
        '''
        while len(self.persons) > 1:
            print('-------------------------------------------------------')
            pair = sample(self.persons, 2)
            pair[0].hit(pair[1])
            print(f'<{pair[0].name}> наносит удар по <{pair[1].name}> на '
                f'{round((1 - pair[1].defence) * pair[0].damage, 2)} урона!')
            if pair[1].hp <= 0:
                self.persons.remove(pair[1])
                continue

            pair[1].hit(pair[0])
            print(f'<{pair[1].name}> наносит удар по <{pair[0].name}> на '
                f'{round((1 - pair[0].defence) * pair[1].damage, 2)} урона!')
            if pair[0].hp <= 0:
                self.persons.remove(pair[0])
        if self.persons:
            print(f'And the winner is {self.persons[0].name}. Congratulations!')


if __name__ == "__main__":
    hero_names = []
    response = requests.get('https://swapi.dev/api/people').json()
    for hero in response['results']:
        hero_names.append(hero['name'])
    while response['next']:
        response = requests.get(response['next']).json()
        for hero in response['results']:
            hero_names.append(hero['name'])
    
    arena = Arena(num_things=100, num_persons=20, auto_setup=False)
    arena.init_things()
    arena.init_persons(names=hero_names)
    arena.set_random_equipment()
    arena.fight()
    
