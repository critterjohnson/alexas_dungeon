# dungeon.py - contains room and dungeon classes
import constants
import random


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
			self.generateFloor(0)  # this should go last


	def generateFloor(self, floorNum):
		floor = Floor(floorNum)
		self.floors.append(floor)


	# checks that a room exists
	def room_exists(self, floor, row, col):
		# negative indecies mean the room doesn't exist
		if row < 0 or col < 0:
			return False
		try:
			if self.floors[floor].rooms[row][col] is not None:
				return True
			else:
				return False
		except IndexError:
			return False


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
	# --- Constructor ---
	def __init__(self, floorNum=1, serialized=None):
		self.floorNum = floorNum
		self.rooms = []
		self.serialized = {}
		self.entry = None

		if serialized is not None:
			self.deserialize(serialized)

		else:
			self.generate(self.floorNum)


	# --- Methods ---
	# creates a room "randomly" based off of constant values
	def generate(self, floorNum):
		gen_code = constants.floors[floorNum]
		# generate rooms regardless of dependencies
		for row in gen_code:
			line = []
			for room in row:
				if room is None:
					line.append(None)

				else:
					rand = random.randrange(0, 100)
					if rand <= room["chanceExists"]:
						curRoom = Room(
									typ=room["type"],
									enemies=room["enemyWeight"])
						line.append(curRoom)

					else:
						line.append(None)
			self.rooms.append(line)
		# delete rooms that are missing their dependencies
		# everything is (y, x)
		for row in range(len(gen_code)):
			for col in range(len(gen_code[row])):
				curRoom = self.rooms[row][col]
				if curRoom is None:
					break

				dependencies = gen_code[row][col]["dependencies"]
				if dependencies is not None:
					print(gen_code[row][col])
					print(dependencies)
					for dependency in dependencies:
						if self.rooms[dependency[0]][dependency[1]] is None:
							self.rooms[row][col] = None
				# adds this room as the floor's entry point
				if curRoom.typ == 2:
					self.entry = [row, col]


	def __repr__(self):
		string = ""
		for row in self.rooms:
			for room in row:
				string += str(room) + " | "
			string += "\n"
		return string


	def serialize(self):
		self.serialized["floorNum"] = self.floorNum
		self.serialized["entry"] = self.entry
		
		# serializes rooms
		rooms = []
		for row in self.rooms:
			line = []
			for room in row:
				if room is not None:
					line.append(room.serialize())
				else:
					line.append(None)
			rooms.append(line)
		self.serialized["rooms"] = rooms

		return self.serialized


	def deserialize(self, serialized):
		self.floorNum = serialized["floorNum"]
		self.entry = serialized["entry"]
		
		# deserializes rooms
		self.rooms = []
		for row in serialized["rooms"]:
			line = []
			for room in row:
				line.append(Room(serialized=room))
			self.rooms.append(line)



class Room(object):
	# --- Constructor ---
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


	# --- Methods ---
	def __repr__(self):
		string = ""
		string += "type: " + str(self.typ) + " "
		string += "enemies: " + str(self.enemies)
		return string


	def serialize(self):
		self.serialized["typ"] = self.typ
		self.serialized["enemies"] = self.enemies  # this will have to change

		return self.serialized
	

	def deserialize(self, serialized):
		self.typ = serialized["typ"]
		self.enemies = serialized["enemies"]  # this will have to change later
