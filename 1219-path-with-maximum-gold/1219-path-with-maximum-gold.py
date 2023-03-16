class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backTracking(i, j, total, visited):
            nonlocal ans
            ans = max(ans, total)
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0 or (x, y) in visited:
                        continue
                    total += grid[x][y]
                    visited.add((x, y))
                    if backTracking(x, y, total, visited):
                        return True
                    total -= grid[x][y]
                    visited.remove((x, y))
        
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    backTracking(i, j, grid[i][j], set([(i, j)]))
        
        return ans