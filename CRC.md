Class: Game
Responsibilties: Winner(score), score to total, turn, dice roll 1 switches players
Collaborators: Die, Players turn, players score

Class: Die
Responsibilties: 6 sides, roll
Collaborators: Game

Class: Player
Responsibilites: score, rolls to sum
Collaborators: CompPlayer

Class: CompPlayer
Responsibilites: score, rolls to sum, 20 points or more = hold
Collaborators: Player
