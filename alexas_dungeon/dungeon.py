# dungeon.py - contains room and dungeon classes
import constants
import random
from container import *


class Dungeon(object):
	def __init__(self,
	 			 numFloors=1, 
	 			 serialized=None,):
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
		serialized = {}
		serialized["numFloors"] = self.numFloors

		# serializes floors
		serialized["floors"] = []
		for floor in self.floors:
			serialized["floors"].append(floor.serialize())

		return serialized


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
									enemies=room["enemyWeight"],
									floor=floorNum)
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
		serialized = {}
		serialized["floorNum"] = self.floorNum
		serialized["entry"] = self.entry
		
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
		serialized["rooms"] = rooms

		return serialized


	def deserialize(self, serialized):
		self.floorNum = serialized["floorNum"]
		self.entry = serialized["entry"]
		
		# deserializes rooms
		self.rooms = []
		for row in serialized["rooms"]:
			line = []
			for room in row:
				if room is not None:
					line.append(Room(serialized=room))
				else:
					line.append(None)
			self.rooms.append(line)



class Room(object):
	# --- Constructor ---
	def __init__(self,
				 serialized=None,
				 typ=None,
				 chest=None,
				 enemies=None,
				 floor=0
				 ):
		self.typ = typ
		self.enemies = enemies  # change this later
		self.chest = chest
		if self.typ == 3:
			self.chest = Chest(floor=floor)

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
		serialized = {}
		serialized["typ"] = self.typ
		serialized["enemies"] = self.enemies  # this will have to change
		if self.chest is not None:
			serialized["chest"] = self.chest.serialize()
		else:
			serialized["chest"] = None

		return serialized
	

	def deserialize(self, serialized):
		self.typ = serialized["typ"]
		self.enemies = serialized["enemies"]  # this will have to change later
		# serializes chest if necessary
		if serialized["chest"] is not None:
			self.chest = Chest(serialized=serialized["chest"])
		else:
			self.chest = None
