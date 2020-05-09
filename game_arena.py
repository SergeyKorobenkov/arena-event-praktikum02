import random
from termcolor import cprint

from game_engine import generate_team, NAMES, ENEMY_NAMES, get_info, save_info

MY_TEAM = []
ENEMY_TEAM = []
generate_team(team=MY_TEAM, names=NAMES, team_name='Наши')
generate_team(team=ENEMY_TEAM, names=ENEMY_NAMES, team_name='Бандерлоги')
counter = 1

try:
    while MY_TEAM and ENEMY_TEAM:
        cprint(
            f' ************************* Ход:{counter} *************************',
            color='red')
        perk = random.choice(MY_TEAM)
        cprint(f'******** Команда: {perk.team} ********', color='yellow')
        perk.attack(ENEMY_TEAM)
        cprint(perk, color='magenta')
        save_info(team=MY_TEAM, step=counter)
        if not ENEMY_TEAM:
            break
        enemy_perk = random.choice(ENEMY_TEAM)
        cprint(f'******** Команда: {enemy_perk.team} ********',
               color='yellow')
        enemy_perk.attack(MY_TEAM)
        cprint(enemy_perk, color='cyan')
        save_info(team=ENEMY_TEAM, step=counter)
        if not counter % 10:
            user_choice = input(
                'Хотите узнать инфо о персонажах команд? y/n:\n\n\n')
            if user_choice.lower() != 'n':
                get_info(team=MY_TEAM)
                get_info(team=ENEMY_TEAM)
        counter += 1
except Exception as exc:
    print("----------------------------------------------------", exc)

winner = MY_TEAM if MY_TEAM else ENEMY_TEAM
print(f'Победила команда {winner[0].team}')
print(f'В живых остались: {", ".join([perk.name for perk in winner])}')
