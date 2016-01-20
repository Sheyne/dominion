"""
Represents a game of dominion. 

Definition of terms:

card:			a card in the game, always represented by the Card class.
player:			a player in the game, represented by anything that can be used 
				as a hashable key. 
deck:			the collection of cards that a player "owns"
draw pile:		the collection of cards a player has the potential to draw
discard pile:	the collection of cards a player has discarded
hand:			the collection of cards in a players hand
trash:			the collection of cards that have been trashed


# TODO figure out how to account for "reveals"
"""
class Game(object):
	def __init__(self, cards, players):
		"""
		Initialize the game with a set of cards to be in play and players to be involved. 

		`cards` should be a set (or any iterable with no duplicates) of `Card` objects.
		`players` should be a set-like iterable of unique identifiers
		"""

		## todo make sure to copy cards to a new set, so that if it's a once time iterable
		## we don't loose cards (same with players)
		## e.g. 
		# self.cards = set(cards)

	def play(self, player, card):
		"""
		Have the player play this card.

		return boolean indicating whether playing this card was legal
		"""

	def hand(self, player):
		"return an iterable of the hand of the given player"

	def deck(self, player):
		"""
		return an iterable containing the deck of a given player
		"""