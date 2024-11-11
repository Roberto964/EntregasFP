'''
Created on 9 nov 2024

@author: rober
'''
from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod


# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P',int,float)

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements



class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        for i in range(len(self._elements)):
            if i ==self._elements[i]:
                return i
                break
        return len(self._elements)
        
                
            
    def add(self, e: E) -> None:
        index:int = self.__index_order(e)
        self._elements.insert(index,e)
        
        


class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        for i in range(len(self._elements)):
            if i ==self._elements[i]:
                return i
                break
        return int(i)
    
    def add(self, e: E) -> None:
        index:int = self.__index_order(e)
        self._elements.insert(index,e)
        



class Cola(Agregado_lineal[E]):
    
    def __init__(self):
        super().__init__()
    
    @classmethod
    def of(cls) -> 'Cola[E]':
        return cls()
        

    def add(self, e: E) -> None:
        self._elements.append(e)
    
    def remove(self)->E:
        if not self._elements:
            raise IndexError('La lista está vacía')
        return self._elements.pop(0)
    
    def __str__(self) -> str:
        elementos = ', '.join(str(e) for e in self._elements)
        return f'Cola({elementos})'
        


class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._prioridades: List[P] = []
        
    @property
    def size(self) -> int:
        return len(self._elements)
        

    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        :return: Boolean
        """
        return self.size == 0
        

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """
        return self._elements.copy()
        
    def add(self, e: E, priority: P) -> None:
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        index = self.__index_order(priority)
        self._elements.insert(index,e)
        self._prioridades.insert(index,priority)
        
        

    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.#pop
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        while self.is_empty():
            raise IndexError('La cola está vacía')
        return self._elements.pop(0)
    
    def remove_all(self)->List[E]:#te devuelve una lista de los elementos eliminados
        eliminado:List[E] = []#lista con los elementos eliminados
        while not self.is_empty():#si NO está vacia añade los elementos eliminados a la lista de E
            eliminado.append(self.remove())#añade los elementos eliminados
        return eliminado#te devuelve la lista vacia si la lista esta vacia
            
        
            
    def __index_order(self, priority: P) -> int:
        for index, current_priority in enumerate(self._prioridades):
            if priority < current_priority:
                return index
        return len(self._prioridades)
            
        

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.#Aqui usamos de nuevo el algo.add
        :param ls: Lista de tuplas (elemento, prioridad)
        """
        for e1, p1 in ls:
            self.add(e1,p1)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index:int = self._elements.index(e)
            current_priority:P = self._prioridades[index]
            
            if new_priority < current_priority:
                # Remover el elemento y su prioridad actuales
                self._elements.pop(index)
                self._prioridades.pop(index)
                # Añadir el elemento con la nueva prioridad
                self.add(e, new_priority)
                
    def __str__(self) -> str:
        elementos = ", ".join(f'{e}, {p}' for e, p in zip(self._elements, self._prioridades))
        return f'La Cola prioridad es: [{elementos}]'




class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.
    
    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def of(cls)->Pila[E]:
        return cls(Pila[E])
    
    def add(self,e:E)->None:
        self._elements.insert(0,e)
        
#order = lambda x : -x
#miLista = Lista_ordenada(order)
#miLista.add(3)
#print(miLista._elements)

#miCola:Cola_prioridad = Cola_prioridad()
#miCola.add_all([('perro',1),('gato',2),('leon',7),('lobo',5)])
##print(miCola)

