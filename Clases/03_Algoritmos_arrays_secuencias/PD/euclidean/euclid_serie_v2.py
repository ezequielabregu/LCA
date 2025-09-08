"""La función de Bjorklund (euclidena v2) implementa correctamente el algoritmo de Bjorklund, 
que es un proceso más complejo que "distribuye" iterativamente los pulsos lo más uniformemente posible. 
Este enfoque maneja correctamente los casos en los que los pulsos no pueden distribuirse uniformemente a lo largo de los pasos, 
y siempre genera un ritmo euclidiano correcto."""

def euclidean(pulses, steps):
    pattern = []
    counts = [0]*steps
    remainders = [0]*steps
    divisor = steps - pulses
    remainders[0] = pulses
    level = 0
    while True:
        counts[level] = divisor // remainders[level]
        remainders[level+1] = divisor % remainders[level]
        divisor = remainders[level]
        level += 1
        if remainders[level] <= 1:
            break
    counts[level] = divisor

    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)
        else:
            for _ in range(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)

    build(level)
    pattern = pattern[::-1]
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[:i]
    return ' '.join(map(str, pattern))

# Variables
pulses = 8
steps = 11
euclidean_rhythm = euclidean(pulses, steps)
print(euclidean_rhythm)