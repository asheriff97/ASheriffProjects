BLACKJACK MP FLOW LIST

Print welcome message
Gather player counts
Instantiate players.
    Players are dictionaries with the following keys:
        Name, Hands, Bet, Insurance Bet, nat_bj (bool) and Balance (1000) ** Needs more? **
Prompt how many decks the players want to play with (1-8)
    If decks < 1 or decks > 8
        Print error message
        Prompt again
    else
        Create deck with decks number of decks
        If deck <= 2
            Bet payout is 6:5
        else (deck >= 3)
            bet payout is 3:2

MAIN GAME LOOP
Create and Shuffle Deck
Retrieve each players bets
Deal cards to everyone, including dealer, one by one
Calculate everyones score, including dealer
Show dealer's first card in hand, second card is hidden
Check each player for blackjack
    If dealer has blackjack
        if player has blackjack
            Tie
        else
            Players loses bet

Enter loop to check each players hand and display player hands
    If player has blackjack
        nat_bj = true
        Skip player
    if dealers first card is an ace
        Ask player if they want insurance (y/n)
        If yes
            if nat_nj = true
                Prompt if they would like "Even money (1:1 Payout right now) (y/n)"
                Bet is 1x insurance bet. E.g. if they bet 100 to begin with, they're automatically paid out $100, but do not win extra if the dealer busts/loses.
            else
                Ask player how much they want to bet for insurance
                Bet must be less than or equal to half of original bet
                Set that players insurance_bet to the bet
            
        if no
            If dealer has blackjack
                Calculate player wins/losses, skips all turns


if nat_bj = true AND insurance_bet == "even_money"
    Pay out 1x bet
else if nat_bj = true AND insurance_bet == 0
    Pay out 1.5x bet










        Ask player if they want to hit, DD, split, insurance, stand











