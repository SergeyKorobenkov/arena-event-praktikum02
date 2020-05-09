import random
from models import *


THINGS_MAX = 100
THINGS_LIMIT_FOR_PERSON = 4
PERSONS_MAX = 11
WARRIORS = random.randint(1, 10)
PALLADINS = PERSONS_MAX - WARRIORS


def main():
    things = [Thing.generate_random() for _ in range(1, THINGS_MAX)]
    things.sort(key=lambda thing: thing.defence_percentage)
    people = [Warrior.generate_random() for _ in range(1, WARRIORS + 1)]
    people += [Paladin.generate_random() for _ in range(1, PALLADINS + 1)]
    for person in people:
        things_for_person = [things.pop() for _ in range(0, random.randint(1, THINGS_LIMIT_FOR_PERSON))]
        person.set_things(things_for_person)
    while len(people) > 1:
        attacker, defendant = random.choices(people, k=2)
        # random.choices оказывается умеет выбирать два одинаковых из списка :(
        if attacker == defendant:
            continue
        defendant.damage_received(attacker.attack)
        print(f'{attacker.name} наносит удар по {defendant.name} на {attacker.attack} урона')
        if defendant.hp <= 0:
            print(f'{defendant.name} убит')
            people.remove(defendant)

    print(f'There can be the only one: {people[0]}')


if __name__ == '__main__':
    main()
