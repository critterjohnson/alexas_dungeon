from .errors import *


class AlexaRequest:
	"""Represents a request sent by Alexa
	
	--- Attributes ---
	version - str
		the version of the request
	session_is_new - bool
		True if session was just created
	session_id - str
		id of the current session
	app_id - str
		id of the skill
	attributes - dict
		session attributes that persist in session
	user_id - str
		id of the user
	access_token - str
		user's access token
	consent_token - str
		user's consent token
	device_id - str
		id of the device being used
	supported_interfaces - str
		interfaces supported by the current device
	api_endpoint - str
		endpoint of the Alexa API
	api_access_token - str
		access token for the Alexa API
	audio_player - dict
		AudioPlayer object containing audio player properties

	--- Methods ---
	slot_value(name)
		returns the slot value of the slot name passed in
	"""

	def __init__(self, event):
		self.event = event

	# --- Getters
	@property
	def version(self):
		return self.event["version"]

	@property
	def session_is_new(self):
		return self.event["session"]["new"]

	@property
	def session_id(self):
		return self.event["session"]["sessionid"]

	@property
	def app_id(self):
		return self.event["sessoin"]["applicationId"]

	@property
	def attributes(self):
		return self.event["session"]["attributes"]

	@property
	def user_id(self):
		return self.event["session"]["user"]["userId"]

	@property
	def access_token(self):
		return self.event["session"]["user"]["accessToken"]

	@property
	def consent_token(self):
		return self.event["session"]["user"]["permissions"]["consentToken"]

	@property
	def device_id(self):
		return self.event["context"]["System"]["device"]["deviceId"]

	@property
	def supported_interfaces(self):
		return self.event["context"]["System"]["device"]["deviceId"]

	@property
	def api_endpoint(self):
		return self.event["context"]["System"]["apiEndpoint"]

	@property
	def api_access_token(self):
		return self.event["context"]["System"]["apiAccessToken"]

	@property
	def audio_player(self):  # replace with an AudioPlayer object
		return self.event["context"]["System"]["AudioPlayer"]


	# --- Methods
	def has_value(self, slotName):
		"""Returns True if a slot has a value

		--- Parameters ---
		slotName - str
			the name of the slot to check for a value
		"""
		if "value" in self.event["request"]["intent"]["slots"][slotName]:
			return True
		else:
			return False


	def slot_value(self, slotName):
		"""Returns the slot value of a given slot
		
		--- Parameters ---
		slotName - str
			the name of the slot to get the value of
		"""
		if self.has_value(slotName):
			return self.event["request"]["intent"]["slots"][slotName]["value"]
		else:
			raise(NoSlotValueError("There was no slot value for slot '%s'" % slotName))
