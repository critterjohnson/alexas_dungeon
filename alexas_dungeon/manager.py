# manager.py - methods to handle requests and responses
from alexatools import *
from game import *


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
		response = AlexaResponse()
		new = Game.new_game()
		response.session_attributes = new["game"]
		response.text = new["message"]
		response.should_end_session = False
		return response


	@at.handler("MoveRooms")
	def move_player(request):
		response = AlexaResponse()
		# ensures the player has created a new game
		if request.attributes is None:
			response.text = "You must create a new game first."
			return response

		# ensures the player has given a value to slot 'dir'
		if not request.has_value("dir"):
			response.text = "Invalid direction."
			return response

		game = Game(serialized=request.attributes)
		response.text = game.move_rooms(direction=request.slot_value("dir"))

		response.session_attributes = game.serialize()
		response.should_end_session = False
		return response


	@at.handler("ViewInventory")
	def view_inventory(request):
		text = ""
		# loops through the inventory types
		for key, val in request.attributes["player"]["inventory"].items():
			if not isinstance(val, int):
				for i in range(len(val)):
					if val[i] is not None:
						text += "{type} slot {number} contains {item}. ".format(
							type = key,
							number = i,
							item = val[i]["name"])
		response = AlexaResponse()
		response.text = text
		response.session_attributes = request.attributes
		return response


	return at.run()
