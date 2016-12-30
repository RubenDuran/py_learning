class Hand(object):

    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can have a value of 1 or 11
        self.ace = False

        def __str__(self):
            ''' Return a string of current hand composition'''
            hand_comp = ""
            for card in self.cards:
                card_name = card.__str__()
                hand_comp += " " + card_name

            return 'The hand has %s' %hand_comp

        def card_add(self,card):
            ''' Add another card to the hand'''
            self.cards.append(card)

            # Check for Aces
            if card.rank == 'A':
                self.ace = True
            self.value += card_val[card.rank]


            def calc_val(self):
                '''Calculate the value of the hand, make aces an 11 if they
                don't bust the hand'''

                if (self.ace == True and self.value < 12):
                     return self.value + 10
                else:
                    return self.value

            def draw(self,hidden):
                if hidden == True and playing == True:
                    #Don't show first hidden card
                    starting_card = 1
                else:
                    starting_card = 0
                for x in range(starting_card,len(self.cards)):
                    self.cards[x].draw()
