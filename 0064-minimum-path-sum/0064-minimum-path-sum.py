class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def recur(r, c):
            if r == m or c == n:
                return float("inf")
            if r == m - 1 and c == n - 1:
                return grid[m - 1][n - 1]
            
            ans = grid[r][c] + min(recur(r + 1, c), recur(r, c + 1))
            return ans
        
        m = len(grid)
        n = len(grid[0])
        return recur(0, 0)