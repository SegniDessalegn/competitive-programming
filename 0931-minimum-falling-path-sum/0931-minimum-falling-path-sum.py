class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [matrix[0][j] for j in range(N)]
        
        for i in range(1, N):
            new_dp = []
            for j in range(N):
                new_dp.append(matrix[i][j] + min(dp[max(0, j - 1)], dp[j], dp[min(N - 1, j + 1)]))
            dp = new_dp
        
        return min(dp)