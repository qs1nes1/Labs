from random import randint

from cell import Cell


class Model:
	"""Class with game logic."""

	def __init__(self):
		self.flagged_cells = -1
		self.seconds_from_start = 1

	def set_contoller(self, contoller):
		self.contoller = contoller

	def new_game(self, game_level=0):
		"""Starts the game at a certain difficulty level."""
		levels = [
			self.empty_func,
			self.new_game_junior,
			self.new_game_middle,
			self.new_game_senior
		]
		levels[game_level]()
		self.contoller.set_start_button()
		self.contoller.stop_timer()
		self.contoller.clear_timer()
		if self.flagged_cells != -1:
			self.contoller.set_mines_board(self.MINES_MAX)
		self.create_field()

	"""TODO: Write test to find out when mines amounts
	   greater then spots."""