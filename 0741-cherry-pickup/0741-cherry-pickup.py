class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        def recur(r1, c1, c2):
            r2 = r1 + c1 - c2
            if n in [r1, r2, c1, c2] or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            if r1 == c1 == n - 1:
                return grid[r1][c1]
            if memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            ans += max(recur(r1, c1+1, c2+1), recur(r1+1, c1, c2+1), recur(r1, c1+1, c2), recur(r1+1, c1, c2))
            memo[r1][c1][c2] = ans
            return ans
        
        n = len(grid)
        memo = [[[None for _ in range(n)] for __ in range(n)] for __ in range(n)]
        return max(0, recur(0, 0, 0))