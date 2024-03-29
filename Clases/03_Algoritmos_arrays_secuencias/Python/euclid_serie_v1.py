""" La función de Bjorklund (euclidiana v1) es más simple que la v2 intenta distribuir los pulsos de manera uniforme a lo 
largo de los pasos simplemente asignando un pulso (1) a cada paso en la lista de espacios para 
los pulsos. Sin embargo, este enfoque no maneja correctamente los casos en los que los pulsos no 
pueden distribuirse uniformemente a lo largo de los pasos, y por lo tanto no siempre genera un ritmo 
euclidiano correcto.
"""
def euclidean(pulses, steps):
    slots = [0] * steps
    for i in range(pulses):
        slots[i * steps // pulses] = 1
        print(f"i: {i}, index: {i * steps // pulses},serie: {slots}")
    return ''.join(map(str, slots))

# Variables
pulses = 4
steps = 11
serie_euclideana = euclidean(pulses, steps)
print(serie_euclideana)