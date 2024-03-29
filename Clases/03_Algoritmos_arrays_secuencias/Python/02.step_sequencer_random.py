import time
import mido
import random

# 1. Define una estructura de datos para representar cada paso de la secuencia (8 pasos)
secuencia = [None] * 8

# 2. Define un arreglo para almacenar los valores de notas MIDI para cada paso
notas_midi = [60, 62, 64, 65, 67, 69, 71, 72]  # Escala de Do mayor

# 3. Inicializa los parámetros del secuenciador
paso_actual = random.randint(0, 7)
tempo = 960  # pulsos por minuto
num_pasos = len(secuencia)

# Abre el puerto MIDI virtual (utilizar el nombre correcto del puerto, ver MIDI_port_name.py)
puerto_salida = mido.open_output('IAC Driver Bus 1')

# 4. Inicia un bucle para reproducir continuamente la secuencia
while True:
    # a. Calcula la duración de tiempo para cada paso basado en el tempo
    duracion_paso = 60.0 / tempo  # duración de un pulso en segundos

    # b. "Reproduce" la nota MIDI correspondiente al paso actual
    nota_actual = int(notas_midi[paso_actual])  # Asegúrate de que es un entero
    secuencia[paso_actual] = nota_actual
    print(f"Step: {paso_actual} --- Note: {secuencia[paso_actual]}")

    # Envía el mensaje MIDI
    mensaje = mido.Message('note_on', note=nota_actual)
    puerto_salida.send(mensaje)

    # c. Incrementa el paso actual
    paso_actual = random.randint(0, 7)


    # d. Si el paso actual excede el número de pasos, restablécelo a 0
    if paso_actual >= num_pasos:
        paso_actual = 0

    # e. Espera la duración calculada antes de pasar al siguiente paso
    time.sleep(duracion_paso)

    # Apaga la nota MIDI
    mensaje = mido.Message('note_off', note=nota_actual)
    puerto_salida.send(mensaje)