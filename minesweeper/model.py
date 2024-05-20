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

	def empty_func(self):
		"""When player did not change game level
		   and we want play last one."""
		pass

	def new_game_junior(self):
		self.FIELD_WIDTH = 10
		self.FIELD_HEIGHT = 10
		self.MINES_MAX = 10

	def new_game_middle(self):
		self.FIELD_WIDTH = 14
		self.FIELD_HEIGHT = 6
		self.MINES_MAX = 15

	def new_game_senior(self):
		self.FIELD_WIDTH = 15
		self.FIELD_HEIGHT = 15
		self.MINES_MAX = 25

	def create_field(self):
		# Creating field.
		self.first_click = True
		self.seconds_from_start = 1
		self.flagged_cells = 0
		self.open_cells = 0
		self.must_open_cells = (self.FIELD_WIDTH * self.FIELD_HEIGHT
								- self.MINES_MAX)
		self.is_game_over = False
		self.stop_game = False
		self.field = []
		for y in range(self.FIELD_HEIGHT):
			_xrow = []
			for x in range(self.FIELD_WIDTH):
				cell = Cell(x, y)
				_xrow.append(cell)
			self.field.append(_xrow)

		# Setting mines at field.
		mines_ammout = 0
		while mines_ammout < self.MINES_MAX:
			_x = randint(0, self.FIELD_WIDTH - 1)
			_y = randint(0, self.FIELD_HEIGHT - 1)
			if not self.field[_y][_x].mined:
				mines_ammout += 1
				self.field[_y][_x].mined = True

	def get_cell(self, x, y):
		return self.field[y][x]

	def open_cell(self, x, y):
		if not self.stop_game:
			if self.first_click:
				self.contoller.create_timer()
				self.first_click = False
			cell = self.get_cell(x, y)
			# Check if the cell is not mined.
			last_state = cell.state
			cell.open()
			if cell.state == "opened" and last_state != cell.state:
				self.open_cells += 1
				self.checked = []
				if not cell.mined:
					mines_number = self.check_neighbors(cell)
					cell.int_state = mines_number
			if cell.state == "opened":
				if cell.mined:
					# If this cell was mined game over.
					cell.state = "opened"
					self.is_game_over = True
					self.stop_game = True
				else:
					pass

			if self.is_game_over:
				self.game_over()

	def check_neighbors(self, cell):
		neighbors_mines = 0
		self.checked.append(cell)
		if self.is_mined(cell, cell.x - 1, cell.y - 1): neighbors_mines += 1
		if self.is_mined(cell, cell.x, cell.y - 1): neighbors_mines += 1
		if self.is_mined(cell, cell.x + 1, cell.y - 1): neighbors_mines += 1
		if self.is_mined(cell, cell.x - 1, cell.y): neighbors_mines += 1
		if self.is_mined(cell, cell.x + 1, cell.y): neighbors_mines += 1
		if self.is_mined(cell, cell.x - 1, cell.y + 1): neighbors_mines += 1
		if self.is_mined(cell, cell.x, cell.y + 1): neighbors_mines += 1
		if self.is_mined(cell, cell.x + 1, cell.y + 1): neighbors_mines += 1
		if neighbors_mines == 0:
			self.open_neighbors(cell)
			pass
		return neighbors_mines

	def open_neighbors(self, cell):
		self.open_one_neighbor(cell, cell.x - 1, cell.y - 1)
		self.open_one_neighbor(cell, cell.x, cell.y - 1)
		self.open_one_neighbor(cell, cell.x + 1, cell.y - 1)
		self.open_one_neighbor(cell, cell.x - 1, cell.y)
		self.open_one_neighbor(cell, cell.x + 1, cell.y)
		self.open_one_neighbor(cell, cell.x - 1, cell.y + 1)
		self.open_one_neighbor(cell, cell.x, cell.y + 1)
		self.open_one_neighbor(cell, cell.x + 1, cell.y + 1)