#Building Blackjack in Python

import random
import time
from BJFuncs import *

player_balance = 1000

while True:
    player_wins = False
    #double_down = False
    tie = False
    deck = create_deck()
    card_count = 0
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    
    player_score = adjust_score_for_ace(player_card, sum(card_value(card) for card in player_card))
    dealer_score = adjust_score_for_ace(dealer_card, sum(card_value(card) for card in dealer_card))

    bet = int(input(f"Your balance is ${player_balance}. How much do you want to bet? \n")) #need to add input validation so game doesnt break on non-int
    if bet > player_balance:
        print("You cannot bet more than your current balance.")
        continue

    print("\nDealer's Hand: {} [Hidden]".format(dealer_card[0]))

    while player_score < 21:

        print("Player's Hand:", player_card)
        print("Player's Score:", player_score)
        print("\n")

        choice = input('What do you want? ["hit" to request another card, "dd" to double-down, or "stand" to stop]: ').lower()
        if (choice == "hit" or choice == "dd"): #You can only double down on the first hand. Need to make a check so you cant double down after the first hand.
            card_count += 1
            new_card = deck.pop()
            player_card.append(new_card)
            player_score = adjust_score_for_ace(player_card, sum(card_value(card) for card in player_card))
            if (choice == "dd" and card_count == 1):
                bet *= 2
                if bet > player_balance:
                    print("You do not have enough balance to double down.")
                    bet /= 2
                else:
                    print("Your bet is now ${}.".format(bet))
                    print("Player's Hand:", player_card)
                    print("Player's Score:", player_score)
                    print("\n")
                    break #Only dealt one more card, so we break out of the loop
            elif(choice == "dd" and card_count > 1):
                print("You can only double down on on a two-card hand. You hit.\n")
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please try again.")


    if player_score >= 21: #We skip dealers turn if player blackjacks or busts on their turn
        pass
    else: 
        time.sleep(1)
        print("Dealer turns their second card over to reveal a {}".format(dealer_card[1]))
        while dealer_score < 17:
            time.sleep(2)
            new_card = deck.pop()
            dealer_card.append(new_card)
            dealer_score = adjust_score_for_ace(dealer_card, sum(card_value(card) for card in dealer_card))
            print("Dealer unveils a {}".format(new_card))

    time.sleep(1)
    print("\nDealer's Hand:", dealer_card)
    print("Dealer's Score:", dealer_score)
    print("Player's Hand:", player_card)
    print("Player's Score:", player_score,"\n")

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
        print("Thanks for playing. Your final balance is ${}.".format(player_balance))
        if player_balance > 1000:
            print("You walked away with an extra ${}".format(player_balance - 1000), "in your pocket!")
        else:
            print("You lost ${}".format(1000 - player_balance), "of your money. Better luck next time!")
        break

