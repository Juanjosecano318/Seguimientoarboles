import json

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_adivinanzas.json", "r",encoding="utf-8") as archivo:
    arbol_adivinanzas = json.load(archivo)

