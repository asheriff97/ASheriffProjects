TO-DO

- Fix the game
    - When the player has a hand over 21, they automatically lose. DONE
    - When you're in the cmd prompt pressing "stop" closes out of the whole game

MAJOR
 - Add some form of graphic interface
 - Allow option to make a Ace valued at 11 or 1 (soft/hard hands)
    - If a hand has an ace would bust with an 11, make it a 1


MODERATE 
 - Add Betting IN PROGRESS
 - Add Double Down/Split/Etc(?)
 - Make second card of dealer hidden when dealt
 - Add a play again option DONE
 - Need to make a check to see if player automatically wins with a blackjack, they do not get option to hit/dd/stand etc.

 - What do you want? ["hit" to request another card, "dd" to double-down, or "stand" to stop]: stand
Dealer turns their second card over to reveal a ('Ace', 'Spades')
Dealer unveils a ('Ace', 'Diamonds')
Dealer unveils a ('10', 'Diamonds')
Dealer unveils a ('9', 'Diamonds')
Dealer unveils a ('King', 'Diamonds')
Dealer unveils a ('Queen', 'Spades')
Dealer unveils a ('7', 'Spades')

Dealer's Hand: [('2', 'Spades'), ('Ace', 'Spades'), ('Ace', 'Diamonds'), ('10', 'Diamonds'), ('9', 'Diamonds'), 
('King', 'Diamonds'), ('Queen', 'Spades'), ('7', 'Spades')]
Dealer's Score: 20
Player's Hand: [('Ace', 'Hearts'), ('6', 'Clubs')]
Player's Score: 17

Dealer wins (Dealer Has Higher Score than Player)
You lost. Your balance is now $900.

MINOR
 - Fix the vocabulary (Stand/Hit) DONE
 - Add line spaces BETTER
 - Clean up final if/else win prompt DONE(?)
 - Improve readability BETTER
 - Combine score functions into one large function

"After the boxes have finished playing, the dealer's hand is resolved by drawing cards until the hand achieves a total of 17 or higher. If the dealer has a total of 17 including an ace valued as 11 (a "soft 17"), some games require the dealer to stand while other games require another draw. The dealer never doubles, splits, or surrenders. If the dealer busts, all remaining player hands win. If the dealer does not bust, each remaining bet wins if its hand is higher than the dealer's and loses if it is lower."