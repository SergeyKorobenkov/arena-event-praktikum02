class Thing:
    def __init__(self, name: str, hp: int, dmg: int, defence: float) -> None:
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.defence = defence

    def getHP(self) -> int:
        return self.hp

    def getDmg(self) -> int:
        return self.dmg

    def getDef(self) -> float:
        return self.defence

    def __str__(self):
        return (
            f"name: {self.name}\n"
            f"hp: {self.hp}\n"
            f"dmg: {self.dmg}\n"
            f"def: {self.defence}\n"
        )
