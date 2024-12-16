'''
Created on 28 nov 2024

@author: rober

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List, Set, Optional
from Entrega3.Grafos import Grafo#from grafos.grafo import Grafo --> Adáptalo a tu proyecto
from Entrega2.Clases import Cola,Pila#from estructuras.Estructuras import Pila,Cola --> Adáptalo a tu proyecto


# Importa la clase Grafo desde su módulo

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
    """
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino usando una Cola.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados= set()
    cola:Cola=Cola()
    cola.add(inicio)
    predecesores:dict[V,Optional[V]]={inicio:None}
    recorrido:str='Forward'
    while not cola.is_empty():
        vertice=cola.remove()
        print(vertice)
        if vertice==destino:
            break
        if vertice not in visitados:
            visitados.add(vertice)
            for vecino in grafo.successors(vertice, recorrido):
                print(vecino)
                if vecino not in visitados:
                    cola.add(vecino)
                    predecesores[vecino]=vertice
    return reconstruir_camino(predecesores, destino)
                        
    

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    return reconstruir_camino(predecesores, destino)
    """
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino usando una Pila.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados = set()
    pila:Pila = Pila()
    pila.add(inicio)
    predecesores:dict[V,Optional[V]] = {inicio:None}
    Back:str='Back'
    while pila:
        vertice= pila.remove()
        if vertice == destino:
            break
        if vertice not in visitados:
            visitados.add(vertice)
            for vecino in grafo.successors(vertice,Back):
                if vecino not in visitados:
                    pila.add(vecino)
                    predecesores[vecino]=vertice
    return reconstruir_camino(predecesores, destino)
            

def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    """
    función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino
    """
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    
    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """
    camino:list[V]=[]
    vertice_actual:Optional[V]=destino
    
    while vertice_actual is not None:
        camino.insert(0, vertice_actual)
        vertice_actual=predecesores.get(vertice_actual)
        
    return camino



if __name__ == '__main__':

    predecesores={"A":None,"B":'A',"C":'A',"C":'B'}
    
    print(reconstruir_camino(predecesores, "C"))
    
    
    