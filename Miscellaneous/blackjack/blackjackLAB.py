#Building Blackjack in Python LABORATORY
#I mess around in here before adding to the main file.

import random
from BJFuncs import *

player_balance = 1000

while True:
    player_wins = False
    #double_down = False
    tie = False
    deck = create_deck()
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    
    player_score = adjust_score_for_ace(player_card, sum(card_value(card) for card in player_card))
    dealer_score = adjust_score_for_ace(dealer_card, sum(card_value(card) for card in dealer_card))

    bet = int(input(f"Your balance is ${player_balance}. How much do you want to bet? \n")) #need to add input validation so game doesnt break on non-int
    if bet > player_balance:
        print("You cannot bet more than your current balance.")
        continue

    print("\nCards Dealer Has:", dealer_card)
    print("Score Of The Dealer:", dealer_score)
    while player_score <= 21:

        print("Cards Player Has:", player_card)
        print("Score Of The Player:", player_score)
        print("\n")

        choice = input('What do you want? ["hit" to request another card, "dd" to double-down, or "stand" to stop]: ').lower()
        if (choice == "hit" or choice == "dd"): #You can only double down on the first hand. Need to make a check so you cant double down after the first hand.
            new_card = deck.pop()
            player_card.append(new_card)
            player_score += card_value(new_card)
            player_score = adjust_score_for_ace(player_card, player_score)
            if choice == "dd":
                bet *= 2
                if bet > player_balance:
                    print("You do not have enough balance to double down.")
                    bet /= 2
                else:
                    print("Your bet is now ${}.".format(bet))
                    #double_down = True
                    break
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please try again.")

    while dealer_score < 17:
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score += card_value(new_card)
        dealer_score = adjust_score_for_ace(dealer_card, dealer_score)

    print("\nCards Dealer Has:", dealer_card)
    print("Score Of The Dealer:", dealer_score)
    print("Cards Player Has:", player_card)
    print("Score Of The Player:", player_score,"\n")

    #Determine the winner of the game
    if (player_score == 21 and dealer_score != 21): #Win (BlackJack)
        print("BLACKJACK! Player wins!")
        player_wins = True
    elif player_score > 21: #Player Bust
        print("BUST! Player loses!")
    elif dealer_score > 21: #Dealer Bust
        print("DEALER BUST! Player wins!!!")
        player_wins = True
    elif player_score > dealer_score: #Win
        print("Player wins (Player Has Higher Score than Dealer)")
        player_wins = True
    elif dealer_score > player_score: #Dealer Higher Score
        print("Dealer wins (Dealer Has Higher Score than Player)")
    else:
        tie = True
        print("It's a tie.")
        

    # After deciding the winner, update the player balance
    if (player_wins):
        winning_amount = int(1.5 * bet) #Calculate the amount won based on the bet and a 3:2 payout ratio.
        player_balance += winning_amount 
        print("You won! Your balance is now ${}.".format(player_balance))
        print("You won ${}.".format(winning_amount))
    elif (tie):
        print("Your balance is still ${}.".format(player_balance))
    else:
        player_balance -= bet
        print("You lost. Your balance is now ${}.".format(player_balance))
    
    if player_balance <= 0:
        print("You're out of money! Game over.")
        break

    new_game = input("\nDo you want to play again? (yes/no) ").lower()
    if new_game != 'yes':
        break

