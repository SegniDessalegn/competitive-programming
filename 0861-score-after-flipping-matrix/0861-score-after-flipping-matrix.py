class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 0:
                grid[i] = [0 if grid[i][j] == 1 else 1 for j in range(cols)]
        
        for j in range(1, cols):
            count = 0
            for i in range(rows):
                count += grid[i][j]
            if count < len(grid) / 2:
                for i in range(rows):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        
        score = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][-j - 1] == 1:
                    score += 2 ** j
        
        return score