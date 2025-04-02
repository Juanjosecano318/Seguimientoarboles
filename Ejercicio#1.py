import json   #Ejercicio 1

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_diagnostico_medico.json", "r",encoding="utf-8") as archivo:
    arbol_diagnostico = json.load(archivo)

class Node:
    def __init__(self, pregunta: str | None = None, diagnostico: str | None = None):
        self.pregunta: str | None = pregunta
        self.left = Node | None  #sub abrol izqueirdo SI
        self.right = Node | None  #sub arbol derecho NO
        self.diagnostico: str | None = diagnostico

class DecisionTreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def recorrer_arbol(self, node: Node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(f"Diagnostico {self.data}")
            return












