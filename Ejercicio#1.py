import json   #Ejercicio 1

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_diagnostico_medico.json", "r",encoding="utf-8") as archivo:
    arbol_diagnostico = json.load(archivo)

class Node:
    def __init__(self, pregunta: str | None = None, diagnostico: str | None = None):
        self.pregunta: str | None = pregunta
        self.left = None  #Subárbol izquierdo (respuesta "sí")
        self.right = None  #Subárbol derecho (respuesta "no")
        self.diagnostico: str | None = diagnostico
    def is_leaf(self):
        """Devuelve True si el nodo es una hoja (tiene diagnóstico y no tiene hijos)."""
        return self.diagnostico is not None and self.left is None and self.right is None

class DecisionTreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def recorrer_arbol(self, node: Node):
        # Si el nodo es None, no hacemos nada (caso base)
        if node is None:
            return
        # Si el nodo tiene un diagnóstico, mostramos el diagnóstico
        if node.left is None and node.right is None:
            print(f"Diagnostico {self.data}")
            return

        print(node.pregunta)
        respuesta = input("¿Respuesta (sí/no)? ").strip().lower()















