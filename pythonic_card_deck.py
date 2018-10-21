import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suite'])

class FrenchDeck:
    ranks = [str(n) for n in range (2,11)] + list('JQKA')
    suites = 'spades diamons clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suite)    for suite in self.suites
                                            for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

    def add(self, card):
        if card not in self._cards:
            self._cards.append(card)
        
    def __len__(self):
            return len(self._cards)

    def __getitem__(self, position):
            return self._cards[position]

    def __str__(self):
        sb = ["LEN FRENCH DECK: {0}".format(self.__len__())]
        sb = sb + ["CARD: {0}".format(card) for card in self._cards]
        return "\n".join(sb)

if __name__ == "__main__":
    deck = FrenchDeck()
    deck.shuffle()
    deck.add(Card('2', 'spades'))
