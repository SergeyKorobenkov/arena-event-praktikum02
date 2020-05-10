import pytest
from game.person import Warrior


class TestWarrior:
    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ])
    def test_init(self, kwargs):
        """Test of object initialisation"""
        warrior = Warrior(**kwargs)
        assert hasattr(warrior, 'name'), f"Attribute _name doesn't exist"
        assert hasattr(warrior, 'protect'), f"Attribute _protect doesn't exist"
        assert hasattr(warrior, 'damage'), f"Attribute _damage doesn't exist"
        assert hasattr(warrior, 'hp'), f"Attribute _hp doesn't exist"

        """Testing that all Attributes only read"""
        with pytest.raises(AttributeError):
            warrior.name = 'Update name'
        with pytest.raises(AttributeError):
            warrior.protect = 0.05
        with pytest.raises(AttributeError):
            warrior.damage = 60
        with pytest.raises(AttributeError):
            warrior.hp = 150

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

