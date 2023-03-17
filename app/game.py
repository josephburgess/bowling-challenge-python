class Game:
    def __init__(self):
        self.scorecard = []

    def add(self, frame):
        self.scorecard.append(frame)

    def calculate_face_value(self):
        return sum(frame.get_total() for frame in self.scorecard)
