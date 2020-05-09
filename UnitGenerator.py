from typing import List
import random
from models.Person import Paladin, Warrior
from models.Thing import Thing


BRAVE_WORDS = [
    'adventurous', 'audacious', 'confident', 'courageous',
    'daring', 'dashing', 'fearless', 'foolhardy',
    'gallant', 'gutsy', 'heroic', 'reckless',
    'resolute', 'spirited', 'spunky', 'stout',
    'strong', 'valiant', 'stupid', 'firm',
    'forward', 'game', 'hardy', 'militant',
    'stalwart', 'chivalrous', 'dauntless', 'defiant',
    'doughty', 'gritty', 'herolike', 'imprudent',
    'indomitable', 'intrepid', 'lionhearted', 'nervy',
    'plucky', 'stouthearted', 'unabashed', 'unafraid',
    'unblenching', 'undauntable', 'undaunted', 'undismayed',
    'unfearful', 'valorous', 'venturesome', 'clever'
]

UNIT_WORDS = [
    'dogface', 'fighter', 'legionary', 'legionnaire',
    'regular', 'serviceman', 'soldier', 'trooper',
    'champion', 'fighter', 'hero', 'soldier',
    'GI', 'battler', 'combatant', 'conscript',
    'trooper'
]

WEAPONS_WORDS = [
    'bola', 'boomerang', 'bow', 'crossbow',
    'longbow', 'grapeshot', 'flamethrower',
    'sling', 'spear', 'bayonet', 'club',
    'dagger', 'halberd', 'lance', 'pike',
    'quarterstaff', 'sabre', 'sword', 'tomahawk'
]

ARMOUR_WORDS = [
    'gloves', 'shield', 'helmet', 'boots'
]

UNIT_TYPES = [
    Paladin,
    Warrior
]

THING_TYPES = [
    'weapon',
    'armour'
]

UNIT_PARAMS = {
    'min_dmg': 8,
    'max_dmg': 15,
    'min_hp': 50,
    'max_hp': 100,
    'min_defence': 0.000,
    'max_defence': 0.199
}

thing_params = {
    'min_dmg': 0,
    'max_dmg': 5,
    'min_hp': 0,
    'max_hp': 20,
    'min_defence': 0.000,
    'max_defence': 0.100
}


class UnitGenerator:

    def GenerateUnits(self, quant: int) -> List['Person']:
        units = []
        for _ in range(quant):
            units.append(self.GenerateUnit())
        return units

    def GenerateUnit(self, params=UNIT_PARAMS, unitTypes=UNIT_TYPES) -> 'Person':
        unitType = random.choice(unitTypes)

        name = self.GenerateName('unit')
        hp = random.randrange(params['min_hp'], params['max_hp'])
        dmg = random.randrange(params['min_dmg'], params['max_dmg'])
        defence = round(random.uniform(
            params['min_defence'], params['max_defence']), 3)

        unit = unitType(name, hp, dmg, defence)

        return unit

    def GenerateThings(self, quant: int) -> List['Thing']:
        things = []
        for _ in range(quant):
            things.append(self.GenerateThing())
        return things

    def GenerateThing(self, params=thing_params, thingTypes=THING_TYPES) -> 'Thing':
        thingType = random.choice(thingTypes)

        name = self.GenerateName(thingType)
        hp = random.randrange(params['min_hp'], params['max_hp'])
        dmg = random.randrange(params['min_dmg'], params['max_dmg'])
        defence = round(random.uniform(
            params['min_defence'], params['max_defence']), 3)

        thing = Thing(name, hp, dmg, defence)

        return thing

    def GenerateName(self, wordType: str) -> str:
        name = [word.capitalize() for word in random.choices(BRAVE_WORDS, k=2)]

        if wordType == 'unit':
            name.append(
                random.choice(UNIT_WORDS).capitalize()
            )
        elif wordType == 'weapon':
            name.append(
                random.choice(WEAPONS_WORDS).capitalize()
            )
        elif wordType == 'armour':
            name.append(
                random.choice(ARMOUR_WORDS).capitalize()
            )

        return (" ").join(name)

    def UnitThingMassGenerate(self, unitsQuant=5, minThings=0, maxThings=2) -> List['Person']:
        units = []
        for _ in range(unitsQuant):
            unit = self.GenerateUnit()
            for _ in range(minThings, maxThings):
                unit.setThings([self.GenerateThing()])
            units.append(unit)
        return units


if __name__ == "__main__":
    gen = UnitGenerator()
    print(gen.GenerateName('unit'))
    print(gen.GenerateName('weapon'))
    print(gen.GenerateName('armour'))
    print(gen.GenerateUnit())
    print(gen.GenerateThing())
    units = gen.UnitThingMassGenerate()
    for u in units:
        print(u)
