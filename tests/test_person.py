from models.person import Paladin, Person, Warrior
from models.thing import Thing


class TestPerson:
    def test_init_person(self):
        human = Person(name='Обыденный', hp=100,
                       attack=1, defence_percent=10)
        assert human.name == 'Обыденный'
        assert human.attack == 1
        assert human.hp == 100
        assert human.defence_percent == 10.0
        assert human.my_class_name == 'Обыватель'

    def test_deal_damage_without_critical(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10)
        human.critical_chance = 0
        damage, critical = human.deal_damage()
        assert damage == 100
        assert critical is False

    def test_deal_critical_damage(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10,
                       critical_chance=100)
        damage, critical = human.deal_damage()
        assert damage == 150, 'Не выпал крит'
        assert critical is True, 'Не выпал крит'

    def test_take_damage(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10)
        human.take_damage(100)
        assert human.hp == 10

    def test_dress_thing(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10)
        thing = Thing(name='Оружие', life=10, attack=100,
                      defence=10, critical_chance=1)
        human.dress_thing(thing)
        assert human.hp == 110
        assert human.attack == 200
        assert human.defence_percent == 20
        assert human.critical_chance == 6

    def test_undress_thing(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10)
        thing = Thing(name='Оружие', life=10, attack=100,
                      defence=10, critical_chance=1)
        human.dress_thing(thing)
        assert human.hp == 110
        assert human.attack == 200
        assert human.defence_percent == 20
        assert human.critical_chance == 6

        human.undress_thing(thing)

        assert human.hp == 100
        assert human.attack == 100
        assert human.defence_percent == 10
        assert human.critical_chance == 5

    def test_death(self):
        human = Person(name='Обыденный', hp=100,
                       attack=100, defence_percent=10)
        human.take_damage(111)
        assert human.hp == 0
        assert human.deal_damage() == (0, False)


class TestPaladin:
    def test_init_paladin(self):
        paladin = Paladin(name='Светоносный', hp=1000,
                          attack=100, defence_percent=10)
        assert paladin.name == 'Светоносный'
        assert paladin.attack == 100
        assert not paladin.hp == 1000, 'Множитель здоровья не сработал'
        assert paladin.hp == 2000, 'Множитель здоровья не равен 2'
        assert not paladin.defence_percent == 10, 'Множитель брони не сработал'
        assert paladin.defence_percent == 20, 'Множитель здоровья не равен 2'
        assert paladin.my_class_name == 'Паладин'


class TestWarrior:
    def test_init_paladin(self):
        warrior = Warrior(name='Кровожадный', hp=1000,
                          attack=100, defence_percent=10)
        assert warrior.name == 'Кровожадный'
        assert not warrior.attack == 100, 'Множитель атаки не сработал'
        assert warrior.attack == 200, 'Множитель атаки не равен 2'
        assert warrior.hp == 1000
        assert warrior.defence_percent == 10.0
        assert warrior.my_class_name == 'Воин'

