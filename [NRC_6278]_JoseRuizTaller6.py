""""    Autor: José Ruiz
        ID: L00380361
        Materia: Inteligencia Artificial
"""
""" 
____________________________________________________________________________________________________________________________
En este programa se trata de la búsqueda primero en amplitud. Recorre sistemáticamente el gráfico, 
nivel por nivel, y crea un árbol BFS en el camino. La búsqueda en amplitud se puede utilizar para resolver muchos problemas, 
como encontrar el camino más corto entre dos nodos. Por lo tanto, determina el nivel de cada nodo e incluso resolver 
juegos de rompecabezas y laberintos.
____________________________________________________________________________________________________________________________

"""

#Se importar la libreria Queue clase correspondiente del queue módulo.
from queue import Queue

"""
______________________________________________________________________
La clase Esquema contiene una representación gráfica, 
en este caso una matriz de adyacencia, 
y todos los métodos que pueda necesitar cuando trabaje con gráficos.
______________________________________________________________________

""" 

class Esquema:
    
    """     ATRIBUTOS
    VARIABLES
        (tamaño_de_nodos : int) ==> número de nodos del grafo
        (dirigido: boolean) ==> determina si es dirigido o no dirigido
        (m_conexion: int) ==> guarda la secuencia de números 
        (m_agregando_lista: estructura del diccionario) ==> lista de adyacencia
_______________________________________________________________________________________________________________
    
    Siempre que se crea un objeto o instancia de una clase, 
     se llama al constructor (método __init__() en Python) para inicializar los atributos de la instancia.
     La palabra clave punto es para especificar que estamos pasando el valor a los atributos de la instancia y 
     no a la variable o argumento local con el mismo nombre.
_______________________________________________________________________________________________________________     
    
    """
    #Constructor y los atributos del grafo
    def __init__(punto, tamaño_de_nodos, dirigido=True):
        
        """
        Parámetros
            (tamaño_de_nodos: int) ==>  acabamiento de nodos de entrada 
            (dirigido: boolean) ==> correspondencia del grafo 

        """
        #Se inicializa en la variable tamaño_de_nodos
        punto.m_tamaño_de_nodos = tamaño_de_nodos
        #Se inicializa en la variable m_conexion
        punto.m_conexion = range(punto.m_tamaño_de_nodos)
        #Se inicializa en la variable m_dirigido
        punto.m_dirigido = dirigido
        #Se crea la estructura del diccionario de datos
        punto.m_agregando_lista = {union: set() for union in punto.m_conexion}
    
    #Añadiendo borde al grafo
    #Se agrega los parametros en la funcion agregando_arista
    def agregar_arista(punto, nodo1, nodo2, peso=1):
        
        """ Añadiendo Grafos
        Se identifica la llave como identificador para su ingreso de valores.
        Los parámetros son:
        (nodo1: int) ==> correspondiente al primer valor del nodo 
        (node2: int) ==> correspondiente al segundo valor del nodo
        (peso: int) ==> inicializando el valor a 1 
        La condicion de los nodo es que si es falso retornara verdadero para agregar
        la llave del nodo 2 y por el valor del nodo 1
        Si dirigido es falso devolvera True para ingresar como llave el nodo2 y su valor el nodo 1 """        
        
        #Se añade el peso y el nodo
        punto.m_agregando_lista[nodo1].add((nodo2, peso))
        """Si en dirigido corresponde a falso retornara verdadero para ingresar la llave del nodo 2 y el valor en nodo 1
        """
        if not punto.m_dirigido:
            #Se agrega el peso y el nodo
            punto.m_agregando_lista[nodo2].add((nodo1, peso))
    
    #Añadiendo el diccionario
    def print_agregando_lista(self):
        #Se realiza el recorrido
        for key in self.m_agregando_lista.keys():
            #Imprimira el recorrido con el valor y la llave
            print("union", key, ": ", self.m_agregando_lista[key])
    
    #Imprimira el reccorrido BFS
    def interseccion(punto, inicio_vinculo):
        llegadas = set()
        cola = Queue()
        cola.put(inicio_vinculo)
        llegadas.add(inicio_vinculo)
        while not cola.empty():
            union_vigente = cola.get()
            print(union_vigente, end = " ")
            for (proxima_union, weight) in punto.m_agregando_lista[union_vigente]:
                if proxima_union not in llegadas:
                    cola.put(proxima_union)
                    llegadas.add(proxima_union)

"""Se usa para ejecutar el código solo si el archivo se ejecutó directamente y no se importó."""
if __name__ == "__main__":
    g = Esquema(5, determinado=False)

    g.agregar_arista(0, 1)
    g.agregar_arista(0, 2)
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 4)
    g.agregar_arista(2, 3)
    g.print_aproximidad()

    print ("A continuación, la primera travesía en profundidad"
                    " (a partir del vértice 0)")
    
    g.interseccion(0)
    print()