import random


def roll():
    die_score = random.choice([1, 2, 3, 3, 4, 5, 6])
    return die_score


class Game:

    # Initializer / Instance attributes
    def __init__(self, score):
        self.score = {self.player: 0, self.computer: 0}
        self.player = Player()


class Player:

   # Initializer / Instance attributes
    def __init__(self):
        self.points = 0

    def player_roll(self):
        choice = input("Would you like to (r)oll or (h)old? ")
        if choice == "r":
            print("You rolled a", roll())
        elif choice == "h":
            print("You hold to the Computer.")
            return choice


class Computer:

    def __init__(self):
        self.points = 0


roll()
player = Player()
player.player_roll()
