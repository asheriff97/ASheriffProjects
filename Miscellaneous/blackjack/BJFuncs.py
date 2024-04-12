#Functions

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

def adjust_score_for_ace(cards, score):
    number_of_aces = sum(card[0] == 'Ace' for card in cards)
    while score > 21 and number_of_aces > 0:
        score -= 10  # Subtracting 10 as if changing an Ace from 11 to 1
        number_of_aces -= 1
    return score
