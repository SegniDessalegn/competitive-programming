class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        max_length = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    max_length = max(max_length, dp[i][j])
        
        return max_length * max_length
    