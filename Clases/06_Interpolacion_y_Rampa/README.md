# Interpolación y Rampa

En este encuentro partimos del algoritmo clave de un contador y desde ahí profundizamos hacia los conceptos de interpolación y rampa. Previamente, en ["04-bucles-e-iteraciones"](https://github.com/ezequielabregu/LCA/blob/main/Clases/04_Bucles_e_Iteraciones/README.md), exploramos algoritmos para la creación de imágenes estáticas. La evolución de esos algoritmos tenía un desarrollo temporal independiente de sus resultados, imágenes permanentes e invariables en el tiempo.

De la mano del contador, la interpolación y la rampa, vimos cómo el tiempo del algoritmo se capitaliza en el resultado estético. Para ilustrar esto, estudiamos  un algoritmo que recrea el inicio del trabajo *Cubic Limit* (1975), de Manfred Mohr.

**Video de la obra:** [Cubic Limit](https://drive.google.com/file/d/1EtrNBF_zOrxUDOaZdq0FjQ_lAxMpmB4g/view?usp=sharing)

Como punto de partida, tomamos el siguiente diagrama de un contador:

![Diagrama del contador](https://github.com/ezequielabregu/LCA/blob/main/Clases/06_Interpolacion_y_Rampa/00-contador-bucle_while.jpg)

Y comentamos dos variaciones, disponibles en este [enlace](https://drive.google.com/drive/folders/1HCSf8EDDRIruEkqJCtuJ4mg7oz2nwpxd?usp=sharing).

Luego, exploramos la interpolación como la obtención o generación de nuevos puntos intermedios entre otros preexistentes. Es el cálculo o método a partir del cual se puede insertar algo entre medio de otras cosas, considerando la relación entre lo insertado y su contexto de inserción.

Comentamos y profundizamos el concepto con imágenes hasta llegar a ![la fórmula de Newton:](https://github.com/ezequielabregu/LCA/blob/main/Clases/06_Interpolacion_y_Rampa/06-interpolacion_lineal_formula_Newton.png)

Luego, vimos la implementación de esa fórmula en PD+Gem. Primero con una única interpolación a partir de dos puntos (cada uno definido por sus coordenadas X, Y) y un valor intermedio de X, obtenemos el valor de Y para ese punto intermedio según el método de Newton de interpolación lineal. [Patches para esta implementación](https://drive.google.com/drive/folders/17ukodswhS1l_XcQYsZynUOMLK4oDWtNm?usp=sharing).

Posteriormente, realizamos una doble interpolación lineal agregando el eje Z en los siguientes patches disponibles [aquí](https://drive.google.com/drive/folders/1M2Oz9P1Gyu0PNkC7cjvAvueGmfFPB4uU?usp=sharing).

En la segunda mitad del encuentro, nos adentramos en el concepto de Rampa. Recuperamos el algoritmo del contador y lo planteamos para su desarrollo temporal. Así, definimos al generador de rampa, un contador controlado y definido en función del tiempo. 

Un generador de rampa internamente calcula el paso necesario para que se generen los valores intermedios entre sus límites según un tiempo definido como argumento o parámetro de control.

En Pure Data, uno de los objetos generadores de rampa es `line`.

Exploramos el concepto de rampa en PD+Gem con los siguientes patches disponibles [aquí](https://drive.google.com/drive/folders/10WeJjUiGj2N9ciDNTBjbnkb_F8RULvXx?usp=sharing).

Finalmente, revisamos el patch de recreación de la obra de Manfred Mohr que se presentó al inicio del encuentro (sólo la primera parte) [aquí](https://drive.google.com/drive/folders/1yas4XHLdbBW5JNXWsNHhqV1DFHOiETUp?usp=sharing).

Y aquí tienen el enlace directo a una captura de la recreación: [Captura](https://drive.google.com/file/d/1cB7EAy0duXsg90m7psZGnYW-Z4Fqw_99/view?usp=sharing)

Videos de clase de otro curso:
[parte 1](https://www.youtube.com/watch?v=dH5kJSNjLEo)
[parte 2](https://www.youtube.com/watch?v=mAhCZJKfnG0) 
[parte 3](https://www.youtube.com/watch?v=VHKu50m4Ys0)


---

## GEM

Les comparto una introducción a GEM, dividida en tres partes: tres videos con tres patches (uno para cada uno).

Los patches están todos juntos en este [drive](https://drive.google.com/drive/folders/1jbwJzeqHl_H5u5WQUppeYlqN-gSE5786?usp=sharing).

Los videos:
- [Introducción General](https://www.youtube.com/watch?v=f-7KTDyXLLA)
- [Video](https://www.youtube.com/watch?v=3DyYt8xnUBc)
- [Convertidor Gráfico Sonoro](https://www.youtube.com/watch?v=bvKzAOsvjbg)
