from player import HumanPlayer, ComputerRandomPlayer
class TicTacToe:
    def __init__(self):
        self.board = self.make_board()

    def print_board_game(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")\


    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        return False

    @staticmethod
    def print_board_num():
        for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def empty_board(self):
        return " " in self.board

    def available_square(self):
        return [i for i, value in enumerate(self.board) if value == " "]


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_num()
    letter = "X"
    while game.empty_board():
        if letter == "X":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter}'s turn to square {square}")
                game.print_board_game()

        letter = "O" if letter == "X" else "X"

    if print_game:
        print("It's a tier")


play(TicTacToe(), ComputerRandomPlayer("X"), HumanPlayer("O"), print_game=True)
