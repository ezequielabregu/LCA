import pygame
import time
import numpy as np
import mido

# MIDI Configuration
OUTPUT_PORT_NAME = "IAC Driver Bus 1"

# Tempo Variables
BPM = 120 * 6  # Beats per minute
TEMPO_MULTIPLIER = 60.0 / BPM

# Game of Life Variables
GRID_WIDTH = 40
GRID_HEIGHT = 30
CELL_SIZE = 20

# Colors
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)
CURSOR_COLOR = (255, 0, 0)

def generate_midi_notes(active_cells, midi_port, active_notes):
    lowest_note = 36  # Adjust the lowest MIDI note here
    channel = 1
    velocity = 64

    # Turn off notes from the previous step
    for note in active_notes:
        note_off_msg = mido.Message('note_off', note=note, velocity=velocity, channel=channel)
        midi_port.send(note_off_msg)

    # Update the list of active notes
    active_notes = [lowest_note + GRID_HEIGHT - 1 - step for step in active_cells]

    # Turn on new notes
    for note in active_notes:
        note_on_msg = mido.Message('note_on', note=note, velocity=velocity, channel=channel)
        midi_port.send(note_on_msg)

    return active_notes

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1 : row + 2, col - 1 : col + 2]) - cells[row, col]
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

def draw_cells(screen, cells, size):
    for row, col in np.ndindex(cells.shape):
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("MIDI Step Sequencer")

    cells = np.zeros((GRID_HEIGHT, GRID_WIDTH))
    screen.fill(COLOR_GRID)
    update(screen, cells, CELL_SIZE)

    pygame.display.flip()
    pygame.display.update()

    running = False
    step = 0
    generate_life = True  # Flag to generate new Game of Life when cursor returns to start

    midi_port = mido.open_output(OUTPUT_PORT_NAME)
    if midi_port is None:
        print("Error: MIDI output port not found.")
        return

    active_notes = []  # Add this line before the main loop
    previous_step = []

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            if step == 0 and generate_life:
                cells = update(screen, cells, CELL_SIZE, with_progress=True)
                generate_life = False
            draw_cells(screen, cells, CELL_SIZE)
            pygame.draw.rect(screen, CURSOR_COLOR, (step * CELL_SIZE, 0, CELL_SIZE - 1, CELL_SIZE - 1))
            pygame.display.update()

            # MIDI Note generation and sending
            active_cells = [i for i, row in enumerate(cells[:, step]) if row == 1]
            active_notes = generate_midi_notes(active_cells, midi_port, active_notes)

            step = (step + 1) % GRID_WIDTH

            if step == 0:
                generate_life = True

            time.sleep(TEMPO_MULTIPLIER)

    midi_port.close()

if __name__ == "__main__":
    main()
