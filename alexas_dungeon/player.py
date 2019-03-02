# player.py - classes and methods for the Player
from inventory import *

class Player(object):
	def __init__(self,
				 row=0, 
				 col=0, 
				 orient="right",
				 inventory=None,
				 serialized=None):
		self.row = row
		self.col = col
		self.orient = orient
		self.inventory = inventory

		if serialized is not None:
			self.deserialize(serialized)

		else:
			self.inventory = Inventory()
			# TODO - replace this with a constant value
			self.inventory.weapons.append(
				Weapon(name="Starter Sword",
					   stack_limit=1))


	def serialize(self):
		serialized = {}
		serialized["row"] = self.row
		serialized["col"] = self.col
		serialized["orient"] = self.orient
		serialized["inventory"] = self.inventory.serialize()
		return serialized

	def deserialize(self, serialized):
		self.row = serialized["row"]
		self.col = serialized["col"]
		self.orient = serialized["orient"]
		self.inventory = Inventory(serialized=serialized["inventory"])
