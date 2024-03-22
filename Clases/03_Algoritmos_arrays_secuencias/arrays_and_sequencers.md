# Algoritmos, arrays y secuenciadores

[**<-- VOLVER AL INICIO**](/README.md)

**EN CONSTRUCCIÓN!**

[![A simple Tango dance sequence](http://img.youtube.com/vi/AsPhnlXehBk/0.jpg)](http://www.youtube.com/watch?v=AsPhnlXehBk)

[![A simple Flamenco dance sequence](http://img.youtube.com/vi/dvkBqfAXo2Q&ab/0.jpg)](http://www.youtube.com/watch?v=dvkBqfAXo2Q&ab)

**Secuenciador (Sequencer)**: es una herramienta para organizar y controlar la reproducción de `eventos` en una secuencia temporalmente ordenada. Esta secuencia se compone de una serie de pasos discretos, donde cada paso representa un intervalo de tiempo regular y puede contener información sobre la activación o desactivación de eventos.

Además de controlar eventos musicales como notas, acordes y percusiones, un step sequencer puede también gestionar una variedad de otros eventos. Esto incluye cambios de parámetros en instrumentos virtuales o sintetizadores de video o audio, automatización de efectos en tiempo real, control de iluminación en actuaciones en vivo o instalaciones multimedia, activación de muestras de para crear patrones y secuencias de efectos, así como el disparo de eventos de control MIDI para controlar hardware o software externo.

&nbsp;

| P1  | P2  | P3  | P4  | P5  | P6  | P7  | P8  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| x   | x   | x   | x   | x   | x   | x   | x   |
| i0   | i1   | i2   | i3   | i4   | i5   | i6   | i7   |

- Cada celda representa un paso en el secuenciador.
- "P1" a "P8" indican los pasos numerados del 1 al 8.
- Las celdas vacías representan los pasos sin - eventos o notas.
- Puedes llenar cada celda con notas o eventos para representar la secuencia deseada.

&nbsp;

## Ejercicio 1

*Representar mediante pseudo código un secuenciador de 8 pasos (step sequencer)*

&nbsp;

### Formulación (pseudo código)

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
   a. Establecer Paso Actual a 0.
   b. Solicitar al usuario que ingrese el Tempo.
   c. Establecer NúmeroDePasos en 8.

2. Bucle:
   a. Mientras verdadero:
      i. Calcular la duración de tiempo para cada paso basado en el Tempo.
      ii. Reproducir la nota MIDI correspondiente al PasoActual.
      iii. Incrementar Paso Actual.
      iv. Si Paso Actual excede NúmeroDePasos, restablecerlo a 0.
      v. Esperar la duración calculada antes de pasar al siguiente paso.
```

&nbsp;

## Implementación en Python del secuenciador de 8 pasos

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

Es un simple secuenciador de pasos MIDI. Utiliza la biblioteca `mido` para enviar mensajes MIDI y la biblioteca `time` para controlar el tiempo de la secuencia.

El script comienza importando las bibliotecas necesarias y definiendo algunas estructuras de datos y variables iniciales. La lista `secuencia` contendrá la secuencia de notas a ser tocadas, y se llena inicialmente con valores `None`. La lista `notas_midi` contiene los valores de nota MIDI para cada paso en la secuencia, representando una escala de Do Mayor.

Luego, el script inicializa algunos parámetros para el secuenciador. La variable `paso_actual` lleva el seguimiento del paso actual en la secuencia, `tempo` establece el tempo en pulsos por minuto, y `num_pasos` almacena el número total de pasos en la secuencia.

El script abre un puerto de salida MIDI virtual utilizando `mido.open_output()`. Es posible que necesite cambiar el nombre del puerto, 'IAC Driver Bus 1', dependiendo de la configuración de su sistema.

La parte principal del script es un bucle `while` que reproduce continuamente la secuencia. Para cada paso, calcula la duración del paso en función del tempo, reproduce la nota MIDI correspondiente, incrementa el paso actual y luego espera la duración calculada antes de pasar al siguiente paso. Si el paso actual supera el número de pasos en la secuencia, reinicia el paso actual a 0. Después de que se toca cada nota, se envía un mensaje MIDI 'note_off' para detener la reproducción de la nota.



&nbsp;

## Ejercicio 2

*Representar mediante pseudo código un secuenciador random*

&nbsp;

## Implementación Random Step Sequencer

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

Este script de Python es una versión modificada del secuenciador paso a paso de MIDI del ejemplo anterior. La principal diferencia está en cómo se incrementa el paso actual (`paso_actual`).

En el script original, el paso actual se incrementaba secuencialmente, creando un patrón predecible de notas. En esta versión modificada, el paso actual se establece como un número entero aleatorio entre 0 y 7, inclusive. Esto significa que la secuencia de notas se reproducirá en un orden aleatorio, creando un patrón más impredecible.

&nbsp;

## Piano Phase

(Steve Reich)

![](https://payload.cargocollective.com/1/2/82587/8130024/reich_gif_432x432_b_crop_pixel_fixed.gif)

[Ver Partitura Piano Phase (S. Reich)](./Biblio%20/SteveReich-PianoPhase.pdf)

Piano Phase, puede concebirse como un algoritmo. Comenzando con dos pianos que tocan la misma secuencia de notas a la misma velocidad, uno de los pianistas comienza a acelerar gradualmente su tempo. 

Cuando la separación entre las notas interpretadas por los dos pianos alcanza una fracción de la duración de una nota, la fase se ha invertido y el ciclo se repite. Este proceso se repite continuamente, creando un efecto hipnótico de desfasamiento rítmico que evoluciona a lo largo del tiempo, sin fin, como una secuencia infinita de iteraciones.

![Phase Difference](https://www.nist.gov/sites/default/files/images/2022/01/27/phase-difference.gif)

[![Piano Phase Visualization](http://img.youtube.com/vi/Jqoieg0Vqag&t/0.jpg)](http://www.youtube.com/watch?v=Jqoieg0Vqag&t)

&nbsp;

### Ejercicio 3

*Describe en forma de algoritmo el proceso de Piano Phase. Utiliza pseudocódigo para representar el algoritmo.*

&nbsp;

#### Formulación del algoritmo (pseudo código)

```text

1. Inicializar dos pianistas con la misma secuencia de notas.
2. Establecer una velocidad de tempo inicial para ambos pianistas.
3. Repetir hasta que se alcance la fase deseada:
     a. Aumentar gradualmente la velocidad del tempo del segundo pianista.
     b. Comparar la posición de las notas entre ambos pianistas.
     c. Cuando la separación entre las notas de los pianistas alcance una fracción de la duración de una nota, invertir la fase.
     d. Continuar el proceso de reproducción.
4. Repetir el ciclo indefinidamente para crear un efecto de desfasamiento rítmico continuo y evolutivo.
```

### Implementación en Python de Piano Phase (1 solo sequencer)


```python
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
```

---

[**<-- VOLVER AL INICIO**](/README.md)