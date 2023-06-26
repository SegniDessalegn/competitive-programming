class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = {(i, j): 0 for j in range(n) for i in range(m)}
        dp[(m - 1, n - 1)] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1
        for j in range(n - 2, -1, -1):
            prev = dp[(m - 1, j + 1)]
            needed = prev - dungeon[m - 1][j]
            needed = max(1, needed)
            dp[(m - 1, j)] = needed
        
        for i in range(m - 2, -1, -1):
            prev = dp[(i + 1, n - 1)]
            needed = prev - dungeon[i][n - 1]
            needed = max(1, needed)
            dp[(i, n - 1)] = needed
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                bottom = dp[(i + 1, j)]
                right = dp[(i, j + 1)]
                needed = min(bottom, right) - dungeon[i][j]
                needed = max(1, needed)
                dp[(i, j)] = needed
        
        return dp[(0, 0)]