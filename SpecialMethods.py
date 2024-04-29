# pythonic card deck
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    # Supports slicing, iteration
    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ =='__main__':
    deck  = FrenchDeck()
    print(len(deck))
    # print(deck[0])
    # print(choice(deck))
    # print(deck[:3])
    for card in sorted(deck, key = spades_high):
        print(card)
    # for card in deck:
    #     print(card)
    # print(Card('Q', 'hearts') in deck)