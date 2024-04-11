import time
import pygame
import numpy as np

from pythonosc import udp_client

# OSC Configuration
#Reference in https://gitlab.com/ayrsd/audiostellar/-/blob/units/OSC_Documentation.md
OSC_IP = "127.0.0.1"
OSC_PORT = 8000  # Replace with the port AudioStellar is listening on

COLOR_BG = (10, 10, 10,)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("conway's game of life")

def send_osc_messages(cells, osc_client):
    rows, cols = cells.shape
    for i in range(rows):
        for j in range(cols):
            if cells[i, j] == 1:
                x = j / cols
                y = i / rows
                osc_client.send_message("/GOL/play/xy", [x, y]) #Add "GOL" to OSC Address 1

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    osc_client = udp_client.SimpleUDPClient(OSC_IP, OSC_PORT)

    running = False

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            send_osc_messages(cells, osc_client)
            pygame.display.update()

        time.sleep(0.1)


if __name__ == "__main__":
    main()

