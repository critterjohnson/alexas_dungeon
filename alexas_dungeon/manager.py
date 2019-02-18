from dungeon import *
from state import *
import constants


dungeon = Dungeon(numFloors=5)

#print("\n")

# testing serialization
#print("SERIALIZE")
#serialized = dungeon.serialize()
#print(serialized)
#print(serialized["numFloors"])

#print("\n")

# testing deserialization
#print("DESERIALIZE")
#dungeon2 = Dungeon(serialized=serialized)
#print(dungeon2.floors[0].rooms)
#print(dungeon2.numFloors)
#print(dungeon2.serialize())

#print("\n")

# testing constants
#print("CONSTANTS")
#print(constants.floors)

# testing room generation
#print("ROOM GENERATION")
##print(dungeon.serialize())
print(dungeon.floors[0])
