import time
import mido
import threading

# Define una secuencia de notas MIDI para representar la parte musical
#notas_midi = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]
notas_midi = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]  

# Abre dos puertos de salida MIDI
puerto_salida1 = mido.open_output('IAC Driver Bus 1')
puerto_salida2 = mido.open_output('IAC Driver Bus 2')

# Inicializa los parámetros del secuenciador
tempo = 120 * 4  # pulsos por minuto
duracion_paso = 60.0 / tempo  # duración de un pulso en segundos

# Define a function to send MIDI messages
def send_midi_message(port, sleep_time):
    paso_actual = 0
    while True:
        # "Reproduce" la nota MIDI correspondiente al paso actual
        nota_actual = notas_midi[paso_actual]
        mensaje_on = mido.Message('note_on', note=nota_actual)
        port.send(mensaje_on)
        time.sleep(sleep_time)
        port.send(mido.Message('note_off', note=mensaje_on.note))  # Sends the 'note_off' message

        # Incrementa el paso actual
        paso_actual += 1
        if paso_actual >= len(notas_midi):
            paso_actual = 0

# Create and start threads for each MIDI message
threading.Thread(target=send_midi_message, args=(puerto_salida1, duracion_paso)).start()
threading.Thread(target=send_midi_message, args=(puerto_salida2, duracion_paso * 0.99)).start()