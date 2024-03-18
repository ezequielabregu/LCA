import time
import mido

# Define una secuencia de notas MIDI para representar la parte musical
notas_midi = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]  # Escala de Do mayor

# Abre dos puertos de salida MIDI
puerto_salida1 = mido.open_output('IAC Driver Bus 1')

# Inicializa los parámetros del secuenciador
tempo = int(120 * 4)  # pulsos por minuto
duracion_paso = 60.0 / tempo  # duración de un pulso en segundos

# Inicia un bucle para reproducir continuamente la secuencia
# Inicia un bucle para reproducir continuamente la secuencia
paso_actual = 0
while True:
    # "Reproduce" la nota MIDI correspondiente al paso actual en ambos instrumentos
    nota_actual = notas_midi[paso_actual]
    mensaje_on = mido.Message('note_on', note=nota_actual)
    mensaje_off = mido.Message('note_off', note=nota_actual)

    puerto_salida1.send(mensaje_on)
    time.sleep(duracion_paso)  # Espera la duración de un pulso antes de pasar al siguiente paso
    puerto_salida1.send(mensaje_off)  # Envía el mensaje 'note_off'

    # Incrementa el paso actual
    paso_actual += 1
    if paso_actual >= len(notas_midi):
        paso_actual = 0