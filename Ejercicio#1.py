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

class DecisionTree:
    def __init__(self, data):
        """Construye el árbol de decisiones a partir de un diccionario JSON."""
        self.root = self.build_tree(data)

    def build_tree(self, data):
        """Función recursiva para construir el árbol."""
        if "diagnostico" in data:
            return Node(diagnostico=data["diagnostico"])  # Nodo hoja con diagnóstico

        node = Node(pregunta=data["pregunta"])  # Nodo con pregunta
        node.left = self.build_tree(data["si"])  # Construir lado izquierdo (respuesta "sí")
        node.right = self.build_tree(data["no"])  # Construir lado derecho (respuesta "no")
        return node

    def recorrer_arbol(self, node: Node):
        """
                Función recursiva para recorrer el árbol de decisiones y hacer preguntas al usuario hasta llegar a un diagnóstico.

                :param node: Nodo actual del árbol. Si no se pasa, comenzamos desde la raíz.
                """
        if node is None:
            return

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
            self.recorrer_arbol(node)


    def verificar_camino(self):
        return self.__verificar_caminos(self.root)

    def __verificar_caminos(self,node: Node) -> bool:
        if node is None:
            return True

        if node.is_leaf():
            print(f"El nodo con diagnostico, {node.diagnostico} es hoja")
            return True

        print(f"El nodo con pregunta, {node.pregunta} no es una hoja")
        left_valid = self.__verificar_caminos(node.left)
        right_valid = self.__verificar_caminos(node.right)

        if left_valid and right_valid:
            return True
        else:
            return False

# Crear el árbol y ejecutarlo
if __name__ == "__main__":
    decision_tree = DecisionTree(arbol_diagnostico)
    decision_tree.recorrer_arbol(decision_tree.root)



















