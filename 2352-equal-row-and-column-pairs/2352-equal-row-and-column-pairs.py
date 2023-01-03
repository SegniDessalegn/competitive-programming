class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = self.count(grid)
        column_count = self.count(self.transpose(grid))
        
        count = 0
        for row in row_count:
            if row in column_count:
                count += (row_count[row] * column_count[row])
        
        return count
    
    def transpose(self, grid):
        for i in range(len(grid)):
            for j in range(i, len(grid[0])):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        return grid
    
    def count(self, grid):
        rows = {}
        for row in grid:
            tuple_row = tuple(row)
            rows[tuple_row] = rows.get(tuple_row, 0) + 1
        return rows