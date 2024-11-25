class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node):
            nonlocal result
            
            queue = deque([node])
            
            while queue:
                curr = queue.popleft()
                neighbour_flower = set()
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
                    else:
                        neighbour_flower.add(result[neighbour - 1])
                
                for i in range(1, 5):
                    if i not in neighbour_flower:
                        result[curr - 1] = i
        
        visited = set()
        result = [None] * n
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
        
        return result
    