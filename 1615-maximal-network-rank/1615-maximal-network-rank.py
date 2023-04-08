class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = set()
        for i in range(len(roads)):
            edges.add(tuple(roads[i]))
        
        graph = defaultdict(int)
        for node, neighbour in edges:
            graph[node] += 1
            graph[neighbour] += 1
        
        maximal = 0
        for node1 in graph:
            for node2 in graph:
                if node1 != node2:
                    rank = graph[node1] + graph[node2]
                    if (node1, node2) in edges or (node2, node1) in edges:
                        rank -= 1
                    maximal = max(maximal, rank)
        
        return maximal