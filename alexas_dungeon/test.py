from manager import *

event = {
	"version": "1.0",
	"session": {
		"new": False,
		"sessionId": "amzn1.echo-api.session.40c8a1b2-6d36-4433-9772-ebf6300111b9",
		"application": {
			"applicationId": "amzn1.ask.skill.ebab492b-fe32-4752-a720-5bdf879ebb81"
		},
		"attributes": {
			"dungeon": {
			        "numFloors": 1,
			        "floors": [
			        {
			          "floorNum": 0,
			          "entry": [
			            1,
			            0
			          ],
			          "rooms": [
			            [
			              None,
			              {
			                "typ": 1,
			                "enemies": 2,
			                "chest": None
			              }
			            ],
			            [
			              {
			                "typ": 2,
			                "enemies": 0,
			                "chest": None
			              },
			              {
			                "typ": 3,
			                "enemies": 0,
			                "chest": "unopened"
			              }
			            ]
			          ]
			        }
			      ]
			    },
			    "player": {
			      "row": 1,
			      "col": 0,
			      "orient": "right",
			      "inventory": {
			        "weapons": [
			          {
			            "name": "Starter Sword",
			            "stack_limit": 1
			          },
			          {
			            "name": "Starter Sword",
			            "stack_limit": 1
			          }
			        ],
			        "max_weapons": 2,
			        "spells": [],
			        "max_spells": 2,
			        "armor": [],
			        "max_armor": 3,
			        "ammo": [],
			        "max_ammo": 4,
			        "passive": [],
			        "max_passive": 2
			      }
			    },
			    "state": "moving",
			    "cur_floor": 0
    },
		"user": {
			"userId": "amzn1.ask.account.AGLRQPFNFQGID2KZ7OX4MELKJ4ICPZWTKHOGO6AU3ISUYIU6WVFDESDRQCY55VDA4ZHU75PE7CUYTPSDWWB7YY67IOBRNKOMWZHRF4SP6UFUAPJOWTDAN6F7H5YILSSLBX5TWLN4HJR5L47I7ZHG6ZQYV2MDIVEIXJ7RAF6ZG66KCDNO7SLROADZMTMNJO7YHCG5PUYDNYGJCHQ"
		}
	},
	"context": {
		"System": {
			"application": {
				"applicationId": "amzn1.ask.skill.ebab492b-fe32-4752-a720-5bdf879ebb81"
			},
			"user": {
				"userId": "amzn1.ask.account.AGLRQPFNFQGID2KZ7OX4MELKJ4ICPZWTKHOGO6AU3ISUYIU6WVFDESDRQCY55VDA4ZHU75PE7CUYTPSDWWB7YY67IOBRNKOMWZHRF4SP6UFUAPJOWTDAN6F7H5YILSSLBX5TWLN4HJR5L47I7ZHG6ZQYV2MDIVEIXJ7RAF6ZG66KCDNO7SLROADZMTMNJO7YHCG5PUYDNYGJCHQ"
			},
			"device": {
				"deviceId": "amzn1.ask.device.AEWVMLB4HDTNYAFTIYNYT7DO66SARKAC7SR23XP5HZ3OJLDY5WRVB6UUPOLDJR3ODHHSWIJYG5QQGZYM5MPRMIIZWNYTKZUM77GDWSKJZKSODRHKBT3OYFCBFFASD4GAAUN2NUFOS6AEFZAN2SBXBG5LEA2Q",
				"supportedInterfaces": {}
			},
			"apiEndpoint": "https://api.amazonalexa.com",
			"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmViYWI0OTJiLWZlMzItNDc1Mi1hNzIwLTViZGY4NzllYmI4MSIsImV4cCI6MTU1MDgwOTM3MiwiaWF0IjoxNTUwODA5MDcyLCJuYmYiOjE1NTA4MDkwNzIsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVXVk1MQjRIRFROWUFGVElZTllUN0RPNjZTQVJLQUM3U1IyM1hQNUhaM09KTERZNVdSVkI2VVVQT0xESlIzT0RISFNXSUpZRzVRUUdaWU01TVBSTUlJWldOWVRLWlVNNzdHRFdTS0paS1NPRFJIS0JUM09ZRkNCRkZBU0Q0R0FBVU4yTlVGT1M2QUVGWkFOMlNCWEJHNUxFQTJRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUdMUlFQRk5GUUdJRDJLWjdPWDRNRUxLSjRJQ1BaV1RLSE9HTzZBVTNJU1VZSVU2V1ZGREVTRFJRQ1k1NVZEQTRaSFU3NVBFN0NVWVRQU0RXV0I3WVk2N0lPQlJOS09NV1pIUkY0U1A2VUZVQVBKT1dUREFONkY3SDVZSUxTU0xCWDVUV0xONEhKUjVMNDdJN1pIRzZaUVlWMk1ESVZFSVhKN1JBRjZaRzY2S0NETk83U0xST0FEWk1UTU5KTzdZSENHNVBVWUROWUdKQ0hRIn19.h9Yh2cKu8DXb7vl1Ma_9u5Qgjr7_4jjRo0u_krnPR7NRRGxziNCSRYooLpbKdq8jihlcc1l40QXf1dAx9Ke0tq9A-YkaY5_9lGm_c1h8w9ZdssH5v3XQPipiSqaYYyWmDDmQKwHv7WH917KuxwAM-ZzAl5Rj2r9NwFNs94x0R9Po8SNnOE2wpnott6mB9ePaLF6FE9_C-nReYwQlK78ncdvAtcCDR_kofUWeYenQlUp68em49wZDe0RBKDSqEtI6DKKHWGefGCIhbT4b3njkAZ4pMrRSr-A7I6seHOYgnCXp2s0HwWJFqgA199LvfFYUcB6QElCGseWNqH2k9QJ76w"
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
		"type": "IntentRequest",
		"requestId": "amzn1.echo-api.request.abc3c835-09d9-4a3c-8a7c-712100d6194a",
		"timestamp": "2019-02-22T04:17:52Z",
		"locale": "en-US",
		"intent": {
			"name": "NewGame",
			"confirmationStatus": "NONE",
			"slots": {
				"dir": {
					"name": "dir",
					"value": "forward",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.ebab492b-fe32-4752-a720-5bdf879ebb81.direction",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "forward",
											"id": "965dbaac085fc891bfbbd4f9d145bbc8"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE",
					"source": "USER"
				}
			}
		}
	}
}
print(lambda_handler(event, "hello"))
