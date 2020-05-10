import pytest
from game.thing import Thing


class TestThing:
    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ])
    def test_init(self, kwargs):
        """Test of object initialisation"""
        thing = Thing(**kwargs)
        assert hasattr(thing, 'name'), f"Attribute name doesn't exist"
        assert hasattr(thing, 'protect'), f"Attribute protect doesn't exist"
        assert hasattr(thing, 'damage'), f"Attribute damage doesn't exist"
        assert hasattr(thing, 'hp'), f"Attribute hp doesn't exist"

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

