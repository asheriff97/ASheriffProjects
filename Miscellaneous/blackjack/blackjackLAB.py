#Building Blackjack in Python LABORATORY
#I mess around in here before adding to the main file.
from ast import Continue
import random
import time
from BJFuncs import create_deck, card_value, adjust_score_for_ace, players_turn, split_hand


player_balance = 1000

while True:
    player_wins = False
    tie = False
    split = False
    count = int(input("How many decks would you like to play with? (1-8) "))
    deck = create_deck(count)

    #deck = [('6', 'Hearts'), ('10', 'Diamonds'), ('4', 'Clubs'), ('6', 'Spades'), ('9', 'Diamonds'),
    #         ('King', 'Clubs'), ('4', 'Diamonds'), ('4', 'Hearts')]

    card_count = 0
    #random.shuffle(deck)
    print(deck)
	
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    player_score = adjust_score_for_ace(player_card, sum(card_value(card) for card in player_card))
    dealer_score = adjust_score_for_ace(dealer_card, sum(card_value(card) for card in dealer_card))

    #If Dealer has a blackjack immediately, we re-deal everyones hands
    if dealer_score == 21:
        print("Dealer has a blackjack. Re-dealing hands.")
        continue

    bet = int(input(f"Your balance is ${player_balance}. How much do you want to bet? \n")) #need to add input validation so game doesnt break on non-int
    if bet > player_balance:
        print("You cannot bet more than your current balance.")
        continue

    print("\nDealer's Hand: {} [Hidden]".format(dealer_card[0]))
    print("Player's Hand:", player_card)

	#CHECK IF SPLITTING IS POSSIBLE
    if (player_card[0][0] == player_card[1][0]): #If the first two cards are the same, ask if the player wants to split
        response = input("You have two {}s. Do you want to split? (yes/no) ".format(player_card[0][0])).lower() #need to add input validation
        if response == "yes": #If the player wants to split, we create two hands and deal a card to each hand
            player_card1, player_card2, player_score1, player_score2, card_count, bet, player_balance, split = split_hand(player_card, deck, card_count, bet, player_balance) 
        else:
            player_card, player_score, card_count, bet, player_balance = players_turn(player_card, deck, card_count, player_score, bet, player_balance, split=False) 
    
    print("OUT OF LOOP") #TESTING
    print(player_card1, player_card2, player_score1, player_score2, card_count, bet, player_balance, split) #TESTING


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

