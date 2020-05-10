from editor import (
    create_different_characters,
    create_different_equipments,
    equip_characters,
)
from utils import (
    choose_winner,
    make_bet,
    say_bye,
    greet_viewers,
)


def main():
    equipments = create_different_equipments()
    characters = create_different_characters()
    equip_characters(characters, equipments)

    greet_viewers()
    bet = make_bet(characters)
    winner = choose_winner(characters)

    say_bye(winner, bet)


if __name__ == "__main__":
    main()
