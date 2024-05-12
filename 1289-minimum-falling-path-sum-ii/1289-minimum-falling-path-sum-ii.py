class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        @cache
        def dp(i, j):
            if not(0 <= j < N):
                return float("inf")
            
            if i == N - 1:
                return grid[i][j]
            
            recieved = float("inf")
            for k in range(N):
                if k != j:
                    recieved = min(recieved, dp(i + 1, k))
            
            curr = grid[i][j]
            
            if recieved != float("inf"):
                curr += recieved
            
            return curr
        
        ans = float("inf")
        for j in range(N):
            ans = min(ans, dp(0, j))
        
        return ans
    