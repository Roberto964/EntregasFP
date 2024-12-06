'''
Created on 28 nov 2024

@author: rober
'''

from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx#da error no se por qué, voy a terminar y si me da erro pregunto al profesor

# Definición de tipos genéricos
V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    """
    Representaciónde un grafo utilizando un diccionario de adyacencia.
    """
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}  # Diccionario de adyacencia son los vertices
    
    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
        """
        Método de factoría para crear un nuevo grafo.
        
        :param es_dirigido: Indica si el grafo es dirigido (True) o no dirigido (False).
        :return: Nuevo grafo.
        """
        return Grafo(es_dirigido)

    def add_vertex(self, vertice: V) -> None:
        """
        Añade un vértice al grafo si no existe.
        
        :param vertice: Vértice a añadir.
        """
        if not vertice in self.adyacencias:
            self.adyacencias[vertice] = {}

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        """
        Añade una arista al grafo entre dos vértices.
        Si el grafo es no dirigido, añade la arista en ambos sentidos.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :param arista: Arista a añadir.
        """
        if origen not in  self.adyacencias:
            self.adyacencias[origen]={}
            
        if destino not in self.adyacencias:
            self.adyacencias[destino]={}
        
        self.adyacencias[origen][destino] = arista#une el vertice del q sale([origen]) con el vertice al q se dirige([destino]) 
        

    def successors(self, vertice: V, recorrido:str = 'Forward') -> Set[V]:#preguntar al profesor como elijo el recorrido
        """
        Devuelve los sucesores de un vértice.
        
        :param vertice: Vértice del que se buscan los sucesores.
        :return: Conjunto de sucesores.
        """
        
        if vertice not in self.adyacencias:
            raise ValueError('No está')
        
        if recorrido == 'Forward':
            return set(self.adyacencias[vertice])
        
        if recorrido == 'Back':
            return { i for i,siguiente in self.adyacencias.items() if vertice in siguiente}
        
        else:
            raise ValueError('Tiene que ser Forward o back')
        """
        #Esquema de la manera clasica del recorrido back#
        b=set()
        for i,siguiente in self.adyacencias.items():
            if vertice in siguiente:
                b.add(i)
        return b
        """
                

    def predecessors(self, vertice: V) -> Set[V]:
        """
        Devuelve los predecesores de un vértice.
        
        :param vertice: Vértice del que se buscan los predecesores.
        :return: Conjunto de predecesores.
        """
        """
        Manera clasica de hacerla y de ahi saco la manera por comprensión
        siguientes = set()
        if self.es_dirigido:
            for i,continuos in self.adyacencias.items():
                if vertice in continuos:
                    siguientes.add(i)
        else:
            raise ValueError('El grafo debe sesr dirigido')
        
        return siguientes
        """
        if self.es_dirigido:
            return {i for i,continuos in self.adyacencias.items() if vertice in continuos}
        else:
            raise ValueError('El grafo debe sesr dirigido')  
            

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        """
        Devuelve el peso de la arista entre dos vértices.
        
        :param origen: Vértice de origen(source).
        :param destino: Vértice de destino(target).
        :return: Peso de la arista, o None si no existe.
        """
        if origen in self.adyacencias and destino in self.adyacencias[destino]:
                return self.adyacencias[origen][destino]#muestra el peso de la arista entre ambos vertices
        else:
            raise ValueError('No existe una arista entre ambos vértices')
            

    def vertices(self) -> Set[V]:
        """
        Devuelve el conjunto de vértices del grafo.
        
        :return: Conjunto de vértices.
        """
        return set(self.adyacencias)
    
    def edge_exists(self, origen: V, destino: V) -> bool:
        """
        Verifica si existe una arista entre dos vértices.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: True si existe la arista, False en caso contrario.
        """
        if origen in self.adyacencias and destino in self.adyacencias[origen]:
            return True
        else:
            return False

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        """
        Crea un subgraph basado en un conjunto de vértices.
        
        :param vertices: Conjunto de vértices del subgraph.
        :return: Nuevo grafo con los vértices y aristas correspondientes.
        """
        subgrafo = Grafo[V,E]()#creo una instancia:sirve para poder usar las propiedades del metodo grafo en el subgrafo
        for origen in vertices:#nos aseguramos de q el vertice está en el grafo original
            if origen in self.adyacencias:#recorremos los vertices en la lista de self.adyacencias
                for destino,peso in self.adyacencias[origen].items():
                    if destino in vertices:
                        subgrafo.add_edge(origen, destino, peso)
                
        return subgrafo

    def inverse_graph(self) -> Grafo[V, E]:
        """
        Devuelve el grafo inverso (solo válido para grafos dirigidos).
        
        :return: Grafo inverso.
        :raise ValueError: Si el grafo no es dirigido.
        """
        inverso=Grafo[V,E]()#vuelvo a crear una instancia
        if not self.es_dirigido:
            raise ValueError('El grafo debe de ser dirigido')
    
        for origen in self.adyacencias:
            for destino,peso in self.adyacencias[origen].items():
                inverso.add_edge(destino,origen,peso)
        return inverso
            
            
    def draw(self, titulo: str = "Grafo", 
            lambda_vertice: Callable[[V], str] = str, 
            lambda_arista: Callable[[E], str] = str) -> None:
        """
        Dibuja el grafo utilizando NetworkX y Matplotlib. las funciones lambda permiten personalizar la representación
        de los vértices y aristas.
        
        :param titulo: Título del gráfico
        :param lambda_vertice: Función lambda para representar los vértices
        :param lambda_arista: Función lambda para representar las aristas
        """
        # Crear un grafo de NetworkX
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        # Añadir nodos y aristas
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))  # Usamos lambda_vertice para personalizar el nodo
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))  # Usamos lambda_arista para personalizar la arista
    
        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Distribución de los nodos
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))  # Usamos las etiquetas personalizadas de los vértices
    
        # Dibujar las etiquetas de las aristas (con la representación personalizada)
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()

        
    def __str__(self) -> str:
        """
        Representación textual del grafo.
        
        Formato libre. Por ejemplo:
            vertice1 -> vertice2 (peso), vertice3 (peso)
            vertice2 -> vertice1 (peso)
            ...
        """
        resultado=[]
        for origen,destinos in self.adyacencias.items():
            conexion:list[str]=[]
            for destino,peso in destinos.items():
                conexion.append(f'{destino},{peso}')
            resultado.append(f'{origen}->{",".join(conexion)}')
        return "\n".join(resultado)
                
                

if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo:Grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_vertex("E")
    grafo.add_vertex("F")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    grafo.add_edge("C", "B", 2)
    grafo.add_edge("F", "B", 4)
    grafo.add_edge("E", "C", 8)
    grafo.add_edge("D", "C", 7)
    grafo.add_edge("A", "D", 9)
    print(grafo)
    # Dibujar el grafo
    #grafo.draw(titulo="Mi Grafo Dirigido")
    
    grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
