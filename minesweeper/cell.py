class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mined = False
        self.state = "closed"  # possible states: closed, opened, flagged, questioned
        self.int_state = 0  # used for display purposes

    def open(self):
        if self.state == "closed" or self.state == "questioned":
            self.state = "opened"

    def next_mark(self):
        if self.state == "closed":
            self.state = "flagged"
        elif self.state == "flagged":
            self.state = "questioned"
        elif self.state == "questioned":
            self.state = "closed"
