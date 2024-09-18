class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        RED = 0
        BLUE = 1
        colors = [-1] * N
        
        def dfs(node, parent):
            
            for neighbour in graph[node]:
                if neighbour != parent:
                    
                    if neighbour in visited:
                        if colors[neighbour] == colors[node]:
                            return False
                        continue
                    
                    if colors[node] == RED:
                        colors[neighbour] = BLUE
                    else:
                        colors[neighbour] = RED
                    
                    visited.add(neighbour)
                    if not dfs(neighbour, node):
                        return False
            
            return True
        
        visited = set()
        for node in range(N):
            if node not in visited:
                visited.add(node)
                colors[node] = RED
                
                if not dfs(node, -1):
                    return False
        
        return True
    