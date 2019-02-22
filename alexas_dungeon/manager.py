from dungeon import *
from state import *
from alexatools import *
from player import *
import constants


def lambda_handler(event, context):
	at = AlexaTools(event, context)


	@at.handler("LaunchRequest")
	def launch(request):
		response = AlexaResponse()
		response.text = "Welcome to Rogue Walker."
		response.should_end_session = False
		return response


	@at.handler("NewGame")
	def new_game(request):
		dung = Dungeon(numFloors=1)
		response = AlexaResponse()
		player = Player(dung.floors[0].entry[0], dung.floors[0].entry[1])
		response.session_attributes = {"dungeon": dung.serialize(),
									   "player": player.serialize(),
									   "curFloor": 0}
		response.text = "New game created."
		response.should_end_session = False
		return response


	@at.handler("MoveRooms")
	def move_player(request):
		response = AlexaResponse()
		if not request.has_value("dir"):
			response.text = "Invalid direction."
		dung = Dungeon(serialized=request.attributes["dungeon"])
		player = Player(serialized=request.attributes["player"])
		curFloor = request.attributes["curFloor"]
		direction = request.slot_value("dir")

		# MOVE
		orient = player.orient
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

		if dung.room_exists(curFloor, player.row + move[0], player.col + move[1]):
			player.row += move[0]
			player.col += move[1]
			response.text = "Moved rooms."

			# changes orientation based on movement direction
			if move == (0, 1):
				player.orient = "right"
			elif move == (0, -1):
				player.orient = "left"
			elif move == (1, 0):
				player.orient = "down"
			elif move == (-1, 0):
				player.orient = "up"
		else:
			response.text = "No room in that location."
		response.session_attributes = {"dungeon": dung.serialize(),
									   "player": player.serialize(),
									   "curFloor": curFloor}
		response.should_end_session = False
		return response

	return at.run()
