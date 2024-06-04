import pytest
from minesweeper.model import Cell, Model

@pytest.fixture
def model():
    return Model()

def test_initial_state(model):
    assert model.flagged_cells == -1
    assert model.seconds_from_start == 1

def test_new_game_junior(model):
    model.new_game_junior()
    assert model.FIELD_WIDTH == 10
    assert model.FIELD_HEIGHT == 10
    assert model.MINES_MAX == 10

def test_new_game_middle(model):
    model.new_game_middle()
    assert model.FIELD_WIDTH == 14
    assert model.FIELD_HEIGHT == 6
    assert model.MINES_MAX == 15

def test_new_game_senior(model):
    model.new_game_senior()
    assert model.FIELD_WIDTH == 15
    assert model.FIELD_HEIGHT == 15
    assert model.MINES_MAX == 25

def test_create_field(model):
    model.new_game_junior()
    model.create_field()
    assert len(model.field) == model.FIELD_HEIGHT
    assert len(model.field[0]) == model.FIELD_WIDTH
    mines_count = sum(cell.mined for row in model.field for cell in row)
    assert mines_count == model.MINES_MAX

def test_open_cell_no_mine(model):
    model.new_game_junior()
    model.create_field()
    cell = model.get_cell(0, 0)
    cell.mined = False
    model.open_cell(0, 0)
    assert cell.state == "opened"
    assert cell.int_state >= 0

def test_open_cell_with_mine(model):
    model.new_game_junior()
    model.create_field()
    cell = model.get_cell(0, 0)
    cell.mined = True
    model.open_cell(0, 0)
    assert cell.state == "opened"
    assert model.is_game_over

def test_game_status_win(model):
    model.new_game_junior()
    model.create_field()
    model.must_open_cells = 1
    model.open_cells = 1
    assert model.game_status() == "Win"

def test_game_status_lose(model):
    model.new_game_junior()
    model.create_field()
    model.is_game_over = True
    assert model.game_status() == "Lose"

def test_game_status_ongoing(model):
    model.new_game_junior()
    model.create_field()
    assert model.game_status() == "Game"

# Run the test
if __name__ == "__main__":
    pytest.main()
