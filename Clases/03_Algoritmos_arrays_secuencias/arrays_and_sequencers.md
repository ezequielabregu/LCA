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

---

## The Euclidean Algorithm Generates Traditional Musical Rhythms

Godfried Toussaint (2005)

[Link al artículo original](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)

#### Resumen

El algoritmo euclidiano (que nos llega de Los Elementos de Euclides) calcula el máximo común divisor de dos enteros dados. Se muestra aquí que la estructura del algoritmo euclidiano puede ser utilizada para generar, de manera muy eficiente, una gran variedad de ritmos utilizados como líneas de tiempo (ostinatos) en la música subsahariana en particular, y en la música mundial en general. Estos ritmos, aquí llamados ritmos euclidianos, tienen la propiedad de que sus patrones de inicio están distribuidos de la manera más uniforme posible. Los ritmos euclidianos también encuentran aplicación en aceleradores de física nuclear y en ciencias de la computación, y están estrechamente relacionados con varias familias de palabras y secuencias de interés en el estudio de la combinatoria de palabras, como las cadenas euclidianas, a las que se comparan los ritmos euclidianos.


### Hipótesis

Varios investigadores han observado que en los ritmos de la música tradicional del mundo hay una tendencia a encontrar patrones distribuidos lo más regular o uniformemente posible.

```text
Patrones de regularidad máxima se pueden describir mediante el uso del algoritmo de Euclides sobre el máximo común divisor de dos números enteros
```

### Patrones de regularidad máxima

x = nota

· = silencio

[×· ×· ×· ×· ] 	→ 	[1 0 1 0 1 0 1 0 ]
(8,4) = 4 notas distribuidas regularmente en los 8 pulsos 


[×· ·×· ·×·] 	→ 	[1 0 0 1 0 0 1 0 ]
(8,3) = 3 notas distribuidas regularmente en 8 pulsos

### Algoritmo de Euclides

Uno de los algoritmos más antiguos conocidos, descrito en Los Elementos de Euclides (alrededor del 300 a.C.) en la Proposición 2 del Libro VII, hoy conocido como el algoritmo euclidiano, calcula el máximo común divisor de dos enteros dados. La idea es muy simple. El número más pequeño se resta repetidamente del mayor hasta que el mayor sea cero o se vuelva más pequeño que el menor, en cuyo caso se llama el resto. Este resto luego se resta repetidamente del número más pequeño para obtener un nuevo resto. Este proceso continúa hasta que el resto es cero. Para ser más precisos, consideremos como ejemplo los números 5 y 8 como antes. Primero, 5 se divide en 8 una vez con un resto de 3. Luego, 3 se divide en 5 una vez con un resto de 2. Luego, 2 se divide en 3 una vez con un resto de 1. Finalmente, 2 se divide en 2 una vez con un resto de 0. Por lo tanto, el máximo común divisor es 1. Aunque el algoritmo original de Euclides usaba sustracción repetida de esta manera, la división estándar funcionará igual de bien, e incluso es más rápida. Los pasos de este proceso pueden resumirse mediante la siguiente secuencia de ecuaciones:

8 = (1)(5) + 3

5 = (1)(3) + 2

3 = (1)(2) + 1

2 = (1)(2) + 0

En concreto, consiste en hacer divisiones sucesivas para hallar el máximo común divisor de dos números positivos (m.c.d. de aquí en adelante).

El `m.c.d.` de dos números a y b, suponiendo que a > b, primero dividimos a entre b, y obtenemos el resto r de la división.

El m.c.d. de a y b es el mismo que el de b y r. 
Cuando dividimos a entre b, obtenemos un cociente c y un resto r de tal manera que se cumple que:

`a = c · b + r`

**Ejemplos:**

calculemos el máximo común de 17 y 7. 

Como `17 = 7 · 2 + 3`, entonces el m.c.d.(17, 7) es igual al m.c.d.(7, 3). De nuevo, como 7 = 3 · 2 + 1, entonces el m.c.d.(7, 3) es igual al m.c.d.(3, 1). 

Aquí es claro que el m.c.d. entre 3 y 1 es simplemente 1. Por tanto, el m.c.d entre 17 y 7 es 1 también.

m.c.d. (17,7) = 1

17 = 7 . 2 + 3

7 = 3 . 2 + 1

3 = 1 . 3 + 0

&nbsp;

**Otro ejemplo:**

m.c.d. (8,3) = 1

8 = 3 . 2 + 2

3 = 2 . 1 + 1

2 = 1 . 2 + 0


### ¿Cómo se transforma el cálculo del m.c.d. en patrones distribuidos con regularidad máxima?


Representar una secuencia binaria de k unos y n−k ceros, donde cada bit [0] representa un intervalo de tiempo y los unos [1] se envía una señal. 

El problema entonces se reduce a lo siguiente: 

construir una secuencia binaria de n bits con k unos tal que los k unos se distribuyan lo más uniformemente posible entre los n − k ceros.

Un caso simple es cuando k divide uniformemente n (sin resto), en cuyo caso debemos colocar unos cada n/k bits. 
Por ejemplo, si n = 16 y k = 4, entonces la solución es 

[1000100010001000]. 

Este caso corresponde a que n y k tienen un divisor común de k (en este caso 4). 

De manera más general, si el máximo común divisor entre n y k es g, esperaríamos que la solución se descomponga en g repeticiones de una secuencia de n/g bits.

**Esta conexión con los máximos comunes divisores sugiere que se podría calcular un ritmo de máxima uniformidad usando un algoritmo como el de Euclides.**

### Esta conexión con los máximos comunes divisores sugiere que se podría calcular un ritmo de máxima uniformidad usando un algoritmo como el de Euclides.

**1.** Alineamos el número de notas  y el número de silencios (7 unos y 10 ceros)

**2, 3 y 4.** Formamos grupos de 7, los cual corresponde a efectuar la división de 17 entre 7; obtenemos 7 grupos de formados por [1 0] y sobran 3 ceros, lo cual indica que en el paso siguiente formaremos grupos de 3 hasta que queden uno o cero grupos.

**5.** De nuevo, esto es equivalente a efectuar la división de 7 entre 3. En nuestro caso, queda un solo grupo y hemos terminado.

**4.** Finalmente, el ritmo se obtiene leyendo por columnas y de izquierda a derecha la agrupación obtenida, paso a paso.

### Implementación en PD - Euclidean sequencer

```text
(index * hits ) % steps
↓
[< notas]
```

donde:

índice = índice de la euclid serie (array)

hits = notas

steps = pulsos
