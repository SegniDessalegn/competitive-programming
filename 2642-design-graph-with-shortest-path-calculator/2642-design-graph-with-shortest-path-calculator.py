class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        
        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))
    
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        distance = {node: float("inf") for node in range(self.n)}
        distance[node1] = 0
        heap = [(0, node1)]
        
        while heap:
            cost, node = heapq.heappop(heap)
            for neighbour, ncost in self.graph[node]:
                ccost = cost + ncost
                if ccost < distance[neighbour]:
                    heapq.heappush(heap, (ccost, neighbour))
                    distance[neighbour] = ccost
        
        return distance[node2] if distance[node2] != float("inf") else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)