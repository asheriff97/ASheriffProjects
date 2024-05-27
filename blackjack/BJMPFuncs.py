#BlackjackMP Functions
import time

def create_deck(count):
    """
    Creates a deck of 52 cards, with each card being a tuple of the form (card, category).
    """
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    deck = []
    for i in range(count):
        deck += [(card, category) for category in card_categories for card in card_list]
    return deck

def card_value(card):
    """
    Returns the value of a card as an integer. Ace is 11, Jack, Queen, and King are 10.
    """
    if card[0] in ['Jack','Queen','King']:
        return 10
    elif card[0] == 'Ace': #Make the option to prompt value of 1 or 11
        return 11
    else:
        return int(card[0])    

def adjust_score_for_ace(cards, score):
    """
    Adjusts the score if it's over 21 and there are Aces counted as 11 in the hand.
    """
    number_of_aces = sum(card[0] == 'Ace' for card in cards)
    while score > 21 and number_of_aces > 0:
        score -= 10  # Subtracting 10 as if changing an Ace from 11 to 1
        number_of_aces -= 1
    return score

def create_players(count):
    players = []
    for i in range(count): 
        player_name = input(f"Enter player {i+1}'s name: ")
        players.append({"name": player_name, "player_score": [], "balance": 1000, "hands": [[]], "bets": [0], "nat_bj": False, "split": False})
    return players

def place_bets(players):
    for player in players:
    #players place bets before hands are dealt
        print(player["name"] + "'s total balance: " + str(player["balance"]))
        player["bets"][0] = int(input(player["name"] + ", how much would you like to bet? "))
        if player["bets"] > player["player_balance"]:
            print("You cannot bet more than your current balance.")
            player["bets"][0] = int(input("How much would you like to bet? "))


def deal_initial_hands(deck, players, dealer_hand):
    """
    Deals the initial hands to each player and the dealer.
    """
    for i in range(2):
        for player in players:
            time.sleep(1)
            player["hands"][0].append(deck.pop()) #Add a card to each player's first hand
            print("Dealer reveals " + player["name"] + "'s hand: ", player["hands"][0][i])

        dealer_hand.append(deck.pop()) #Dealer's cards
    print("Dealer's hand: ", dealer_hand[0], "and a hidden card")



      




'''
    for player in players:
        for hand in player["hands"]:
            hand.extend([deck.pop(), deck.pop()])
            '''

def player_turn(players, deck):
    for index, hand in enumerate(players["hands"]):
        card_count = 0
        print("Player: " + players["name"] + "'s turn. We detect that you have " + str(len(players["hands"])) + " hands.")
        #First check if split is possible
        print(players["name"] + "'s hand: ", hand)
        split(players, deck, index, hand)
        while players["player_score"] < 21: #While the player's score is less than 21
            print(players["name"] + "'s hand: ", hand)
            print([players["player_score"]])
            choice = input('What do you want? ["h" to hit, "dd" to double-down, or "s" to stand]: ').lower()
            if (choice == "hit" or choice == "dd"): #You can only double down on the first hand. Need to make a check so you cant double down after the first hand.
                card_count += 1
                new_card = deck.pop()
                hand.append(new_card)
                players["player_score"] = adjust_score_for_ace(hand, sum(card_value(card) for card in hand))
                if (choice == "dd" and card_count == 1):
                    players["bets"][index] *= 2
                    if players["bets"][index] > players["balance"]: #I think this is wrong but we check later
                        print("You do not have enough balance to double down.")
                        players["bets"][index] /= 2
                    else:
                        print("Your bet is now ${}.".format(players["bets"][index]))
                        print("Player's Hand:", hand)
                        print("Player's Hand Score:", players["player_score"])
                        print("\n")
                        break #Only dealt one more card, so we break out of the loop
                elif(choice == "dd" and card_count > 1):
                    print("You can only double down on on a two-card hand. You hit.\n")
            elif choice == "stand":
                break
            else:
                print("Invalid choice. Please try again.")

def split(players, deck, index, hand):
    if hand[0][0] == hand[1][0]: #If the first two cards are the same
        split = input("Would you like to split your hand? (y/n)")
        if (split == 'y' and players["balance"] >= players["bets"][index]): #If the player wants to split and has enough money to do so
            players["hands"].append([hand.pop(), deck.pop()]) #Add a new hand with the second card of the first hand
            hand.append(deck.pop()) #Add a new card to the first hand
            players["bets"].append(players["bets"][index]) #The new hand has the same bet as the first hand
            print(players["bets"]) #Testing
            print("First hand: ", hand) #Testing
            print("Second hand: ", players["hands"][index+1]) #Testing
        elif (split == 'y' and players["balance"] < players["bets"][index]): #
            print("You don't have enough money to split your hand.")
            print("Your hand: ", hand) #Testing
        elif (split == 'n'):
            pass
        else:
            print("Something went wrong. LINE 100")



    




        

def dealer_turn(dealer_card, dealer_score, deck):
    print("Dealer turns their second card over to reveal a {}".format(dealer_card[1]))
    while dealer_score < 17:
        time.sleep(2)
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score = adjust_score_for_ace(dealer_card, sum(card_value(card) for card in dealer_card))
        print("Dealer unveils a {}".format(new_card))