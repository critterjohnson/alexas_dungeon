# item.py - classes and methods for in-game items

class Item(object):
	def __init__(self, 
				 name=None,
				 stack_limit=None,
				 serialized=None):
		if serialized is not None:
			self.deserialize(serialized)
		else:
			self.name = name
			self.stack_limit = stack_limit
	
	def serialize(self):
		serialized = {
			"name": self.name,
			"stack_limit": self.stack_limit,
		}
		return serialized

	def deserialize(self, serialized):
		self.name = serialized["name"]
		self.stack_limit = serialized["stack_limit"]
