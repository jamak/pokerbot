from cards import Card
from cards import suitList as suits
from cards import rankList as ranks
from operator import and_ as ans
from operator import eq
royal = set([10, "J", "Q", "K", "A"])
hand_types = {"HC":ranks, "1P":ranks, "":ranks, "":ranks[5:], "":ranks[5:],  }

class Hand(object):
    """a poker hand"""
    def __init__(self, cards):
        super(Hand, self).__init__()
        self.cards = cards
        self.rank = None

    def by_suit(self):
        """sort the cards by face"""
        self.cards.sort(key=lambda card: card.suit)

    def by_rank(self):
        """sort the cards by value"""
        self.cards.sort(key=lambda card: card.rank)

    def beats(self, hand):
        """returns True if this Hand beats hand"""
        return self.rank > hand.rank

    def is_royal(self):
        """docstring for is_royal"""
        return reduce(ans, (c.face() for c in self.cards))

    def is_a_straight(self):
        """true if it's a straight, false otherwise"""
        lin = sorted(R.suit for R in self.cards)
        return lin == range(min(lin), max(lin) + 1)


    def is_a_flush(self):
        """true if it's a flush, false otherwise"""
        return reduce(eq,(cd.suit for cd in self.cards))

    def straight_flush(self):
        """true if it's a straight flush, false otherwise"""
        return self.is_a_straight() and self.is_a_flush()

    def royal_flush(self):
        """docstring for royal_flush"""
        return self.is_a_straight() and self.is_a_flush() and self.is_royal()

class HandTest(object):
    """Should register as a royal flush"""
    def __init__(self, hand):
        super(HandTest, self).__init__()
        self.hand = hand

    def tests(self):
        """tests assertions"""
        assert self.hand.royal_flush()
        self.hand.by_suit()
        assert self.hand.cards == [Card(0, 12), Card(0, 13), Card(0, 11), Card(0, 10), Card(0, 14)]
