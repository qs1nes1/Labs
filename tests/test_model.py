# test_model.py
import unittest
from minesweeper.model import Model
from minesweeper.cell import Cell

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def test_new_game_junior(self):
        self.model.new_game(1)
        self.assertEqual(self.model.FIELD_WIDTH, 10)
        self.assertEqual(self.model.FIELD_HEIGHT, 10)
        self.assertEqual(self.model.MINES_MAX, 10)

    def test_new_game_middle(self):
        self.model.new_game(2)
        self.assertEqual(self.model.FIELD_WIDTH, 14)
        self.assertEqual(self.model.FIELD_HEIGHT, 6)
        self.assertEqual(self.model.MINES_MAX, 15)

    def test_new_game_senior(self):
        self.model.new_game(3)
        self.assertEqual(self.model.FIELD_WIDTH, 15)
        self.assertEqual(self.model.FIELD_HEIGHT, 15)
        self.assertEqual(self.model.MINES_MAX, 25)

    def test_create_field(self):
        self.model.new_game(1)
        self.model.create_field()
        self.assertEqual(len(self.model.field), 10)
        self.assertEqual(len(self.model.field[0]), 10)

    def test_get_cell(self):
        self.model.new_game(1)
        cell = self.model.get_cell(5, 5)
        self.assertEqual(cell.x, 5)
        self.assertEqual(cell.y, 5)

    def test_open_cell(self):
        self.model.new_game(1)
        self.model.create_field()
        cell = self.model.get_cell(5, 5)
        self.model.open_cell(5, 5)
        self.assertTrue(cell.state == "opened" or cell.state == "flagged")

    def test_next_mark(self):
        self.model.new_game(1)
        self.model.create_field()
        cell = self.model.get_cell(5, 5)
        self.model.next_mark(5, 5)
        self.assertEqual(cell.state, "flagged")
        self.assertEqual(self.model.flagged_cells, 1)

    def test_game_over(self):
        self.model.new_game(1)
        self.model.create_field()
        for row in self.model.field:
            for cell in row:
                if cell.mined:
                    cell.state = "opened"
        self.model.game_over()
        for row in self.model.field:
            for cell in row:
                if cell.mined:
                    self.assertEqual(cell.int_state, 13)
                else:
                    self.assertNotEqual(cell.int_state, 14)
