import pytest
from game.person import Warrior
from game.thing import Thing


class TestWarrior:
    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ])
    def test_init(self, kwargs):
        """Test of object initialisation"""
        warrior = Warrior(**kwargs)
        assert hasattr(warrior, 'name'), f"Attribute name doesn't exist"
        assert hasattr(warrior, 'protect'), f"Attribute protect doesn't exist"
        assert hasattr(warrior, 'damage'), f"Attribute damage doesn't exist"
        assert hasattr(warrior, 'hp'), f"Attribute hp doesn't exist"

    @pytest.mark.parametrize("kwargs", [{'name': 123, 'protect': 0.1, 'damage': 25, 'hp': 40}])
    def test_init_name_incorrect(self, kwargs):
        """Testing incorrect values of name param"""
        with pytest.raises(TypeError):
            warrior = Warrior(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': '0.1', 'damage': 25, 'hp': 40},
        {'name': 'Khonan', 'protect': 12, 'damage': 25, 'hp': 40}
    ])
    def test_init_protect_incorrect(self, kwargs):
        """Testing incorrect values of protect param"""
        with pytest.raises(TypeError):
            warrior = Warrior(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40},
    ])
    def test_init_damage(self, kwargs):
        """Testing doubled values of damage param"""
        warrior = Warrior(**kwargs)
        assert warrior.damage == kwargs['damage'] * 2, f"{warrior.damage} don't equal {kwargs['damage'] * 2}"

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': '25', 'hp': 40},
    ])
    def test_init_damage_incorrect(self, kwargs):
        """Testing incorrect values of damage param"""
        with pytest.raises(TypeError):
            warrior = Warrior(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': '40'},
    ])
    def test_init_hp_incorrect(self, kwargs):
        """Testing incorrect values of hp param"""
        with pytest.raises(TypeError):
            warrior = Warrior(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': 40},
    ])
    def test_set_things(self, kwargs):
        warrior = Warrior(**kwargs)
        things = [Thing('Sword', 0.0, 50, 0), Thing('Armor', 0.1, 0, 100)]
        warrior.set_things(things)
        result = warrior.get_things()
        for thing in result:
            assert thing in things

