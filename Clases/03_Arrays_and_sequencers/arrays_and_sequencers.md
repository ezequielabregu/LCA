# Arrays and sequencers

**EN CONSTRUCCIÓN!**

**Secuenciador por pasos (Step Sequencer)**: es una herramienta para organizar y controlar la reproducción de eventos en una secuencia temporalmente ordenada. Esta secuencia se compone de una serie de pasos discretos, donde cada paso representa un intervalo de tiempo regular y puede contener información sobre la activación o desactivación de eventos.
Además de controlar eventos musicales como notas, acordes y percusiones, un step sequencer puede también gestionar una variedad de otros eventos. Esto incluye cambios de parámetros en instrumentos virtuales o sintetizadores de video o audio, automatización de efectos en tiempo real, control de iluminación en actuaciones en vivo o instalaciones multimedia, activación de muestras de para crear patrones y secuencias de efectos, así como el disparo de eventos de control MIDI para controlar hardware o software externo.

&nbsp;

| P1  | P2  | P3  | P4  | P5  | P6  | P7  | P8  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| x   | x   | x   | x   | x   | x   | x   | x   |

- Cada celda representa un paso en el secuenciador.
- "P1" a "P8" indican los pasos numerados del 1 al 8.
- Las celdas vacías representan los pasos sin - eventos o notas.
- Puedes llenar cada celda con notas o eventos para representar la secuencia deseada.

&nbsp;

## Definición del problema

Representar mediante pseudo código un secuenciador de 8 pasos (step sequencer)

&nbsp;

### Formulación 1 (pseudo código)

```text
1. Definir una estructura de datos para representar cada paso de la secuencia (por ejemplo, array, lista).
2. Definir un arreglo para contener los valores de las notas MIDI para cada paso.
3. Inicializar los parámetros del secuenciador:
   - Paso actual = 0
   - Tempo
   - Número de pasos = 8
4. Iniciar un bucle para reproducir continuamente la secuencia:
   a. Calcular la duración de tiempo para cada paso basado en el tempo.
   b. Reproducir la nota MIDI correspondiente al paso actual.
   c. Incrementar el paso actual.
   d. Si el paso actual excede el número de pasos, reiniciarlo a 0.
   e. Esperar la duración calculada antes de pasar al siguiente paso.
5. Permitir la entrada del usuario para cambiar el tempo o las notas MIDI durante la ejecución, si se desea.
```

&nbsp;

### Formulación 2 (pseudo código)

```text
Estructuras de Datos:
- Definir una estructura de datos para representar cada paso de la secuencia (por ejemplo, array, lista).

Variables:
- Definir un arreglo para almacenar los valores de notas MIDI para cada paso.
- Inicializar los parámetros del secuenciador:
  - PasoActual = 0
  - Tempo
  - NúmeroDePasos = 8

Algoritmo:
1. Inicialización:
   a. Establecer PasoActual a 0.
   b. Solicitar al usuario que ingrese el Tempo.
   c. Establecer NúmeroDePasos en 8.

2. Bucle:
   a. Mientras verdadero:
      i. Calcular la duración de tiempo para cada paso basado en el Tempo.
      ii. Reproducir la nota MIDI correspondiente al PasoActual.
      iii. Incrementar PasoActual.
      iv. Si PasoActual excede NúmeroDePasos, restablecerlo a 0.
      v. Esperar la duración calculada antes de pasar al siguiente paso.

3. Manejar la Entrada del Usuario:
   a. Continuamente verificar la entrada del usuario.
   b. Si el usuario ingresa Tempo o notas MIDI:
      i. Actualizar las variables correspondientes en consecuencia.
      ii. Reiniciar el bucle del secuenciador con los parámetros actualizados.
```

&nbsp;

## Implementación en Python

```python
import time
import mido

# 1. Define una estructura de datos para representar cada paso de la secuencia (8 pasos)
secuencia = [None] * 8

# 2. Define un arreglo para almacenar los valores de notas MIDI para cada paso
notas_midi = [60, 62, 64, 65, 67, 69, 71, 72]  # Escala de Do mayor

# 3. Inicializa los parámetros del secuenciador
paso_actual = 0
tempo = 120  # pulsos por minuto
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
    paso_actual += 1


    # d. Si el paso actual excede el número de pasos, restablécelo a 0
    if paso_actual >= num_pasos:
        paso_actual = 0

    # e. Espera la duración calculada antes de pasar al siguiente paso
    time.sleep(duracion_paso)

    # Apaga la nota MIDI
    mensaje = mido.Message('note_off', note=nota_actual)
    puerto_salida.send(mensaje)
```

&nbsp;

### Implementación Random Step Sequencer

```python
import time
import mido
import random

# 1. Define una estructura de datos para representar cada paso de la secuencia (8 pasos)
secuencia = [None] * 8

# 2. Define un arreglo para almacenar los valores de notas MIDI para cada paso
notas_midi = [60, 62, 64, 65, 67, 69, 71, 72]  # Escala de Do mayor

# 3. Inicializa los parámetros del secuenciador
paso_actual = random.randint(0, 7)
tempo = 120  # pulsos por minuto
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
```

### Piano Phases

(Steve Reich)


```python
import time
import mido

# Define una secuencia de notas MIDI para representar la parte musical
notas_midi = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]  # Escala de Do mayor

# Abre dos puertos de salida MIDI
puerto_salida1 = mido.open_output('IAC Driver Bus 1')
puerto_salida2 = mido.open_output('IAC Driver Bus 2')

# Inicializa los parámetros del secuenciador
tempo = int(120 * 8)  # pulsos por minuto
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
    puerto_salida1.send(mensaje_off)

    puerto_salida2.send(mensaje_on)
    time.sleep(duracion_paso * 0.99)  # El segundo instrumento toca ligeramente más rápido
    puerto_salida2.send(mensaje_off)

    # Incrementa el paso actual
    paso_actual += 1
    if paso_actual >= len(notas_midi):
        paso_actual = 0
```

&nbsp;

