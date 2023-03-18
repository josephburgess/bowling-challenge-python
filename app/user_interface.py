class UserInterface:
    def __init__(self, game, io=None):
        self.game = game
        self.io = io if io else print

    def get_roll_one(self):
        self.roll_one = self.validate_roll_input("Enter your first roll: ", 0, 10)
        return self.roll_one

    def get_roll_two(self):
        remaining_pins = (
            10
            if self.game.frame_count == 10 and self.roll_one == 10
            else 10 - self.roll_one
        )
        self.roll_two = (
            self.validate_roll_input("Enter your second roll: ", 0, remaining_pins)
            if remaining_pins > 0
            else 0
        )
        return self.roll_two

    def get_roll_three(self):
        if self.game.frame_count != 10:
            self.roll_three = 0
            return self.roll_three

        self.roll_three = (
            self.validate_roll_input("Enter your bonus last roll: ", 0, 10)
            if self.roll_one == 10 or self.roll_one + self.roll_two == 10
            else 0
        )
        return self.roll_three

    def validate_roll_input(self, prompt, min_value, max_value):
        roll = input(prompt)
        if not roll.isdigit() or int(roll) < min_value or int(roll) > max_value:
            print(
                f"Invalid input. Please enter a number between {min_value} and {max_value}."
            )
            return self.validate_roll_input(prompt, min_value, max_value)
        return int(roll)
