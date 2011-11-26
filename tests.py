from hand import Hand
from cards import Card

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
