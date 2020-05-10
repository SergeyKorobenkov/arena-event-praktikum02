import pytest
from game.thing import Thing


class TestThing:
    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ])
    def test_init(self, kwargs):
        """Test of object initialisation"""
        thing = Thing(**kwargs)
        assert hasattr(thing, 'name'), f"Attribute _name doesn't exist"
        assert hasattr(thing, 'protect'), f"Attribute _protect doesn't exist"
        assert hasattr(thing, 'damage'), f"Attribute _damage doesn't exist"
        assert hasattr(thing, 'hp'), f"Attribute _hp doesn't exist"

        """Testing that all Attributes only read"""
        with pytest.raises(AttributeError):
            thing.name = 'Update name'
        with pytest.raises(AttributeError):
            thing.protect = 0.05
        with pytest.raises(AttributeError):
            thing.damage = 60
        with pytest.raises(AttributeError):
            thing.hp = 150

    @pytest.mark.parametrize("kwargs", [{'name': 123, 'protect': 0.1, 'damage': 25, 'hp': 40}])
    def test_init_name_incorrect(self, kwargs):
        """Testing incorrect values of name param"""
        with pytest.raises(TypeError):
            thing = Thing(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': '0.1', 'damage': 25, 'hp': 40},
        {'name': 'Sword', 'protect': 12, 'damage': 25, 'hp': 40}
    ])
    def test_init_protect_incorrect(self, kwargs):
        """Testing incorrect values of protect param"""
        with pytest.raises(TypeError):
            thing = Thing(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': '25', 'hp': 40},
    ])
    def test_init_damage_incorrect(self, kwargs):
        """Testing incorrect values of damage param"""
        with pytest.raises(TypeError):
            thing = Thing(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': '40'},
    ])
    def test_init_hp_incorrect(self, kwargs):
        """Testing incorrect values of hp param"""
        with pytest.raises(TypeError):
            thing = Thing(**kwargs)

