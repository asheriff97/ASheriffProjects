TO-DO

- Fix the game
    - When the player has a hand over 21, they automatically lose. DONE
    - When you're in the cmd prompt pressing "stop" closes out of the whole game

MAJOR
 - Add some form of graphic interface
 - Allow option to make a Ace valued at 11 or 1 (soft/hard hands)
    - If a hand has an ace would bust with an 11, make it a 1
- Add Splitting (IN PROGRESS)
    - If the player splits Aces, the bet payouts change to 1:1


MODERATE 
 - Add Betting IN PROGRESS
 - Add Double Down/Split/Etc(?)
 - Make second card of dealer hidden when dealt
 - Add a play again option DONE
 - Add insurance option
    - If the dealer's face up card is an Ace, the player can make an insurance bet, bet pays 2:1
    - If the dealer has a blackjack, the player loses their original bet but wins the insurance bet
    - If the dealer does not have a blackjack, the player loses the insurance bet and the game continues as normal
 - Need to make a check to see if player automatically wins with a blackjack, they do not get option to hit/dd/stand etc.
 


MINOR
 - Fix the vocabulary (Stand/Hit) DONE
 - Add line spaces BETTER
 - Clean up final if/else win prompt DONE(?)
 - Improve readability BETTER
 - Make an option to slowly reveal the dealer's hand DONE
 - Combine score functions into one large function DONE
 - Add a way to check to see if Dealer has blackjack with starting hand, the turn is void and the player gets their money back DONE


"After the boxes have finished playing, the dealer's hand is resolved by drawing cards until the hand achieves a total of 17 or higher. If the dealer has a total of 17 including an ace valued as 11 (a "soft 17"), some games require the dealer to stand while other games require another draw. The dealer never doubles, splits, or surrenders. If the dealer busts, all remaining player hands win. If the dealer does not bust, each remaining bet wins if its hand is higher than the dealer's and loses if it is lower."

List of cards in deck:
[('6', 'Hearts'), ('10', 'Diamonds'), ('4', 'Clubs'), ('6', 'Spades'), ('9', 'Diamonds'), ('King', 'Clubs'), ('4', 'Diamonds'), ('4', 'Hearts'), ('6', 'Clubs'), ('Ace', 'Diamonds'), ('3', 'Hearts'), ('5', 'Spades'), ('Queen', 'Clubs'), ('3', 'Clubs'), ('Queen', 'Hearts'), ('Jack', 'Diamonds'), ('10', 'Spades'), ('9', 'Spades'), ('9', 'Clubs'), ('7', 'Spades'), ('4', 'Spades'), ('2', 'Clubs'), ('5', 'Clubs'), ('5', 'Hearts'), ('2', 'Diamonds'), ('2', 'Spades'), ('8', 'Spades'), ('8', 'Diamonds'), ('Jack', 'Spades'), ('8', 'Hearts'), ('Ace', 'Hearts'), ('10', 'Hearts'), ('Jack', 'Clubs'), ('3', 'Diamonds'), ('Ace', 'Clubs'), ('King', 'Spades'), ('3', 'Spades'), ('Jack', 'Hearts'), ('Ace', 'Spades'), ('Queen', 'Spades'), ('King', 'Hearts'), ('7', 'Diamonds'), ('10', 'Clubs'), ('7', 'Clubs'), ('Queen', 'Diamonds'), ('8', 'Clubs'), ('King', 'Diamonds'), ('5', 'Diamonds'), ('2', 'Hearts'), ('9', 'Hearts'), ('7', 'Hearts'), ('6', 'Diamonds')]