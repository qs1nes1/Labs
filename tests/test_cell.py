import unittest
from minesweeper.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(0, 0)

    def test_initial_state_is_closed(self):
        self.assertEqual(self.cell.state, "closed")

    def test_open_state_is_opened(self):
        self.cell.open()
        self.assertEqual(self.cell.state, "opened")

    def test_next_mark_state_is_flagged(self):
        self.cell.next_mark()
        self.assertEqual(self.cell.state, "flagged")

    def test_next_mark_state_is_questioned(self):
        self.cell.next_mark()  # flagged
        self.cell.next_mark()  # questioned
        self.assertEqual(self.cell.state, "questioned")

    def test_next_mark_state_is_closed(self):
        self.cell.next_mark()  # flagged
        self.cell.next_mark()  # questioned
        self.cell.next_mark()  # closed
        self.assertEqual(self.cell.state, "closed")

    def test_open_state_is_questioned(self):
        self.cell.next_mark()  # flagged
        self.cell.next_mark()  # questioned
        self.cell.open()
        self.assertEqual(self.cell.state, "opened")

if __name__ == "__main__":
    unittest.main()
