import random as r

class Thing:
    """ class Thing

    Thing for person included next parametres:\n
    name - Name of thing;\n
    protection - Percent of protection, default value is None;\n
    attack - Attack parameter\n
    hp - Hit point of thing
    """

    def __init__(self, name=None, protection=None, attack=None, hp=None):
        self.name = self.__ganerate_name(name)
        self.protection = self.__ganerate_protection(protection)
        self.attack = self.__generate_attack(attack)
        self.hp = self.__generate_hp(hp)

    def __ganerate_name(self, name):
        if name:
            return name
        return 'Artifact' + str(r.randint(1, 40))

    def __ganerate_protection(self, protection):
        if protection:
            return protection
        return r.randint(1, 10)

    def __generate_attack(self, attack):
        if attack:
            return attack
        return r.randint(0, 30)

    def __generate_hp(self, hp):
        if hp:
            return hp
        return r.randint(0, 10)


def generate_things(count):
    things_list = []
    for thing in range(0, count):
        thing = Thing()
        things_list.append(thing)
    return things_list    


class Person:
    """ class Person
    
    The Person(charcter) has the following description:\n
    name - Name of person;\n
    b_attack - Base attack of person, default = random 10-20;\n
    b_protection - Base percent of protection of person, default = random 5-10;\n
    hp - Hit poin of person, default = random 30 - 70
    """

    name_list = ['Torvald', 'Odin', 'Hara', 'Ermund', 'Ostrix', 'Ardiun',
                 'Armandur', 'Ragnar', 'Aslaught', 'Sorin', 'Trubadur', 
                 'Bary', 'Durmandur', 'Astrix', 'Clover', 
                 'Gudin', 'Devan', 'Axe', 'Zoom', 'Slack']

    def __init__(self, name=None, b_attack=None, b_protection=None, hp=None):
        self.name = self.__generate_name(name)
        self.b_attack = self.__generate_b_attack(b_attack)
        self.b_protection = self.__generate_b_protection(b_protection)
        self.hp = self.__generate_hp(hp)
    
    def __generate_name(self, name):
        if name:
            return name
        return self.name_list[r.randint(0, 19)]
    
    def __generate_b_attack(self, b_attack):
        if b_attack:
            return b_attack
        return r.randint(10, 20)

    def __generate_b_protection(self, b_protection):
        if b_protection:
            return b_protection
        return r.randint(5, 10)
    
    def __generate_hp(self, hp):
        if hp:
            return hp
        return r.randint(30, 70)


def generate_persons(count):
    persons_list = []
    for person in range(0, count):
        person = Palladin()
        persons_list.append(person)
        person = Warrior()
        persons_list.append(person)
    return persons_list

    
class Palladin(Person):
    def __init__(self, name=None, b_attack=None, b_protection=None, hp=None):
        super().__init__(b_attack)
        self.name = self.name + '-Palladin'
        self.hp = self.hp * 2
        self.b_protection = self.b_protection * 2
        

class Warrior(Person):
    def __init__(self, name=None, b_attack=None, b_protection=None, hp=None):
        super().__init__(b_protection, hp)
        self.name = self.name + '-Warrior'
        self.b_attack = self.b_attack * 2


def setThigs(a, b):
    print(f"--------------------Генерация {len(a)} предметов и {len(b)} "
          f"героев классов Palladin и Warrior-------------------------------")
    for i in range(0, len(a)):
        print(f"Предмет: {a[i].name}, Защита = {a[i].protection}, "
              f"Атака = {a[i].attack}, Бонус ХП =  {a[i].hp}")
        index = r.randint(0, len(b)-1)
        b[index].name = b[index].name + '(' + a[i].name + ')'
        b[index].b_attack = b[index].b_attack + a[i].attack
        b[index].b_protection = b[index].b_protection + a[i].protection
        b[index].hp = b[index].hp + a[i].hp
        print(f"Бог Рандом вручил {a[i].name} герою {b[index].name}. Статы "
              f"повышены: Баз.Атака = {b[index].b_attack}, "
              f"Баз.Защита = {b[index].b_protection}, Жизни = {b[index].hp}")
    print("------------------Распределение предметов окончено----------------")
    return b

a = generate_things(int(input("Какое количество предметов желаете использовать для битвы?\n")))
b = generate_persons(int(input("Какое количество пар Palladin-Warrior желаете призвать из Асгарда?\n")))
fighters_list = setThigs(a, b)


def fight(fighters_setThigs):
    print()
    print("----------------------------Бой начался---------------------------")
    fighters = fighters_setThigs
    while len(fighters) > 1:
        A = 0
        B = r.randint(1, len(fighters)-1)
        finalProtection_A = fighters[A].b_protection / 100
        finalProtection_B = fighters[B].b_protection / 100
        attack_damage_A = int(fighters[A].b_attack - fighters[A].b_attack * finalProtection_B)
        attack_damage_B = int(fighters[B].b_attack - fighters[B].b_attack * finalProtection_A)
        while fighters[A].hp > 0 and fighters[B].hp > 0:
            fighters[A].hp = int(fighters[A].hp - attack_damage_B)
            print(f"{fighters[B].name} наносит удар по {fighters[A].name} на "
                f"{attack_damage_B} урона.")
            if fighters[A].hp <= 0:
                print(f"!!!!!!!!!!!Боец {fighters[A].name} повержен!!!!!!!!!!")
                print("-------------------Новый раунд------------------------")
                del fighters[A]
                fighters = sorted(fighters, key=lambda A: r.random())
                break
            fighters[B].hp = int(fighters[B].hp - attack_damage_A)
            print(f"{fighters[A].name} наносит удар по {fighters[B].name} на "
                f"{attack_damage_A} урона.")
            if fighters[B].hp <= 0:
                print(f"!!!!!!!!!!!!Боец {fighters[B].name} повержен!!!!!!!!!")
                print("-------------------Новый раунд------------------------")
                del fighters[B]
                fighters = sorted(fighters, key=lambda A: r.random())
                break
    print("==========================Бой окончен=============================")
    print(f"{fighters[0].name} победил на Арене, у него остались {fighters[0].hp} жизней")

fight(fighters_list)