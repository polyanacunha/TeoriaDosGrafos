from __future__ import annotations
from dataclasses import dataclasses

@dataclasses
class Edge:
    u: int
    v: int

def reversed(self) -> Edge:
    return Edge(self.v,self.u)

def __str__(self) -> str:
    return f"{self.u} -> {self.v}"



