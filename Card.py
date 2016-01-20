"""
Written by Dietrich Geisler
Last modified 1/14/2016
"""

class card:
	def __init__(self, name, cost, type):
		self.name = name
		self.cost = cost
		self.type = type
		
class treasure_card(card):
	def __init__(self, name, cost, value):
		super(name, cost, 't')
		self.value = value
		
class victory_card(card):
	def __init__(self, name, cost, value):
		super(name, cost, 'v')
		self.value = value
		
"""
info must be a tab-deliminated string detailing how this action card functions
"""
class action_card(card):
	def __init__(self, name, cost, info):
		super(name, cost, 'a')
		self.action = []
		for item in info:
			self.action.append(item)