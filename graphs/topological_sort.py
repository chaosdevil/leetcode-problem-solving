# topological sorting

from collections import defaultdict
from typing import List

class Graph:
    def __init__(self, V) -> None:
        self.adj_list = defaultdict(list)
        self.vertices = V

    def add_edge(self, u, v):
        self.adj_list[u].append(v)


def topological_sort(g: Graph):
    stack = []
    visited = [False] * g.vertices
    for n in range(g.vertices):
        if not visited[n]:
            dfs(g.adj_list, n, stack, visited)
    return stack[::-1]

def dfs(adj_list: dict, current: int, stack: list, visited: list):
    # plan : depth-first search
    
    visited[current] = True

    # check neighbors of current vertex
    for neighbor in adj_list[current]:
        if not visited[neighbor]:
            dfs(adj_list, neighbor, stack, visited)
    stack.append(current)


if __name__ == "__main__":
    V = 6
    graph = Graph(6)

    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)

    print(topological_sort(graph))
