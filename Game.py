"""
Written by Dietrich Geisler
Last modified 1/14/2016
"""

from Card import *

class pile:
	def __init__(self, count, type):
		self.count = count
		self.type = type
		
	def buy(self):
		self.count -= 1
		return type.value

class game:
	def __init__(self):
		self.cards = []
		self.cards.append(pile(60, treasure_card("copper", 0, 1)))
		self.cards.append(pile(40, treasure_card("silver", 3, 2)))
		self.cards.append(pile(30, treasure_card("gold", 6, 3)))
		self.cards.append(pile(8, victory_card("estate", 2, 1)))
		self.cards.append(pile(8, victory_card("duchy", 5, 3)))
		self.cards.append(pile(8, victory_card("province", 8, 6)))
		self.cards.append(pile(10, victory_card("curse", 0, -1)))

g = game()
print(g.cards[0].buy())