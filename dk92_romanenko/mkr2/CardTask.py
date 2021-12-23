import enum
from random import randrange
from typing import NamedTuple

"""This module realise card environment for
game dev. in gambling. There demonstating
demo below. Can be as import module as callable
program.


"""

unicode_suits = {
    'spades': '♠',
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣'
}

err_text = 'SuitErr: Your suits are not the same'

size_classic = 36
size_french = 52
# for 36
rank_set_classic = {
    '6', '7', '8',
    '9', '10', 'J',
    'Q', 'K', 'A'
}
# for 54
rank_set_french = {
    '2', '3',
    '4', '5'
}

rank_set_french = rank_set_french.union(rank_set_classic)


def generate_card_deck(rank_set):
    """Return generater list from <rank_set>-number classes"""
    card_list = []
    for rank_id in rank_set:
        for suit_id in Suit:
            card_list.append(Card(suit_id.name, rank_id))

    return card_list


class SuitErr():
	def __init__(self):
		self.txt = err_text


class Suit(enum.Enum):
	"""Enum list of suits"""
	spades = 0
	hearts = 1
	diamonds = 2
	clubs = 3


class Card(NamedTuple):
	"""Card class"""

	suit: str
	rank: str


class CardDeck:
	"""A class to represent a classic card deck.

	Attributes:
		sets: list of ranks in card deck

	Methods:
		shuffle(times): shuffle card deck
		hangout(num_players, num_cards): hangout crads for players
		gen_new_deck(): generate new deck after game

	"""

	def __init__(self, sets = rank_set_classic):
		"""
        Constructs all the necessary attributes for the object.

        Parameters:
            sets: list of ranks in card deck
        """
		self.sets = sets
		self.cards = generate_card_deck(self.sets)
		self.size = len(self.cards)


	def __eq__(self, other: Card):
		return self.rank == self.rank


	def __ne__(self, other: Card):
		return self.rank != other.rank


	def __lt__(self, other: Card):
		return self.rank < other.rank


	def __gt__(self, other: Card):
		return self.rank > other.rank


	def __le__(self, other: Card):
		return self.rank <= other.rank


	def __ge__(self, other: Card):
		return self.rank >= other.rank

	def shuffle(self, times):
		"""
		Shuffle card deck in random position

		Args:
			times: set number of shuffle's intterations   
		Returns:
			none (void)
		"""
		for swaps in range(times):
			element_a = randrange(self.size)
			element_b = randrange(self.size)
			tmp = self.cards[element_a]
			self.cards[element_a] = self.cards[element_b]
			self.cards[element_b] = tmp


	def handout(self, num_players, num_cards):
		"""
		Shuffle card deck in random position

		Args:
			num_players: how many players need cards
			num_cards: how many cards need for players
		Returns:
			type <list>, cards pair
		"""
		completed_players_sets = []
		if (num_cards * num_players) > self.size:
			return completed_players_sets
		else: 
			for player in range(num_players):
				completed_players_sets.append(self.cards[:num_cards])
				del self.cards[:num_cards]

			self.size = len(self.cards)
			return completed_players_sets	


	def gen_new_deck(self):
		self.cards = generate_card_deck(self.sets)
		self.size = len(self.cards)


class FrenchDeck(CardDeck):
	"""inheritance of CardDeck for French-type deck"""
	def __init__(self):
		CardDeck.__init__(self, rank_set_french)
		

if __name__ == '__main__':

	# Demonstation of CardDeck
	card_dck = CardDeck()

	print(card_dck.cards)
	print(card_dck.size)
	print('\n')

	card_dck.shuffle(30)

	print(card_dck.handout(3, 3))
	print(card_dck.size)
	print('\n')

	print(card_dck.cards)
	print('\n')

	card_dck.gen_new_deck()

	print(card_dck.cards)
	print(card_dck.size)

	# Demonstation of FrenchDeck
	card_dck = FrenchDeck()

	print(card_dck.cards)
	print(card_dck.size)
	print('\n')

	card_dck.shuffle(30)

	print(card_dck.handout(3, 3))
	print(card_dck.size)
	print('\n')

	print(card_dck.cards)
	print('\n')

	card_dck.gen_new_deck()

	print(card_dck.cards)
	print(card_dck.size)

	str(card_dck)