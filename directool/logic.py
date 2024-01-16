import math

from character import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        # Check winner (2)
        self.current_winner = None

    def print_board_game(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            # Check winner (4):
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Check winner (3)
    def check_winner(self, square, letter):
        row_ind = math.floor(square/3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3 # 5 => 2 => 2 - 5 - 8
        col = [self.board[col_ind+(3*i)] for i in range(3)]
        if all([s == letter for s in col]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    @staticmethod
    def print_board_num():
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def empty_board(self):
        return " " in self.board

    def available_square(self):
        return [i for i, value in enumerate(self.board) if value == " "]


def play(game, player_x, player_o, print_game=True):
    if print_game:
        print("Welcome to the hell!")
        game.print_board_num()

    letter = "A"

    while game.empty_board():
        if letter == "A":
            square = player_x.get_move(game)
        else:
            square = player_o.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(" ")
                print(f"{letter}'s turn, move to square {square}")
                game.print_board_game()
            # Check win - (1)
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

        letter = "B" if letter == "A" else "A"

    if print_game:
        print("It's a tie")


play(TicTacToe(), ComputerPlayer("A"), HumanPlayer("B"), print_game=True)
