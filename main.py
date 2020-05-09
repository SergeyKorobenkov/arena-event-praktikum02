from Arena import Arena
from UnitGenerator import UnitGenerator
from Logger import Logger


MAX_THINGS = 4
TOTAL_UNITS = 40
TOTAL_THINGS = 200

Logger = Logger()
Arena = Arena(Logger)

UG = UnitGenerator()
units = UG.GenerateUnits(TOTAL_UNITS)
things = UG.GenerateThings(TOTAL_THINGS)

Arena.BringUnits(units)
Arena.BringThings(things)
Arena.DistributeThings(MAX_THINGS)

lastManStanding: 'Person'
lastManStanding = Arena.Battle()

#print(lastManStanding)
# Нарратор: "и тут он увидел 40 новых бойцов выходящих к нему на арену..."
#Arena.BringUnits(UG.GenerateUnits(TOTAL_UNITS))
#Arena.DistributeThings(MAX_THINGS)
#lastManStanding = Arena.Battle()