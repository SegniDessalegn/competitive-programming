class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        dp = [[0 for _ in range(N + 1)] for __ in range(M + 1)]
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        result = 0
        for i in range(M + 1):
            for j in range(N + 1):
                result += dp[i][j]
        
        return result
    