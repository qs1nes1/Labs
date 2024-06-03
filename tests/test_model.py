import pytest
from minesweeper.model import Model

def test_initial_state():
    model = Model()
    assert model.flagged_cells == -1
    assert model.seconds_from_start == 1

def test_new_game_junior():
    model = Model()
    model.new_game(1)
    assert model.FIELD_WIDTH == 10
    assert model.FIELD_HEIGHT == 10
    assert model.MINES_MAX == 10

def test_new_game_middle():
    model = Model()
    model.new_game(2)
    assert model.FIELD_WIDTH == 14
    assert model.FIELD_HEIGHT == 6
    assert model.MINES_MAX == 15

def test_new_game_senior():
    model = Model()
    model.new_game(3)
    assert model.FIELD_WIDTH == 15
    assert model.FIELD_HEIGHT == 15
    assert model.MINES_MAX == 25

def test_create_field():
    model = Model()
    model.new_game(1)
    model.create_field()
    assert len(model.field) == model.FIELD_HEIGHT
    assert len(model.field[0]) == model.FIELD_WIDTH
    mines_count = sum(cell.mined for row in model.field for cell in row)
    assert mines_count == model.MINES_MAX

def test_open_cell():
    model = Model()
    model.new_game(1)
    model.create_field()
    cell = model.get_cell(0, 0)
    model.open_cell(0, 0)
    assert cell.state == "opened"

def test_next_mark():
    model = Model()
    model.new_game(1)
    model.create_field()
    cell = model.get_cell(0, 0)
    model.next_mark(0, 0)
    assert cell.state == "flagged"
    model.next_mark(0, 0)
    assert cell.state == "closed"
