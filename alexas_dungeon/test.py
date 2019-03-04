from manager import *

event = {
	"version": "1.0",
	"session": {
		"new": False,
		"sessionId": "amzn1.echo-api.session.b1f72fbe-e160-45e9-a166-62049d7702bb",
		"application": {
			"applicationId": "amzn1.ask.skill.ebab492b-fe32-4752-a720-5bdf879ebb81"
		},
		"attributes": {
			"state": "moving",
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
									"chest": {
										"opened": False,
										"item": None
									}
								}
							]
						]
					}
				]
			},
			"cur_floor": 0,
			"player": {
				"row": 1,
				"col": 1,
				"orient": "right",
				"inventory": {
					"weapons": [
						{
							"name": "Starter Sword",
							"stack_limit": 1,
							"typ": "Weapon"
						}
					],
					"max_weapons": 2,
					"spells": [
						{
							"name": "Water Bolt",
							"stack_limit": 1,
							"typ": "Spell"
						}
					],
					"max_spells": 2,
					"armor": [],
					"max_armor": 3,
					"ammo": [],
					"max_ammo": 4,
					"passive": [],
					"max_passive": 2
				}
			}
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
			"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmViYWI0OTJiLWZlMzItNDc1Mi1hNzIwLTViZGY4NzllYmI4MSIsImV4cCI6MTU1MTYyOTY5MywiaWF0IjoxNTUxNjI5MzkzLCJuYmYiOjE1NTE2MjkzOTMsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVXVk1MQjRIRFROWUFGVElZTllUN0RPNjZTQVJLQUM3U1IyM1hQNUhaM09KTERZNVdSVkI2VVVQT0xESlIzT0RISFNXSUpZRzVRUUdaWU01TVBSTUlJWldOWVRLWlVNNzdHRFdTS0paS1NPRFJIS0JUM09ZRkNCRkZBU0Q0R0FBVU4yTlVGT1M2QUVGWkFOMlNCWEJHNUxFQTJRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUdMUlFQRk5GUUdJRDJLWjdPWDRNRUxLSjRJQ1BaV1RLSE9HTzZBVTNJU1VZSVU2V1ZGREVTRFJRQ1k1NVZEQTRaSFU3NVBFN0NVWVRQU0RXV0I3WVk2N0lPQlJOS09NV1pIUkY0U1A2VUZVQVBKT1dUREFONkY3SDVZSUxTU0xCWDVUV0xONEhKUjVMNDdJN1pIRzZaUVlWMk1ESVZFSVhKN1JBRjZaRzY2S0NETk83U0xST0FEWk1UTU5KTzdZSENHNVBVWUROWUdKQ0hRIn19.XE-OkK6vTj4L4ds2GBuI_7SyjRR8QTOuUqw8_rvVp5ta0hBRdYFNLR7U9Jxltg_VLbpVKWSVabm48om0Mj8GrFc9c77oBenOIMWalyQEZWIo7-weFhxQDQOwDhhL0-jc4YXNuDrtwfUsRtPzhwypm-T6ISfD55fhM_oif7zjI0BCPzXcYlUZ6PPHjNEMpRbnNNcfc4LG8CBiRImE4SgUyGuJD9OqN3MeN1UU1Pmd7rEWFiTGHFKswTyjkKO1Hh8kTm3briSyzlEJBXeJSOvqxFvyYb13nMBZpKzP5hYmibEtl4Zqq22PNa5q1DTmW8IPFDnzOowWLmjcnLEHPB6_9Q"
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
		"requestId": "amzn1.echo-api.request.62712ebe-97ba-4491-8fff-d2e1909b6361",
		"timestamp": "2019-03-03T16:09:53Z",
		"locale": "en-US",
		"intent": {
			"name": "DropItem",
			"confirmationStatus": "NONE",
			"slots": {
				"item": {
					"name": "item",
					"value": "Elven Sword",
					"confirmationStatus": "NONE",
					"source": "USER"
				},
				"item_type": {
					"name": "item_type",
					"value": "weapon",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.ebab492b-fe32-4752-a720-5bdf879ebb81.itemTypes",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "weapon",
											"id": "282aa351a2bd30655fbc060bd4f33766"
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
