#Blackjack Multiplayer
import random
import time
from BJMPFuncs import *

print("Welcome to Multiplayer Blackjack!")

player_count = int(input("How many players are there? ")) #Need to make ability for players to cash out before game is over

players = create_players(player_count)  

deck = create_deck()
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


