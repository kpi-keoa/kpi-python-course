from typing import NamedTuple
import random


SUITS = '\u2665\u2666\u2663\u2660'
RANG_TO_VALUE = { 11 : "B", 12: "D", 13: "K",14:"A"}

''' Викорестання змінних потрібно для того, щоб не сторювати їх локальні дублікати '''

class  Card(NamedTuple):
   suit: str
   rang: int 
   
   def print_card(self):
       str_rang = RANG_TO_VALUE.get(self.rang, str(self.rang))

       print (f'\n┌───────┐',f'\n| {str_rang:<2}    |',
               f'\n|       |\n|   {self.suit}   |',
               f'\n|       |\n|    {str_rang:>2} |\n└───────┘' 
               )

''' Ініціалізація классу однієї карти '''

class CardDack():
    DECK_LEN = 36
    FERST_CARD = 6


    def __init__(self, deck = None ):
        self.deck = deck or [None] * self.DECK_LEN
        for i in range(1, len(SUITS) + 1):
            for j in range(self.FERST_CARD, 14+ 1):
                self.deck[(i - 1) * (15-self.FERST_CARD) + (j - self.FERST_CARD)] = Card(SUITS[i-1], j )

    def __eq__(self,other):
        if (self.suit == other.suit):
           return self.rang == other.rang

    def __lt__(self, other):
        if (self.suit == other.suit):
           return self.rang < other.rang

    def shuffle(self):
        random.shuffle(self.deck)

    def handout(self,card_numb,namber_player):
        deck_index = 0
        players_cards =[]
        for i in range(namber_player):
            current_player_cards = []
            for j in range(card_numb): 
                current_player_cards.append(self.deck[deck_index])
                deck_index+= 1
            players_cards.append(current_player_cards)
        self.deck = self.deck[deck_index:]
        return players_cards

class FrenchDeck(CardDack):
    DECK_LEN = 52
    FERST_CARD = 2

''' Опис виконування класу та функцій 
    

 Два класи (FrenchDeck та CardDack) мають однаковий конструктор. 
 Змінна DECK_LEN використовується для ініціалізації списку з заданою довжиною.
 Змінна FERST_CARD задає значення першої карти для подальшого розрахунку. 
 Функція shuffle реалізована як метод классу. 
 Функція handout використовується для того, щоб сторити список списків(руку гравця).
 Функція self.deck = self.deck[deck_index:] використовується для зрізу списку колоди(забирання карт з колоди).
    
    '''

def print_deck(deck):
    for item in deck:
        item.print_card()


if __name__=="__main__":

    print ('Начало работы. Первая Колода')
    ferst_deck = CardDack()
    ferst_deck.shuffle()
    print_deck(ferst_deck.deck)

    print ('Начало работы. Вторая Колода')
    second_deck = FrenchDeck()
    second_deck.shuffle()
    print_deck(second_deck.deck)

    if( ferst_deck.deck[1] == second_deck.deck[1]):
        print('Карти однакові')
    else:
        print('Карти не однакові')


    print ('Конец работы. ')