from Persons import *
from Things import *

if __name__ == '__main__':
    persons = create_persons()
    #Базовый набор, каждому по 1му предмету
    base_kit = forgeSomeStuff(10)
    for i in range(0, len(persons)):
        persons[i].setThings([base_kit[i]])
        persons[i].setThings(forgeSomeStuff(randint(1,3)))

    for person in persons:
        print("Приветствуем участника: " + person.getStat())

    round_num = 1

    while(len(persons) > 1):
            print(f'\n************* Раунд № {round_num} ************')
            len_before_round = len(persons)
            persons_after_round = []

            for i in range(0, int(len_before_round/2)):
                if len(persons) == 1:
                    break
                attacker = persons.pop(randint(0, len(persons)-1))
                defender = persons.pop(randint(0, len(persons)-1))
                defender.getDamage(attacker)
                persons_after_round.append(attacker)
                if defender.is_a_life:
                    persons_after_round.append(defender)

            persons = persons_after_round
            round_num += 1


    print('\nПобедитель: ' + persons[0].getStat())





