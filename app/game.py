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
