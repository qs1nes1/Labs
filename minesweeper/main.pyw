import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pygame
import sys
from utils import create_board, draw_board, display_message, check_win, draw_timer, reveal_adjacent
from constants import CELL_SIZE, SCREEN_EXTRA_HEIGHT, smiley_image, smiley_won_image, smiley_lost_image

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
FONT = pygame.font.Font(None, 36)

# Настройки уровней сложности
LEVELS = {
    "Легкий": {"size": (10, 10), "mines": 10},
    "Средний": {"size": (16, 16), "mines": 40},
    "Сложный": {"size": (30, 16), "mines": 99},
}

def main():
    level = "Легкий"
    board_size = LEVELS[level]["size"]
    mines_count = LEVELS[level]["mines"]
    board = create_board(board_size, mines_count)
    revealed = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
    flagged = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
    screen_width = board_size[0] * CELL_SIZE
    screen_height = board_size[1] * CELL_SIZE + SCREEN_EXTRA_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Сапер")
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    game_over = False
    running = True
    show_levels = False

    def reset_game(selected_level):
        nonlocal level, board, revealed, flagged, start_time, game_over, screen_width, screen_height, board_size, mines_count, show_levels
        level = selected_level
        board_size = LEVELS[level]["size"]
        mines_count = LEVELS[level]["mines"]
        board = create_board(board_size, mines_count)
        revealed = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
        flagged = [[False for _ in range(board_size[0])] for _ in range(board_size[1])]
        screen_width = board_size[0] * CELL_SIZE
        screen_height = board_size[1] * CELL_SIZE + SCREEN_EXTRA_HEIGHT
        screen = pygame.display.set_mode((screen_width, screen_height))
        start_time = pygame.time.get_ticks()
        game_over = False
        show_levels = False

    def draw_buttons():
        button_width = 140
        button_height = SCREEN_EXTRA_HEIGHT - 20  # Установим высоту кнопки на уровне со смайликом и таймером
        padding = 10
        buttons = []
        level_button_rect = pygame.Rect(screen_width - button_width - padding, padding, button_width, button_height)
        buttons.append(("Уровни сложности", level_button_rect))
        pygame.draw.rect(screen, WHITE, level_button_rect)
        pygame.draw.rect(screen, BLACK, level_button_rect, 2)  # Добавляем рамку для кнопки "Уровни сложности"
        text = FONT.render("Уровни", True, BLACK)
        text_rect = text.get_rect(center=level_button_rect.center)
        screen.blit(text, text_rect)
        if show_levels:
            for idx, (name, settings) in enumerate(LEVELS.items()):
                button_rect = pygame.Rect(screen_width - button_width - padding, SCREEN_EXTRA_HEIGHT + (idx + 1) * (button_height + padding), button_width, button_height)
                buttons.append((name, button_rect))
                pygame.draw.rect(screen, WHITE, button_rect)
                pygame.draw.rect(screen, BLACK, button_rect, 2)  # Добавляем рамку для кнопок уровней
                text = FONT.render(name, True, BLACK)
                text_rect = text.get_rect(center=button_rect.center)
                screen.blit(text, text_rect)
        return buttons

    def draw_smiley(game_over, screen_width):
        if game_over:
            smiley = smiley_lost_image if not check_win(board, revealed) else smiley_won_image
        else:
            smiley = smiley_image
        smiley_rect = smiley.get_rect(center=(screen_width // 2, SCREEN_EXTRA_HEIGHT // 2))
        screen.blit(smiley, smiley_rect)
        return smiley_rect

    while running:
        screen.fill(WHITE)
        current_time = pygame.time.get_ticks()
        if not game_over:
            time_elapsed = (current_time - start_time) // 1000

        draw_board(board, revealed, flagged, screen, CELL_SIZE, FONT)  # Отрисовываем игровое поле
        buttons = draw_buttons()  # Отрисовываем кнопки поверх игрового поля
        smiley_rect = draw_smiley(game_over, screen_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if smiley_rect.collidepoint(event.pos):
                    reset_game(level)
                clicked_on_button = False
                for name, button_rect in buttons:
                    if button_rect.collidepoint(event.pos):
                        clicked_on_button = True
                        if name == "Уровни сложности":
                            show_levels = not show_levels
                        else:
                            reset_game(name)
                if not game_over and not clicked_on_button:
                    x, y = event.pos[0] // CELL_SIZE, (event.pos[1] - SCREEN_EXTRA_HEIGHT) // CELL_SIZE
                    if 0 <= x < board_size[0] and 0 <= y < board_size[1]:
                        if event.button == 1:  # Левая кнопка мыши
                            if not flagged[y][x]:
                                revealed[y][x] = True
                                if board[y][x] == 'M':
                                    game_over = True
                                elif board[y][x] == ' ':
                                    reveal_adjacent(board, revealed, x, y)
                        elif event.button == 3:  # Правая кнопка мыши
                            if not revealed[y][x]:
                                flagged[y][x] = not flagged[y][x]

        draw_timer(screen, time_elapsed, CELL_SIZE)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
