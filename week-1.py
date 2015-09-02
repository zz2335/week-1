# DATA MINING THE CITY
# WEEK-1 ASSIGNMENT

# This iassingment will get you familiar with the basic elements of Python by programming a simple card game.
# We will create a custom class to represent each player in the game, which will store information about their
# current pot, as well as a series of methods defining how they play the game.
# We will also build several functions to control the flow of the game and get data back at the end.

# I have included a rough framework of the solution here along with comments along the way to help you
# complete the assingment. Places where you should write code are denoted by the [] brackets and CAPITAL TEXT.
# You should be able to work directly in this document, and as you go run the program through the Python interpreter 
# to check your work. A copy of the expected print out of the finished program is included in the week-1 repository.



# We will start by importing the 'random' library, which will allow us to use it's function 
# for picking a random entry from a list.

import random

# First we will establish some general variables for our game, including the 'stake' of the game 
# (how much money each play is worth), as well as a list representing the cards used in the game.
# To make things easier, we will just use a list 0-9 for the cards.

gameStake = 50  
cards = range(10)

# Next, let's define a new class to represent each player in the game.

class Player:
    
    # create here two local variables to store a unique ID for each player and the player's current 'pot' of money
    # [FILL IN YOUR VARIABLES HERE]
    
    # in the __init__() function, use the two input variables to initialize the ID and starting pot of each player
    
    def __init__(self, inputID, startingPot):
        # [CREATE YOUR INITIALIZATIONS HERE]
        
    # create a function for playing the game. This function should take on input for the card of the dealer.
    # it should then take a random card from 
    
    def play(self, dealerCard):
        # [CREATE CODE FOR SELECTING A RANDOM CARD]
        
        # here we should have a conditional that tests the player's card value against the dealer card
        # and returns a statement saying whether the player won or lost the hand
        # before return the statement, make sure to either add or subtract the stake from the player's pot so that
        # the 'pot' variable tracks the player's money
        
        if playerCard < dealerCard:
            # [INCREMENT THE PLAYER'S POT, AND RETURN A MESSAGE]
        else:
            # [INCREMENT THE PLAYER'S POT, AND RETURN A MESSAGE]
        
    # create an accessor function to return the current value of the player's pot
    def returnPot(self):
        # [FILL IN THE RETURN STATEMENT]
        
    # create an accessor function to return the player's ID
    def returnID(self):
        # [FILL IN THE RETURN STATEMENT]


# Next we will create some functions outside the class definition which will control the flow of the game
# The first function will play one round. It will take as an input the collection of players, and iterate through each one,
# calling each player's '.play() function

def playHand(players):
    
    for player in players:
        dealerCard = random.choice(cards)
        #[EXECUTE THE PLAY() FUNCTION FOR EACH PLAYER USING THE DEALER CARD, AND PRINT OUT THE RESULTS]
        
# Next we will define a function that will check the balances of each player, and print out a message with the
# player's ID and their balance.

def checkBalances(players):
    
    for player in players:
        #[PRINT OUT EACH PLAYER'S BALANCE BY USING EACH PLAYER'S ACCESSOR FUNCTIONS]
  
  
# Now we are ready to start the game. First we create an empy list to store the collection of players in the game

players = []      

# Then we create a loop that will run a certain number of times, each time creating a player with a unique ID 
# and a starting balance. Each player should be appended to the empty list, which will store all the players.
# Hint: you can pass the 'i' iterator of the loop as the ID, and set a constant value for the balance (such as 500).

for i in range(5):
    players.append(Player(i, 500))

# Once the players are created, we will create a loop to run the game a certain amount of times. Each step of the loop
# should start with a print statement announcing the start of the game, and then call the playHand function, passing as 
# an input the list of players

for i in range(10):
    print ''
    print 'start game ' + str(i)
    playHand(players)

# Finally, we will analyze the results of the game by running the 'checkBalances()' function and passing it our list of players.

print ''
print 'game results:'
checkBalances(players)
