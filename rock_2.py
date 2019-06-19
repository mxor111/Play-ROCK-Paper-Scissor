import random

moves = ["rock", "paper", "scissors"]

class Player():
    my_move = None
    their_move = None

def move(self):
    return 'rock'

def learn(self, my_move, their_move):
    self.my_move = their_move
    self.their_move = their_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or

            (one == 'scissors' and two == 'paper') or

            (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):

    def move(self):
        return (random.choice(moves))

class HumanPlayer(Player):

    def move(self):
        while True:
            user = input("Rock, Paper or Scissors? ")
            if user.lower() not in moves:
                print("Invalid input choose Rock, Paper or Scissors")
            else:
                return(user.lower())

class ReflectPlayer(Player):

    def move():
        if self.their_move is None:
            return random.choice(moves)
            return self.their_move

class CyclePlayer(Player):

    def move():
        if self.my_move == None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count_win = 0
        self.count_lose = 0
        self.count_tie = 0

    def play_round(self):
        move1=self.p1.move()
        move2=self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

    def play_game(self):
        print("Game start!")
        for round in [1, 2, 3]:
            print(f"Round {round}:")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.count_win += 1
        elif beats(move2, move1):
            self.count_lose += 1
        else:
            if move1 == move2:
                self.count_tie += 1
            print(f"wins: {self.count_win} losses: {self.count_lose}")
            print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
