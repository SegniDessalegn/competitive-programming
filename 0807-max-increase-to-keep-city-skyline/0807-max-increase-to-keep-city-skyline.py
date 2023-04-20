class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = []
        max_col = []
        for i in range(n):
            curr_max = grid[i][0]
            for j in range(n):
                curr_max = max(curr_max, grid[i][j])
            max_row.append(curr_max)
        
        for j in range(n):
            curr_max = grid[0][j]
            for i in range(n):
                curr_max = max(curr_max, grid[i][j])
            max_col.append(curr_max)
        
        total_heights = 0
        for i in range(n):
            for j in range(n):
                total_heights += min(max_row[i], max_col[j]) - grid[i][j]
        
        return total_heights