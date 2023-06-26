class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        def recur(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            ans = [0 for _ in range(k)]
            for dx, dy in directions:
                r, c = i + dx, j + dy
                if r < m and c < n:
                    rems = recur(r, c)
                    for idx in range(k):
                        ans[(idx + grid[i][j]) % k] += rems[idx] % (10 ** 9 + 7)
            dp[(i, j)] = ans
            return ans
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1)]
        dp = {(m - 1, n - 1): [0 for _ in range(k)]}
        dp[(m - 1, n - 1)][grid[m - 1][n - 1] % k] = 1
        return recur(0, 0)[0] % (10 ** 9 + 7)