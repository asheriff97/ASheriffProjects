#Blackjack Multiplayer
import random
import time
from BJMPFuncs import *

print("Welcome to Multiplayer Blackjack!")

player_count = int(input("How many players are there? ")) #Need to make ability for players to cash out before game is over
players = create_players(player_count)  

deck_count = int(input("How many decks would you like to play with? (1-8)")) #Need to input validate

#Set bet payout ratio
if deck_count < 1 or deck_count > 8:
    print("Invalid number of decks. Defaulting to 1 deck.")
    deck_count = 1
    if deck_count <= 2:
        bet_payout = 1.2
    else:
        bet_payout = 1.5

print("Entering game...")
time.sleep(1)
print("Player count: " + str(player_count))
print("Deck count: " + str(deck_count))
print("Bet payout: " + str(bet_payout))

while True:
    deck = create_deck(deck_count)
    random.shuffle(deck)

    dealer_hand = []
    deal_initial_hands(deck, players, dealer_hand)

    '''
    #Testing hands
    print("Dealer's hand: " + str(dealer_hand))
    for player in players:
        print(player["name"] + "'s hand: " + str(player["hands"][0]))
        '''


    #dealer_score = adjust_score_for_ace(dealer_hand, sum(card_value(card) for card in dealer_hand))

    for player in players:
    #players place bets before hands are dealt
        print(player["name"] + "'s total balance: " + str(player["balance"]))
        player["bets"][0] = int(input(player["name"] + ", how much would you like to bet? "))

    #deal_initial_hands(deck, players)

    #Testing Splitting
    players[0]["hands"][0] = [('7', 'Hearts'), ('7', 'Spades')]



    for player in players:
        player_turn(player, deck)




    dealer_turn(dealer_hand, deck)

    #Need to make ability for players to cash out before game is over


