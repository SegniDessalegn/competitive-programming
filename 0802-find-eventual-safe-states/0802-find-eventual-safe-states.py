class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # topological sort using graph coloring
        
        n = len(graph)
        color = [0 for _ in range(n)]
        order = []
        def dfs(i):
            if color[i] == 1:
                return False
            color[i] = 1
            for j in graph[i]:
                if color[j] != 2:
                    if not dfs(j):
                        return False
            color[i] = 2
            return True
        
        for i in range(n):
            if dfs(i):
                order.append(i)
        
        return sorted(order)