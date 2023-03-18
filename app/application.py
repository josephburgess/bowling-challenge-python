from . import Game, Frame, UserInterface


class Application:
    def __init__(self):
        self.game = Game()
        self.UI = UserInterface(self.game)

    def run(self):
        self.title_text()
        for i in range(10):
            print(f"\nYou are on frame {self.UI.game.frame_count}")
            roll_one = self.UI.get_roll_one()
            roll_two = self.UI.get_roll_two()
            roll_three = self.UI.get_roll_three()
            frame = Frame(roll_one, roll_two, roll_three)
            self.UI.game.add(frame)
        print(f"Your total score is: {self.UI.game.calculate_grand_total()}")

    def title_text(self):
        print("Welcome! This simple calculator will keep track of your bowling score.")
        print("Input rolls and your score will be printed at the end of the game.")
