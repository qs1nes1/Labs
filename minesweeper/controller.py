class Controller:
    """Controller class for the connection between Model and View."""

    def __init__(self, model):
        self.model = model
        self.model.set_controller(self)

    def setView(self, view):
        self.view = view

    def left_click(self, x, y):
        self.model.open_cell(x, y)
        self.view.update()
        status = self.get_status()
        if status == "Win":
            print("You won!")
        elif status == "Lose":
            print("You lost!")

    def right_click(self, x, y):
        self.model.next_mark(x, y)
        self.view.update()

    def create_timer(self):
        self.view.top_box.top_panel.timer.run_timer()

    def stop_timer(self):
        self.view.top_box.top_panel.timer.stop_timer()

    def clear_timer(self):
        self.view.top_box.top_panel.timer.clear_timer()

    def set_start_button(self):
        self.view.update()

    def set_win_button(self):
        self.view.update()

    def set_mines_board(self, mines):
        self.view.update()

    def get_status(self):
        return self.model.game_status()

    def start_new_game(self):
        self.model.new_game(game_level=1)
        self.view.update()

    def start_new_game_smile(self):
        self.model.new_game(game_level=0)
        self.view.update()

    def start_new_game_junior(self):
        self.model.new_game(game_level=1)
        self.model.last_level = 1
        self.view.update()

    def start_new_game_middle(self):
        self.model.new_game(game_level=2)
        self.model.last_level = 2
        self.view.update()

    def start_new_game_senior(self):
        self.model.new_game(game_level=3)
        self.model.last_level = 3
        self.view.update()
