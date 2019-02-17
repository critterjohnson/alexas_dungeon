# state.py - state and effects for the player and enemies

class State(object):
	def __init__(self, serialized=None):
		self.effects = []
		self.serialized = {}

		if serialized is not None:
			self.deserialize(serialized)


	def serialize(self):
		# serializes effects
		self.serialized["effects"] = []
		for effect in self.effects:
			self.serialized["effects"].append(effect.serialize())

		return self.serialized


	def deserialize(self, serialized):
		# deserializes effects
		for effect in serialized["effects"]:
			self.effects.append(Effect(serialized=serialized))



class Effect(object):
	def __init__(self, serialized):
		self.serialized = {}

		if serialized is not None:
			self.deserialize(serialized)


	def serialize(self):
		pass

	def deserialize(self):
		pass
