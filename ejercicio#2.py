import json

# Abrir el archivo JSON y cargarlo en una variable
with open("arbol_adivinanzas.json", "r",encoding="utf-8") as archivo:
    arbol_adivinanzas = json.load(archivo)

class Node:
    def __init__(self, pregunta: str = None, repuesta: str = None):
        self.pregunta: str = pregunta  # Pregunta para diferenciar objetos
        self.respuesta: str = repuesta  # Respuesta si es un nodo hoja (objeto adivinado)
        self.left = None # Respuesta "sí"
        self.right = None # Respuesta "no"

class Adivinador:
    def __init__(self, root=None, pregunta_inicial="¿Es un animal?"):
        """Inicializa el árbol de adivinanzas con una pregunta base si no se proporciona un árbol."""
        if root:
            self.root = root
        else:
            self.root = Node(pregunta=pregunta_inicial)  # Nodo raíz con la pregunta inicial

    def preorden(self,node):
        """Recorre el árbol en preorden mostrando las preguntas."""
        if node is None:
            nodo = self.root

        if nodo.pregunta:
            print(f"Pregunta: {nodo.pregunta}")

        if nodo.left:
            self.preorden(nodo.left)
        if nodo.right:
            self.preorden(nodo.right)
