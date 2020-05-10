import pytest
from game.thing import Thing


class TestThing:
    init_records = [
        {'name': 'Sword', 'protect': 0.1, 'damage': 25, 'hp': 40}
    ]

    @pytest.mark.parametrize("kwargs", init_records)
    def test_init(self, kwargs):
        thing = Thing(**kwargs)
        assert hasattr(thing, '_name'), f"Attribute _name doesn't exist"
        assert hasattr(thing, '_protect'), f"Attribute _protect doesn't exist"
        assert hasattr(thing, '_damage'), f"Attribute _damage doesn't exist"
        assert hasattr(thing, '_hp'), f"Attribute _hp doesn't exist"

        # check that values are correct, descriptors
