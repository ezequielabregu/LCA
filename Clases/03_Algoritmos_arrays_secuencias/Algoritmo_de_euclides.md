## The Euclidean Algorithm Generates Traditional Musical Rhythms

Godfried Toussaint (2005)

![Eucliden image](https://d3i71xaburhd42.cloudfront.net/ebe337c4fe489311fead27027473d60c8b54f414/5-Figure1-1.png)

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

[1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0].

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


### Referencias

- [The Euclidean Algorithm Generates Traditional Musical Rhythms](https://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf)
- [Piano-Phase](https://www.chenalexander.com/Piano-Phase)