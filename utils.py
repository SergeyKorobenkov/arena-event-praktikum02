import random
import time


def greet_viewers():
    '''
    The function print greeting message. You can write any text
    in 'greeting' variable
    '''

    greeting = ('Quarantine began and the last packaging of\n'
                'toilet paper remained in the supermarket.\n'
                'Who will get it? Make bets, Ladies and Gentlemen!\n')

    print(greeting)


def choose_winner(characters):
    '''
    The function chooses winner from lust of characters.

    Parameters:
        characters (list): list of Paladin or Warrior objects.

    Returns:
        characters[0] (Paladin or Warrior): Paladin or Warrior object winner
    '''

    while len(characters) > 1:
        attacking = random.choice(characters)

        defending_characters = characters[:]
        defending_characters.remove(attacking)

        defending = random.choice(defending_characters)

        damage = attacking.make_attack(defending)
        print(
            f'{attacking.name} attacks {defending.name} '
            f'and inflicts {damage:.2f} damage'
        )

        if defending.hp <= 0:
            characters.remove(defending)
            print(f'{defending.name} retires')

        time.sleep(0.1)

    return characters[0]


def make_bet(characters):
    '''
    The function returns betting name.

    Parameters:
        characters (list): list of Paladin or Warrior objects.

    Returns:
        bet (str): betting name.
    '''

    characters_names = [character.name for character in characters]

    while True:
        print(f'Our Heroes: {", ".join(characters_names)}')
        print('Who are you betting on?\n')

        bet = input('Enter name: ')
        print()

        if bet in characters_names:
            print('Your bid has been accepted.')
            return bet
        else:
            print('We do not have such fighter. Try again!\n')


def say_bye(winner, bet):
    '''
    The function print info about winner and informs user passed his
    bet or not.

    Parameters:
        winner (Paladin or Warrior): Paladin or Warrior object who won
        bet (str): users betting name
    '''

    equipments_names = [equipment.name for equipment in winner.equipments]
    print()
    print(f'{winner.name} is winner!')
    print(f'Winners equipments are: {", ".join(equipments_names)}\n')

    if winner.name == bet:
        print('You guessed! You won! For this you get...our congratulations!')
    else:
        print('Too bad, your bid failed! You missed a valuable prize...')
