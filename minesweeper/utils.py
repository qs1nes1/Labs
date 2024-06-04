# utils.py
import random
import pygame
from constants import mine_image, flag_image, mine_clicked_image, misflagged_image, blank_image, open_images, timer_images

def create_board(size, mines):
    board = [[' ' for _ in range(size[0])] for _ in range(size[1])]
    for _ in range(mines):
        x, y = random.randint(0, size[0] - 1), random.randint(0, size[1] - 1)
        while board[y][x] == 'M':
            x, y = random.randint(0, size[0] - 1), random.randint(0, size[1] - 1)
        board[y][x] = 'M'
        for i in range(max(0, x - 1), min(size[0], x + 2)):
            for j in range(max(0, y - 1), min(size[1], y + 2)):
                if board[j][i] != 'M':
                    if board[j][i] == ' ':
                        board[j][i] = 1
                    else:
                        board[j][i] += 1
    return board

def draw_board(board, revealed, flagged, screen, cell_size, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * cell_size, (y + 1) * cell_size, cell_size, cell_size)  # Смещаем вниз на один ряд для таймера
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if revealed[y][x]:
                if cell == 'M':
                    screen.blit(mine_image, rect.topleft)
                else:
                    screen.blit(open_images[cell if cell != ' ' else 0], rect.topleft)
            else:
                if flagged[y][x]:
                    screen.blit(flag_image, rect.topleft)
                else:
                    screen.blit(blank_image, rect.topleft)

def display_message(message, screen, font, screen_width, screen_height):
    BLACK = (0, 0, 0)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  # Ждем 1 секунду

def check_win(board, revealed):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 'M' and not revealed[row][col]:
                return False
    return True

def draw_timer(screen, time_elapsed, cell_size):
    digits = [int(d) for d in str(time_elapsed).zfill(3)]
    for i, digit in enumerate(digits):
        screen.blit(timer_images[digit], (i * cell_size, 0))  # Размещаем таймер сверху экрана

def reveal_adjacent(board, revealed, x, y):
    if board[y][x] != ' ':
        return
    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and not revealed[ny][nx]:
                    revealed[ny][nx] = True
                    if board[ny][nx] == ' ':
                        queue.append((nx, ny))
