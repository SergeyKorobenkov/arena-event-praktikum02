import Arena
import UnitGenerator
import Logger


MAX_THINGS = 4
TOTAL_UNITS = 40
TOTAL_THINGS = 200

Logger = Logger.Logger()
Arena = Arena.Arena(Logger)

UG = UnitGenerator.UnitGenerator()
units = UG.GenerateUnits(TOTAL_UNITS)
things = UG.GenerateThings(TOTAL_THINGS)

Arena.BringUnits(units)
Arena.BringThings(things)
Arena.DistributeThings(MAX_THINGS)

lastManStanding: 'Person'
lastManStanding = Arena.Battle()

#print(lastManStanding)