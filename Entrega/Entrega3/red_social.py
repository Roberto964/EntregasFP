'''
Created on 28 nov 2024

@author: rober
'''
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from Entrega3.Recorridos import * #from grafos.recorridos import * --> Adáptalo a tu proyecto
from Entrega3.Grafos import Grafo#from grafos.grafo import * --> Adáptalo a tu proyecto


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni,nombre,apellidos,fecha_nacimiento)
    
    def __str__(self) -> str:
        elementos:str=(f'{self.dni}-{self.nombre}')
        return elementos

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)
    
    def __str__(self) -> str:
        return (f'{self.id} - días activa: {self.dias_activa} - número de iteracciones {self.interacciones}')
#{id} - días activa: {dias_activa} - num interacciones {interacciones}

class Red_social(Grafo[Usuario, Relacion]):
    """
    Representa una red social basada en el grafo genérico.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una nueva Red Social.
        
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.
        
        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        """
        red = Red_social(es_dirigido)

        with open(f1,"r",encoding='utf-8') as f:
            for linea in f:
                dni, nombre, apellidos, fecha_nacimiento = linea.strip().split(",")
                usuario = Usuario(dni=dni, nombre=nombre, apellidos=apellidos, fecha_nacimiento=date.fromisoformat(fecha_nacimiento))
                red.usuarios_dni[dni] = usuario
                red.add_vertex(usuario)
    
        with open(f2,"r",encoding='utf-8') as s:
            for linea in s:
                origen, destino, interacciones, dias_activa = linea.strip().split(",")
                usuario_origen = red.usuarios_dni[origen]
                usuario_destino = red.usuarios_dni[destino]
                relacion = Relacion.of(int(interacciones), int(dias_activa))
                red.add_edge(usuario_origen, usuario_destino, relacion)
    
        return red
        """
        
        rs = Red_social.of(es_dirigido=es_dirigido)
        
        for line in open(f1):
            ls = line.strip('\n').split(',')
            fecha = (datetime.strptime(ls[3],'%Y-%m-%d'))
            rs.usuarios_dni |= {ls[0]:Usuario.of(ls[0],ls[1],ls[2],fecha)}
            rs.add_vertex(Usuario.of(ls[0],ls[1],ls[2],fecha))
        
        for line in open(f2):
            ls = line.strip('\n').split(',')
            rs.add_edge(rs.usuarios_dni[ls[0]],rs.usuarios_dni[ls[1]],Relacion.of(ls[2],fecha))
        
        return rs     
                
if __name__ == '__main__':
    raiz = '../../' # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(raiz+'resources/usuarios.txt', raiz+'resources/relaciones.txt', es_dirigido=False)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    print(camino)
    g_camino = rrss.subgraph(set(camino))
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: str(e.id))
        
