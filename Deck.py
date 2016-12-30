import random

class Deck(object):
    def __init__(self):
        ''' Create a deck in order '''
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        ''' Shuffle the deck, python actually already has a shuffle method in
        its random lib '''
        random.shuffle(self.deck)

     def deal(self):
         ''' Grab the first item in the deck '''
         single_card = self.deck.pop(
         return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()
        return "The deck has" + deck_comp
