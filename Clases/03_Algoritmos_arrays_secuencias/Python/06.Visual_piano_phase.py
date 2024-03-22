import time
import mido
import threading
import pygame
import queue
import numpy as np

# Define una secuencia de notas MIDI para representar la parte musical
notas_midi = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]  # Escala de Do mayor

# Abre dos puertos de salida MIDI
puerto_salida1 = mido.open_output('IAC Driver Bus 1')
puerto_salida2 = mido.open_output('IAC Driver Bus 2')

# Inicializa los parámetros del secuenciador
tempo = 120 * 4  # pulsos por minuto
duracion_paso = 60.0 / tempo  # duración de un pulso en segundos

# Create queues to store the notes
notes1 = queue.Queue()
notes2 = queue.Queue()

# Define a function to send MIDI messages
def send_midi_message(port, sleep_time, notes_queue):
    paso_actual = 0
    while True:
        # "Reproduce" la nota MIDI correspondiente al paso actual
        nota_actual = notas_midi[paso_actual]
        mensaje_on = mido.Message('note_on', note=nota_actual)
        port.send(mensaje_on)
        notes_queue.put(nota_actual)  # Store the note
        time.sleep(sleep_time)
        port.send(mido.Message('note_off', note=mensaje_on.note))  # Sends the 'note_off' message

        # Incrementa el paso actual
        paso_actual += 1
        if paso_actual >= len(notas_midi):
            paso_actual = 0

# Create and start threads for each MIDI message
threading.Thread(target=send_midi_message, args=(puerto_salida1, duracion_paso, notes1)).start()
threading.Thread(target=send_midi_message, args=(puerto_salida2, duracion_paso * 0.99, notes2)).start()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create lists to store the past positions
past_positions1 = []
past_positions2 = []

# Main Pygame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    # Calculate the angle based on the current time
    theta = 2 * np.pi * (time.time() % 1)

    # Get the most recent note from each queue
    if not notes1.empty():
        note1 = notes1.get()
        x1 = 400 + note1 * 3 * np.cos(theta)  # Increase the radius
        y1 = 300 + note1 * 3 * np.sin(theta)  # Increase the radius
        past_positions1.append((int(x1), int(y1)))

    if not notes2.empty():
        note2 = notes2.get()
        x2 = 400 + note2 * 3 * np.cos(theta)  # Increase the radius
        y2 = 300 + note2 * 3 * np.sin(theta)  # Increase the radius
        past_positions2.append((int(x2), int(y2)))

    # Draw lines between the past positions to form the curves
    for i in range(1, len(past_positions1)):
        pygame.draw.line(screen, (0, 0, 255), past_positions1[i-1], (past_positions1[i-1][0], past_positions1[i][1]), 2)
        pygame.draw.line(screen, (0, 0, 255), (past_positions1[i-1][0], past_positions1[i][1]), past_positions1[i], 2)

    for i in range(1, len(past_positions2)):
        pygame.draw.line(screen, (255, 0, 0), past_positions2[i-1], (past_positions2[i-1][0], past_positions2[i][1]), 2)
        pygame.draw.line(screen, (255, 0, 0), (past_positions2[i-1][0], past_positions2[i][1]), past_positions2[i], 2)

    pygame.display.flip()
    clock.tick(60)