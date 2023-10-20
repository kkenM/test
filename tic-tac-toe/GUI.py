import os


class GUI:

    def __init__(self):
        self.game_data = [
            # indices where X or O can go
            # [0][1],[0][5],[0][9]
            # [1][1],[1][5],[1][9]
            # [2][1],[2][5],[2][9]
            [" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
            ["═", "═", "═", "╬", "═", "═", "═", "╬", "═", "═", "═"],
            [" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "],
            ["═", "═", "═", "╬", "═", "═", "═", "╬", "═", "═", "═"],
            [" ", " ", " ", "║", " ", " ", " ", "║", " ", " ", " "]
        ]

        pass

    # Displays the tictactoe board using the gameData list
    def display_board(self):
        os.system('cls')
        for row in self.game_data:
            for col in row:
                print(col, end="")
            print("")

    # Takes in an algebraic move a1, c3, etc
    # checks if its the player or bots turn
    # updates the game_data list with the correct symbol
    def update_board_list(self, alg_move):
        pass

    # Changes the current state of the is_player_turn boolean
    def update_turn(self):
        pass

    # prompts the player for an algebraic ttt move
    # checks if input is in the correct format then prints a success
    # or failure message
    def prompt_move(self):
        pass


test = GUI()

test.display_board()
