class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(n):
                curr_min = float("inf")
                for k in range(n):
                    curr_min = min(curr_min, dp[i - 1][k] + moveCost[grid[i - 1][k]][j])
                dp[i][j] += curr_min
        
        return min(dp[m - 1])