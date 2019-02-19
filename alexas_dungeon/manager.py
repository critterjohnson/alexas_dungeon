from dungeon import *
from state import *
from alexatools import *
import constants


def lambda_handler(event, context):
	at = AlexaTools(event, context)

	@at.handler("LaunchRequest")
	def launch(request):
		dung = Dungeon(numFloors=1)
		response = AlexaResponse()
		response.session_attributes = {"dungeon": dung.serialize()}
		return response

	return at.run()


# testing
if __name__ == "__main__":
	event = {
		"version": "1.0",
		"session": {
			"new": True,
			"sessionId": "amzn1.echo-api.session.df1c4379-8e49-4db6-a5ec-d6a24d5f97e8",
			"application": {
				"applicationId": "amzn1.ask.skill.72472507-d7d8-4fdb-976e-0f6c8d68d38d"
			},
			"user": {
				"userId": "amzn1.ask.account.AESUOTE2XHUUL5HSROYFZEDW44X7OPOK2XDSAASZAZIUQNSRY5XUFDRSFPTLADTAIQFNW625MOFVLBG4WF3Z2XT5GDBFVZ2XHIMSLYASNYB5QW3EBLXTQGRB6BQJ3MCCWKEBLFDALMKCYU2I6FZKVECTUFLPN3USKB2X2JL2PCZ5NTK26WY3ZQRIPAZ7SQY7HKVWHNAQW3XYMOY"
			}
		},
		"context": {
			"System": {
				"application": {
					"applicationId": "amzn1.ask.skill.72472507-d7d8-4fdb-976e-0f6c8d68d38d"
				},
				"user": {
					"userId": "amzn1.ask.account.AESUOTE2XHUUL5HSROYFZEDW44X7OPOK2XDSAASZAZIUQNSRY5XUFDRSFPTLADTAIQFNW625MOFVLBG4WF3Z2XT5GDBFVZ2XHIMSLYASNYB5QW3EBLXTQGRB6BQJ3MCCWKEBLFDALMKCYU2I6FZKVECTUFLPN3USKB2X2JL2PCZ5NTK26WY3ZQRIPAZ7SQY7HKVWHNAQW3XYMOY"
				},
				"device": {
					"deviceId": "amzn1.ask.device.AHBBECUWVUNBD5CA3S6RLHGQ7NBZFKYTRSK7NBE5NNJT5TO3MMUTHZUS3EMRRJEFWKCC2ZRQX45G55YQFCGMQKVJAO7INITSUKBFGUDRLEISTHCXB5KTRJBSTKWJSZ3ERN6AHHPBBZBGT6ODD2SSKXKNC4IA",
					"supportedInterfaces": {}
				},
				"apiEndpoint": "https://api.amazonalexa.com",
				"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjcyNDcyNTA3LWQ3ZDgtNGZkYi05NzZlLTBmNmM4ZDY4ZDM4ZCIsImV4cCI6MTU1MDQ3MDQ5MSwiaWF0IjoxNTUwNDcwMTkxLCJuYmYiOjE1NTA0NzAxOTEsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhCQkVDVVdWVU5CRDVDQTNTNlJMSEdRN05CWkZLWVRSU0s3TkJFNU5OSlQ1VE8zTU1VVEhaVVMzRU1SUkpFRldLQ0MyWlJRWDQ1RzU1WVFGQ0dNUUtWSkFPN0lOSVRTVUtCRkdVRFJMRUlTVEhDWEI1S1RSSkJTVEtXSlNaM0VSTjZBSEhQQkJaQkdUNk9ERDJTU0tYS05DNElBIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUVTVU9URTJYSFVVTDVIU1JPWUZaRURXNDRYN09QT0syWERTQUFTWkFaSVVRTlNSWTVYVUZEUlNGUFRMQURUQUlRRk5XNjI1TU9GVkxCRzRXRjNaMlhUNUdEQkZWWjJYSElNU0xZQVNOWUI1UVczRUJMWFRRR1JCNkJRSjNNQ0NXS0VCTEZEQUxNS0NZVTJJNkZaS1ZFQ1RVRkxQTjNVU0tCMlgySkwyUENaNU5USzI2V1kzWlFSSVBBWjdTUVk3SEtWV0hOQVFXM1hZTU9ZIn19.ffSNAQ4Dt8nxoonQ2u3uNbwDOC95DhhTRX_HzTmg3Sx_tchCNt3OJg2FtekOsmlMqQ5D1Cs_YWqBCoVshetOn9gn6hR-iAR2lKPQs2cwi2BPrwwhuH3vwpfEvUJ5OZQ1WffjhhpG22hm0uSFarOviNrBdYH8_cx3IMp0E7O5p08KSccAA7HOgoPVDzs4JHWYYYG4EqXllvC_ljHeACiejmFjR7R52MgyBnVrTIz3K5x2XUBXCkFwXQ4STYsHm4pUg_wmpYJlX3SxXKRQxWvgNiv879wq3Zs5TeKcBTQj6U2fowwa1mrQxOyCoU6DCDnTB_Jlq-cq2xJqPwb_A0FMLw"
			},
			"Viewport": {
				"experiences": [
					{
						"arcMinuteWidth": 246,
						"arcMinuteHeight": 144,
						"canRotate": False,
						"canResize": False
					}
				],
				"shape": "RECTANGLE",
				"pixelWidth": 1024,
				"pixelHeight": 600,
				"dpi": 160,
				"currentPixelWidth": 1024,
				"currentPixelHeight": 600,
				"touch": [
					"SINGLE"
				]
			}
		},
		"request": {
			"type": "LaunchRequest",
			"requestId": "amzn1.echo-api.request.01dfbcad-bd41-48e8-9b29-3a483cfdbb78",
			"timestamp": "2019-02-18T06:09:51Z",
			"locale": "en-US",
			"shouldLinkResultBeReturned": False
		}
	}
	print(lambda_handler(event, "hello"))
