# dungeon.py - contains room and dungeon classes

class Dungeon(object):
	def __init__(self,
	 			 numFloors=1, 
	 			 serialized=None,):
		self.serialized = {}
		self.numFloors = numFloors
		self.floors = []

		# deserialized serialized object
		if serialized is not None:  # dungeon has already been created
			self.deserialize(serialized)

		else:  # no dungeon has been created
			self.generateFloor(1)  # this should go last


	def generateFloor(self, floorNum):
		floor = Floor(floorNum)
		self.floors.append(floor)


	def serialize(self):
		self.serialized["numFloors"] = self.numFloors

		# serializes floors
		self.serialized["floors"] = []
		for floor in self.floors:
			self.serialized["floors"].append(floor.serialize())
		return self.serialized


	def deserialize(self, serialized):
		self.numFloors = serialized["numFloors"]

		# deserializes floors
		for floor in serialized["floors"]:
			self.floors.append(Floor(serialized=floor))
	


class Floor(object):
	def __init__(self, floorNum=1, serialized=None):
		self.floorNum = floorNum
		self.rooms = []
		self.serialized = {}

		if serialized is not None:
			self.deserialize(serialized)

		else:
			self.generate(self.floorNum)


	def generate(self, floorNum):
		# creates a basic, 3 room floor - change this later
		self.rooms = [
					  [
					  	Room(typ=1,
					  		 enemies=0,),
					  	Room(typ=2,
					  		 enemies=0,)
					  ]
					 ]


	def serialize(self):
		self.serialized["floorNum"] = self.floorNum
		
		# serializes rooms
		rooms = []
		for row in self.rooms:
			line = []
			for room in row:
				line.append(room.serialize())
			rooms.append(line)
		self.serialized["rooms"] = rooms
		return self.serialized


	def deserialize(self, serialized):
		self.floorNum = serialized["floorNum"]
		
		# deserializes rooms
		self.rooms = []
		for row in serialized["rooms"]:
			line = []
			for room in row:
				line.append(Room(serialized=room))
			self.rooms.append(line)



class Room(object):
	def __init__(self,
				 serialized=None,
				 typ=None,
				 enemies=None,
				 ):
		self.typ = typ
		self.enemies = enemies  # change this later
		self.serialized = {}

		# deserialized serialized object
		if serialized is not None:
			self.deserialize(serialized)


	def serialize(self):
		self.serialized["typ"] = self.typ
		self.serialized["enemies"] = self.enemies  # this will have to change later
		return self.serialized
	

	def deserialize(self, serialized):
		self.typ = serialized["typ"]
		self.enemies = serialized["enemies"]  # this will have to change later
