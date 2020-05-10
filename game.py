import random, time


class Thing:
    def add_things(self, count):
        things_name = ['Средняя броня', 'нож', "кирпич", "Легкая броня", "ремень", "бронижелет", "бутылка", "куртка", "носки", "Тяжелая броня", "шлем", "брюки", "хомяк", "удочка", 
        "ботинки", "грабли", "щит", "меч", "коробка", 'Двуручные топоры', 'Экзотическое оружие', 'Огнестрельное оружие', 'Магия Огня', 'Магия Жизни', 'Алхимия']
        things = []    
        print('Создаем атрибуты для персонажей')
        time.sleep(1)
        print('Название атрибута,   защита,         атака,                  жизнь')
        for i in range(count):
            property = {}
            name = random.choice(things_name)
            protection = random.randint(0, 10)
            attack = random.randint(1, 20)
            life = random.randint(0, 50)
            print(name + '               ' + str(protection) + '               ' + str(attack) + '                    ' + str(life))
            time.sleep(1)
            things.append([name, protection, attack, life])
        return things


class Person:
    vars_list = []
    def __init__(self, name_person):
        self.name_person = name_person
        self. base_protection = random.randint(0, 10)
        self.base_attack = random.randint(10, 30)
        self.hp = random.randint(20, 60)
        
    def info(self):
        print(self.vars_list)
  
   
    def setThings(self, things):
         for var in self.vars_list:
            if len(things) > 0:
                try:
                    for i in range(random.randint(1, 4)):
                        thin = (random.choice(things))
                        time.sleep(1)
                        print(f' Воин {var[0]} получает предмет {thin[0]}')
                        var[1] += thin[1]
                        if var[1] > 100:
                            var[1] = 100
                        var[2] += thin[2]
                        if var[2] > 100:
                            var[2] = 100
                        var[3] += thin[3]
                        if var[3] > 100:
                            var[3] = 100
                        index = things.index(thin)
                        things.pop(index)
                        print(f'Новый уровень воина {var}')
                        time.sleep(1)
                        
                except:
                        print('Предметов больше нет')
            else:
                break

    def wars(self):
        try:
            war1 = list(self.vars_list[0])
            war2 =list(self.vars_list[1])
            time.sleep(1)
            print(f'Сражение воина {war1[0]} и воина {war2[0]}')
            time.sleep(1)
            war1_attack_damage = war1[2]-war2[1]
            war2_attack_damage = war2[2]-war1[1]
            i = 0
            while i < 1:                
                war2[3] -= war1_attack_damage
                time.sleep(1)
                print(f'Воин {war1[0]} наносит удар по воину {war2[0]} на {war1_attack_damage} урона')
                time.sleep(1)
                if war2[3] >= 0:
                    war1[3] -= war2_attack_damage
                    time.sleep(1)
                    print(f'Воин {war2[0]} наносит удар по воину {war1[0]} на {war2_attack_damage} урона')
                    time.sleep(1)
                    if war1[3] <= 0:
                        print(f'{war1[0]} побежден(')
                        time.sleep(1)
                        self.vars_list.pop(self.vars_list.index(self.vars_list[0]))
                        print(f'Осталось участников {len(self.vars_list)}')
                        time.sleep(1)
                        break
                else:
                    print(f'{war2[0]} побежден(') 
                    time.sleep(1)
                    self.vars_list.pop(self.vars_list.index(self.vars_list[1]))
                    
                    print(f'Осталось участников {len(self.vars_list)}')
                    break
        except:
            time.sleep(1)
            print(f'Победитель - {self.vars_list[0][0]}')            


class Paladin(Person):
    def add_person(self):
        self. base_protection = self.base_protection * 2
        self.hp = self.hp * 2
        self.vars_list.append([self.name_person, self.base_protection, self.base_attack, self.hp])
        time.sleep(1)
        print(f'Cоздан Защитник по имени {self.name_person}, уровень защиты: {self.base_protection}, уровень атаки: {self.base_attack}, количество жизни: {self.hp}')
        

    def info(self):
        print(self.vars_list)
        


class Warrior(Person):
    def add_person(self):
        self.base_attack = self.base_attack * 2
        self.vars_list.append([self.name_person, self.base_protection, self.base_attack, self.hp])
        time.sleep(1)
        print(f'Cоздан Нападающий по имени {self.name_person}, уровень защиты: {self.base_protection}, уровень атаки: {self.base_attack}, количество жизни: {self.hp}')
        
        
    def info(self):
        print(self.vars_list)



names_person = ['Агутин Леонид', 'Аллегрова Ирина', 'Билан Дима', 'Брежнева Вера', 'Газманов Олег', 'Глызин Алексей', 'Дорн Иван', 'Ёлка', 'Жуков Рома', 'Зинчук Виктор (гитарист)', 'Корнелюк Игорь', 'Лепс Григорий', 'Моисеев Борис', 'Александр Овечкин', 'Роман Абрамович', 'Алла Пугачева', 'Мария Шарапова', 'Владимир Высоцкий', 'Валентин Юдашкин', 'Федор Бондарчук']

person = Person('1')

i = 0
while i < 10:
    pal_war = random.randint(0, 1)
    if pal_war == 0:
        name = random.choice(names_person)
        Paladin(name).add_person()
        names_person.pop(names_person.index(name))
        i += 1
    elif pal_war == 1:
        name = random.choice(names_person)
        Warrior(name).add_person()
        names_person.pop(names_person.index(name))
        i += 1


person.setThings(Thing().add_things(random.randint(10, 30)))
for i in range(10):
    person.wars()




