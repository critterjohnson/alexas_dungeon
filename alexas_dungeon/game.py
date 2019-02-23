# game.py - classes and methods to manage the game
from dungeon import *
from state import *
from player import *
from item import *
import constants


class Game(object):
	def __init__(self, serialized=None):
		if serialized is not None:
			self.deserialize(serialized)

		# starts a new game
		else:
			self.dungeon = Dungeon(numFloors=1)
			self.player = Player(self.dungeon.floors[0].entry[0], 
								 self.dungeon.floors[0].entry[1])
			self.state = "moving"
			self.cur_floor = 0


	@staticmethod
	def new_game():
		"""Starts a new game
		returns the following dict:
		{
			"game": (game object),
			"message": new game message,
		}
		"""
		response = {
					"game": Game().serialize(),
					"message": "New game created.",
				}
		return response


	def move_rooms(self, direction):
		if not self.state == "moving":
			return "You can't do that right now."

		orient = self.player.orient
		# moves the player forward
		if direction == "forward":
			if orient == "right":
				move = (0, 1)
			elif orient == "down":
				move = (1, 0)
			elif orient == "left":
				move = (0, -1)
			elif orient == "up":
				move = (-1, 0)
		# moves the player right
		elif direction == "right":
			if orient == "right":
				move = (1, 0)
			elif orient == "down":
				move = (0, -1)
			elif orient == "left":
				move = (-1, 0)
			elif orient == "up":
				move = (0, 1)
		# moves the player back
		elif direction == "back":
			if orient == "right":
				move = (0, -1)
			elif orient == "down":
				move = (-1, 0)
			elif orient == "left":
				move = (0, 1)
			elif orient == "up":
				move = (1, 0)
		# moves the player left
		elif direction == "left":
			if orient == "right":
				move = (-1, 0)
			elif orient == "down":
				move = (0, 1)
			elif orient == "left":
				move = (1, 0)
			elif orient == "up":
				move = (0, -1)

		if self.dungeon.room_exists(self.cur_floor, 
									self.player.row + move[0], 
									self.player.col + move[1]):
			self.player.row += move[0]
			self.player.col += move[1]

			# changes orientation based on movement direction
			if move == (0, 1):
				self.player.orient = "right"
			elif move == (0, -1):
				self.player.orient = "left"
			elif move == (1, 0):
				self.player.orient = "down"
			elif move == (-1, 0):
				self.player.orient = "up"
			return "Moved rooms."

		else:
			return "No room in that location."


	def serialize(self):
		serialized = {
			"dungeon": self.dungeon.serialize(),
			"player": self.player.serialize(),
			"state": self.state,
			"cur_floor": self.cur_floor,
		}
		return serialized


	def deserialize(self, serialized):
		self.dungeon = Dungeon(serialized=serialized["dungeon"])
		self.player = Player(serialized=serialized["player"])
		self.state = serialized["state"]
		self.cur_floor = serialized["cur_floor"]
