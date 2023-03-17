class Game:
    def __init__(self):
        self.scorecard = []

    def add(self, frame):
        self.scorecard.append(frame)

    def calculate_face_value(self):
        return sum(frame.get_total() for frame in self.scorecard)

    def calculate_spares(self):
        spare_bonus = 0
        for index, frame in enumerate(self.scorecard):
            previous_frame = self.scorecard[index - 1]

            if index > 0 and previous_frame.is_spare():
                spare_bonus += frame.get_first()

        return spare_bonus
