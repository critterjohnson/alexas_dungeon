# item.py - classes and methods for in-game items
import json
import random
import constants

class Item(object):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		self.name = name
		self.stack_limit = stack_limit
		if serialized is not None:
			self.deserialize(serialized)

	
	def serialize(self):
		serialized = {
			"name": self.name,
			"stack_limit": self.stack_limit,
		}
		return serialized


	def deserialize(self, serialized):
		self.name = serialized["name"]
		self.stack_limit = serialized["stack_limit"]



class Weapon(Item):
	def __init__(self, 
				 name=None,
				 stack_limit=1,
				 serialized=None):
		super().__init__(name=name,
						 stack_limit=stack_limit,
						 serialized=serialized)


	def serialize(self):
		serialized = super().serialize()
		serialized["typ"] = "Weapon"
		return serialized



class Spell(Item):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		super().__init__(name=name,
						 stack_limit=stack_limit,
						 serialized=serialized)


	def serialize(self):
		serialized = super().serialize()
		serialized["typ"] = "Spell"
		return serialized



class Armor(Item):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		super().__init__(name=name,
						 stack_limit=stack_limit,
						 serialized=serialized)


	def serialize(self):
		serialized = super().serialize()
		serialized["typ"] = "Armor"
		return serialized



class Ammo(Item):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		super().__init__(name=name,
						 stack_limit=stack_limit,
						 serialized=serialized)


	def serialize(self):
		serialized = super().serialize()
		serialized["typ"] = "Ammo"
		return serialized



class Passive(Item):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		super().__init__(name=name,
						 stack_limit=stack_limit,
						 serialized=serialized)


	def serialize(self):
		serialized = super().serialize()
		serialized["typ"] = "Passive"
		return serialized



def gen_item(floor):
	rarities = constants.item_rarities
	rarity_vals = constants.rarity_values
	rand = random.randint(1, 100)
	rare = 0
	for i in range(len(rarity_vals)):
		val = rarity_vals[i]
		rare += val  # rare keeps track of the current percentage
		if rand <= rare:
			rarity = rarities[i]
			break
	# gets the list of items from the JSON file
	with open("items.json") as file:
		item_list = json.load(file)[str(floor)]
	rarity_list = item_list[rarity]
	item_name = random.choice(list(rarity_list))
	item_data = rarity_list[item_name]

	if item_data["type"] == "Weapon":
		item = Weapon(name=item_name,
					  stack_limit=item_data["stack_limit"])
	elif item_data["type"] == "Spell":
		item = Spell(name=item_name,
					 stack_limit=item_data["stack_limit"])
	elif item_data["type"] == "Armor":
		item = Armor(name=item_name,
					 stack_limit=item_data["stack_limit"])
	elif item_data["type"] == "Ammo":
		item = Ammo(name=item_name,
					stack_limit=item_data["stack_limit"])
	elif item_data["type"] == "Passive":
		item = Passive(name=item_name,
					   stack_limit=item_data["stack_limit"])
	return item
