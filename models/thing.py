class Thing:
    def __init__(self, name: str, defence: int, attack: int,
                 life: int, critical_chance: int):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.life = life
        self.critical_chance = critical_chance

    def __str__(self):
        return self.name

    @property
    def info(self) -> dict:
        data = {self.name: {
            'Здоровье': self.life,
            'Атака': self.attack,
            'Защита': f'{self.defence}%',
            'Критический шанс': f'{self.critical_chance}%'
        }}
        return data
