import pygame


class View:
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Minesweeper")
        self.font = pygame.font.SysFont('Arial', 25)
        self.cell_size = 30  # Размер ячейки
        self.update()

    def set_won(self):
        # Implement win state display in Pygame
        pass

    def set_lost(self):
        # Implement lose state display in Pygame
        pass

    def set_mines(self, mines):
        # Implement mines counter display in Pygame
        pass

    def draw_cell(self, cell):
        x = cell.x * self.cell_size
        y = cell.y * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

        if cell.state == 'closed':
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
        elif cell.state == 'opened':
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            if cell.int_state > 0:
                text = self.font.render(str(cell.int_state), True, (0, 0, 0))
                self.screen.blit(text, (x + 10, y + 5))
        elif cell.state == 'flagged':
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            pygame.draw.circle(self.screen, (255, 0, 0), rect.center, self.cell_size // 4)

        pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Граница ячейки

    def update(self):
        self.screen.fill((255, 255, 255))
        for row in self.model.field:
            for cell in row:
                self.draw_cell(cell)
        pygame.display.flip()


# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                x, y = event.pos
                controller.left_click(x // view.cell_size, y // view.cell_size)
            elif event.button == 3:  # Right click
                x, y = event.pos
                controller.right_click(x // view.cell_size, y // view.cell_size)

    view.update()
    clock.tick(30)

pygame.quit()
