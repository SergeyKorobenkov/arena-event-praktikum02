from typing import List
from models.Thing import Thing


class Person:

    def __init__(self, name: str, hp: int, dmg: int, defence: float) -> None:
        self.name = name
        self.lifeState = True
        self.baseHP = hp
        self.baseDmg = dmg
        self.baseDef = defence

        self.things = []

        # battle specific
        self.dmgTaken = 0

    def setThings(self, things: List['Thing']) -> None:
        self.things += things

    def getThingsHP(self) -> int:
        return sum([thing.getHP() for thing in self.things])

    def getThingsDmg(self) -> int:
        return sum([thing.getDmg() for thing in self.things])

    def getThingsDef(self) -> float:
        return sum([thing.getDef() for thing in self.things])

    def getName(self) -> str:
        return self.name

    def getLifeState(self) -> bool:
        return self.lifeState

    def getHP(self) -> int:
        return self.baseHP + self.getThingsHP()

    def getDef(self) -> float:
        totalDef = self.baseDef + self.getThingsDef()
        # sorry, you are too strong, nerf
        if totalDef >= 1:
            return 0.999
        else:
            return totalDef

    def getDmg(self) -> int:
        return self.baseDmg + self.getThingsDmg()

    def handleDmg(self, attacker: 'Person') -> None:
        self.dmgTaken += attacker.getDmg() - attacker.getDmg() * self.getDef()

        if self.getHP() - self.dmgTaken <= 0:
            self.lifeState = False

    def __str__(self):
        thingsoutput = "\nThings list:\n"
        for thing in self.things:
            thingsoutput += str(thing)

        return (
            f"type: {self.__class__.__name__}\n"
            f"name: {self.name}\n"
            f"state: {self.lifeState}\n"
            f"base hp: {self.baseHP}\n"
            f"base dmg: {self.baseDmg}\n"
            f"base def: {self.baseDef}\n"
            f"things hp: {self.getThingsHP()}\n"
            f"things dmg: {self.getThingsDmg()}\n"
            f"things def: {self.getThingsDef()}\n"
            f"total hp: {self.getHP()}\n"
            f"total dmg: {self.getDmg()}\n"
            f"total def: {self.getDef()}\n"
            f"dmg taken: {self.dmgTaken}\n"
        ) + thingsoutput


class Paladin(Person):

    def __init__(self, name: str, hp: int, dmg: int, defence: float) -> None:
        hp = hp * 2
        defence = defence * 2
        super().__init__(name, hp, dmg, defence)


class Warrior(Person):

    def __init__(self, name: str, hp: int, dmg: int, defence: float) -> None:
        dmg = dmg * 2
        super().__init__(name, hp, dmg, defence)
