import random


class Thing:
    """Класс для вещей."""
    def __init__(self, name, defence, attack, hp):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp


class Person:
    """Класс для персонажей"""
    def __init__(self, name, hp, base_attack, base_defence):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
    
    def setThings(self, things):
        self.things = things
    
    # Здесь будут ещё методы, чтобы реализовать бой
    def get_hit(self, attack_damage):
        finalProtection = self.base_defence + sum(item.defence for item in self.things)
        damage_done = attack_damage*(1-finalProtection)
        self.hp -= damage_done
        return damage_done


class Paladin(Person):

    def __init__(self, name, hp, base_attack, base_defence):
        super().__init__(name, 2*hp, base_attack, 2*base_defence)
    

class Warrior(Person):

    def __init__(self, name, hp, base_attack, base_defence):
        super().__init__(name, hp, 2*base_attack, base_defence)

def create_characters(n):
    #Сделаем набор вещей, пусть для начала будет 10 штук
    ALL_THINGS=(
        Thing('Бронежилет', 0.1, 0, 50),
        Thing('Монтировка', 0.005, 10, 60),
        Thing('HEV', 0.1, 0, 100),
        Thing('BFG', 0, 30, 50),
        Thing('Glock', 0, 15, 20),
        Thing('Дробовик', 0, 0, 35),
        Thing('Каска', 0.06, 0, 35),
        Thing('Очки', 0.01, 0, 10),
        Thing('Борода', 0.03, 0, 80),
        Thing('Бочка', 0.01, 5, 60)
        )
    ans = []
    NAMES = (
    'Гордон', 'Аликс', 'Хэдкраб', 'Барнакл', 'Нихилант',
    'Combine Soldier', 'Elite Combine Soldier', 'Ихтиозавр',
    'Думгай', 'Гжегож Бженчишчикевич', 'Швейк', 'Уильям Бласковиц',
    'Макс Хаас', 'Ethan Mars', 'Madison Paige', 'Norman Jayden',
    'Scott Shelby', 'Коннор', 'Маркус', 'Кэра'
    )
    actual_names = random.sample(NAMES, n)
    for i in range(n):
        new_name = actual_names[i]
        new_hp = random.randint(100, 200)
        new_base_attack = random.randint(10, 30)
        new_base_defence = 0.1*random.random()
        if random.randint(0,1) == 0:
            new_character = Paladin(new_name, new_hp, new_base_attack, new_base_defence)
        else:
            new_character = Warrior(new_name, new_hp, new_base_attack, new_base_defence)
        #Создадим персонажу случайный набор вещей от 1 до 4 штук
        number_of_things = random.randint(1, 4)
        new_character_things = random.sample(ALL_THINGS, number_of_things)
        new_character.setThings(new_character_things)
        ans.append(new_character)
    return ans

def play_arena(arena_characters):
    alive = len(arena_characters)
    while alive > 1:
        # Выберем из всех персонажей на арене двоих -- нападающего и защищающегося
        defender = arena_characters.pop(random.randint(0, alive-1)) # Не забыть вернуть его обратно,если будет жив
        attacker_id = random.randint(0, alive - 2)
        attacker_name, attack_damage = arena_characters[attacker_id].name, arena_characters[attacker_id].base_attack
        damage_done = defender.get_hit(attack_damage)
        print(f'{attacker_name} наносит удар по {defender.name} на {damage_done:.2f} урона')
        if defender.hp <= 0:
            print(f'{defender.name} идёт отдыхать')
        else:
            arena_characters.append(defender)
        alive = len(arena_characters)
    winner = arena_characters[0]
    print(f'Побеждает {winner.name} со следующими предметами: '
        f'{", ".join(th.name for th in winner.things)} '
        f'и оставшимся здоровьем в количестве {winner.hp:.2f} хп!')

arena_characters = create_characters(10)
play_arena(arena_characters)
