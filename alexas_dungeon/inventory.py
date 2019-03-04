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


	def drop_item(self, item_type=None, slot=None, item=None):
		# if the slot is passed and not the item
		if item is None:
			# gets the proper item type list
			if item_type == "weapon":
				item_list = self.weapons
			elif item_type == "spell":
				item_list = self.spells
			elif item_type == "armor":
				item_list = self.armor
			elif item_type == "ammo":
				item_list = self.ammo
			elif item_type == "passive":
				item_list = self.passive
			# checks to make sure there is an item in the slot
			if not slot >= len(item_list) - 1:
				return "There is no item in that slot."
			# deletes the item
			item = item_list[slot]
			del item_list[slot]
			return "Dropped %s" % item.name
		# if the item is passed and not the slot
		else:
			found = False
			for i in range(len(self.weapons)):
				if self.weapons[i].name.lower() == item:
					del self.weapons[i]
					found = True
					break
			for i in range(len(self.spells)):
				if self.spells[i].name.lower() == item:
					del self.spells[i]
					found = True
					break
			for i in range(len(self.armor)):
				if self.armor[i].name.lower() == item:
					del self.armor[i]
					found = True
					break
			for i in range(len(self.ammo)):
				if self.ammo[i].name.lower() == item:
					del self.ammo[i]
					found = True
					break
			for i in range(len(self.passive)):
				if self.passive[i].name.lower() == item:
					del self.passive[i]
					found = True
					break
			if found:
				return "Dropped %s" % item
			else:
				return "You do not have %s" % item


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
