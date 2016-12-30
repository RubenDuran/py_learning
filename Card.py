# Card class for Blackjack
class Card(object):
    suits = ("hearts", "diomonds", "clubs", "spades")
    rankings = ("A","2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "k")

    # Point values dict (Note: Aces can also be 11, check self.ace for details)
    card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
    '10':10, 'J':10, 'Q':10, 'K':10}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print (self.suit + self.rank)
