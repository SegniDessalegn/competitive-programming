class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i = 0, j = 0):
            if i >= len(triangle):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = min(dp(i + 1, j), dp(i + 1, j + 1)) + triangle[i][j]
            return memo[(i, j)]

        return dp()
