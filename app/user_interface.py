class UserInterface:
    def __init__(self, game, io=None):
        self.game = game
        self.io = io if io else print

    def get_roll_one(self):
        self.roll_one = int(input("Enter your first roll: "))
        return self.roll_one
