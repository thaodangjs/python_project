import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(self)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"Enter 0-8:\n")
            try:
                val = int(square)
                if val not in game.available_square():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Not valid square, try again")
        return val



class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(self)

    def get_move(self, game):
        val = random.choice(game.available_square())
        return val
