import json


class AlexaResponse(object):
	"""Represents a response to for an Alexa skill

	--- Attributes ---
	version - int, str
		the version of the skill
	session_attributes - dict
		contains key-value pairs that persist in session
	output_speech_type - str
		the type of output speech (PlainText, ssml)
	text - str
		the text for Alexa to speak
	ssml - str
		str with ssml (Speech Synthesis Markup language) for Alexa to speak
	play_behavior - str
		behavior for responding
	card_type - str
		type of card to create
	card_title - str
		title of card to create
	card_content - str
		content of card of type Simple
	card_text - str
		content of card of type Standard
	card_small_image_url - str
		url for small card image
	card_large_image_url - str
		url for large card image
	reprompt_type - str
		speech type for repropmt
	reprompt_text - str
		text for reprompt
	repropmt_ssml - str
		str with ssml for Alexa to speak
	reprompt_play_behavior - str
		play behavior for reprompting
	should_end_session - bool
		whether or not to end the current session on response
	directives - list
		list of directives to respond with

	--- Methods ---
	addDirective(directive)
		adds directive to the current list of directives
	"""

	def __init__(self,
				 version="1.0",
				 session_attributes={},
				 output_speech_type=None,
				 text=None,
				 ssml=None,
				 play_behavior="ENQUEUE",
				 card_type=None,
				 card_title=None,
				 card_content=None,
				 card_text=None,
				 card_small_image_url=None,
				 card_large_image_url=None,
				 reprompt_type=None,
				 reprompt_text=None,
				 reprompt_ssml=None,
				 reprompt_play_behavior="ENQUEUE",
				 should_end_session=True,
				 directives=None,
				 ):
		"""
		--- Parameters ---
		version - int, str
			the version of the skill
		session_attributes - dict
			contains key-value pairs that persist in session
		output_speech_type - str
			the type of output speech (PlainText, ssml)
		text - str
			the text for Alexa to speak
		ssml - str
			str with ssml (Speech Synthesis Markup language) for Alexa to speak
		play_behavior - str (default is ENQUEUE)
			behavior for responding
		card_type - str
			type of card to create
		card_title - str
			title of card to create
		card_content - str
			content of card of type Simple
		card_text - str
			content of card of type Standard
		card_small_image_url - str
			url for small card image
		card_large_image_url - str
			url for large card image
		reprompt_type - str
			speech type for repropmt
		reprompt_text - str
			text for reprompt
		repropmt_ssml - str
			str with ssml for Alexa to speak
		reprompt_play_behavior - str
			play behavior for reprompting
		should_end_session - bool
			whether or not to end the current session on response
		directives - list
			list of directives to respond with

		if text is given but no output_speech_type is specified,
		defaults to PlainText

		if output_speech_type is not specified, and no text is given,
		no output speech is added

		if card_type is not specified, no card is added

		if no card image urls are specified, no card image is added

		if reprompt_type is not specified, no reprompt
		is added
		"""

		# builds the response skeleton
		self.response = {
			"version": "1.0",
			"response": {},  # creates the response object
		}

		# declares variables for managing objects
		if output_speech_type is None and text is None:
			self._hasOutputSpeech = False
		else:
			self._hasOutputSpeech = True

		if directives is None:
			self._hasDirectives = False
		else:
			self._hasDirectives = True

		if card_type is None:
			self._hasCard = False
		else:
			self._hasCard = True

		if card_small_image_url is None or card_large_image_url is None:
			self._hasImage = False
		else:
			self._hasImage = True

		if reprompt_type is None and reprompt_text is None:
			self._hasReprompt = False
		else:
			self._hasReprompt = True

		# if the user only supplies text, changes output_speech_type accordingly
		if output_speech_type is None and (not text is None):
			output_speech_type = "PlainText"
			version = "1.0"

		# private variables
		self._version = version
		self._session_attributes = session_attributes
		self._output_speech_type = output_speech_type
		self._text = text
		self._ssml = ssml
		self._play_behavior = play_behavior
		self._card_type = card_type
		self._card_title = card_title
		self._card_text = card_text
		self._card_content = card_content
		self._card_small_image_url = card_small_image_url
		self._card_large_image_url = card_large_image_url
		self._repropmt_type = reprompt_type
		self._reprompt_text = reprompt_text
		self._reprompt_ssml = reprompt_ssml
		self._reprompt_play_behavior = reprompt_play_behavior
		self._should_end_session = should_end_session
		self._directives = directives

		# assigns values according to parameters
		# note that these call the setter for each
		self.version = version
		self.session_attributes = session_attributes
		self.output_speech_type = output_speech_type
		self.text = text
		self.ssml = ssml
		self.play_behavior = play_behavior
		self.card_type = card_type
		self.card_title = card_title
		self.card_text = card_text
		self.card_content = card_content
		self.card_small_image_url = card_small_image_url
		self.card_large_image_url = card_large_image_url
		self.reprompt_type = reprompt_type
		self.reprompt_text = reprompt_text
		self.reprompt_ssml = reprompt_ssml
		self.reprompt_play_behavior = reprompt_play_behavior
		self.should_end_session = should_end_session
		self.directives = directives


	# --- Getters
	@property
	def version(self):
		return self._version


	@property
	def session_attributes(self):
		return self._session_attributes


	@property
	def output_speech_type(self):
		return self._output_speech_type


	@property
	def text(self):
		return self._text


	@property
	def ssml(self):
		return self._ssml


	@property
	def play_behavior(self):
		return self._play_behavior


	@property
	def card_type(self):
		return self._card_type


	@property
	def card_title(self):
		return self._card_title


	@property
	def card_content(self):
		return self._card_content


	@property
	def card_text(self):
		return self._card_text


	@property
	def card_small_image_url(self):
		return self._card_small_image_url


	@property
	def card_large_image_url(self):
		return self._card_large_image_url


	@property
	def reprompt_type(self):
		return self._reprompt_type


	@property
	def reprompt_text(self):
		return self._reprompt_text


	@property
	def reprompt_ssml(self):
		return self._reprompt_ssml


	@property
	def reprompt_play_behavior(self):
		return self._reprompt_play_behavior


	@property
	def should_end_session(self):
		return self._should_end_session


	@property
	def directives(self):
		return self._directives
	
	
	# --- Setters
	# all setters create their respective objects if necessary and
	# add given value to the response
	@version.setter
	def version(self, ver):
		self.response["version"] = str(ver)
		self._version = ver


	@session_attributes.setter
	def session_attributes(self, attributes):
		self.response["sessionAttributes"] = attributes
		self._session_attributes = attributes


	@output_speech_type.setter
	def output_speech_type(self, tp):
		if tp is not None:
			self._hasOutputSpeech = True
			self.response["response"]["outputSpeech"] = {}  # creates the output speech object
			self.response["response"]["outputSpeech"]["type"] = tp
		self._output_speech_type = tp

		# adds values to the output speech object if they were set before
		# the object's creation
		self.text = self._text
		self.ssml = self._ssml
		self.reprompt_play_behavior = self._reprompt_play_behavior


	@text.setter
	def text(self, text):
		if self._hasOutputSpeech:
			if self.output_speech_type == "PlainText":  # only adds if applicable
				self.response["response"]["outputSpeech"]["text"] = text
		elif not self._hasOutputSpeech and not text is None:
			self.output_speech_type = "PlainText"
			self.text = text
		self._text = text


	@ssml.setter
	def ssml(self, ssml):
		if self._hasOutputSpeech:
			if self.output_speech_type == "SSML":  # only adds if applicable
				self.response["response"]["outputSpeech"]["ssml"] = ssml
		elif not self._hasOutputSpeech and ssml is not None:
			self.output_speech_type = "SSML"
			self.ssml = ssml
		self._ssml = ssml


	@play_behavior.setter
	def play_behavior(self, play_behavior):
		if self._hasOutputSpeech:
			self.response["response"]["outputSpeech"]["playBehavior"] = play_behavior
		self._play_behavior = play_behavior


	@card_type.setter
	def card_type(self, card_type):
		if card_type is not None:
			self._hasCard = True
			self.response["response"]["card"] = {} # creates the card object
			self.response["response"]["card"]["type"] = card_type
		self._card_type = card_type

		# adds values to the card object if they were set before
		# the object's creation
		self.card_title = self._card_title
		self.card_text = self._card_text
		self.card_content = self._card_content
		self.card_small_image_url = self._card_small_image_url
		self.card_large_image_url = self._card_large_image_url


	@card_title.setter
	def card_title(self, card_title):
		if self._hasCard and card_title is not None:
			if self.card_type is not "LinkAccount":  # only adds if applicable
				self.response["response"]["card"]["title"] = card_title
		self._card_title = card_title


	@card_text.setter
	def card_text(self, card_text):
		if self._hasCard and card_text is not None:
			if self.card_type == "Standard":  # only adds if applicable
				self.response["response"]["card"]["text"] = card_text
		self._card_text = card_text


	@card_content.setter
	def card_content(self, card_content):
		if self._hasCard and card_content is not None:
			if self.card_type == "Simple":
				self.response["response"]["card"]["content"] = card_content
		self._card_content = card_content


	@card_small_image_url.setter
	def card_small_image_url(self, url):
		if self._hasCard:
			if self.card_type == "Standard":  # only adds if applicable
				if "image" not in self.response["response"]["card"]:
					self.response["response"]["card"]["image"] = {} # creates the image object
				self.response["response"]["card"]["image"]["smallImageUrl"] = url
		elif not self._hasCard and url is not None:
			if self.card_type == "Standard":
				if "image" not in self.response["response"]["card"]:
					self.response["response"]["card"]["image"] = {} # creates the image object
				self.response["response"]["card"]["image"]["smallImageUrl"] = url
		self._card_small_image_url = url


	@card_large_image_url.setter
	def card_large_image_url(self, url):
		if self._hasCard:
			if self.card_type == "Standard":  # only adds if applicable
				if "image" not in self.response["response"]["card"]:
					self.response["response"]["card"]["image"] = {} # creates the image object
				self.response["response"]["card"]["image"]["largeImageUrl"] = url
		elif not self._hasCard and url is not None:
			if self.card_type == "Standard":
				if "image" not in self.response["response"]["card"]:
					self.response["response"]["card"]["image"] = {} # creates the image object
				self.response["response"]["card"]["image"]["largeImageUrl"] = url
		self._card_large_image_url = url


	@reprompt_type.setter
	def reprompt_type(self, tp):
		if tp is not None:
			self._hasReprompt = True
			self.response["response"]["reprompt"] = {} # creates the reprompt object
			self.response["response"]["reprompt"]["outputSpeech"] = {}
			self.response["response"]["reprompt"]["outputSpeech"]["type"] = tp
		self._reprompt_type = tp

		# adds values to the reprompt speech object if they were set before
		# the object's creation
		self.reprompt_text = self._reprompt_text
		self.repropmt_ssml = self._reprompt_ssml
		self.reprompt_play_behavior = self._reprompt_play_behavior


	@reprompt_text.setter
	def reprompt_text(self, text):
		if self._hasReprompt:
			if self.reprompt_type == "PlainText":  # only adds if applicable
				self.response["response"]["reprompt"]["outputSpeech"]["text"] = text
		elif not self._hasReprompt and text is not None:
			self.reprompt_type = "PlainText"
			self.reprompt_text = text
		self._reprompt_text = text


	@reprompt_ssml.setter
	def reprompt_ssml(self, ssml):
		if self._hasReprompt:
			if self.reprompt_type == "SSML": # only adds if applicable
				self.response["response"]["reprompt"]["outputSpeech"]["ssml"] = ssml
		elif not self._hasReprompt and ssml is not None:
			self.reprompt_type = "SSML"
			self.response["response"]["reprompt"]["outputSpeech"]["ssml"] = ssml
		self._reprompt_ssml = ssml


	@reprompt_play_behavior.setter
	def reprompt_play_behavior(self, behavior):
		if self._hasReprompt:
			self.response["response"]["reprompt"]["outputSpeech"]["playBehavior"] = behavior
		self._reprompt_play_behavior = behavior


	@directives.setter
	def directives(self, directives):
		# if no previous directives have been added
		if not self._hasDirectives and not directives is None:
			self._hasDirectives = True
			self.response["response"]["directives"] = []  # creates the directives array
		# if there are directives
		elif self._hasDirectives and directives is not None:
			# if there have been directives previously
			if not self._directives is None:
				self.response["response"]["directives"].extend(directives)
			# if directives have been added previously
			elif self._directives is None:
				self.response["response"]["directives"] = []  # creates the directives array
				self.response["response"]["directives"].extend(directives)
		self._directives = directives


	@should_end_session.setter
	def should_end_session(self, should_end_session):
		self.response["response"]["shouldEndSession"] = should_end_session
		self._should_end_session = should_end_session


	# --- Methods
	def addDirective(self, directive):
		"""Adds a directive to the response

		--- Parameters ---
		directive - dict
			the directive to add
		"""

		self._hasDirectives = True
		self.directives = [directive]


	def serialize(self):
		"""Serializes into JSON"""

		return json.dumps(self.response)
	