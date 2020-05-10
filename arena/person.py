class Person():

    list_things = []

    def __init__(self, name, hp, attack_damage, start_protection):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.start_protection = start_protection


    def set_things(self, things):
        self.list_things = things


    def show(self):
        print("\n{:<12} - hp: {:>3}, attack_damage: {:>2}"
        ",  start_protection: {:<4}".format(self.name, self.hp, self.attack_damage
        , self.start_protection))
        print("Thigs:")
        for th in self.list_things:
            print("\t", end="")
            th.show()


    def show_charged(self):
        print("{:<12} - final_hp: {:>3}, final_attack_damage: {:>2}"
        ",  final_protection: {:<4}".format(self.name, self.hp, self.attack_damage
        , self.start_protection))

    
    def get_demage_from(self, player_attack):
        damage = player_attack.attack_damage - player_attack.attack_damage * self.start_protection
        damage = round(damage, 2)
        # print("{:<12} получает {:>5} урона".format(self.name, damage))
        print("{:<12} наносит удар по {:<12} на {:>5} урона".format(self.name, player_attack.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} покидает нас =(")
            return True
        else:
            return False

class Paladin(Person):
    def __init__(self, name, hp, attack_damage, start_protection):
        super().__init__(name, hp*2, attack_damage, start_protection*2)


class Warrior(Person):
    def __init__(self, name, hp, attack_damage, start_protection):
        super().__init__(name, hp, attack_damage*2, start_protection)


class Thing():
    def __init__(self, name, protection, attack, hp):
        self.name = name
        if protection > 0.1:
            self.protection = 0.1
        else:
            self.protection = protection

        if attack > 5:
            self.attack = 5
        else:
            self.attack = attack

        if hp > 10:
            self.hp = 10
        else:
            self.hp = hp
    

    def show(self):
        print("{:<8} - pr: +{:<4}, at: +{}, hp: +{:>2}".format(self.name, self.protection, self.attack, self.hp))
