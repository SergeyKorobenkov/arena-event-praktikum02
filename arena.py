import random


class Thing: 
    def __init__(self, cl_name, cl_health, cl_protect):  
        self.cl_name = cl_name
        self.cl_health = cl_health
        self.cl_protect = cl_protect
        
        
class Person:

    def __init__(self, name, health, attack, protect):  
        self.name = name
        self.health = health
        self.attack = attack
        self.protect = protect
        self.things = []
        self.finalProtection = self.protect
        self.finalHealth = self.health
        
    def add_thing(self, thing):
        self.things.append(thing)
        self.finalProtection += thing.cl_protect
        self.finalHealth += thing.cl_health

    def attack_damage(self1, self2):
        attack_hp = self1.attack - self1.attack * self2.finalProtection
        return attack_hp
        
    def print_p(self):
        print(f'Имя бойца - {self.name}, атака - {self.attack}, здоровье - {self.finalHealth}, защита - {int(round(self.finalProtection,2)*100)} %') 

    def pers_hp(self): 
        return self.finalHealth  
   
    def war(self1,self2):
        while self2.finalHealth != 0 or self1.finalHealth != 0:
            self2.finalHealth = Person.pers_hp(self2) - Person.attack_damage(self1, self2)
            if self2.finalHealth < 0:
                print(f'{self1.name} атаковал {self2.name}, {self2.name} погиб')
                sp1.remove(self2)
                break
            else:
                print(f'{self1.name} атаковал {self2.name}, у {self2.name} осталось {self2.finalHealth } HP')      
            self1.finalHealth = Person.pers_hp(self1) - Person.attack_damage(self2, self1)
            if self1.finalHealth < 0:
                print(f'{self2.name} атаковал {self1.name}, {self1.name} погиб')
                sp1.remove(self1)
                break
            else:
                print(f'{self2.name} атаковал {self1.name}, у {self1.name} осталось {self1.finalHealth } HP')
            if self2.finalHealth < 0 or self1.finalHealth < 0:
                self2.finalHealth = 0
                self1.finalHealth = 0


class Paladin(Person):

    def __init__(self, name, health, attack, protect): 
        super().__init__(self, name, health, attack)    
        self.name = name
        self.attack = attack
        self.things = []
        self.finalProtection = protect * 2
        self.finalHealth = health * 2


class Warrior(Person): 

    def __init__(self, name, health, attack, protect): 
        super().__init__(self, name, health, protect)     
        self.name = name
        self.attack = attack * 2
        self.things = []
        self.finalProtection = protect
        self.finalHealth = health


hauberk = Thing('кольчуга', 30, 0.07)
gloves = Thing('перчатки', 10, 0.02)
helmet = Thing('шлем', 20, 0.05)
boots = Thing('ботинки', 5, 0.01)
shild = Thing('щит', 40, 0.1)
hands = Thing('защита рук', 20, 0.03)
legs = Thing('защита ног', 30, 0.03)

name_list = ['Вова', 'Гена', 'Миша', 'Леша', 'Вася', 'Витя', 'Саша', 'Коля', 'Андрей', 'Денис', 'Виталик', 'Никита', 'Дима', 'Рома', 'Стас', 'Леня', 'Женя']
war_pers1 = Warrior(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers2 = Person(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers3 = Warrior(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers4 = Paladin(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers5 = Person(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers6 = Warrior(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers7 = Paladin(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers8 = Person(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers9 = Paladin(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))
war_pers10 = Person(random.choice(name_list), random.randint(80,100), random.randint(1,10), random.uniform(0,0.1))

th = []
sp1 = [war_pers1, war_pers2, war_pers3, war_pers4, war_pers5, war_pers6, war_pers7, war_pers8, war_pers9, war_pers10] 
sp_p = []

def thing_choise():
    sp = [hauberk, gloves, helmet, boots, shild, hands, legs]
    return sp[spi]

for person in sp1:
    pk = 4
    spi = random.randint(0,6)
    while pk > 0:
        sp_p.append(person)
        a = thing_choise()
        
        if person in sp_p: 
            pk -=1
            if spi not in th:
                th.append(spi)
                Person.add_thing(person , a)
            
    else:
        continue 

print()        
print('Список бойцов и их характеристики:')
print()
for pers in sp1:
    Person.print_p(pers)
       
def boi():
    i1 = 0
    i2 = len(sp1) - 1
    print()
    print('Бой начинается')
    print()
    Person.war(sp1[i1], sp1[i2])
    
while len(sp1) != 1:
    boi() 

print()
print(f'{sp1[0].name} победитель Арены')  
print()    
