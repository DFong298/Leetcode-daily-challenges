class Graph:
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[0 for i in range(n)] for j in range(n)]
        for e in edges:
            self.adj[e[0]][e[1]] = e[2]

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]][edge[1]] = edge[2]
        
    #not optimal - better to implement floyd-warshall
    def shortestPath(self, node1: int, node2: int) -> int:
        distTo = [float('inf') for _ in range(len(self.adj))]
        distTo[node1] = 0
        q = [(0, node1)]

        while q:
            d, u = heapq.heappop(q)
            if u == node2:
                return d
            if d > distTo[u]: continue

            for v in range(len(self.adj[u])):
                if self.adj[u][v] != 0:
                    alt = d + self.adj[u][v]
                    if alt < distTo[v]:
                        distTo[v] = alt
                        heapq.heappush(q, (distTo[v], v))

        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)