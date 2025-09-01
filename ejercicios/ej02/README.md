## **Pautas**
Elijan una obra de Vera Molnar de la selección que les comparto a continuación y diseñen un algoritmo (en prosa, sólo con palabras; sin código ni diagrama de flujo) que pueda generar una imagen similar.<br>
Quien quiera y le parezca más accesible puede trabajar con pseudocódigo.<br>
No hace falta que sea una recreación exacta y precisa de la versión original, sino algo inspirado en ese antecedete.<br>
<br>
[Referencias](https://drive.google.com/drive/folders/13w5lbU2EMfWkbsygKDA0gSrGPLXkd9Xj)
<br>
## **Ejemplo sobre obra modelo:  Quadrilateres (1986)**
- Tomar una hoja y elementos para dibujar en negro, gris y rojo.<br>
- Dividir la hoja en 3 filas y 3 columnas, formando una cuadrículo de 9 casillas.<br>
- Repetir la siguiente serie de isntruccion en cada una de esas casilla:<br>
{<br>
	- Dibujar un cuadrado con los siguiente parámetros:<br>
		- Posición: centrado en la casilla<br>
		- Ángulo: Rotacion aleatoria entre -10 y +10 grados<br>
		- Tamaño: aleatorio entre el 70% y el 90% de la casilla<br>
		- Grosor del contorno: finito<br>
		- Grosos del contorno: a elección entre negro, gris o rojo<br>
	- Repetir estos pasos y dibujar 30 cuadrados en esta misma casilla, variando los parámetros<br>
}<br>
- Fin<br>
