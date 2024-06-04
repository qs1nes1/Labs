import pytest
from minesweeper.cell import Cell  # This assumes cell.py is in the same directory

def test_initial_state():
    cell = Cell(0, 0)
    assert cell.x == 0
    assert cell.y == 0
    assert cell.state == "closed"
    assert cell.int_state == 0

def test_open_cell():
    cell = Cell(0, 0)
    cell.open()
    assert cell.state == "opened"
    assert cell.int_state == 0

def test_next_mark_closed_to_flagged():
    cell = Cell(0, 0)
    cell.next_mark()
    assert cell.state == "flagged"

def test_next_mark_flagged_to_closed():
    cell = Cell(0, 0)
    cell.state = "flagged"
    cell.next_mark()
    assert cell.state == "closed"

# Run the tests
if __name__ == "__main__":
    pytest.main()
