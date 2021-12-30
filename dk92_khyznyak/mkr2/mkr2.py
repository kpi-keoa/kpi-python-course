#!/usr/bin/env python
import sys
import enum
from random import randrange
from typing import NamedTuple

print("This program is my credit work, that realizes decks of cards.")

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

unicode_suits = {
    'hearts': '♥️',
    'diamonds': '♦️',
    'peaks': '♠️',
    'cross': '♣️'
}

size_classic = 36
size_french = 52

rank_carddeck = {
    'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6'
}

rank_frenchdeck = {'A', 'K', 'Q', 'J', '10',
    '9', '8', '7', '6',
    '5', '4', '3', '2'}

rank_frenchdeck = rank_frenchdeck.union(rank_carddeck)

err_text = 'Change your card`s suit'

class SuitErr():
    def init(self):
        self.txt = err_text

class Card(NamedTuple):
    """Class Card includes suit and rank."""

    suit = ""
    rank = ""

class CardDeck:
    """Classic deck."""

    def init(self, sets = rank_carddeck):
        """Constructing attributes. """
        self.sets = sets
        self.cards = generate_card_deck(self.sets)
        self.size = len(self.cards)

    def shuffle(self, times):
        for mix in range(times):
            random.shuffle(self.cards)


    def handout(self, n_players, m_cards):
        """Give cards for players"""
        completed_players_sets = []
        if (n_players * m_cards) > self.size:
            return completed_players_sets
        else:
            for player in range(n_players):
                completed_players_sets.append(self.cards[:m_cards])
                del self.cards[:m_cards]

        self.size = len(self.cards)
        return completed_players_sets


    def comparison (self, other: Card):
        if self.rank == other.rank:
            return self.rank == other.rank
        elif self.rank != other.rank:
            return self.rank != other.rank
        elif self.rank < other.rank:
            return self.rank < other.rank
        elif self.rank > other.rank:
            return self.rank > other.rank


    def gen_deck(self):
        """Generating new deck"""
        self.cards = generate_card_deck(self.sets)
        self.size = len(self.cards)


class FrenchDeck(CardDeck):
    """Change for french type"""
    def init(self):
        self.rank_carddeck = {'A', 'K', 'Q', 'J', '10',
    '9', '8', '7', '6',
    '5', '4', '3', '2'}
