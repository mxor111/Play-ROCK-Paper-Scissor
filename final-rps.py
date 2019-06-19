#!/usr/bin/env python3
# ROCK PAPER SCISSOR - MICHELE

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']
p1 = input("Player 1 Whats's your name?")
P2 = input("Player 2 What's your name?")

"""The Player class is the parent class for all of the Players
in this game"""

# Remember the Rules:  Rock beats scissor, Scissor beats paper, paper
# beats rock


class Player():
    my_move = None
    thier_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass



class RandomPlayer(Player):
    def move(RandomPlayer):
        return (random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        while True:  # addng validator
            user = input("Rock, Paper or Scissors? ")
            if user.lower() not in moves:
                print("Invalid input choose Rock, Paper or Scissors")

            else:
                return user.lower()  # not sure


class ReflectPlayer(Player):

    def move(ReflectPlayer):
        if self.their_move is None:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = their_move


class CyclePlayer(Player):

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.move == "paper":
            return "scissors"
        else:
            return "rocK"


def move():
    if self.my_move is None:
        return random.choice(moves)
        if self.my_move == 'rock':
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
    if self.their_move is None:
        return random.choice(moves)
        if self.their_move == 'rock':
            return "paper"
        else:
            return "scissors"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2) is True:
            self.p1_score += 1
            print('Player 1 You Win!')
            if move1 == move2:
                print('Tie Game')
            else:
                self.p2_score += 1
                print('Player 2 You Win!')
        print(f"Score: Player 1 {self.p1_score}, Player 2 {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Let's Play! and Welcome")
        for round in range(7):
            print(f"Round {round}:")
            self.play_round()
        print("Game over Pay Again!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
