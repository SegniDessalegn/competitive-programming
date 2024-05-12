class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[0] * N for _ in range(N)]
        dp[-1] = grid[-1][:]
        
        def get_mins(arr):
            idx1 = 0
            idx2 = 1

            if arr[1] < arr[0]:
                idx1 = 1
                idx2 = 0
            
            for i in range(2, len(arr)):
                if arr[i] <= arr[idx1]:
                    idx2 = idx1
                    idx1 = i
                elif arr[i] < arr[idx2]:
                    idx2 = i

            return (idx1, idx2)
        
        for i in range(N - 2, -1, -1):
            idx1, idx2 = get_mins(dp[i + 1])
            for j in range(N - 1, -1, -1):
                if j != idx1:
                    dp[i][j] = grid[i][j] + dp[i + 1][idx1]
                else:
                    dp[i][j] = grid[i][j] + dp[i + 1][idx2]
                
        return min(dp[0])
    