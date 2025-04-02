import json

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_diagnostico_medico.json", "r",encoding="utf-8") as archivo:
    arbol_diagnostico = json.load(archivo)

class Node:
    def __init__(self, pregunta: str | None = None, diagnostico: str | None = None):
        self.pregunta: str | None = pregunta
        self.si = Node | None  #sub abrol izqueirdo
        self.no = Node | None  #sub arbol derecho
        self.diagnostico: str | None = diagnostico

class DecisionTreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right




