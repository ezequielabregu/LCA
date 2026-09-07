"""
Piano Phase (1967) - Steve Reich
=================================
Implementación algorítmica de la obra completa para dos salidas MIDI.

No es un simple "loop que se repite": modela el proceso formal completo tal
como está descrito en la partitura y en la bibliografía analítica de la obra:

  - Tres secciones, cada una con un patrón melódico más corto que la anterior
    (12 notas -> 8 notas -> 4 notas).
  - Dentro de cada sección, el Piano 2 recorre TODAS las posiciones de fase
    posibles respecto del Piano 1 (tantas como notas tiene el patrón): un
    piano se queda fijo, el otro acelera muy gradualmente hasta desplazarse
    exactamente un pulso hacia adelante (la duración de esa transición, de
    4 a 16 vueltas del bucle, queda a elección del pianista 2 en cada
    pasaje), se estabiliza en la nueva relación y repite el proceso, hasta
    volver al unísono y cerrar el ciclo.
  - Entre secciones, un piano hace un fundido de salida, el que queda toca
    solo y cambia de patrón, y luego el otro reingresa con fundido de
    entrada ya con el patrón nuevo. Qué piano lidera el fundido se alterna
    de una transición a la otra, tal como ocurre en la partitura real.

Nota sobre fidelidad: el patrón de 12 notas (E F# B C# D F# E C# B F# D C#)
y la macroforma (12 -> 8 -> 4 notas, fundidos alternados, vuelta a unísono
al cerrar cada sección) están verificados contra fuentes analíticas de la
obra. Las alturas exactas de los patrones de 8 y 4 notas varían levemente
entre transcripciones y análisis de la partitura; acá se derivan truncando
el patrón de 12 notas original (sus primeras 8 y primeras 4 notas), una
reducción simple y coherente con el propio proceso reductivo de Reich. Si
tenés la partitura a mano y querés fidelidad literal de alturas en esas dos
secciones, alcanza con reemplazar PATRON_8 / PATRON_4 más abajo.
"""

import random
import sys
import time

import mido

# ---------------------------------------------------------------------------
# 1. MATERIAL MELODICO
# ---------------------------------------------------------------------------

PATRON_12 = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]  # E F# B C# D F# E C# B F# D C#
PATRON_8 = PATRON_12[:8]
PATRON_4 = PATRON_12[:4]

# ---------------------------------------------------------------------------
# 2. CONFIGURACION MUSICAL Y DE INTERPRETACION
# ---------------------------------------------------------------------------

PUERTO_PIANO_1 = "IAC Driver Bus 1"
PUERTO_PIANO_2 = "IAC Driver Bus 2"  # si no existe, se cae a un solo puerto con 2 canales
CANAL_PIANO_2_FALLBACK = 1  # canal usado por el piano 2 solo si comparte puerto con el 1

PULSO_BASE = 0.150  # duración de una semicorchea en segundos, a tempo estable
ARTICULACION = 0.85  # fracción del pulso que suena la nota (el resto es silencio de separación)

VELOCIDAD_BASE = 92
VELOCIDAD_MIN_FADE = 10

REPETICIONES_POSICION = 4  # veces que se repite el patrón en cada posición de fase estable

# En la partitura, la duración de cada transición de desfasaje queda a
# elección del pianista 2 (el pianista 1 toca siempre al mismo tempo);
# la indicación habitual es de 4 a 16 repeticiones del bucle. Cada
# transición sortea un valor dentro de ese rango (ver elegir_ciclos_transicion).
CICLOS_TRANSICION_MIN = 4
CICLOS_TRANSICION_MAX = 16

REPETICIONES_SOLO = 4  # repeticiones de un piano solo durante el cambio de patrón
REPETICIONES_FADE = 4  # repeticiones usadas para cada fundido de entrada/salida

# "vivo"    -> toca en tiempo real por los puertos MIDI configurados arriba
# "archivo" -> exporta la obra completa como un archivo .mid de dos pistas
MODO = "vivo"
ARCHIVO_SALIDA = "/mnt/user-data/outputs/piano_phase.mid"


# ---------------------------------------------------------------------------
# 3. UTILIDADES DE TIEMPO
# ---------------------------------------------------------------------------

def ventana_triangular(n):
    """Forma triangular normalizada (pico 1.0 en el centro) de longitud n."""
    if n <= 1:
        return [1.0] * max(n, 1)
    centro = (n - 1) / 2
    return [1 - abs((i - centro) / centro) for i in range(n)]


