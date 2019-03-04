import json

with open("items.json") as file:
	json_data = json.load(file)

item_slot = {"name": "item_list", "values": []}

for a, b in json_data.items():
	floor_data = b
	for c, d in floor_data.items():
		rarity_data = d
		for e, f in rarity_data.items():
			item_name = e
			item_slot["values"].append(
				{
					"name": {
						"value": e
					}
				})

print(json.dumps(item_slot))
