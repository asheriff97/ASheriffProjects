#Building Blackjack in Python

import random

def create_deck():
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    return [(card, category) for category in card_categories for card in card_list]

def card_value(card):
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == 'Ace': #Make the option to prompt value of 1 or 11
        return 11
    else:
        return int(card[0])

player_balance = 1000

while True:
    player_wins = False
    deck = create_deck()
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)

    bet = int(input(f"Your balance is ${player_balance}. How much do you want to bet? ")) #need to add input validation so game doesnt break on non-int
    if bet > player_balance:
        print("You cannot bet more than your current balance.")
        continue

    while player_score <= 21:
        print("Cards Player Has:", player_card)
        print("Score Of The Player:", player_score)
        print("\n")

        choice = input('What do you want? ["hit" to request another card, "stand" to stop]: ').lower()
        if choice == "hit":
            new_card = deck.pop()
            player_card.append(new_card)
            player_score += card_value(new_card)
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please try again.")

    

    while dealer_score <= 17:
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score += card_value(new_card)

    print("\nCards Dealer Has:", dealer_card)
    print("Score Of The Dealer:", dealer_score)
    print("Cards Player Has:", player_card)
    print("Score Of The Player:", player_score,"\n")

    #Determine the winner of the game
    if (player_score == 21 and dealer_score != 21):
        print("BLACKJACK! Player wins!")
        player_wins = True
    elif player_score > 21:
        print("BUST! Player loses!")
    elif dealer_score > 21:
        print("DEALER BUST! Player wins!!!")
        player_wins = True
    elif player_score > dealer_score:
        print("Player wins (Player Has High Score than Dealer)")
        player_wins = True
    elif dealer_score > player_score:
        print("Dealer wins (Dealer Has High Score than Player)")
    else:
        print("It's a tie.")
        

    # After deciding the winner, update the player balance
    if player_wins:
        winning_amount = int(1.5 * bet) #Calculate the amount won based on the bet and a 3:2 payout ratio.
        player_balance += winning_amount #DOUBLE CHECK THIS
        print("You won! Your balance is now ${}.".format(player_balance))
        print("You won ${}.".format(winning_amount))

    else:
        player_balance -= bet
        print("You lost. Your balance is now ${}.".format(player_balance))
    
    if player_balance <= 0:
        print("You're out of money! Game over.")
        break

    new_game = input("Do you want to play again? (yes/no) ").lower()
    if new_game != 'yes':
        break

