"""Реализованы две дополнительные опции
    1. Защищающийся герой контратакует
    2. Атакующий герой забирает все доспехи проигравшего
"""

#Game options
# 1. defending hero responds with attack, RESPONSE_KOEF - responding attack koeffient
contrattack = True
CONTR_KOEF = 0.5
# 2. attacking hero takes the trophy from the defeated one
take_trophy = True

#Game base settings
NUM_OF_HEROES = 10

#init heroes params
HP_MIN, HP_MAX = 100, 110
ATTACK_MIN, ATTACK_MAX = 5, 20
PROTECTION_MAX = 0.25

#init things params
T_HP_MAX = 20
T_ATTACK_MAX = 10
T_PROTECTION_MAX = 0.1
NUM_OF_THINGS_PER_HERO_MIN = 1
NUM_OF_THINGS_PER_HERO_MAX = 4


things_list = [
    'Cape of Conjuring',
    'Dragon Wing Tabard',
    'Vampires Cowl',
    'Surcoat of Counterpoise',
    'Ambassadors Sash',
    'Everflowing Crystal Cloak',
    'Recanters Cloak',
    'Cape of Velocity',
    'Angel Wings',
    'Cloak of the Undead King',
    'Dragonbone Greaves',
    'Dead Mans Boots',
    'Boots of Polarity',
    'Sandals of the Saint',
    'Boots of Levitation',
    'Helm of the Alabaster Unicorn',
    'Skull Helmet',
    'Helm of Chaos',
    'Crown of the Supreme Magi',
    'Sea Captains Hat',
    'Helm of Heavenly Enlightenment',
    'Spellbinders Hat',
    'Admirals Hat',
    'Shield of the Dwarven Lords',
    'Shield of the Yawning Dead',
    'Buckler of the Gnoll King',
    'Targ of the Rampaging Ogre',
    'Shield of the Damned',
    'Dragon Scale Shield',
    'Lions Shield of Courage',
    'Sentinels Shield',
    'Charm of Mana',
    'Talisman of Mana',
    'Mystic Orb of Mana',
    'Wizards Well',
    'Orb of Silt',
    'Orb of the Firmament',
    'Orb of Driving Rain',
    'Orb of Tempestuous Fire',
    'Tome of Earth',
    'Tome of Air',
    'Tome of Water',
    'Tome of Fire',
    'Sphere of Permanence',
    'Orb of Inhibition',
    'Orb of Vulnerability',
    'Bird of Perception',
    'Stoic Watchman'
]

heroes = [
    'Edric',
    'Orrin',
    'Sylvia',
    'Valeska',
    'Tyris',
    'Catherine',
    'Roland',
    'Adela',
    'Adelaide',
    'Caitlin',
    'Cuthbert',
    'Ingham',
    'Loynis',
    'Rion',
    'Jenova',
    'Kyrre',
    'Alagar',
    'Coronius',
    'Elleshar',
    'Malcom'
]