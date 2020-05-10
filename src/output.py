from time import sleep

from src import game_settings


def print_battle_stats(attacker, enemy):
    print("{:29} attacks     {}".format(attacker.name, enemy.name))
    print("H:{:5.2f} A:{:2} D:{:2}% {:11}-------     H:{:2} A:{:2} D:{}%".format(attacker.full_health, attacker.full_attack, int(attacker.full_defence_proc * 100), ' ', enemy.full_health, enemy.full_attack, int(enemy.full_defence_proc * 100)))


def print_stat(stat_list, command):
    WIDE_LINE = "\n<------------------------- " + "-" * len(stat_list[-1].name + " wins Arena Battle!!!") + " ------------------------->"
    final_table = []
    if command == 'winner':
        print(f"Arena Battle Winner:")
        print(f"--{stat_list[-1]}")
        print(f"----Fights: {stat_list[-1].stat_fights}, Wins: {stat_list[-1].stat_wins}, Max damage: {stat_list[-1].stat_max_damage}, Total damage: {stat_list[-1].stat_damage}")
        print(f"----Winner items:")
        for item in stat_list[-1].items_list:
            print(f"------{item.name}")
        print(WIDE_LINE)
        sleep(game_settings.STATISTICS_DELAY)
    elif command == 'fights':
        sorted_stat_list = \
            sorted(stat_list, key=lambda x: x.stat_fights, reverse=True)
        max_fights = sorted_stat_list[0].stat_fights
        print(f"Maximum Fights in Arena Battle: {max_fights}")
        for i in sorted_stat_list:
            if max_fights > i.stat_fights:
                break
            else:
                if i.name == stat_list[-1].name:
                    print(f"--{i.name} (--winner--)")
                else:
                    print(f"--{i.name}")
                print(f"----Fights: {i.stat_fights}, Wins: {i.stat_wins}, Max damage: {i.stat_max_damage}, Total damage: {i.stat_damage}")
        print(WIDE_LINE)
    elif command == 'max_damage':
        sorted_stat_list = \
            sorted(stat_list, key=lambda x: x.stat_max_damage, reverse=True)
        max_damage = sorted_stat_list[0].stat_max_damage
        print(f"Maximum Damage in Arena Battle: {max_damage}")
        for i in sorted_stat_list:
            if max_damage > i.stat_max_damage:
                break
            else:
                if i.name == stat_list[-1].name:
                    print(f"--{i.name} (--winner--)")
                else:
                    print(f"--{i.name}")
                print(f"----Max damage: {i.stat_max_damage}, Fights: {i.stat_fights}, Wins: {i.stat_wins}, Total damage: {i.stat_damage}")
        print(WIDE_LINE)
    elif command == 'damage':
        sorted_stat_list = \
            sorted(stat_list, key=lambda x: x.stat_damage, reverse=True)
        total_damage = sorted_stat_list[0].stat_damage
        print(f"Maximum Total Damage in Arena Battle: {total_damage}")
        for i in sorted_stat_list:
            if total_damage > i.stat_damage:
                break
            else:
                if i.name == stat_list[-1].name:
                    print(f"--{i.name} (--winner--)")
                else:
                    print(f"--{i.name}")
                print(f"----Total damage: {i.stat_damage}, Max damage: {i.stat_max_damage}, Fights: {i.stat_fights}, Wins: {i.stat_wins}")
        print(WIDE_LINE)
    elif command == 'wins':
        sorted_stat_list = \
            sorted(stat_list, key=lambda x: x.stat_wins, reverse=True)
        total_wins = sorted_stat_list[0].stat_wins
        print(f"Maximum Total Wins in Arena Battle: {total_wins}")
        for i in sorted_stat_list:
            if total_wins > i.stat_wins:
                break
            else:
                if i.name == stat_list[-1].name:
                    print(f"--{i.name} (--winner--)")
                else:
                    print(f"--{i.name}")
                print(f"----Wins: {i.stat_wins}, Total damage: {i.stat_damage}, Max damage: {i.stat_max_damage}, Fights: {i.stat_fights}")
        print(WIDE_LINE)
    sleep(game_settings.STATISTICS_DELAY)
    if command == 'full':
        print("\n")
        final_table = \
            sorted(stat_list, key=lambda x: x.stat_damage, reverse=True)
        print("{:33} | {} | {} | {} | {} | {} |".format("Fighter", "Fights", "Wins", " %Wins", "TotDamage", "MaxDamage"))
        print("{} | {} | {} | {} | {} | {} |".format("=======" + 26 * '=', "======", "====", "======", "=========", "========="))

        for i in final_table:
            if i.name == stat_list[-1].name:
                i.name += " (w)"
            print("{:33} | {:^6} | {:^4} | {:6.1%} | {:9.1f} | {:9.1f} |".format(i.name, i.stat_fights, i.stat_wins, i.stat_wins / i.stat_fights, i.stat_damage, i.stat_max_damage))

        print("{} | {} | {} | {} | {} | {} |".format("=======" + 26 * '=', "======", "====", "======", "=========", "========="))


def print_winner(winner):
    print("\n\n<--------------------------" + "-"\
* len(winner.name + " wins Arena Battle!!!") + "-------------------------->")
    print(f'<-------------------------\
{winner.name} wins Arena Battle!!! -------------------------->')
    print("<--------------------------" + "-"\
* len(winner.name + " wins Arena Battle!!!") + "-------------------------->")
    print("Backend by Praktikum student preparing statistics using time.sleep()")
    print("...")
    sleep(game_settings.STATISTICS_DELAY * 2)


def print_full_battle_stats(winner, stat_list):
    stat_list.append(winner)
    print_stat(stat_list, 'winner')
    print_stat(stat_list, 'fights')
    print_stat(stat_list, 'max_damage')
    print_stat(stat_list, 'damage')
    print_stat(stat_list, 'wins')
    print_stat(stat_list, 'full')
