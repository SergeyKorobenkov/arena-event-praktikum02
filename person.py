PERSON_BASE = {
    'hp': 1,
    'damage': 1,
    'protection': 1,
}


class Person(object):
    __things = []
    __attack_damage = 0
    __is_fighting = False

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.rank = 'Новичок'
        self._hp = kwargs.get('hp') or PERSON_BASE['hp']
        self._damage = kwargs.get('damage') or PERSON_BASE['damage']
        self._protection = kwargs.get('protection') or PERSON_BASE['protection']

    @property
    def info(self):
        return f'{self.name} - {self.rank} (урон: {self.damage}, защита: {self.protection})'

    @property
    def hp(self):
        return self._hp + sum([thing.hp for thing in self.__things])

    @property
    def damage(self):
        return self._damage + sum([thing.damage for thing in self.__things])

    @property
    def protection(self):
        return self._protection + sum([thing.protection for thing in self.__things])

    @property
    def things(self):
        return self.__things

    @things.setter
    def things(self, value):
        self.__things = value

    @property
    def is_fighting(self):
        return self.__is_fighting

    @is_fighting.setter
    def is_fighting(self, value):
        self.__is_fighting = value

    @property
    def attack_damage(self):
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, value):
        self.__attack_damage = value

    @property
    def current_hp_percent(self):
        current_hp = self.hp - self.attack_damage
        return current_hp / self.hp * 100 if current_hp >= 0 else 0

    @property
    def is_defeated(self):
        return self.hp - self.attack_damage <= 0


class Paladin(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rank = 'Палладин'
        self._hp = self._hp * 2
        self._protection = self._protection * 2


class Warrior(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rank = 'Воин'
        self.name = kwargs.get('name')
        self._damage = self._damage * 2
