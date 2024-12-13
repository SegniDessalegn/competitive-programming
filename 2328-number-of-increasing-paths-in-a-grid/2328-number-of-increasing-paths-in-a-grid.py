class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        @cache
        def traverse(i, j):
            count = 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if (0 <= ni < M) and (0 <= nj < N) and grid[ni][nj] > grid[i][j]:
                    count += traverse(ni, nj)
                    count %= MOD
            
            return count
        
        M = len(grid)
        N = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        MOD = 10 ** 9 + 7
        count = 0
        for i in range(M):
            for j in range(N):
                count += traverse(i, j)
                count %= MOD
        
        return count
    