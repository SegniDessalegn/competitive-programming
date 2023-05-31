class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        def recur(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            dp[(i, j)] = recur(i, j + 1) + recur(i + 1, j)
            return dp[(i, j)]
        
        return recur(0, 0)