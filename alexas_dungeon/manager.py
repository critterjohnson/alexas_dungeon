# manager.py - methods to handle requests and responses
from alexatools import *
from game import *


def lambda_handler(event, context):
	at = AlexaTools(event, context)


	# --- Builtins ---
	@at.handler("LaunchRequest")
	def launch(request):
		response = AlexaResponse()
		response.text = "Welcome to Rogue Walker."
		response.should_end_session = False
		return response


	# --- Game Management ---
	@at.handler("NewGame")
	def new_game(request):
		response = AlexaResponse()
		new = Game.new_game()
		response.session_attributes = new["game"]
		response.text = new["message"]
		response.should_end_session = False
		return response


	# --- Movement ---
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

	# --- Inventory Management ---
	@at.handler("ViewInventory")
	def view_inventory(request):
		response = AlexaResponse()
		# ensures the player has created a new game
		if request.attributes is None:
			response.text = "You must create a new game first."
			return response

		text = ""
		# loops through the inventory types
		for key, val in request.attributes["player"]["inventory"].items():
			if not isinstance(val, int):
				for i in range(len(val)):
					if val[i] is not None:
						text += "{type} slot {number} contains {item}. ".format(
							type = key,
							number = i + 1,
							item = val[i]["name"])
		response.text = text
		response.session_attributes = request.attributes
		response.should_end_session = False
		return response


	@at.handler("DropItem")
	def drop_item(request):
		response = AlexaResponse()
		# ensures the player has created a new game
		if request.attributes is None:
			response.text = "You must create a new game first."
			return response

		game = Game(serialized=request.attributes)
		if not request.has_value("item"):
			item_type = request.slot_value("item_type")
			slot = int(request.slot_value("number")) - 1
		else:
			item = request.slot_value("item")
			item_type = None
			slot = None
		text = game.player.inventory.drop_item(item_type=item_type, 
											   slot=slot,
											   item=item)
		response.text = text
		response.session_attributes = game.serialize()
		response.should_end_session = False
		return response


	# --- Misc --
	@at.handler("OpenChest")
	def open_chest(request):
		response = AlexaResponse()
		# ensures the player has created a new game
		if request.attributes is None:
			response.text = "You must create a new game first."
			return response
		text = ""
		game = Game(serialized=request.attributes)
		text = game.open_chest()
		response.text = text
		response.session_attributes = game.serialize()
		response.should_end_session = False
		return response


	return at.run()
