import pytest
from game.person import Paladin
from game.thing import Thing


class TestPalading:
    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ])
    def test_init(self, kwargs):
        """Test of object initialisation"""
        paladin = Paladin(**kwargs)
        assert hasattr(paladin, 'name'), f"Attribute name doesn't exist"
        assert hasattr(paladin, 'protect'), f"Attribute protect doesn't exist"
        assert hasattr(paladin, 'damage'), f"Attribute damage doesn't exist"
        assert hasattr(paladin, 'hp'), f"Attribute hp doesn't exist"

    @pytest.mark.parametrize("kwargs", [{'name': 123, 'protect': 0.1, 'damage': 25, 'hp': 40}])
    def test_init_name_incorrect(self, kwargs):
        """Testing incorrect values of name param"""
        with pytest.raises(TypeError):
            paladin = Paladin(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40},
    ])
    def test_init_protect(self, kwargs):
        """Testing doubled values of protect param"""
        paladin = Paladin(**kwargs)
        assert paladin.protect == kwargs['protect'] * 2, f"{paladin.protect} don't equal {kwargs['protect'] * 2}"

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': '0.1', 'damage': 25, 'hp': 40},
        {'name': 'Khonan', 'protect': 12, 'damage': 25, 'hp': 40}
    ])
    def test_init_protect_incorrect(self, kwargs):
        """Testing incorrect values of protect param"""
        with pytest.raises(TypeError):
            paladin = Paladin(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': '25', 'hp': 40},
    ])
    def test_init_damage_incorrect(self, kwargs):
        """Testing incorrect values of damage param"""
        with pytest.raises(TypeError):
            paladin = Paladin(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40},
    ])
    def test_init_hp(self, kwargs):
        """Testing doubled values of protect param"""
        paladin = Paladin(**kwargs)
        assert paladin.hp == kwargs['hp'] * 2, f"{paladin.hp} don't equal {kwargs['hp'] * 2}"

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': '40'},
    ])
    def test_init_hp_incorrect(self, kwargs):
        """Testing incorrect values of hp param"""
        with pytest.raises(TypeError):
            paladin = Paladin(**kwargs)

    @pytest.mark.parametrize("kwargs", [
        {'name': 'Khonan', 'protect': 0.1, 'damage': 25, 'hp': 40},
    ])
    def test_set_things(self, kwargs):
        paladin = Paladin(**kwargs)
        things = [Thing('Sword', 0.0, 50, 0), Thing('Armor', 0.1, 0, 100)]
        paladin.set_things(things)
        result = paladin.get_things()
        for thing in result:
            assert thing in things




