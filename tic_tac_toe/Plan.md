# Tic Tac Toe Game

class GUI()
-print the tic tac toe board
-update the ttt board
-prompt the user for input

    -functions
        __init__
            -data
                -tic tac toe board
                    1 2 3
                a   x| |
                b  _______
                c  _______
                    | |

                -dictionary of 9 keys a-c|1-3
                -isPlayerTurn = True
                -gameData = [[][][]] 2D list storing "algebraic" notation of moves and icon identifier
                    ex:
                        [
                            [(a1,None),(a2,None),(a3,None)],
                            [(b1,None)],(b2,"X"),(b3,"X")],
                            [etc]
                        ]

        printBoard
            -prints to board using the game data

        getPlayerInput
            -prompts user for an agebraic tic tac toe move ie a.3., or c1
