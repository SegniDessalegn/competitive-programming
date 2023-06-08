class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid[0])
        for g in grid:
            left, right = 0, n - 1
            while left <= right:
                i = (left + right) // 2
                if g[i] >= 0:
                    left = i + 1
                else:
                    right = i - 1
            res += (n - left)
        return res