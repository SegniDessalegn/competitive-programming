class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        dp = defaultdict(lambda: float("inf"))
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            dp[(u, v)] = w
            dp[(v, u)] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        dp[(i, j)] = 0
                    else:
                        dp[(i, j)] = min(dp[(i, j)], dp[(i, k)] + dp[(k, j)])
        
        ans = -1
        min_count = n
        for i in range(n):
            curr_count = 0
            for j in range(n):
                if dp[(i, j)] <= distanceThreshold:
                    curr_count += 1
            
            if curr_count <= min_count:
                min_count = curr_count
                ans = i
        
        return ans
    