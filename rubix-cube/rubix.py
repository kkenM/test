import random

class RubixArray:
    def __init__(self):

        #3D array representing the 6 faces of the cube
        self.rubix_list = [
            [
                [],
                [],
                []
            ],
            [
                [],
                [],
                []
            ],
            [
                [],
                [],
                []
            ],
            [
                [],
                [],
                []
            ],
            [
                [],
                [],
                []
            ],
            [
                [],
                [],
                []
            ],
        ]

        self.color_list = ["W","W","W","W","W","W","W","W","W",
                      "Y","Y","Y","Y","Y","Y","Y","Y","Y",
                      "O","O","O","O","O","O","O","O","O",
                      "R","R","R","R","R","R","R","R","R",
                      "G","G","G","G","G","G","G","G","G",
                      "B","B","B","B","B","B","B","B","B"
                      ]
    
    def randomize_cube(self):
        random.shuffle(self.color_list)

        for side in self.rubix_list:
            for row in side:
                for cube in row:
                    self.rubix_list[side[row[cube]]] = self.color_list.pop()

    def display_cube(self):
        for side in self.rubix_list:
            for row in side:
                for cube in row:
                    print(cube + " ", end="")
                print("")

rubix = RubixArray()
rubix.randomize_cube()
rubix.display_cube()