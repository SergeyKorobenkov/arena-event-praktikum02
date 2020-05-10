import random as r

from .game_constants import *
from .game_classes import Item, Paladin, Warrior


class Game():

    @staticmethod
    def generate_item_list():
        item_list = []
        items_amount = r.randint(0, MAX_ITEMS_AMOUNT)
        for _ in range(10, items_amount):
            if round(r.random()):
                item = Item(f'Weapon {_}', damage=r.randrange(1, 25))
            else:
                item = Item(f'Armor {_}',
                            defence=r.randrange(1, 10), hp=r.randrange(0, 20))
            item_list.append(item)
        r.shuffle(item_list)
        return item_list

    @staticmethod
    def generate_fighters():
        names = FIGHTER_NAME_LIST.copy()
        r.shuffle(names)
        items = Game.generate_item_list()
        fighter_list = []
        for _ in range(0, NUMBER_OF_FIGHTERS):
            name = names.pop()
            param_list = {
                'hp': r.randint(50, 100),
                'damage': r.randint(1, 10),
                'defence': r.randint(1, 10)
            }
            if round(r.random()):
                fighter = Paladin(f'{name}', **param_list)
            else:
                fighter = Warrior(f'{name}', **param_list)
            if items:
                item_amount = r.randint(1, MAX_FIGHTER_ITEMS)
                selected_items = []
                for _ in range(0, min(item_amount, len(items))):
                    selected_items.append(items.pop())
                fighter.set_inventory(selected_items)
            fighter_list.append(fighter)
        return fighter_list

    def __init__(self):
        self.active_fighters = Game.generate_fighters()

    def fight(self, fighter1, fighter2):
        while True:
            if fighter1.attack(fighter2):
                return fighter1
            if fighter2.attack(fighter1):
                return fighter2

    def play(self):
        print('Бойцы:\n      ',
              '\n       '.join(str(x) for x in self.active_fighters))
        round_winners = []
        while self.active_fighters:
            fighter1 = self.active_fighters.pop()
            fighter2 = self.active_fighters.pop()
            print(f'\n    На арену входят \n    {fighter1} и {fighter2}\n')
            winner = self.fight(fighter1, fighter2)
            print(f'\n    С арены вышел {winner.name}')
            winner.restore_hp()
            round_winners.append(winner)
            if len(self.active_fighters) == 1:
                lucky_one = self.active_fighters.pop()
                print(
                    f'\nБойцу {lucky_one.name} повезло, он автоматически переходит в следующий раунд \n')
                r.shuffle(round_winners)
                round_winners.append(lucky_one)
                del lucky_one
            if not self.active_fighters:
                if len(round_winners) == 1:
                    game_winner = round_winners.pop()
                    print(f'\nПобедил {game_winner}\n   ', '\n    '.join(
                        str(x) for x in game_winner.inventory))
                    return
                self.active_fighters.extend(round_winners)
                round_winners.clear()
                print('\nРаунд закончен\n')
                print('В следующий раунд переходят:\n      ',
                      '\n       '.join(str(x) for x in self.active_fighters))
