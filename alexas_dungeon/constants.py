"""
--- Room Types ---
2 = Entrance
"""

floors = [
	[
		[None, {"type": 1, "chanceExists": 50, "dependencies": [(1, 1)], "enemyWeight": 2}],
		[{"type": 2, "chanceExists": 100, "dependencies": None, "enemyWeight": 0}, {"type": 1, "chanceExists": 100, "dependencies": None, "enemyWeight": 0}],
	],
]