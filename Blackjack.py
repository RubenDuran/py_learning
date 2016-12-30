#Blackjack game
class Blackjack(object):
    global bet,result,playing,deck,player_hand,dealer_hand,chip_pool
    bet = 0

    def __init__(self):
        self.bet = 0

# First Bet
    def make_bet():
        ''' Ask the player for the bet amount and '''
        print ' What amount of chips would you like to bet? (Enter whole integer please) '

        # While loop to keep asking for the bet
        while bet == 0:
            bet_comp = raw_input() # Use bet_comp as a checker
            bet_comp = int(bet_comp)
            # Check to make sure the bet is within the remaining amount of chips left.
            if bet_comp >= 1 and bet_comp <= chip_pool:
                bet = bet_comp
            else:
                print "Invalid bet, you only have " + str(chip_pool) + " remaining"

    def deal_cards():
        ''' This function deals out cards and sets up round '''

        deck = Deck() # Create a deck
        deck.shuffle() #Shuffle it
        make_bet() #Set up bet

        # Set up both player and dealer hands
        player_hand = Hand()
        dealer_hand = Hand()

        # Deal out initial cards
        player_hand.card_add(deck.deal())
        player_hand.card_add(deck.deal())

        dealer_hand.card_add(deck.deal())
        dealer_hand.card_add(deck.deal())

        result = "Hit or Stand? Press either h or s: "

        if playing == True:
            print 'Fold, Sorry'
            chip_pool -= bet

        # Set up to know currently playing hand
        playing = True
        game_step()

    def hit():
        ''' Implement the hit button '''
        # If hand is in play add card
        if playing:
            if player_hand.calc_val() <= 21:
                player_hand.card_add(deck.deal())

            print "Player hand is %s" %player_hand

            if player_hand.calc_val() > 21:
                result = 'Busted! '+ restart_phrase

                chip_pool -= bet
                playing = False

            else:
                result = "Sorry, can't hit" + restart_phrase

            game_step()

    def stand():
        ''' This function will now play the dealers hand, since stand was chosen '''

        if playing == False:
            if player_hand.calc_val() > 0:
                result = "Sorry, you can't stand!"

        # Now go through all the other possible options
        else:
            # Soft 17 rule
            while dealer_hand.calc_val() < 17:
                dealer_hand.card_add(deck.deal())

            # Dealer Busts
            if dealer_hand.calc_val() > 21:
                result = 'Dealer busts! You win!' + restart_phrase
                chip_pool += bet
                playing = False

            #Player has better hand than dealer
            elif dealer_hand.calc_val() < player_hand.calc_val():
                result = 'You beat the dealer, you win!' + restart_phrase
                chip_pool += bet
                playing = False

            # Push
            elif dealer_hand.calc_val() == player_hand.calc_val():
                result = 'Tied up, push!' + restart_phrase
                playing = False

            # Dealer beats player
            else:
                result = 'Dealer Wins!' + restart_phrase
                chip_pool -= bet
                playing = False

        game_step()

    def game_step():
        '''Function to print game step/status on output'''

        #Display Player Hand
        print ""
        print('Player Hand is: '),
        player_hand.draw(hidden =False)

        print 'Player hand total is: '+str(player_hand.calc_val())

        #Display Dealer Hand
        print('Dealer Hand is: '),
        dealer_hand.draw(hidden=True)

        # If game round is over
        if playing == False:
            print  " --- for a total of " + str(dealer_hand.calc_val() )
            print "Chip Total: " + str(chip_pool)

        # Otherwise, don't know the second card yet
        else:
            print " with another card hidden upside down"

        # Print result of hit or stand.
        print result

        player_input()

    def game_exit():
        print 'Thanks for playing!'
        exit()

    def player_input():
        ''' Read user input, lower case it just to be safe'''
        plin = raw_input().lower()

        if plin == 'h':
            hit()
        elif plin == 'd':
            deal_cards()
        elif plin == 's':
            stand()
        elif plin == 'q':
            game_exit()
        else:
            print "Invalid Input...Enter h, s, d, or q: "
            player_input()

    def intro():
        statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
        print statement
