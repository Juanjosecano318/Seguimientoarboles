import json

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_diagnostico_medico.json", "r",encoding="utf-8") as archivo:
    arbol_diagnostico = json.load(archivo)

# Verificar que el JSON se ha cargado correctamente
print(arbol_diagnostico)