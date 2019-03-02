# container.py - classes and methods for item containers
from item import *

class Chest(object):
	def __init__(self,
				 opened=False,
				 item=None,
				 floor=None,
				 serialized=None):
		self.opened = opened
		self.item = item

		if serialized is not None:
			self.deserialize(serialized)
		# generates an item based off of the floor
		else:
			self.item = gen_item(floor)


	def serialize(self):
		serialized = {}
		serialized["opened"] = self.opened
		if self.item is not None:
			serialized["item"] = self.item.serialize()
		else:
			serialized["item"] = None
		return serialized


	def deserialize(self, serialized):
		self.opened = serialized["opened"]
		if serialized["item"] is None:
			self.item = None
		elif serialized["item"]["typ"] == "Weapon":
			self.item = Weapon(serialized=serialized["item"])
		elif serialized["item"]["typ"] == "Spell":
			self.item = Spell(serialized=serialized["item"])
		elif serialized["item"]["typ"] == "Armor":
			self.item = Armor(serialized=serialized["item"])
		elif serialized["item"]["typ"] == "Ammo":
			self.item = Ammo(serialized=serialized["item"])
		elif serialized["item"]["typ"] == "Passive":
			self.item = Passive(serialized=serialized["item"])
