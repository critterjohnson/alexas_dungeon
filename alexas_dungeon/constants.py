"""
--- Room Types ---
1 = Standard
2 = Entrance
3 = Chest
"""

floors = [
	[
		[None, {"type": 1, "chanceExists": 50, "dependencies": [(1, 1)], "enemyWeight": 2}],
		[{"type": 2, "chanceExists": 100, "dependencies": None, "enemyWeight": 0}, {"type": 3, "chanceExists": 100, "dependencies": None, "enemyWeight": 0}],
	],
]


item_rarities = ["common", "uncommon", "rare"]
rarity_values = [60, 30, 10]
