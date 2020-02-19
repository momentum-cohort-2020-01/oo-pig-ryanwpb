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


roll()
