#Building Blackjack in Python

import random

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck = [(card, category) for category in card_categories for card in card_list]

def card_value(card):
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == 'Ace': #Make the option to prompt value of 1 or 11
        return 11
    else:
        return int(card[0])

random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]


while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in dealer_card)
    print("Cards Player Has:", player_card)
    print("Score Of The Player:", player_score)
    print("\n")
    
    if player_score >= 21:
        break       

    choice = input('What do you want? ["hit" to request another card, "stand" to stop]: ').lower()
    if choice == "hit":
        new_card = deck.pop()
        player_card.append(new_card)
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

if (player_score == 21 and dealer_score != 21):
    print("BLACKJACK! Player wins!")
elif player_score > 21:
    print("BUST! Player loses!")
    #break
elif dealer_score > 21:
    print("DEALER BUST! Player wins!!!")
    #break
elif player_score > dealer_score:
    print("Player wins (Player Has High Score than Dealer)")
    #break
elif dealer_score > player_score:
    print("Dealer wins (Dealer Has High Score than Player)")
    #break
else:
    print("It's a tie.")
    #break

