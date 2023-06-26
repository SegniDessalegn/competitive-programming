class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def count(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            
            right = count(i, j + 1)
            bottom = count(i + 1, j)
            dp[(i, j)] = right + bottom
            return dp[(i, j)]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}
        return count(0, 0)