def duraciones_transicion(pulso_base, n_pasos, ganancia_total):
    """
    Duraciones de los n_pasos pulsos del piano que acelera durante una
    transición, distribuidas con una forma triangular (acelera y vuelve a
    tempo de forma suave) de modo que la suma de esos n_pasos pulsos sea
    exactamente `ganancia_total` más corta que a tempo constante. Con
    ganancia_total = pulso_base, el piano que transiciona termina exactamente
    un pulso completo adelantado respecto de a donde estaría a tempo fijo.
    """
    forma = ventana_triangular(n_pasos)
    suma_forma = sum(forma)
    if suma_forma <= 1e-9:
        reduccion = ganancia_total / n_pasos
        return [pulso_base - reduccion] * n_pasos
    escala = ganancia_total / suma_forma
    return [pulso_base - forma[i] * escala for i in range(n_pasos)]


def elegir_ciclos_transicion():
    """
    Cuántas vueltas del bucle dura la próxima transición de desfasaje.
    En la partitura esto lo decide el pianista 2 dentro de un rango de
    4 a 16 repeticiones; acá se sortea dentro de ese mismo rango para que
    cada transición de la pieza tenga una duración distinta, como en una
    interpretación real.
    """
    return random.randint(CICLOS_TRANSICION_MIN, CICLOS_TRANSICION_MAX)


def emitir_notas(eventos, t, piano, notas_con_duracion, velocidad):
    """Agrega eventos note_on/note_off para una secuencia de (nota, duración)."""
    for nota, dur in notas_con_duracion:
        eventos.append((t, piano, "on", nota, velocidad))
        eventos.append((t + dur * ARTICULACION, piano, "off", nota, 0))
        t += dur
    return t


# ---------------------------------------------------------------------------
# 4. MOTOR DE FASEO (proceso interno de cada sección)
# ---------------------------------------------------------------------------

def generar_seccion(eventos, marcas, t_inicio, patron, nombre_seccion):
    """
    Genera una sección completa: el Piano 1 se mantiene siempre fijo, el
    Piano 2 recorre las L posiciones de fase posibles (L = len(patron)) y
    cierra el ciclo volviendo al unísono. Devuelve el tiempo final.
    """
    L = len(patron)
    t = t_inicio
    cnt1 = 0  # índice acumulado de pulsos del piano 1 (nunca se reinicia)
    cnt2 = 0  # índice acumulado de pulsos del piano 2

    marcas.append((t, f"{nombre_seccion}: unisono inicial"))

    for offset in range(L + 1):
        etiqueta = f"posicion de fase {offset}/{L}" if offset < L else "unisono, cierre del ciclo"
        marcas.append((t, f"{nombre_seccion}: {etiqueta}"))

        # --- tramo estable: ambos pianos a igual tempo ---
        n = REPETICIONES_POSICION * L
        seq1 = [(patron[(cnt1 + i) % L], PULSO_BASE) for i in range(n)]
        seq2 = [(patron[(cnt2 + i) % L], PULSO_BASE) for i in range(n)]
        t_ini = t
        t = emitir_notas(eventos, t_ini, 1, seq1, VELOCIDAD_BASE)
        emitir_notas(eventos, t_ini, 2, seq2, VELOCIDAD_BASE)
        cnt1 += n
        cnt2 += n

        if offset == L:
            break  # el círculo ya se cerró, no hace falta otra transición

        # --- tramo de transición: el piano 2 gana exactamente un pulso ---
        # El piano 2 toca n_t pulsos comprimidos; el piano 1 sigue a tempo
        # constante durante (n_t - 1) pulsos: en ese mismo lapso el piano 2
        # queda un pulso adelantado, que es justo una posición de fase más.
        # La duración de la transición (en vueltas del bucle) la elige el
        # pianista 2, dentro del rango habitual de la partitura.
        ciclos = elegir_ciclos_transicion()
        n_t = max(6, ciclos * L)
        marcas.append((t, f"{nombre_seccion}: transicion hacia {offset + 1}/{L} "
                           f"({ciclos} vueltas del bucle, {n_t * PULSO_BASE:.1f}s)"))
        duraciones2 = duraciones_transicion(PULSO_BASE, n_t, PULSO_BASE)
        seq2_t = [(patron[(cnt2 + i) % L], duraciones2[i]) for i in range(n_t)]
        seq1_t = [(patron[(cnt1 + i) % L], PULSO_BASE) for i in range(n_t - 1)]

        t_ini = t
        emitir_notas(eventos, t_ini, 1, seq1_t, VELOCIDAD_BASE)
        t = emitir_notas(eventos, t_ini, 2, seq2_t, VELOCIDAD_BASE)
        cnt1 += n_t - 1
        cnt2 += n_t

    marcas.append((t, f"{nombre_seccion}: fin"))
    return t


