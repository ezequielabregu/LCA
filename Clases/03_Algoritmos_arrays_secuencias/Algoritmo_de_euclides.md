## The Euclidean Algorithm Generates Traditional Musical Rhythms

Godfried Toussaint (2005)

[**<-- VOLVER AL INICIO**](/README.md)

![Eucliden image](https://idmmag.com/wp-content/uploads/2019/02/Euclidean-R-1.jpg)

[Link al artículo original](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)

#### Resumen

El algoritmo euclidiano (que nos llega de Los Elementos de Euclides) calcula el máximo común divisor de dos enteros dados. Se muestra aquí que la estructura del algoritmo euclidiano puede ser utilizada para generar, de manera muy eficiente, una gran variedad de ritmos utilizados como líneas de tiempo (ostinatos) en la música subsahariana en particular, y en la música mundial en general. Estos ritmos, aquí llamados ritmos euclidianos, tienen la propiedad de que sus patrones de inicio están distribuidos de la manera más uniforme posible. Los ritmos euclidianos también encuentran aplicación en aceleradores de física nuclear y en ciencias de la computación, y están estrechamente relacionados con varias familias de palabras y secuencias de interés en el estudio de la combinatoria de palabras, como las cadenas euclidianas, a las que se comparan los ritmos euclidianos.

## Hipótesis

Varios investigadores han observado que en los ritmos de la música tradicional del mundo hay una tendencia a encontrar patrones distribuidos lo más regular o uniformemente posible.

**Los patrones de regularidad máxima se pueden describir mediante el uso del algoritmo de Euclides sobre el máximo común divisor de dos números enteros**

## Patrones de regularidad máxima

El Patrón de Regularidad Máxima es un concepto utilizado en la teoría de la música para crear ritmos euclideanos. Los ritmos euclideanos son patrones rítmicos que distribuyen uniformemente golpes a lo largo de un ciclo de tiempo.

En esencia, el Patrón de Regularidad Máxima busca **distribuir un número específico de golpes de manera equitativa** dentro de un período de tiempo dado. Esto se logra dividiendo el tiempo en partes iguales y asignando golpes a estas divisiones de manera uniforme.

Ejemplo:

x = nota

· = silencio

[×· ×· ×· ×· ] → [1 0 1 0 1 0 1 0 ]
(8,4) = 4 notas distribuidas regularmente en los 8 pulsos 

[×· ·×· ·×·] → [1 0 0 1 0 0 1 0 ]
(8,3) = 3 notas distribuidas regularmente en 8 pulsos

### Algoritmo de Euclides

Uno de los algoritmos más antiguos conocidos, descrito en Los Elementos de Euclides (alrededor del 300 a.C.) en la Proposición 2 del Libro VII, hoy conocido como el algoritmo euclidiano, calcula el máximo común divisor de dos enteros dados.

La idea es muy simple. El número más pequeño se resta repetidamente del mayor hasta que el mayor sea cero o se vuelva más pequeño que el menor, en cuyo caso se llama el resto. Este resto luego se resta repetidamente del número más pequeño para obtener un nuevo resto. Este proceso continúa hasta que el resto es cero. 

Para ser más precisos, consideremos como ejemplo los números 5 y 8.

- Primero, dividimos 8 entre 5. Esto nos da 1 como cociente y un resto de 3. 
- Entonces, dividimos 5 entre 3, lo que nos da 1 como cociente y un resto de 2. 
- Después, dividimos 3 entre 2, lo que nos da 1 como cociente y un resto de 1. 
- Finalmente, dividimos 2 entre 1, lo que nos da 2 como cociente y un resto de 0.

La idea aquí es seguir dividiendo el divisor anterior por el resto obtenido en cada paso, hasta que el resto sea 0. Cuando llegamos a un resto de 0, el divisor anterior es el mayor divisor común de los dos números.

En resumen, el proceso se puede ver como una secuencia de ecuaciones:

```text
8 = (1)(5) + 3
5 = (1)(3) + 2
3 = (1)(2) + 1
2 = (1)(2) + 0
```

*Nota: 8=(1)(5)+3 significa que 8 se divide entre 5 una vez, con un cociente de 1 y un resto de 3.*

&nbsp;

En concreto, consiste en hacer divisiones sucesivas para hallar el `máximo común divisor` de dos números positivos (m.c.d. de aquí en adelante).

El `m.c.d.` de dos números a y b, suponiendo que a > b, primero dividimos a entre b, y obtenemos el resto r de la división.

El m.c.d. de a y b es el mismo que el de b y r. 
Cuando dividimos a entre b, obtenemos un cociente c y un resto r de tal manera que se cumple que:

`a = c · b + r`

**Ejemplos:**

calculemos el máximo común de 17 y 7. 

Como `17 = 7 · 2 + 3`, entonces el m.c.d.(17, 7) es igual al m.c.d.(7, 3). 

De nuevo, como 7 = 3 · 2 + 1, entonces el m.c.d.(7, 3) es igual al m.c.d.(3, 1). 

Aquí es claro que el m.c.d. entre 3 y 1 es simplemente 1. Por tanto, el m.c.d entre 17 y 7 es 1 también.

```text
m.c.d. (17,7) = 1

17 = 7 . 2 + 3

7 = 3 . 2 + 1

3 = 1 . 3 + 0
````

&nbsp;

**Otro ejemplo:**

```text
m.c.d. (8,3) = 1

8 = 3 . 2 + 2

3 = 2 . 1 + 1

2 = 1 . 2 + 0
```

### ¿Cómo se transforma el cálculo del m.c.d. en patrones distribuidos con regularidad máxima?


Representar una secuencia binaria de k unos [1] y n−k ceros [0], donde cada bit [0] representa un intervalo de tiempo y los unos [1] se envía una señal. 

El problema entonces se reduce a lo siguiente: 

`Construir una secuencia binaria de n bits con k unos tal que los k unos se distribuyan lo más uniformemente posible entre los n − k ceros.`

Un caso simple es cuando k divide uniformemente n (sin resto), en cuyo caso debemos colocar unos cada n/k bits.
Por ejemplo, si n = 16 y k = 4, entonces la solución es

[1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0].

Este caso corresponde a que n y k tienen un divisor común de k (en este caso 4). 

De manera más general, si el máximo común divisor entre n y k es g, esperaríamos que la solución se descomponga en g repeticiones de una secuencia de n/g bits.

**Esta conexión con los máximos comunes divisores sugiere que se podría calcular un ritmo de máxima uniformidad usando un algoritmo como el de Euclides.**

&nbsp;

### Ejemplo (13, 5)

Consideremos una secuencia con
n = 13 y k = 5. 

Dado que 13 − 5 = 8, comenzamos por considerar una secuencia que consiste en 5 unos, seguidos de
8 ceros, la cual debe pensarse como 13 secuencias de un bit cada una:

[1 1 1 1 1 0 0 0 0 0 0 0 0]

Empezamos a mover ceros colocando un cero después de cada uno, para producir cinco secuencias de dos bits cada una, con
tres ceros restantes:

[10] [10] [10] [10] [10] [0] [0] [0]

`13 = 5 . 2 + 3`

Luego distribuimos los tres ceros restantes de manera similar, colocando una secuencia [0] después de cada secuencia [10]
para obtener:

[100] [100] [100] [10] [10]

`5 = 3 . 1 + 2`

Ahora tenemos tres secuencias de tres bits cada una, y un remanente de dos secuencias de dos bits cada una.
Por lo tanto, continuamos de la misma manera, colocando una secuencia [10] después de cada secuencia [100] para obtener:

[10010] [10010] [100]

`3 = 2 . 1 + 1`

El proceso se detiene cuando el remanente consiste en una sola secuencia (en este caso, la secuencia [100]), o
nos quedamos sin ceros. 

La secuencia final es, por tanto, la concatenación de [10010], [10010] y [100]:

**[1 0 0 1 0 1 0 0 1 0 1 0 0]**

`2 = 1 . 2 + 0`

&nbsp;

### Ejemplo (17, 7)

Supongamos que tenemos 17 pulsos y queremos distribuir de forma regular 7 notas en los 17 pulsos.

**1.** Alineamos el número de notas  y el número de silencios (7 unos y 10 ceros)

[ 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 ]

|1 1 1 1 1 1 1|0 0 0 0 0 0 0 0 0 0|
|-|-|

**2.** Formamos grupos de 7, los cual corresponde a efectuar la división de 17 entre 7; obtenemos 7 grupos de formados por `[1 0]` y sobran 3 ceros `[000]`, lo cual indica que en el paso siguiente formaremos grupos de 3 hasta que queden uno o cero grupos.

[1 0] [1 0] [1 0] [1 0] [1 0] [1 0] [1 0] [0] [0] [0]

`17 = 7 . 2 + 3`

|1 |1 |1 |1 |1 |1 |1 |0 0 0|
|-|-|-|-|-|-|-|-|
|0|0|0|0|0|0|0|

&nbsp;

**3.** De nuevo, esto es equivalente a efectuar la división de 7 entre 3. En nuestro caso, queda un solo grupo y hemos terminado.

&nbsp;

[1 0 0] [1 0 0] [1 0 0] [1 0] [1 0] [1 0] [1 0]

|1 |1 |1 |1 |1 |1 |1 |
|-|-|-|-|-|-|-|
|0|0|0|0|0|0|0|
|0|0|0|

[1 0 0 1 0] [1 0  1 0 0] [1 0 0 1 0] [1 0]

`7 = 3 . 2 + 1`

|1 |1 |1 |1 |
|-|-|-|-|
|0|0|0|0|0|0|0|
|0|0|0|
|1|1|1|
|0|0|0|

&nbsp;

**4.** Finalmente, el ritmo se obtiene leyendo por columnas y de izquierda a derecha la agrupación obtenida, paso a paso.

**`[1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0]`**

`3 = 1 . 3 + 0`

&nbsp;

### Implementación en Pure Data - Euclidean sequencer

```text
(index * hits ) % steps
↓
[< notas]
```

donde:

index = índice de la euclid serie (array)

hits = número de notas a ejecutarse

steps = array size

### Referencias

- [The Euclidean Algorithm Generates Traditional Musical Rhythms](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)
- [Piano-Phase](https://www.chenalexander.com/Piano-Phase)