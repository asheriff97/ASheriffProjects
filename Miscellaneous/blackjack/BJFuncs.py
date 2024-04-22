#Functions

def create_deck(count):
    """
    Creates a deck of 52 cards, with each card being a tuple of the form (card, category).
    """
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    #Return count number of decks
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

def double_down(bet, player_balance, player_card, player_score):
    bet *= 2
    if bet > player_balance:
        print("You do not have enough balance to double down.")
        bet /= 2
    else:
        print("Your bet is now ${}.".format(bet))
        print("Player's Hand:", player_card)
        print("Player's Score:", player_score)
        print("\n")
    return bet, player_balance

def players_turn(player_card, deck, player_score, card_count, bet, player_balance, split):
    #make card_count local function variable instead of 'global'
    
    if split == False:
        pass  #placeholder

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
                double_down(bet, player_balance, player_card, player_score)
                break #Only dealt one more card, so we break out of the loop
            elif(choice == "dd" and card_count > 1):
                print("You can only double down on on a two-card hand. You hit.\n")
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please try again.")
    return player_card, player_score, card_count, bet, player_balance

def split_hand(player_card, deck, card_count, bet, player_balance):
    """
    Splits the hand into two hands if the first two cards are the same.
    """
    print("You split your hand.")
    split = True
    player_card1 = [player_card[0], deck.pop()]
    player_card2 = [player_card[1], deck.pop()]
    player_score1 = adjust_score_for_ace(player_card1, sum(card_value(card) for card in player_card1))
    player_score2 = adjust_score_for_ace(player_card2, sum(card_value(card) for card in player_card2))
    print("Player's Hand 1:", player_card1)
    print("Player's Score 1:", player_score1)
    print("Player's Hand 2:", player_card2)
    print("Player's Score 2:", player_score2)
    print("\n")
    player_card1, player_score1, card_count, bet1, player_balance = players_turn(player_card1, deck, player_score1, card_count, bet, player_balance, split)
    player_card2, player_score2, card_count, bet2, player_balance = players_turn(player_card2, deck, player_score2, card_count, bet, player_balance, split)
    return player_card1, player_card2, player_score1, player_score2, card_count, bet, player_balance, split

