class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        
        dp = [[0] * N for _ in range(M)]
        dp[M - 1][N - 1] = 1 if dungeon[M - 1][N - 1] > 0 else -dungeon[M - 1][N - 1] + 1
        for j in range(N - 2, -1, -1):
            prev = dp[M - 1][j + 1]
            if dungeon[M - 1][j] > 0:
                prev -= dungeon[M - 1][j]
                dp[M - 1][j] = max(1, prev)
            else:
                dp[M - 1][j] = -dungeon[M - 1][j] + prev
        
        for i in range(M - 2, -1, -1):
            prev = dp[i + 1][N - 1]
            if dungeon[i][N - 1] > 0:
                prev -= dungeon[i][N - 1]
                dp[i][N - 1] = max(1, prev)
            else:
                dp[i][N - 1] = -dungeon[i][N - 1] + prev
        
        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                bottom = dp[i + 1][j]
                right = dp[i][j + 1]
                needed = min(bottom, right) - dungeon[i][j]
                needed = max(1, needed)
                dp[i][j] = needed
        
        return dp[0][0]
