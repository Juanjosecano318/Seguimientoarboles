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
    def __init__(self, root: Node | None = None):
        """
                El árbol de decisiones.

                :param root: Nodo raíz del árbol de decisiones (es el punto de partida).
                """
        self.root: Node | None = root

    def recorrer_arbol(self, node: Node):
        """
                Función recursiva para recorrer el árbol de decisiones y hacer preguntas al usuario hasta llegar a un diagnóstico.

                :param node: Nodo actual del árbol. Si no se pasa, comenzamos desde la raíz.
                """
        if node is None:
            node = self.root

        # Si el nodo tiene un diagnóstico, mostramos el diagnóstico
        if node.is_leaf():
            print(f"diagnostico, {node.diagnostico}")
            return

        print(f"pregunta, {node.pregunta}")
        respuesta = input("¿Respuesta (sí/no)? ").strip().lower()

        if respuesta == "si":
            self.recorrer_arbol(node.left)
        elif respuesta == "no":
            self.recorrer_arbol(node.right)
        else:
            print("Respuesta no valida")

if __name__ == "__main__":
    # Cargar el árbol desde el archivo JSON
    with open("arbol_diagnostico_medico.json", "r", encoding="utf-8") as archivo:
        arbol_diagnostico = json.load(archivo)

    # Crear el árbol de decisiones
    root = Node(pregunta=arbol_diagnostico["pregunta"])
    decision_tree = DecisionTreeNode(root=root)

    # Ejecutar el recorrido del árbol
    decision_tree.recorrer_arbol(decision_tree.root)

















