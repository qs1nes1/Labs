import pytest
from unittest.mock import MagicMock

from minesweeper.controller import *

@pytest.fixture
def mock_model():
    model = MagicMock()
    model.MINES_MAX = 10
    model.flagged_cells = 0
    return model

@pytest.fixture
def mock_view():
    view = MagicMock()
    return view

@pytest.fixture
def controller(mock_model):
    return Controller(mock_model)

def test_left_click(controller, mock_model, mock_view):
    controller.setView(mock_view)
    mock_model.game_status.return_value = "Win"
    controller.left_click(0, 0)
    mock_view.top_box.top_panel.start_btn.set_won.assert_called_once()

    mock_model.game_status.return_value = "Lose"
    controller.left_click(1, 1)
    mock_view.top_box.top_panel.start_btn.set_lost.assert_called_once()

def test_right_click(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.right_click(0, 0)
    mock_model.next_mark.assert_called_once_with(0, 0)
    mock_view.top_box.top_panel.board.set.assert_called_once_with(10)
    mock_view.update.assert_called_once()

def test_create_timer(controller, mock_view):
    controller.setView(mock_view)
    controller.create_timer()
    mock_view.top_box.top_panel.run_timer.assert_called_once()

def test_stop_timer(controller, mock_view):
    controller.setView(mock_view)
    controller.stop_timer()
    mock_view.top_box.top_panel.stop_timer.assert_called_once()

def test_clear_timer(controller, mock_view):
    controller.setView(mock_view)
    controller.clear_timer()
    mock_view.top_box.top_panel.clear_timer.assert_called_once()

def test_set_start_button(controller, mock_view):
    controller.setView(mock_view)
    controller.set_start_button()
    mock_view.top_box.top_panel.start_btn.set_start.assert_called_once()

def test_set_win_button(controller, mock_view):
    controller.setView(mock_view)
    controller.set_win_button()
    mock_view.top_box.top_panel.start_btn.set_won.assert_called_once()

def test_set_mines_board(controller, mock_view):
    controller.setView(mock_view)
    controller.set_mines_board(5)
    mock_view.top_box.top_panel.board.set.assert_called_once_with(5)
    mock_view.update.assert_called_once()

def test_start_new_game(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.start_new_game()
    mock_model.new_game.assert_called_once_with(game_level=1)
    mock_view.update.assert_called_once()

def test_start_new_game_smile(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.start_new_game_smile()
    mock_model.new_game.assert_called_once_with(game_level=0)
    mock_view.update.assert_called_once()

def test_start_new_game_junior(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.start_new_game_junior()
    mock_model.new_game.assert_called_once_with(game_level=1)
    assert mock_model.last_level == 1
    controller.set_fixed_size()
    mock_view.update.assert_called_once()

def test_start_new_game_middle(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.start_new_game_middle()
    mock_model.new_game.assert_called_once_with(game_level=2)
    assert mock_model.last_level == 2
    controller.set_fixed_size()
    mock_view.update.assert_called_once()

def test_start_new_game_senior(controller, mock_model, mock_view):
    controller.setView(mock_view)
    controller.start_new_game_senior()
    mock_model.new_game.assert_called_once_with(game_level=3)
    assert mock_model.last_level == 3
    controller.set_fixed_size()
    mock_view.update.assert_called_once()

def test_set_fixed_size(controller, mock_model, mock_view):
    mock_model.FIELD_WIDTH = 10
    mock_model.FIELD_HEIGHT = 10
    controller.setView(mock_view)
    controller.set_fixed_size()
    mock_view.top_box.field.setFixedWidth.assert_called_once_with(320)
    mock_view.top_box.field.setFixedHeight.assert_called_once_with(320)
    mock_view.setFixedWidth.assert_called_once_with(340)
    mock_view.setFixedHeight.assert_called_once_with(410)

if __name__ == "__main__":
    pytest.main()
