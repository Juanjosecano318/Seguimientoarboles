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
    def __init__(self, root=None, pregunta_inicial=None):
        """Inicializa el árbol con una pregunta base si no se proporciona un árbol."""
        if pregunta_inicial is None:
            pregunta_inicial = "¿Es un ser vivo?"  # Pregunta base por defecto

        self.root = root if root else Node(pregunta=pregunta_inicial)
    def mostrar_preguntas(self):
        """Método público que inicia el recorrido preorden desde la raíz."""
        self.__preorden(self.root)

    def __preorden(self, node):
        """Método privado para recorrer el árbol en preorden mostrando las preguntas."""
        if node is None:
            return  # Caso base: No hacer nada si el nodo es nulo

        if node.pregunta:  # Si el nodo tiene una pregunta, la imprime
            print(f"Pregunta: {node.pregunta}")

        # Llamadas recursivas para recorrer el árbol
        self.__preorden(node.left)
        self.__preorden(node.right)