class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 'closed'  # Возможные состояния: 'closed', 'opened', 'flagged'
        self.int_state = 0  # Количество мин вокруг ячейки

    def open(self):
        self.state = 'opened'

    def next_mark(self):
        if self.state == 'closed':
            self.state = 'flagged'
        elif self.state == 'flagged':
            self.state = 'closed'
