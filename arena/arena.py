from person import *
import randomaizer
import random as r



class Arena():
    
    def __init__(self, count):
        print(f"\nСоздаем арену на {count} бойцов.\n")
        self.count = count
        self.list_player = []

    def preparing(self):
        print("\nГенерируем список бойцов со снаряжением:\n")
        self.list_player = randomaizer.get_random_players(self.count)
        print("\nОдеваем снаряжение и получаем итоговые значения характеристик:\n")
        for pl in self.list_player:
            for th in pl.list_things:
                pl.hp += th.hp
                pl.attack_damage += th.attack
                pl.start_protection = round(pl.start_protection + th.protection, 2)
            pl.show_charged()

    def start(self):
        self.preparing()
        print("\nНачинаем сражение:\n")
        while len(self.list_player) > 1:
            pl_attack = r.choice(self.list_player)
            self.list_player.remove(pl_attack)
            pl_protection = r.choice(self.list_player)
            self.list_player.remove(pl_protection)
            if pl_protection.get_demage_from(pl_attack):
                self.list_player.append(pl_attack)
            else:
                self.list_player.append(pl_attack)
                self.list_player.append(pl_protection)
        print(f"{self.list_player[0].name} остается в живых с {round(self.list_player[0].hp, 2)} hp")




print("start")
arena = Arena(10)
arena.start()
# pers = Warrior("sd", 100, 20, 0.1)
# print(pers.attack_damage)


