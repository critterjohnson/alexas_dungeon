from .alexarequest import AlexaRequest
from ..responsebuilder.alexaresponse import AlexaResponse
from .errors import *


class AlexaTools:
	"""Handles requests sent by Alexa

	--- Attributes ---
	event - dict
		the request JSON sent to Lambda by Alexa
	context 
		the context object sent by Alexa
	handlers - dict
		dictionary of hander functions to handle requests

	--- Methods ---
	handler(name)
		used to decorate an event handler
	run()
		handles the request using provided handlers
	"""

	def __init__(self, event, context):
		"""
		--- Parameters ---
		event - dict
			the event JSON sent by Alexa
		context
			the context object sent by Alexa
		"""

		self.event = event
		self.context = context
		self.handlers = {}


	# adds a function by name to the list of handlers
	# should be used as a decorator
	def handler(self, name):
		"""Used to decorate an event handler
		
		if 'name' is the name of a request type, function will be called
		when that request is given

		if 'name' is the name of an intent, function will be called to
		handle that intent

		--- Parameters ---
		name - str
			the name of the event/intent to handle

		--- Returns ---
		wrapper function with parameter (func) to decorate passed
		function
		"""

		def wrapper(func):
			self.handlers[name] = func
		return wrapper


	# runs the correct handler for the event
	def run(self):
		requestType = self.event["request"]["type"]
		request = AlexaRequest(self.event)
		if requestType == "IntentRequest":
			intent = self.event["request"]["intent"]["name"]
			try:
				response = self.handlers[intent](request)
			except KeyError:
				raise(UnhandledEventError("There was no handler for the intent %s" % intent))
		else:
			try:
				response = self.handlers[requestType](request)
			except KeyError:
				raise(UnhandledEventError("There was no handler for event %s" % requestType))

		if isinstance(response, AlexaResponse):
			return response.response
		else:
			return response
