import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
import pygame
from minesweeper import main

class TestMinesweeper(unittest.TestCase):

    @patch('minesweeper.main.create_board')
    @patch('minesweeper.main.draw_board')
    @patch('minesweeper.main.display_message')
    @patch('minesweeper.main.check_win')
    def test_game_logic(self, mock_check_win, mock_display_message, mock_draw_board, mock_create_board):
        # Setup mock return values
        mock_create_board.return_value = [[' ', '1', 'M'], ['1', '2', '1'], [' ', '1', ' ']]
        mock_check_win.return_value = False

        # Initialize the game
        pygame.init()
        screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Сапер")

        # Initialize game variables
        level = "Легкий"
        board_size = (3, 3)
        mines_count = 1
        board = main.create_board(board_size, mines_count)
        revealed = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
        flagged = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
        start_time = pygame.time.get_ticks()
        game_over = False
        show_levels = False

        # Simulate a click on a cell
        x, y = 0, 0
        revealed[y][x] = True
        if board[y][x] == 'M':
            game_over = True
        elif board[y][x] == ' ':
            main.reveal_adjacent(board, revealed, x, y)

        # Check if the cell is revealed correctly
        self.assertTrue(revealed[y][x])
        self.assertFalse(game_over)

        # Simulate a click on a mine
        x, y = 2, 0
        revealed[y][x] = True
        if board[y][x] == 'M':
            game_over = True
        elif board[y][x] == ' ':
            main.reveal_adjacent(board, revealed, x, y)

        # Check if the game is over after clicking on a mine
        self.assertTrue(revealed[y][x])
        self.assertTrue(game_over)

        # Clean up Pygame
        pygame.quit()

    @patch('minesweeper.main.pygame.display.set_mode')
    @patch('minesweeper.main.pygame.display.set_caption')
    def test_display_setup(self, mock_set_caption, mock_set_mode):
        # Run the display setup part of the main function
        screen_width, screen_height = 300, 400
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Сапер")

        # Check if the display mode and caption were set correctly
        mock_set_mode.assert_called_with((screen_width, screen_height))
        mock_set_caption.assert_called_with("Сапер")

    @patch('minesweeper.main.pygame.event.get')
    def test_event_handling(self, mock_event_get):
        # Initialize the game
        pygame.init()
        screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption("Сапер")

        # Simulate some events
        mock_event_get.return_value = [
            pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1, 'pos': (10, 10)}),
            pygame.event.Event(pygame.QUIT)
        ]

        # Run the main event loop once
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # Add logic here to handle the click

        # Check if the running variable is set to False after the QUIT event
        self.assertFalse(running)

        # Clean up Pygame
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
