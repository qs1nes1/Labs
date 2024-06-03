import pytest
from minesweeper.cell import Cell

def test_initial_state():
    cell = Cell(0, 0)
    assert cell.x == 0
    assert cell.y == 0
    assert cell.state == "closed"
    assert not cell.mined
    assert cell.int_state == 9
    assert cell.counter == 0

def test_open_cell():
    cell = Cell(0, 0)
    cell.open()
    assert cell.state == "opened"
    assert cell.int_state == 0

def test_open_flagged_cell():
    cell = Cell(0, 0)
    cell.state = "flagged"
    cell.open()
    assert cell.state == "flagged"
    assert cell.int_state == 9

def test_open_disable_cell():
    cell = Cell(0, 0)
    cell.state = "disable"
    cell.open()
    assert cell.state == "disable"
    assert cell.int_state == 9

def test_next_mark():
    cell = Cell(0, 0)
    cell.next_mark()
    assert cell.state == "flagged"
    assert cell.int_state == 10

    cell.next_mark()
    assert cell.state == "questioned"
    assert cell.int_state == 11

    cell.next_mark()
    assert cell.state == "closed"
    assert cell.int_state == 9

def test_next_mark_opened_cell():
    cell = Cell(0, 0)
    cell.state = "opened"
    initial_int_state = cell.int_state
    cell.next_mark()
    assert cell.state == "opened"
    assert cell.int_state == initial_int_state

def test_next_mark_disabled_cell():
    cell = Cell(0, 0)
    cell.state = "disable"
    cell.next_mark()
    assert cell.state == "disable"
    assert cell.int_state == 9
