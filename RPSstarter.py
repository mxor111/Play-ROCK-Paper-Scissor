#!usr/bin/env python3
"""This program plays a game of Rock, Paper, Scirssors between two Players, and reports both Player's score each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The player class is the parent classt for all the Players in this game"""

class Player: def move(self):
    return 'rock'

def learn(self, my_move, their_move):
    pass
    #create player classes that remember- at the end of each Game Class calls the LEARN method
    #on each player object to tell that plater what the other player's move was.
    #this means you can have the computer players that change their moves depending on what behaviors
    #happened earlier.  ***to do this you will need to implement learn Methods that save information information
    #instance variables.
def beats(one, two):# use this function to tell if one move beats another- KEEP SCORE
    return ((one=='rock' and two =='scissors') or (one =='scissors'and two =='paper') or (one =='paper' and two =='rock'))

class Game: def_init_(self, p1, p2): #update the game class so that it display outcome of each round and keeps score for both players
    self.pl = pl
    self.p2 = p2

def play_round(self):
    move1 = self.p1.move()
    move2 = self.p2.move()
    print(f"Player 1: {move1} Player 2: {move2}")
    self.pl.learn(move1, move2)
    self.p2.learn(move2, move1)

def play_game(self):
    print("Game Start") for round in range(3):
    print(f"Round{round}:")
    self.play_round()
    print("Game Over!")
    if name == '_main_':
        game = Game(Player(), Player())
        game.play game()

class RandomPlayer: #created a player subclass that plays randomly
    def move(RandomPlayer):
    return ((one=='rock' and two=='paper' and three=='scissors')) or

class ReflectPlayer: # create class that remembers what moves the opponent playerd last rounds
# and plays that move this round. (in other words if you play paper on first round relfect will play paper on second round first)

class CyclePlayer:# that remembers what move it played last round and cycles through different moves each time


class HumanPlayer: #set the program to play a game between HumanPlayer and RandomPlayer
    def game(HumanPlayer(), ReflectPlayer())
    return = game(HumanPlayer(), ReflectPlayer())

#validate user imput - if there are any typos roxk the Human Player code should let them try again.
#announce a winner - the starter code always plays three rounds - you can change the rule




The starter Player class always plays 'rock'. That's not a very good strategy! Create a subclass called RandomPlayer that chooses its move at random. When you call the move method on a RandomPlayer object, it should return one of 'rock', 'paper', or 'scissors' at random.
Change the code so it plays a game between two RandomPlayer objects.


import random
  moves = ['rock', 'paper', 'scissors']

class Player():
  def __init__(self):
          self.score = 0
def move(self):
        return moves[0]
def learn(self, learn_move):
        pass

class RandomPlayer(Player):
    def move(self):
    move_choice = random.choice(moves)
    return (move_choice)

class CopyPlayer(Player):
    def __init__(self):
    Player.__init__(self)
    self.last_move = None
