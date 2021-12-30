from enum import Enum
from random import randrange
from typing import NamedTuple

unicode_suits = {
    'spades': '♠',
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣'
}

size_classic = 36
size_french = 52

set_classic = {
    '6', '7', '8',
    '9', '10', 'J',
    'Q', 'K', 'A'
}

set_french = {'2', '3', '4', '5'}

rank_set_french = set_french.union(set_classic)

def generate_card_deck(rank_set):
    card_list = []
    for rank_id in rank_set:
        for suit_id in Suit:
            card_list.append(Card(suit_id.name, rank_id))

    return card_list

class Suit(Enum):
    spades = 0
    hearts = 1
    diamonds = 2
    clubs = 3


class Card(NamedTuple):
    suit: str
    rank: str


class CardDeck:
    def __init__(self, sets=set_classic):
        self.rank = None
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
        for _ in range(times):
            element_a = randrange(self.size)
            element_b = randrange(self.size)
            tmp = self.cards[element_a]
            self.cards[element_a] = self.cards[element_b]
            self.cards[element_b] = tmp

    def handout(self, num_players, num_cards):
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
    def __init__(self):
        CardDeck.__init__(self, rank_set_french)


if __name__ == '__main__':
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

