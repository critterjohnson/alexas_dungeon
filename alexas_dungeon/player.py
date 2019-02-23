# player.py - classes and methods for the Player

class Player(object):
	def __init__(self,
				 row=0, 
				 col=0, 
				 orient="right", 
				 serialized=None):
		self.row = row
		self.col = col
		self.orient = orient

		if serialized is not None:
			self.deserialize(serialized)


	def serialize(self):
		serialized = {}
		serialized["row"] = self.row
		serialized["col"] = self.col
		serialized["orient"] = self.orient
		return serialized

	def deserialize(self, serialized):
		self.row = serialized["row"]
		self.col = serialized["col"]
		self.orient = serialized["orient"]
