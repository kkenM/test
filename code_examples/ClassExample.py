class GUI:

    # Clase
    # Has functions
    # Has parameters

    def __init__(self, user):

        # define paramters
        self.username = user

    def getUsername(self):
        return self.username

    def setUsername(self, user):
        self.username = user


# Initialize an object of class GUI stored under variable gui_one
gui_one = GUI("Charles in Charge")

gui_one.setUsername("Petah")


print(gui_one.getUsername())
