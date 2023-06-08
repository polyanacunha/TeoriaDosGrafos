from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

@property
def vertex_count(self) -> int:
    return len(self._vertices) #número de vertices

@property
def edge_count(self) -> int:
    return sum(map(len,self._edges)) # número de arestas

# Adiciona um vértice ao grafo e devolve o seu índice
def add_vertex(self, vertex: V) -> int:
    self._vertices.append(vertex)
    self._edges.append([])
    return self.vertex_count - 1 # devolve o índice do vétice adicionado

# Como este é um grafo não direcionado devemos adicionar as arestas nas duas direções.
def add_edge(self, edge: Edge) -> None:
    self._edges[edge.u].append(edge)
    self._edges[edge.v].append(edge.reversed())

# Adiciona uma aresta usando índices dos vértices

def add_edge_by_indices(self, u : int, v : int ) -> None:
    edge: Edge = Edge(u, v)
    self.add_edge(edge)

# Adiciona uma aresta consultando os índices dos vértices
def add_edge_by_vertices(self, first: V, second: V) -> None:
    u: int = self._vertices.index(first)
    v: int = self._vertices.index(second)
    self.add_edge_by_indices(u, v)

# Encontra o vértice em um índice específico
def vertex_at(self, index: int) -> V:
    return self._vertices[index]

# Encontra o índice de um vértice no grafo
def index_of(self, vertex: V) -> int:
    return self._vertices.index(vertex)

# Encontra os vértices aos quais um vértice com determinado índice está conectado
def neighbors_for_index(self, index: int) -> List[V]:
    return list(map(self.vertex_at,[e.v for e in self._edges[index]]))

# Consulta o índice de um vértice e encontra seus vizinhos 
def neighbors_for_vertex(self, vertex: V) -> List[V]:
    return self.neighbors_for_index(self.index_of(vertex))

# Devolve todas as arestas associadas a um vértice em um índice
def edges_for_index(self, vertex: V) -> list[Edge]:
    return self.edges_for_index(self.index_of(vertex))

# Consulta o índice de um vértice e devolve suas arestas 
def edges_for_vertex(self, vertex: V) -> List[Edge]:
    return self.edges_for_index(self.index_of(vertex))

# facilita a exibição elegante de um Graph
def __str__(self) -> str:
    desc: str = ""
    for i in range(self.vertex_count):
        desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
    return desc