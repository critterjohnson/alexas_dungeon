from dungeon import *

dungeon = Dungeon(numFloors=5)
serialized = dungeon.serialize()
print(serialized)

dungeon2 = Dungeon(serialized)
print(dungeon2.floors[0].rooms)
print(dungeon2.numFloors)
print(dungeon2.serialize())
