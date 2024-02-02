class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        distances = defaultdict(lambda: float("inf"))
        distances[(0, 0)] = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        heap = [(0, 0, 0, 0)]
        
        while heap:
            ops, d, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < m and 0 <= c < n and ops + grid[r][c] <= k and d + 1 < distances[(r, c)]:
                    distances[(r, c)] = d + 1
                    heapq.heappush(heap, (ops + grid[r][c], distances[(r, c)], r, c))
        
        return distances[(m - 1, n - 1)] if distances[(m - 1, n - 1)] != float("inf") else -1
    