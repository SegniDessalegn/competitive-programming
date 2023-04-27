class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.graph = {i:[] for i in range(n)}
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.restricted = set(restricted)
        return 1 + self.count_reachables(0, set([0]))
    
    def count_reachables(self, node, visited):
        count = 0
        for n in self.graph[node]:
            if n not in visited and n not in self.restricted:
                visited.add(n)
                count += 1 + self.count_reachables(n, visited)
        return count