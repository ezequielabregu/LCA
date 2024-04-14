# Autómatas Celulares

[**<-- VOLVER AL INICIO**](/README.md)

# Autómatas Celulares

![Autómata Celular](https://mathworld.wolfram.com/images/eps-svg/Code0912_450.svg)

Un autómata celular es un modelo matemático y computacional para un sistema dinámico que evoluciona en pasos discretos. Es adecuado para modelar sistemas naturales que puedan ser descritos como una colección masiva de objetos simples que interactúen localmente unos con otros.

Un autómata celular es una colección de células "coloreadas" en una cuadrícula de forma especificada que evoluciona a través de una serie de pasos discretos en el tiempo según un conjunto de reglas basadas en los estados de las células vecinas. Luego, las reglas se aplican iterativamente durante tantos pasos en el tiempo como se desee.

Los autómatas celulares vienen en una variedad de formas y variedades. Una de las propiedades más fundamentales de un autómata celular es el tipo de cuadrícula en la que se calcula. La cuadrícula más simple de este tipo es una línea `unidimensional`. En dos dimensiones, se pueden considerar cuadrículas cuadradas, triangulares y hexagonales.

También se debe especificar el número de colores (o estados distintos) k que puede asumir un autómata celular. Este número suele ser un entero, siendo k=2 (binario, `[1]` o `[0]`) la elección más simple. Para un autómata binario, el color 0 comúnmente se llama "blanco" y el color 1 comúnmente se llama "negro". Sin embargo, también se pueden considerar autómatas celulares con un rango continuo de valores posibles.

Además de la cuadrícula en la que vive un autómata celular y los colores que pueden asumir sus células, también se debe especificar el `vecindario` sobre el cual las células se afectan entre sí. 

## Autómatas celulares unidimensionales (AC1D)

La opción más simple es `"vecinos más cercanos"`, en la que solo las células directamente adyacentes a una célula dada pueden ser afectadas en cada paso en el tiempo. Dos vecindarios comunes en el caso de un autómata celular bidimensional en una cuadrícula cuadrada son el llamado vecindario de Moore (un vecindario cuadrado) y el vecindario de von Neumann (un vecindario en forma de diamante).

Los autómatas celulares se considera un vector. Cada componente del vector se va a llamar célula. Se supone que cada célula sólo puede tomar dos estados: 

- [0] (blanco) 

- [1] (negro).

Este tipo de autómata se conoce como autómatas celulares unidimensionales (1D)
elementales.
Se va a efectuar un proceso dinámico donde se partirá de una configuración
inicial C(0) de cada una de las células (etapa 0) y en cada nueva etapa se calculará el estado de cada célula de acuerdo al estado de las células vecinas y de la propia célula en la etapa anterior. 

### El caso de la Regla 30

La Regla 30 es un autómata celular binario unidimensional presentado por [Stephen Wolfram](https://es.wikipedia.org/wiki/Stephen_Wolfram) en 1983.
Se considera una matriz unidimensional infinita de células autómatas celulares con sólo dos estados, con cada célula en algún estado inicial. 

A intervalos de tiempo discretos, cada celda cambia de estado espontáneamente en función de su estado actual y el estado de sus dos vecinas.

En qué consiste:

1. Cada celda puede estar en dos estados: viva o muerta.

2. La siguiente generación de una célula se determina por el estado actual de la célula y el de las dos celdas vecinas.

3. Hay 8 posibles configuraciones de estados vecinos (3^2), y para cada una, la Regla 30 define si la célula vive o muere en la siguiente generación.


Para la Regla 30, el conjunto de reglas que gobierna el siguiente estado del autómata es:

| Configuración | Siguiente estado | Código en binario |
|---------------|------------------|-------------------|
| 000           | Muerta           | 000               |
| 001           | Viva             | 011               |
| 010           | Muerta           | 000               |
| 011           | Viva             | 011               |
| 100           | Viva             | 011               |
| 101           | Muerta           | 000               |
| 110           | Viva             | 011               |
| 111           | Muerta           | 000               |

En el siguiente gráfico la fila superior indica el estado de la célula central (la célula llamada i) y de sus dos células vecinas en una determinada etapa y, en la fila inferior, el estado de la célula central en la siguiente etapa.

Por ejemplo, en el primer caso de la figura: 

- si el estado de una célula en una determinada etapa es `[1]` (negro) y 

- si sus dos vecinas en esa misma etapa también están a `[1]` (negro)
  
- entonces el estado de la célula en la siguiente etapa será `[0]` (blanco).

![Rule 30](https://mathworld.wolfram.com/images/eps-svg/ElementaryCARule030_700.svg)
[Fuente](https://mathworld.wolfram.com/CellularAutomaton.html)

Se llama Regla 30 porque en binario, 00011110<sub>2</sub> = 30.

Vamos a desglosar el procedimiento para obtener el siguiente estado en las 8 combinaciones:

**Configuraciones de entrada:** Considera las 8 posibles combinaciones de entrada de las tres células (una célula central y sus dos vecinas izquierda y derecha). Como cada célula puede estar en uno de los dos estados posibles (0 o 1), las combinaciones son 000, 001, 010, 011, 100, 101, 110, y 111.

**Representación binaria de la regla:** La Regla 30 está representada por el número 30 en binario, que es 00011110. Esta representación binaria determina las reglas para el siguiente estado de la célula central en cada una de las 8 combinaciones posibles.

**Correspondencia de bits:** Los 8 bits de la representación binaria (00011110) corresponden a las 8 combinaciones de entrada en orden. De derecha a izquierda, los bits representan el siguiente estado de la célula central para cada combinación de entrada.

Por ejemplo, el bit menos significativo de 00011110 (el bit más a la derecha) es 0. Esto significa que cuando la combinación de entrada es 000, el siguiente estado de la célula central será 0.

**Determinación del siguiente estado:** Para cada combinación de entrada (por ejemplo, 000, 001, 010, 011, 100, 101, 110, 111), el bit correspondiente en la representación binaria de la Regla 30 [00011110] indica el siguiente estado de la célula central.

| Configuración de entrada | Siguiente estado |
|--------------------------|------------------|
| 000                      | 0                |
| 001                      | 1                |
| 010                      | 1                |
| 011                      | 1                |
| 100                      | 1                |
| 101                      | 0                |
| 110                      | 0                |
| 111                      | 0                |

Por ejemplo, si tienes la combinación de entrada 000 y el bit correspondiente en la Regla 30 es 0, el siguiente estado de la célula central será 0.

Por lo tanto, las reglas no son arbitrarias, sino que están determinadas por la representación binaria de la Regla 30, que especifica el siguiente estado de la célula central para cada combinación de entrada de sus vecinas.

### Implementación de la Regla 30 en Python

```python
import numpy as np
import matplotlib.pyplot as plt

def rule30(cells):
    """Applies Rule 30 to the input cells."""
    new_cells = np.zeros_like(cells)
    extended_cells = np.concatenate(([cells[-1]], cells, [cells[0]]))  # Apply periodic boundary conditions
    for i in range(1, len(extended_cells) - 1):
        neighborhood = extended_cells[i-1:i+2]
        if np.array_equal(neighborhood, [1, 1, 1]) or np.array_equal(neighborhood, [1, 1, 0]) or \
           np.array_equal(neighborhood, [1, 0, 1]) or np.array_equal(neighborhood, [0, 0, 0]):
            new_cells[i-1] = 0
        else:
            new_cells[i-1] = 1
    return new_cells

def main():
    # Initialize the cells
    cells = np.zeros(100)
    cells[50] = 1  # Start with one cell in the middle

    # Apply Rule 30 for 100 steps
    history = [cells]
    for i in range(100):
        cells = rule30(cells)
        history.append(cells)

    # Display the history as an image
    plt.imshow(history, cmap='binary')
    plt.show()

if __name__ == "__main__":
    main()
```
Este script de Python utiliza las bibliotecas numpy y matplotlib para simular y visualizar la evolución de un autómata celular usando la Regla 30.

La función `rule30` es el núcleo de este script. Toma una matriz unidimensional de celdas como entrada, donde cada celda es 0 o 1. La función primero crea una nueva matriz `new_cells` con la misma forma que la entrada, pero rellena con ceros. Luego, extiende la matriz de entrada en ambos extremos para aplicar condiciones de contorno periódicas, lo que significa que la primera celda se considera vecina de la última celda y viceversa.

Luego, la función itera sobre cada celda en la matriz extendida (excluyendo las celdas de contorno añadidas). Para cada celda, considera la celda y sus dos vecinas como un vecindario. Si el vecindario coincide con uno de los cuatro patrones específicos ([1, 1, 1], [1, 1, 0], [1, 0, 1], o [0, 0, 0]), la celda correspondiente en `new_cells` se establece en 0. De lo contrario, se establece en 1. Esta es la implementación de la Regla 30. Finalmente, la función devuelve la nueva matriz de celdas.

La función principal inicializa una matriz unidimensional de 100 celdas, todas establecidas en 0 excepto la celda en el medio, que se establece en 1. Luego, aplica la función `rule30` a esta matriz 100 veces, almacenando cada matriz resultante en una lista llamada `history`. Esta lista luego se visualiza como una imagen binaria usando la función `imshow` de matplotlib, donde cada fila corresponde a un paso en la evolución del autómata celular.

El script está diseñado para ejecutarse como un programa independiente. La línea `if __name__ == "__main__":` asegura que la función principal se llame solo cuando el script se ejecuta directamente, no cuando se importa como un módulo.


## Autómatas celulares bidimensionales (AC2D)

Los autómatas celulares bidimensionales son una extensión de los autómatas celulares unidimensionales, donde las células no solo tienen vecinos a su izquierda y derecha, sino también arriba y abajo. Esto permite modelar sistemas más complejos y ricos en estructura, como fenómenos en dos dimensiones, como la propagación de ondas, patrones de crecimiento en biología, propagación de fuego, simulación de fluidos, entre otros.

Los autómatas celulares bidimensionales (AC2D) son modelos computacionales que simulan sistemas dinámicos en una cuadrícula bidimensional.

Se componen de:

1. *Celdas*: Cada celda en la cuadrícula puede tener un estado finito, como vivo o muerto, y puede cambiar de estado según las reglas del autómata.

2. *Vecindad*: Cada celda tiene una vecindad, que es un conjunto de celdas adyacentes que influyen en su estado. La vecindad puede ser rectangular, hexagonal, circular o de cualquier otra forma.

3. *Regla de transición*: La regla de transición define cómo cambia el estado de una celda en función de su estado actual y el estado de las celdas en su vecindad. La regla puede ser determinista o probabilística.

4. *Evolución*: El autómata celular evoluciona a través de iteraciones. En cada iteración, el estado de cada celda se actualiza de acuerdo con la regla de transición.

## Caso de estudio: Conway's Game of Life

![Game of life](https://images.squarespace-cdn.com/content/v1/59413d96e6f2e1c6837c7ecd/1592233649594-7UQA8NZSNXMZWX86FIWN/JB_Game_of_Life.gif?format=2500w)

[Fuente](https://www.artnome.com/news/2020/7/12/the-game-of-life-emergence-in-generative-art)

El Juego de la Vida de Conway, también conocido simplemente como el Juego de la Vida, es un autómata celular ideado por el matemático británico John Horton Conway en 1970. Es el ejemplo más conocido de un autómata celular.

El "juego" es en realidad un juego de cero jugadores, lo que significa que su evolución está determinada por su estado inicial, sin necesidad de entrada de los jugadores humanos. Uno interactúa con el Juego de la Vida creando una configuración inicial y observando cómo evoluciona.

[Ver Artículo Original - MATHEMATICAL GAMES - The fantastic combinations of John Conway's new solitaire game life (Martin Gardner) ](https://ballyalley.com/articles_and_news/LIFE_Article_(Scientific_American)(October_1970).pdf)

`GOL` (Game of Life) y `CGOL` (Conway's Game of Life) son acrónimos comúnmente utilizados.

[![Game of Life](https://img.youtube.com/vi/xP5-iIeKXE8/0.jpg)](https://www.youtube.com/watch?v=xP5-iIeKXE8)

[Fuente](https://www.youtube.com/watch?v=xP5-iIeKXE8)

## Reglas

El universo del Juego de la Vida es una cuadrícula ortogonal bidimensional infinita de celdas cuadradas, cada una de las cuales (en un momento dado) se encuentra en uno de dos estados posibles, `viva` (alternativamente "encendida") o `muerta` (alternativamente "apagada"). En cada paso en el tiempo, ocurren las siguientes transiciones:

**Las cuatro reglas del Juego de la Vida de Conway:**

**1. Sobrepoblación**: Cualquier célula viva con más de tres vecinos vivos muere por sobrepoblación.

**2. Subpoblación**: Cualquier célula viva con menos de dos vecinos vivos muere por subpoblación.

**3. Estabilidad**: Cualquier célula viva con dos o tres vecinos vivos permanece viva en la siguiente generación. 

**4. Reproducción**: Cualquier célula muerta con exactamente tres vecinos vivos se convierte en una célula viva.

&nbsp;

También podemos resumir las reglas en una tabla:

| Regla          | Descripción                    | Estado actual | Vecinos vivos | Estado siguiente |
| -------------- | ------------------------------ | ------------- | ------------- | ---------------- |
| Sobrepoblación | Muerte por exceso de población | Viva          | Más de 3      | Muerta           |
| Subpoblación   | Muerte por aislamiento         | Viva          | Menos de 2    | Muerta           |
| Estabilidad    | Supervivencia                  | Viva          | 2 o 3         | Viva             |
| Reproducción   | Nacimiento                     | Muerta        | 3             | Viva             |

&nbsp;

o podemos resumirlo de la siguiente manera:

0 &rarr; 3 vecinos vivos &rarr; 1

1 &rarr; < 2 o > 3 vecinos vivos &rarr; 0

en donde 0 representa una célula muerta y 1 una célula viva.

&nbsp;

![Game of life rules](https://the-mvm.github.io/assets/img/posts/20210210/GameOfLife.gif)

[Fuente](https://the-mvm.github.io/conways-game-of-life.html)

&nbsp;

![Game of life rules](https://d2r55xnwy6nx47.cloudfront.net/uploads/2024/01/TheRulesOfLifebyMerrillSherman_560-Desktop.svg)

[Fuente](https://www.quantamagazine.org/maths-game-of-life-reveals-long-sought-repeating-patterns-20240118/)

El patrón inicial constituye la 'semilla' (seed) del sistema. La primera generación se crea aplicando las reglas anteriores simultáneamente a cada celda en la semilla; los nacimientos y las muertes ocurren simultáneamente, y el momento discreto en que esto ocurre se llama a veces un paso. (En otras palabras, cada generación es una función pura de la generación anterior). Las reglas continúan aplicándose repetidamente para crear más generaciones.

## Orígenes

Conway estaba interesado en un problema presentado en la década de 1940 por el renombrado matemático John von Neumann, quien intentaba encontrar una máquina hipotética que pudiera construir copias de sí misma y tuvo éxito cuando encontró un modelo matemático para tal máquina con reglas muy complicadas en una cuadrícula rectangular. El Juego de la Vida surgió como el intento exitoso de Conway de simplificar las ideas de von Neumann.

El juego hizo su primera aparición pública en el número de octubre de 1970 de Scientific American, en la columna "Juegos Matemáticos" de Martin Gardner, bajo el título de "Las combinaciones fantásticas del nuevo juego de solitario de John Conway 'vida'".

Desde su publicación, el Juego de la Vida de Conway ha atraído mucho interés debido a las formas sorprendentes en que los patrones pueden evolucionar. 

La vida es un ejemplo de emergencia y autoorganización. Es interesante para físicos, biólogos, economistas, matemáticos, filósofos, científicos generativos y otros observar la manera en que los patrones complejos pueden surgir de la implementación de reglas muy simples. El juego también puede servir como una analogía didáctica, utilizada para transmitir la noción algo contraintuitiva de que "diseño" y "organización" pueden surgir espontáneamente en ausencia de un diseñador.

Conway eligió sus reglas cuidadosamente, después de una considerable experimentación, para cumplir con tres criterios:

1. No debe haber ningún patrón inicial para el cual exista una prueba simple de que la población pueda crecer sin límites.
2. Debe haber patrones iniciales que aparentemente crezcan sin límites.
3. Deben haber patrones iniciales simples que crezcan y cambien durante un período considerable de tiempo antes de llegar a un fin en las siguientes formas posibles:
   - desvaneciéndose completamente (por sobrepoblación o por volverse demasiado dispersos); o
   - asentándose en una configuración estable que permanece inalterada posteriormente, o ingresando en una fase oscilante en la que repiten un ciclo interminable de dos o más períodos.

## Patrones

Muchos tipos diferentes de patrones ocurren en el Juego de la Vida, incluidos patrones estáticos ("naturalezas muertas"), patrones repetitivos ("osciladores" - un superset de naturalezas muertas) y patrones que se trasladan a través del tablero ("naves espaciales"). Ejemplos comunes de estas tres clases se muestran a continuación, con celdas vivas mostradas en negro y celdas muertas mostradas en blanco.

![Gosper glider gun](https://blog.xojo.com/wp-content/uploads/2022/05/CleanShot-2022-05-02-at-14.25.12@2x.png)

&nbsp;

Utilizando las reglas proporcionadas pueden investigar la evolución de los patrones más simples:

![3 celdas](https://pi.math.cornell.edu/~lipa/mec/lifep.png)

&nbsp;

![4 celdas](https://pi.math.cornell.edu/~lipa/mec/4life2.png)

[Fuente](https://pi.math.cornell.edu/~lipa/mec/lesson6.html)

Los patrones que evolucionan durante largos períodos antes de estabilizarse se llaman `Metuselas`, el primero de los cuales descubierto fue el `R-pentomino`. 

![R-pendomino](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Game_of_life_fpento.svg/164px-Game_of_life_fpento.svg.png)

`Diehard` es un patrón que eventualmente desaparece, en lugar de estabilizarse, después de 130 generaciones, lo que se cree que es máximo para patrones iniciales con siete o menos células.

![Diehard](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Game_of_life_diehard.svg/324px-Game_of_life_diehard.svg.png)

`Acorn` tarda 5,206 generaciones en generar 633 células, incluidos 13 planeadores escapados.

![Acorn](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Game_of_life_acorn.svg/292px-Game_of_life_acorn.svg.png)

Conway originalmente conjeturó que ningún patrón puede crecer indefinidamente, es decir, que para cualquier configuración inicial con un número finito de células vivas, la población no puede crecer más allá de algún límite superior finito. El patrón `Gosper glider gun` produce su primer deslizamiento en la 15ª generación, y otro cada 30 generaciones a partir de entonces.

![Gosper's glider gun](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Game_of_life_glider_gun.svg/1000px-Game_of_life_glider_gun.svg.png)

![Gosper glider gun](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

Durante muchos años, este patrón fue la más pequeña conocid0. En 2015, se descubrió una pistola llamada `Simkin glider gun`, que libera un planeador cada 120 generaciones, que tiene menos células vivas pero que está distribuida en una caja delimitadora más grande en sus extremos.

![Simkin glider gun](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Game_of_life_Simkin_glider_gun.svg/1000px-Game_of_life_Simkin_glider_gun.svg.png)

[Fuente](https://medium.com/@swarajkalbande123/conways-game-of-life-life-on-computer-b7edfc85d21a)
![Glider Patterns](https://miro.medium.com/v2/resize:fit:1024/format:webp/0*7nf3iKnIaVET4mnr)


[Fuente](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

&nbsp;

## Implementación de Game of Life en Python

```python
import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10,)  # Color de fondo
COLOR_GRID = (40, 40, 40)  # Color de la cuadrícula
COLOR_DIE_NEXT = (170, 170, 170)  # Color de las células que mueren en la siguiente generación
COLOR_ALIVE_NEXT = (255, 255, 255)  # Color de las células que siguen vivas en la siguiente generación

pygame.init()
pygame.display.set_caption("conway's game of life")  # Título de la ventana del juego

# Función para actualizar la pantalla con las células
def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))  # Matriz para almacenar las células actualizadas

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]  # Cálculo de células vecinas vivas
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT  # Color de la célula actual

        if cells[row, col] == 1:  # Si la célula actual está viva
            if alive < 2 or alive > 3:  # Si tiene menos de 2 o más de 3 vecinos vivos, muere
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:  # Si tiene 2 o 3 vecinos vivos, sigue viva
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:  # Si la célula actual está muerta
            if alive == 3:  # Si tiene exactamente 3 vecinos vivos, revive
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))  # Dibuja la célula en la pantalla

    return updated_cells  # Devuelve las células actualizadas

# Función principal del programa
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Crea la ventana del juego

    cells = np.zeros((60, 80))  # Crea una matriz de células muertas
    screen.fill(COLOR_GRID)  # Rellena la pantalla con el color de la cuadrícula
    update(screen, cells, 10)  # Actualiza la pantalla con las células

    pygame.display.flip()
    pygame.display.update()

    running = False  # Variable para controlar si el juego está en ejecución

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:  # Si se cierra la ventana, termina el programa
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:  # Si se presiona la tecla espacio, se inicia o pausa el juego
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:  # Si se presiona el botón izquierdo del ratón
                pos = pygame.mouse.get_pos()  # Obtiene la posición del ratón
                cells[pos[1] // 10, pos[0] // 10] = 1  # Marca la célula correspondiente como viva
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)  # Rellena la pantalla con el color de la cuadrícula

        if running:  # Si el juego está en ejecución
            cells = update(screen, cells, 10, with_progress=True)  # Actualiza las células con progreso
            pygame.display.update()

        time.sleep(0.001)  # Espera un breve tiempo para controlar la velocidad del juego

if __name__ == "__main__":
    main()
```

Este script de Python es una implementación del Juego de la Vida de Conway, un autómata celular ideado por el matemático británico John Horton Conway. El juego es de cero jugadores, lo que significa que su evolución está determinada por su estado inicial, sin necesidad de más entrada.

El script comienza importando los módulos necesarios: `time`, `pygame` para crear la interfaz gráfica y `numpy` para manejar la cuadrícula del juego como una matriz 2D. Luego define algunas constantes de color para ser utilizadas en la visualización del juego.

Se llama a la función `pygame.init()` para inicializar todos los módulos pygame importados. El título de la ventana se establece en "conway's game of life" usando `pygame.display.set_caption()`.

Se define la función `update()` para actualizar el estado del juego y volver a dibujar la cuadrícula. Toma cuatro argumentos: `screen` (la superficie pygame en la que dibujar), `cells` (el estado actual del juego como una matriz `numpy 2D`), `size` (el tamaño de cada celda en píxeles) y `with_progress` (un booleano que indica si mostrar las celdas que cambiarán en la próxima generación). 

La función crea una nueva matriz 2D `updated_cells` con la misma forma que cells, rellena de ceros. Luego itera sobre cada celda en cells, calcula el número de vecinos vivos y aplica las reglas del juego para determinar si la celda debe estar viva en la próxima generación. La función luego dibuja la celda en pantalla con el color apropiado y devuelve updated_cells.

La función `main()` inicializa pygame, crea una ventana pygame e inicializa el estado del juego como una matriz numpy 2D de ceros (representando celdas muertas). Luego entra en un bucle principal, que procesa eventos de pygame (como cerrar la ventana o presionar una tecla), actualiza el estado del juego si el juego está en marcha y vuelve a dibujar la cuadrícula. El juego puede iniciarse o pausarse presionando la barra espaciadora, y las celdas pueden configurarse manualmente como vivas haciendo clic en ellas con el mouse.

Finalmente, se llama a la función main() para iniciar el juego presionando la barra espaciadora.

## Links de Interés

[The Game Of Life - Emergence In Generative Art - 2020](https://www.artnome.com/news/2020/7/12/the-game-of-life-emergence-in-generative-art)

[Conway’s Game of Life-Life on Computer Swarajkalbande](https://medium.com/@swarajkalbande123/conways-game-of-life-life-on-computer-b7edfc85d21a)

[Wikipedia Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Websites interactivos

[John Conway's Game of Life - An Introduction to celluar Automata](https://beltoforion.de/en/game_of_life/)

[conwaylife.com](https://conwaylife.com/)