THING_BASE = {
    'hp': 1,
    'damage': 1,
    'protection': 1,
}


class Thing(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.hp = kwargs.get('hp') or THING_BASE['hp']
        self.damage = kwargs.get('damage') or THING_BASE['damage']
        self.protection = kwargs.get('protection') or THING_BASE['protection']

    @property
    def info(self):
        return f'{self.name} (урон: {self.damage}, защита: {self.protection})'


class Armor(Thing):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.protection = self.protection * 2


class Weapon(Thing):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.damage = self.damage * 2
