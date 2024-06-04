import sys
sys.path.append('D:\\labsss\\minesweeper')  # Путь к вашему модулю controller.py

import unittest
from unittest.mock import MagicMock
from minesweeper.controller import Controller
from minesweeper.model import Model

class TestController(unittest.TestCase):
    def setUp(self):
        self.mock_view = MagicMock()
        self.mock_model = MagicMock()
        self.controller = Controller(self.mock_model)

    def test_clear_timer(self):
        self.controller.setView(self.mock_view)
        self.controller.clear_timer()
        self.mock_view.top_box.top_panel.timer.clear_timer.assert_called_once()

    def test_create_timer(self):
        self.controller.setView(self.mock_view)
        self.controller.create_timer()
        self.mock_view.top_box.top_panel.timer.run_timer.assert_called_once()

    def test_left_click(self):
        self.controller.setView(self.mock_view)
        self.controller.left_click(0, 0)
        self.mock_view.update.assert_called_once()

    def test_right_click(self):
        self.controller.setView(self.mock_view)
        self.controller.right_click(0, 0)
        self.mock_view.update.assert_called_once()

    def test_set_mines_board(self):
        self.controller.setView(self.mock_view)
        self.controller.set_mines_board(5)
        self.mock_view.update.assert_called_once()

    def test_set_start_button(self):
        self.controller.setView(self.mock_view)
        self.controller.set_start_button()
        self.mock_view.update.assert_called_once()

    def test_set_win_button(self):
        self.controller.setView(self.mock_view)
        self.controller.set_win_button()
        self.mock_view.update.assert_called_once()

    def test_start_new_game(self):
        self.controller.setView(self.mock_view)
        self.controller.start_new_game()
        self.mock_view.update.assert_called_once()

    def test_start_new_game_junior(self):
        self.controller.setView(self.mock_view)
        self.controller.start_new_game_junior()
        self.mock_view.update.assert_called_once()

    def test_start_new_game_middle(self):
        self.controller.setView(self.mock_view)
        self.controller.start_new_game_middle()
        self.mock_view.update.assert_called_once()

    def test_start_new_game_senior(self):
        self.controller.setView(self.mock_view)
        self.controller.start_new_game_senior()
        self.mock_view.update.assert_called_once()

    def test_start_new_game_smile(self):
        self.controller.setView(self.mock_view)
        self.controller.start_new_game_smile()
        self.mock_view.update.assert_called_once()

    def test_stop_timer(self):
        self.controller.setView(self.mock_view)
        self.controller.stop_timer()
        self.mock_view.top_box.top_panel.timer.stop_timer.assert_called_once()

if __name__ == '__main__':
    unittest.main()
