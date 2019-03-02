# inventory.py - inventory class
from item import *

class Inventory(object):
	def __init__(self, serialized=None):
		self.weapons = []
		self.spells = []
		self.armor = []
		self.ammo = []
		self.passive = []
		self.max_weapons = 2
		self.max_spells = 2
		self.max_armor = 3
		self.max_ammo = 4
		self.max_passive = 2

		if serialized is not None:
			self.deserialize(serialized)


	# adds an item to the proper location
	# returns True if possible, False otherwise
	def add(self, item):
		if isinstance(item, Weapon):
			if len(self.weapons) >= self.max_weapons:
				return False
			else:
				self.weapons.append(item)
				return True

		elif isinstance(item, Spell):
			if len(self.spells) >= self.max_spells:
				return False
			else:
				self.spells.append(item)
				return True

		elif isinstance(item, Armor):
			if len(self.armor) >= self.max_armor:
				return False
			else:
				self.armor.append(item)
				return True

		elif isinstance(item, Ammo):
			if len(self.ammo) >= self.max_ammo:
				return False
			else:
				self.ammo.append(item)
				return True

		elif isinstance(item, Passive):
			if len(self.passive) >= self.max_passive:
				return False
			else:
				self.passive.append(item)


	def serialize(self):
		serialized = {
			"weapons": [],
			"max_weapons": self.max_weapons,
			"spells": [],
			"max_spells": self.max_spells,
			"armor": [],
			"max_armor": self.max_armor,
			"ammo": [],
			"max_ammo": self.max_ammo,
			"passive": [],
			"max_passive": self.max_passive,
		}
		# serializes weapons
		for item in self.weapons:
			if item is not None:
				serialized["weapons"].append(item.serialize())
			else:
				serialized["weapons"].append(None)

		# serializes spells
		for item in self.spells:
			if item is not None:
				serialized["spells"].append(item.serialize())
			else:
				serialized["spells"].append(None)

		# serializes armor
		for item in self.armor:
			if item is not None:
				serialized["armor"].append(item.serialize())
			else:
				serialized["armor"].append(None)

		# serializes ammo
		for item in self.ammo:
			if item is not None:
				serialized["ammo"].append(item.serialize())
			else:
				serialized["ammo"].append(None)

		# serializes passive
		for item in self.passive:
			if item is not None:
				serialized["passive"].append(item.serialize())
			else:
				serialized["passive"].append(None)

		return serialized


	def deserialize(self, serialized):
		self.max_weapons = serialized["max_weapons"]
		self.max_spells = serialized["max_spells"]
		self.max_armor = serialized["max_armor"]
		self.max_ammo = serialized["max_ammo"]
		self.max_passive = serialized["max_passive"]

		# TODO - Change code to not use generic Item class
		# deserializes items
		for item in serialized["weapons"]:
			if item is not None:
				self.weapons.append(Weapon(serialized=item))
			else:
				self.weapons.append(None)

		# deserializes spells
		for item in serialized["spells"]:
			if item is not None:
				self.spells.append(Spell(serialized=item))
			else:
				self.spells.append(None)

		# deserializes armor
		for item in serialized["armor"]:
			if item is not None:
				self.armor.append(Armor(serialized=item))
			else:
				self.armor.append(None)

		# deserializes ammo
		for item in serialized["ammo"]:
			if item is not None:
				self.ammo.append(Ammo(serialized=item))
			else:
				self.ammo.append(None)

		# deserializes passive
		for item in serialized["passive"]:
			if item is not None:	
				self.passive.append(Passive(serialized=item))
			else:
				self.passive.append(None)
