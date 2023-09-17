class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # floyd warshal's algorithm and bitmask dynamic programming
        
        N = len(graph)
        distance = [[float("inf")] * N for _ in range(N)]
        for i in range(N):
            distance[i][i] = 0
            for j in graph[i]:
                distance[i][j] = 1
                distance[j][i] = 1
        
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        @cache
        def get_ans(curr, used):
            if used == (1 << N) - 1:
                return 0
            
            count = float("inf")
            for node in range(N):
                if not (used & (1 << node)):
                    count = min(count, distance[curr][node] + get_ans(node, used | (1 << node)))
            
            return count
        
        ans = float("inf")
        for start in range(N):
            ans = min(ans, get_ans(start, 0))
        
        return ans