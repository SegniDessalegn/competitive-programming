class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        distances = [[float("inf")] * N for _ in range(N)]
        distances[0][0] = grid[0][0]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]
        while heap:
            dist, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if 0 <= r < N and 0 <= c < N and max(grid[r][c], dist) < distances[r][c]:
                    heapq.heappush(heap, (max(grid[r][c], dist), r, c))
                    distances[r][c] = max(grid[r][c], dist)
        
        return distances[N - 1][N - 1]