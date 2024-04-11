import pygame
import numpy as np

# Pygame configuration
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)  # Color for the grid

def rule30(left, center, right):
    return left ^ (center or right)

def draw_cells(screen, cells):
    for y, row in enumerate(cells):
        for x, cell in enumerate(row):
            color = WHITE if cell else BLACK
            pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the grid
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    cells = np.zeros((HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE), dtype=np.int8)
    next_cells = np.zeros_like(cells)

    running = True
    evolve = False
    current_row = 0  # Keep track of the current row
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                cells[current_row, x // CELL_SIZE] = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    evolve = not evolve

        screen.fill(BLACK)
        draw_cells(screen, cells)

        if evolve and current_row < HEIGHT // CELL_SIZE - 1:
            for x in range(1, WIDTH // CELL_SIZE - 1):
                next_cells[current_row + 1, x] = rule30(cells[current_row, x-1], cells[current_row, x], cells[current_row, x+1])
            cells, next_cells = next_cells, cells
            current_row += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()