# ---------------------------------------------------------------------------
# 5. TRANSICION ENTRE SECCIONES (fundidos y cambio de patrón)
# ---------------------------------------------------------------------------

def generar_transicion_de_seccion(eventos, marcas, t_inicio, patron_viejo, patron_nuevo, piano_que_se_va):
    """
    piano_que_se_va hace un fundido de salida sobre patron_viejo, calla, y
    reingresa con fundido de entrada ya sobre patron_nuevo. El otro piano
    (piano_que_queda) sigue solo con patron_viejo, cambia sin fundido a
    patron_nuevo, y sostiene ese patrón hasta que el otro reingresa en
    unísono, momento en que arranca la siguiente sección.
    """
    piano_que_queda = 2 if piano_que_se_va == 1 else 1
    Lv, Ln = len(patron_viejo), len(patron_nuevo)
    t = t_inicio

    def fundido(t_ini, patron, piano_que_suena, piano_en_paralelo, subiendo):
        L = len(patron)
        n = REPETICIONES_FADE * L
        t_local = t_ini
        for i in range(n):
            frac = (i + 1) / n
            vel = VELOCIDAD_MIN_FADE + (VELOCIDAD_BASE - VELOCIDAD_MIN_FADE) * (frac if subiendo else 1 - frac)
            vel = max(1, min(127, round(vel)))
            nota = patron[i % L]
            eventos.append((t_local, piano_que_suena, "on", nota, vel))
            eventos.append((t_local + PULSO_BASE * ARTICULACION, piano_que_suena, "off", nota, 0))
            t_local += PULSO_BASE
        if piano_en_paralelo is not None:
            secuencia = [(patron[i % L], PULSO_BASE) for i in range(n)]
            emitir_notas(eventos, t_ini, piano_en_paralelo, secuencia, VELOCIDAD_BASE)
        return t_ini + n * PULSO_BASE

    marcas.append((t, f"fundido de salida, piano {piano_que_se_va}"))
    t = fundido(t, patron_viejo, piano_que_se_va, piano_que_queda, subiendo=False)

    marcas.append((t, f"piano {piano_que_queda} solo, patron anterior"))
    seq = [(patron_viejo[i % Lv], PULSO_BASE) for i in range(REPETICIONES_SOLO * Lv)]
    t = emitir_notas(eventos, t, piano_que_queda, seq, VELOCIDAD_BASE)

    marcas.append((t, f"piano {piano_que_queda} solo, patron nuevo de {Ln} notas"))
    seq = [(patron_nuevo[i % Ln], PULSO_BASE) for i in range(REPETICIONES_SOLO * Ln)]
    t = emitir_notas(eventos, t, piano_que_queda, seq, VELOCIDAD_BASE)

    marcas.append((t, f"fundido de entrada, piano {piano_que_se_va}"))
    t = fundido(t, patron_nuevo, piano_que_se_va, piano_que_queda, subiendo=True)

    return t


# ---------------------------------------------------------------------------
# 6. COMPOSICION DE LA OBRA COMPLETA
# ---------------------------------------------------------------------------

def componer_obra():
    eventos = []
    marcas = []
    t = 0.0

    t = generar_seccion(eventos, marcas, t, PATRON_12, "Seccion I (12 notas)")
    t = generar_transicion_de_seccion(eventos, marcas, t, PATRON_12, PATRON_8, piano_que_se_va=2)
    t = generar_seccion(eventos, marcas, t, PATRON_8, "Seccion II (8 notas)")
    t = generar_transicion_de_seccion(eventos, marcas, t, PATRON_8, PATRON_4, piano_que_se_va=1)
    t = generar_seccion(eventos, marcas, t, PATRON_4, "Seccion III (4 notas)")

    # Coda: la partitura simplemente termina al volver a unisono en la
    # seccion de 4 notas; acá se agrega un fundido conjunto breve de ambos
    # pianos para un cierre prolijo en una version renderizada. Es una
    # decision de implementacion, no un elemento indicado en la partitura.
    marcas.append((t, "coda: fundido final conjunto"))
    L = len(PATRON_4)
    n = REPETICIONES_FADE * L
    t_local = t
    for i in range(n):
        vel = max(1, round(VELOCIDAD_BASE - (VELOCIDAD_BASE - VELOCIDAD_MIN_FADE) * (i + 1) / n))
        nota = PATRON_4[i % L]
        for piano in (1, 2):
            eventos.append((t_local, piano, "on", nota, vel))
            eventos.append((t_local + PULSO_BASE * ARTICULACION, piano, "off", nota, 0))
        t_local += PULSO_BASE
    t = t_local

    eventos.sort(key=lambda e: e[0])
    marcas.sort(key=lambda e: e[0])
    return eventos, marcas, t


