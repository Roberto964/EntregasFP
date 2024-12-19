'''
Created on 19 dic 2024

@author: rober
'''

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from Entrega3.Recorridos import *  # Adáptalo a tu proyecto
from Entrega3.Grafos import Grafo  # Adáptalo a tu proyecto


@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_coromosomas: str

    def __post_init__(self):
        """Método que valida que el número de mutaciones sea válido"""
        if self.num_mutaciones < 0:
            raise ValueError('El número de mutaciones debe ser mayor o igual a 0')

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosomas: str) -> Gen:
        return Gen(nombre, tipo, num_mutaciones, loc_cromosomas)

    @staticmethod
    def parse(file: str) -> list[Gen]:
        genes = []
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"): 
                    continue  # Saltar líneas vacías o comentarios
                parts = line.split(",")
                if len(parts) != 4:
                    raise ValueError(f"Línea mal formateada: {line}")

                nombre, tipo, num_mutaciones, loc_cromosomas = parts
                num_mutaciones = num_mutaciones
                genes.append(Gen.of(nombre.strip(), tipo.strip(), int(num_mutaciones), loc_cromosomas.strip()))
        return genes


@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> RelacionGenAGen:
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(file: str) -> list[RelacionGenAGen]:
        relaciones = []
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  # Saltar líneas vacías o comentarios
                parts = line.split(",")
                if len(parts) != 3:
                    raise ValueError(f"Línea mal formateada: {line}")
                
                nombre_gen1, nombre_gen2, conexion = parts
                conexion = float(conexion)
                relaciones.append(RelacionGenAGen.of(nombre_gen1.strip(), nombre_gen2.strip(), conexion))
        return relaciones


class RedGenica(Grafo[Gen, RelacionGenAGen]):
    """
    Representa una red genética basada en un grafo.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> RedGenica:
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> RedGenica:
        red_genica = RedGenica.of(es_dirigido=es_dirigido)
        
        # Parsear genes desde el archivo f1
        for line in open(f1):
            ls = line.strip('\n').split(',')
            red_genica.genes_por_nombre[ls[0]] = Gen.of(ls[0], ls[1], int(ls[2]), ls[3])
            red_genica.add_vertex(red_genica.genes_por_nombre[ls[0]])

        # Parsear relaciones desde el archivo f2
        for line in open(f2):
            ls = line.strip('\n').split(',')
            gen1 = red_genica.genes_por_nombre[ls[0]]
            gen2 = red_genica.genes_por_nombre[ls[1]]
            conexion = float(ls[2])
            relacion = RelacionGenAGen.of(ls[0], ls[1], int(conexion))
            red_genica.add_edge(gen1, gen2, relacion)
        
        return red_genica


if __name__ == '__main__':
    raiz = '../../'  # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = RedGenica.parse(raiz + 'resources/genes.txt', raiz + 'resources/red_genes.txt', es_dirigido=False)

    # Imprimir el camino más corto entre dos genes (esto depende de cómo implementes bfs y subgraph)
    print("El camino más corto entre gen1 y gen2 es:")
    camino = bfs(rrss, rrss.genes_por_nombre['Gen1'], rrss.genes_por_nombre['Gen2'])
    print(camino)





















