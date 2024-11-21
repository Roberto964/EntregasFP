'''
Created on 21 nov 2024

@author: rober
'''
from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

E = TypeVar('E')

# Supongo que Agregado_lineal es una clase que tienes en el módulo Entrega2.Clases
# Si no es así, tendrás que ajustar la importación.
from Entrega2.Clases import Agregado_lineal

class ColaConLimite(Agregado_lineal):
    def __init__(self, capacidad: int):
        if capacidad <= 0:
            raise ValueError("NO puede ser cero la capacidad.")
        self._elements: List[E] = []
        self.capacidad = capacidad

    def add(self, e: E):
        
        if len(self._elements) >= self.capacidad:
            raise OverflowError("La Cola está llena.")
        self._elements.append(e)
    
    def is_full(self):
        return len(self.cola) == self.capacidad
    

    @classmethod
    def of(cls, capacidad: int) -> ColaConLimite:
        return cls(capacidad)

    def __str__(self):
        return f"Cola: {self._elements} (Capacidad: {self.capacidad})"
    
    
    
class Agregados_lineal(ABC, Generic[E]):
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
    
    def contains(self, e:E):
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]):
        for elemento in self._elements:
            if func(elemento):
                return elemento
        return None
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        return [elemento for elemento in self._elements if func(elemento)]
        
    
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
    
#hasta aqui el codigo ahora pasamos a realizar las pruebas 
    def test_cola_con_limite():
        cola = ColaConLimite.of(3)
        cola.add("Tarea 1")
        cola.add("Tarea 2")
        cola.add("Tarea 3")
        try:
            cola.add("Tarea 4")  
        except OverflowError as e:
            print(e) 
        print(cola)
        print(cola.remove())
        print(cola)
        print(cola.remove())
        print(cola)
        print(cola.remove())
        print(cola)
        try:
            cola.remove() 
        except IndexError as e:
            print(e)

    if __name__ == '__main__':
        test_cola_con_limite()
        
        