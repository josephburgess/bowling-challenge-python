class UserInterface:
    def __init__(self, game, io=None):
        self.game = game
        self.io = io if io else print

    def get_roll_one(self):
        self.roll_one = int(input("Enter your first roll: "))
        return self.roll_one

    def get_roll_two(self):
        remaining_pins = (
            10
            if self.game.frame_count == 10 and self.roll_one == 10
            else 10 - self.roll_one
        )
        self.roll_two = (
            self.validate_roll_two(remaining_pins) if remaining_pins > 0 else 0
        )
        return self.roll_two

    def validate_roll_two(self, remaining_pins):
        roll_two = int(input("Enter your second roll: "))
        if roll_two > remaining_pins:
            print(f"Invalid input. You have {remaining_pins} remaining.")
            return self.validate_roll_two(remaining_pins)
        return roll_two
