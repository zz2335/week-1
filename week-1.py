# DATA MINING THE CITY
# WEEK-1 ASSIGNMENT

# This iassingment will get you familiar with the basic elements of Python by programming a simple card game.
# We will create a custom class to represent each player in the game, which will store information about their
# current pot, as well as a series of methods defining how they play the game.
# We will also build several functions to control the flow of the game and get data back at the end.

# I have included a rough framework of the solution here along with comments along the way to help you
# complete the assingment. You should be able to work directly in this document, and as you go run the 
# program through the Python interpreter to check your work. 
# A copy of the expected print out of the finished program is included in the week-1 repository.


import random

class Player:
    
    playerID = 0
    pot = 0.0
    lastCard = 0
    
    def __init__(self, inputID, startingPot):
        self.playerID = inputID
        self.pot = startingPot
        
    def play(self, dealerCard):
        self.lastCard = random.choice(cards)
        
        if self.lastCard < dealerCard:
            self.pot -= gameStake
            return 'player ' + str(self.playerID) + ' Lose, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
        else:
            self.pot += gameStake
            return 'player ' + str(self.playerID) + ' Win, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
        
    def returnPot(self):
        return self.pot
        
    def returnID(self):
        return self.playerID


def playHand(players):
    
    for player in players:
        print player.play(random.choice(cards))
        
def checkBalances(players):
    
    for player in players:
        print 'player ' + str(player.returnID()) + ' has $' + str(player.returnPot()) + ' left.'
        

gameStake = 50  
cards = range(10)

players = []

for i in range(5):
    players.append(Player(i, 500))

for i in range(10):
    print ''
    print 'start game ' + str(i)
    playHand(players)

print ''
print 'game results:'
checkBalances(players)
