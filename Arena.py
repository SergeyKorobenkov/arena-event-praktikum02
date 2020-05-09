from typing import List
import random


class Arena:

    def __init__(self, logger: 'Logger') -> None:
        self.units = []
        self.things = []
        self.Logger = logger

    def BringUnits(self, units: List['Person']) -> None:
        self.units += units
        self.Logger.Notify('packed')

    def BringThings(self, things: List['Things']) -> None:
        things += self.things
        self.things = self.__things_asc_sort(things)
        self.Logger.Notify('armed')

    def DistributeThings(self, maxThings: int) -> None:
        for unit in self.units:
            if len(self.things) > 0:
                for _ in range(random.randint(0, maxThings)):
                    unit.setThings([
                        self.things.pop(
                            random.randint(0, len(self.things) - 1)
                        )
                    ])
        self.Logger.Notify('distributed')

    def Battle(self) -> 'Person':
        self.Logger.Notify("start")
        while len(self.units) > 1:
            random.shuffle(self.units)
            attacker = self.units[0]
            defender = self.units[1]

            self.Logger.Notify("attack", {
                "defender": defender.getName(),
                "attacker": attacker.getName(),
                "dmg": attacker.getDmg()
            })
            defender.handleDmg(attacker)
            if defender.getLifeState() == False:
                self.Logger.Notify("death", {
                    "defender": defender.getName()
                })
                self.units.remove(defender)

        self.Logger.Notify("victory", {
            "victor": self.units[0].getName()
        })
        return self.units[0]

    def __things_asc_sort(self, things: List['Thing']) -> List['Thing']:
        for i in range(len(things) - 1):
            for j in range(len(things) - i - 1):
                if things[j].getDef() < things[j+1].getDef():
                    things[j], things[j+1] = things[j+1], things[j]
        return things
