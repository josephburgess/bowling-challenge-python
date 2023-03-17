class Game:
    def __init__(self):
        self.scorecard = []

    def add(self, frame):
        self.scorecard.append(frame)

    def calculate_face_value(self):
        return sum(frame.get_total() for frame in self.scorecard)

    def calculate_spares(self):
        return sum(
            self.scorecard[index].get_first()
            for index in range(1, len(self.scorecard))
            if self.scorecard[index - 1].is_spare()
        )

    def calculate_strikes(self):
        strike_bonus = 0
        for index, frame in enumerate(self.scorecard):
            if index == 0:
                continue

            previous_frame = self.scorecard[index - 1]
            next_frame = (
                self.scorecard[index + 1] if index != len(self.scorecard) - 1 else None
            )

            if previous_frame.is_strike():
                strike_bonus += frame.get_first()

                if frame.is_strike() and index != 9:
                    strike_bonus += next_frame.get_first()

                else:
                    strike_bonus += frame.get_second()

        return strike_bonus
