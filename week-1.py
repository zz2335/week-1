# DATA MINING THE CITY
# WEEK-1 ASSIGNMENT
#Zhipeng Zeng (UNI:zz2335) Week 1

import random

gameStake = 50  
cards = range(10)

class Player:
    playerID = 0
    pot = 0.0
    lastCard = 0
    
    # create here two local variables to store a unique ID for each player and the player's current 'pot' of money
    
    # in the __init__() function, use the two input variables to initialize the ID and starting pot of each player
    
    def __init__(self, inputID, startingPot):
        self.playerID = inputID
        self.pot = startingPot
       
        
    # create a function for playing the game. This function should take on input for the card of the dealer.
    # it should then take a random card from 
    
    def play(self, dealerCard):
        self.lastCard = random.choice(cards)

   
        
        # here we should have a conditional that tests the player's card value against the dealer card
        # and returns a statement saying whether the player won or lost the hand
        # before return the statement, make sure to either add or subtract the stake from the player's pot so that
        # the 'pot' variable tracks the player's money
        
        if playerCard < dealerCard:
            self.pot -= gameStake
            return 'player' + str(self.playerID) + 'Lose,' + str(self.lastCard) + 'vs' + str(dealerCard)
        else:
            self.pot += gameStake
            return 'player' + str(self.playerID) + 'win,' + str(self.lastCard) + 'vs' + str(dealerCard)
        
    # create an accessor function to return the current value of the player's pot
    def returnPot(self):
        return self.pot
        
    # create an accessor function to return the player's ID
    def returnID(self):
        return self.playerID


# Next we will create some functions outside the class definition which will control the flow of the game
# The first function will play one round. It will take as an input the collection of players, and iterate through each one,
# calling each player's '.play() function

def playHand(players):
    
    for player in players:
        dealerCard = random.choice(cards)
        print player.play(dealerCard)
        
# Next we will define a function that will check the balances of each player, and print out a message with the
# player's ID and their balance.

def checkBalances(players):
    
    for player in players:
        print 'player' + str(player.returnID()) + 'has $' + str(player.returnPot()) + 'left.'
  
  
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
