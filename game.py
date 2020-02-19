import random


def roll():
    die_score = random.choice([1, 2, 3, 3, 4, 5, 6])
    print(die_score)
    return die_score


class Game:

    # Initializer / Instance attributes
    def __init__(self, score):
        self.score = score
        self.player = Player()


class Player:

   # Initializer / Instance attributes
    def __init__(self):
        self.points = 0

    def player_roll(self):
        choice = input("Would you like to (r)oll or (h)old? ")
        print(choice)
        return choice


# roll()
player = Player()
player.player_roll()
