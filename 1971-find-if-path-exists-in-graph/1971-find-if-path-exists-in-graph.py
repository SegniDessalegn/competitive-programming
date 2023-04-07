class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for node, neighbour in edges:
            graph[node].add(neighbour)
            graph[neighbour].add(node)
        
        queue = deque([source])
        visited = set([source])
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return False