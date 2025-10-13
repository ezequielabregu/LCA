# Aleatoriedad

Hoy trabajamos el concepto de aleatoriedad como eje de estudio, teniendo en cuenta que en el ámbito computacional es referido como pseudo-aleatoriedad. Realizada la aclaración, se usa directamente el término aleatoriedad (sin el "pseudo") entendiendo que en la computación actual de uso cotidiano no existe la posibilidad de una aleatoriedad 100% real. Desde ese lugar, puede ser que a continuación y en los archivos use indistintamente la palabra "aleatoriedad" en español o "random" en inglés, que es el término que se utiliza para referirse a las funciones que generan secuencias pseudo-aleatorias de valores en los diferentes lenguajes de programación.

En la primera parte de lo que estuvimos recorriendo, les propuse una introducción general al concepto y su puesta en diálogo con la producción de arte, con ejemplos de piezas visuales, y luego la apropiación o el traslado del concepto hacia el campo computacional.

Desde ahí, pasamos a explorar lo que está por detrás de los algoritmos o funciones que nos ofercen secuencias aleatorias de valores: las tablas de valores y la ecuación del Generador Lineal Congruencial.

Desde el enlace a continuación pueden descargar los patches que usamos y algunos materiales complementarios: [Patches y materiales complementarios](https://drive.google.com/drive/folders/1CGE7YbBEBW4SnOtkKurjfgO-BzHLNW__)

Desde este otro enlace, los materiales de la empresa Rand: [Materiales de la empresa Rand](https://drive.google.com/drive/folders/1FV2PqRQmaJVYpsYTHQasVij0fc1hnwTH)


Exploramos las posibilidades de la distribución de la probabilidad y tomamos como caso de estudio un trabajo clásico de Michael Noll. Ese ejemplo y algunos materiales sobre Michael Noll: [Materiales sobre Michael Noll](https://drive.google.com/drive/folders/1D7p3QEVkKkT-elpxOlBJ8BuMOiHJ5E4n?usp=sharing)

Sobre Shuffle, vimos que es una permutación del orden de los contenidos de un array. De manera que se plantean analogías con re-ordenar un mazo de cartas o los numeros del bolillero de un bingo, son situaciones para los que la función random suele no ser útil ya que podría repetir dos veces consecutivas el mismo resultado; mientras que Shuffle nos garantiza que ningún resultado se reptia hasta que se compelten las posibilidades dadas (excepto, por supuesto, que en el conjunto de datos iniciales existan esas repeticiones). Bibliografía de referencia de Donald Knuth e implementacion en PD: [shuffle link](https://drive.google.com/drive/folders/1PKiOobrcBefiaMlkVPTBJ-6JKsP6GcyO)

Sobre Drunk, una desviación aleatoria, desde un valor de referencia. Desde se version mas sencilla y elemental, puede ser implementado sencillamente como una suma (al último valor que tengamos) de una variable de 3 posibilidades random (-1, 0, +1). [Implementación en PD](https://drive.google.com/drive/folders/1PKiOobrcBefiaMlkVPTBJ-6JKsP6GcyO).

