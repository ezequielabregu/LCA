import mido

# Obtén una lista de los nombres de los puertos de salida MIDI
nombres_puertos = mido.get_output_names()
for nombre in nombres_puertos:
    print(nombre)