# ---------------------------------------------------------------------------
# 7. SALIDA EN VIVO POR MIDI
# ---------------------------------------------------------------------------

def reproducir_en_vivo(eventos, marcas):
    try:
        puerto1 = mido.open_output(PUERTO_PIANO_1)
    except (OSError, IOError):
        print(f'No se pudo abrir "{PUERTO_PIANO_1}".')
        print("Puertos MIDI disponibles:", mido.get_output_names())
        return

    puerto2_independiente = True
    try:
        puerto2 = mido.open_output(PUERTO_PIANO_2)
    except (OSError, IOError):
        print(f'Aviso: no se encontro "{PUERTO_PIANO_2}"; el piano 2 sale por '
              f'"{PUERTO_PIANO_1}", canal MIDI {CANAL_PIANO_2_FALLBACK + 1}.')
        puerto2 = puerto1
        puerto2_independiente = False

    def enviar(piano, tipo, nota, velocidad):
        puerto = puerto1 if piano == 1 else puerto2
        canal = 0 if (piano == 1 or puerto2_independiente) else CANAL_PIANO_2_FALLBACK
        tipo_mido = "note_on" if tipo == "on" else "note_off"
        vel = max(1, min(127, round(velocidad))) if tipo == "on" else 0
        puerto.send(mido.Message(tipo_mido, note=nota, velocity=vel, channel=canal))

    indice_marca = 0
    inicio = time.perf_counter()
    try:
        for (t, piano, tipo, nota, velocidad) in eventos:
            while indice_marca < len(marcas) and marcas[indice_marca][0] <= t:
                print(f"[{marcas[indice_marca][0]:6.1f}s] {marcas[indice_marca][1]}")
                indice_marca += 1
            espera = (inicio + t) - time.perf_counter()
            if espera > 0:
                time.sleep(espera)
            enviar(piano, tipo, nota, velocidad)
    except KeyboardInterrupt:
        print("Interrumpido por el usuario.")
    finally:
        for nota in set(PATRON_12):
            puerto1.send(mido.Message("note_off", note=nota, velocity=0, channel=0))
            puerto2.send(mido.Message("note_off", note=nota, velocity=0,
                                       channel=0 if puerto2_independiente else CANAL_PIANO_2_FALLBACK))
        puerto1.close()
        if puerto2_independiente:
            puerto2.close()


# ---------------------------------------------------------------------------
# 8. EXPORTACION A ARCHIVO .mid
# ---------------------------------------------------------------------------

def exportar_a_midi(eventos, ruta):
    ticks_por_negra = 960
    microsegundos_por_negra = 500000  # tempo nominal de referencia (120 bpm), fijo
    segundos_por_tick = (microsegundos_por_negra / 1_000_000) / ticks_por_negra

    archivo = mido.MidiFile(ticks_per_beat=ticks_por_negra)
    pista1, pista2 = mido.MidiTrack(), mido.MidiTrack()
    archivo.tracks += [pista1, pista2]
    pista1.append(mido.MetaMessage("set_tempo", tempo=microsegundos_por_negra, time=0))
    pista1.append(mido.MetaMessage("track_name", name="Piano 1", time=0))
    pista2.append(mido.MetaMessage("track_name", name="Piano 2", time=0))

    for pista, num_piano in ((pista1, 1), (pista2, 2)):
        t_anterior = 0.0
        for (t, piano, tipo, nota, velocidad) in eventos:
            if piano != num_piano:
                continue
            delta_ticks = max(0, round((t - t_anterior) / segundos_por_tick))
            tipo_mido = "note_on" if tipo == "on" else "note_off"
            pista.append(mido.Message(tipo_mido, note=nota, velocity=velocidad, channel=0, time=delta_ticks))
            t_anterior = t

    archivo.save(ruta)
    print(f"Archivo MIDI exportado: {ruta}")


# ---------------------------------------------------------------------------
# 9. PUNTO DE ENTRADA
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else MODO

    eventos, marcas, duracion_total = componer_obra()
    print(f"Piano Phase generado: {len(eventos)} eventos MIDI, "
          f"duracion total aproximada {duracion_total / 60:.1f} minutos.")

    if modo == "archivo":
        exportar_a_midi(eventos, ARCHIVO_SALIDA)
    else:
        reproducir_en_vivo(eventos, marcas)