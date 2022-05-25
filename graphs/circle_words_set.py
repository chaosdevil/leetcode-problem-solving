# define alphabet size for graph vertices
CHAR_SIZE = 128
 
 
# A class to represent a graph object
class Graph:
    def __init__(self, N, edges=[]):
        # resize the list to hold `N` elements
        self.adj = [[] for _ in range(N)]
 
        # add an edge from source to destination
        for edge in edges:
            self.addEdge(edge[0], edge[1])
 
    # Function to add an edge `u —> v` to the graph
    # and update in-degree for each edge
    def addEdge(self, u, v):
        self.adj[u].append(v)
 
 
# Function to perform DFS traversal on the graph
def DFS(graph, v, discovered):
    discovered[v] = True        # mark the current node as discovered
 
    # do for every edge `v —> u`
    for u in graph.adj[v]:
        if not discovered[u]:   # `u` is not discovered
            DFS(graph, u, discovered)
 
 
# Function to create transpose of a graph
def transpose(graph, N):
    g = Graph(N)
 
    # for every edge `u —> v`, create a reverse edge `v —> u`
    for u in range(N):
        for v in graph.adj[u]:
            g.addEdge(v, u)
 
    return g
 
 
# Function to check if all non-isolated vertices in a graph are discovered
def isdiscovered(graph, discovered):
    for i in range(len(discovered)):
        if len(graph.adj[i]) and not discovered[i]:
            return False
    return True
 
 
# Function to check if all non-isolated vertices in a graph belong to a
# single strongly connected component
def isSC(graph, N):
 
    # keep track of all previously discovered vertices
    discovered = [False] * N
 
    # start DFS from the first vertex `i` with a non-zero degree
    for i in range(N):
        if len(graph.adj[i]):
            DFS(graph, i, discovered)
            break
 
    # return false if DFS could not explore all non-isolated vertices
    if not isdiscovered(graph, discovered):
        return False
 
    # reset the discovered vertices array for another DFS call
    discovered[:] = [False] * N
 
    # create a transpose graph with the direction of every edge reversed
    g = transpose(graph, N)
 
    # perform DFS on the transpose graph using the same starting vertex `i`
    DFS(g, i, discovered)
 
    # check if the second DFS also explored all non-isolated vertices
    return isdiscovered(g, discovered)
 
 
# Function to check if a given set of words can be rearranged to form a circle
def checkArrangement(words):
 
    # create a directed graph with the same number of nodes as the alphabet size
    graph = Graph(CHAR_SIZE)
 
    # create an empty array to store in-degree for each vertex
    # assign in-degree 0 to each vertex
    indegree = [0] * CHAR_SIZE
 
    # process each word
    for s in words:
        src = ord(s[0])
        dest = ord(s[-1])
 
        # add an edge to the graph from the first character to the last character
        graph.addEdge(src, dest)
 
        # increment the in-degree of the destination vertex by 1
        indegree[dest] += 1
 
    '''
        If the constructed graph has an Eulerian cycle, only then can the given words
        be rearranged to form a circle
    '''
 
    # 1. Check if every vertex has the same in-degree and out-degree
    for i in range(CHAR_SIZE):
        if len(graph.adj[i]) != indegree[i]:
            return False
 
    # 2. Check if all non-isolated vertices belong to a single
    # strongly connected component
    return isSC(graph, CHAR_SIZE)
 
 
if __name__ == '__main__':
 
    words = list(map(str,input().split()))
    print(str(checkArrangement(words)).lower())
 