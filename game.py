import random
from time import sleep

from src import game_settings
from src.oop import create_fighter_pool, create_item_pool
from src.output import print_full_battle_stats, print_battle_stats, print_winner


def arena_game(fighter_pool, stat_pool):

    # Perform the battle
    while 1:
        # set battle participants and print fighters statistics
        current_battle = random.sample(fighter_pool, 2)
        attacker = current_battle[0]
        enemy = current_battle[1]
        print_battle_stats(attacker, enemy)

        # perform fight and collect statistics
        if attacker.attack_enemy(enemy):
            stat_pool.append(enemy)
            fighter_pool.remove(enemy)
            print(f"""== {enemy} was defeated\
(HP:{enemy.full_health}). {attacker} wins! ==""")
            if len(fighter_pool) > 1:
                print(f'===== Current fighters on \
Arena: {len(fighter_pool)} =====\n')
                print("Get Ready for next battle!\n...")
            else:
                print_winner(fighter_pool[0])
                break
        else:
            print(f"{enemy} survived with {enemy.full_health} HP\n")
            print("Get Ready for next battle!\n...")
        sleep(game_settings.FIGHT_DELAY)


if __name__ == "__main__":

    # Create fighter and items (to customize settings see game_settings.py)
    # Default: Fighters(10) , MAX_ITEMS(4)
    stat_pool = []
    fighter_pool = create_fighter_pool(game_settings.FIGHTERS_NUMBER)
    items_pool = create_item_pool(game_settings.MAX_ITEMS_PER_HERO)

    # Apply items to fighters
    for fighter in fighter_pool:
        fighter.setThings(items_pool)

    # Start game
    arena_game(fighter_pool, stat_pool)

    # Print final statistics table
    print_full_battle_stats(fighter_pool[0], stat_pool)
