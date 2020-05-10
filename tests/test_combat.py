from random import randint
from combat import prepare_battle, prepare_persons


class TestCombat:
    def test_combat_has_winner(self):
        participants_count = randint(2, 20)
        battle = prepare_battle(participants_count)
        winner = battle.start()
        assert winner, 'Нет победителя'
        assert battle.life_participants_count == 1, 'Выживщий один'
        assert len(battle.death_participants) == participants_count - 1,\
            'Не все погибщие учтены'
        assert winner not in battle.death_participants, \
            'Победитель записан погибшим'
        assert winner in battle.life_participants,\
            'Победителя нет в списке выживших'

    def test_persons_has_correct_count_things(self):
        persons = prepare_persons(10)
        for person in persons:
            assert len(person.things) in range(1, 5),\
                'Неверное количество вещей'
            assert len(person.things) == len(set(person.things)),\
                'Есть неуникальные вещи'
