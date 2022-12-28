class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_count = self.count_ones_row(grid)
        col_count = self.count_ones_col(grid)
        ans = []
        for i in range(m):
            curr_row = []
            for j in range(n):
                curr_row.append(row_count[i] + col_count[j] - (m - row_count[i]) - (n - col_count[j]))
            ans.append(curr_row)
        return ans
    
    def count_ones_row(self, grid):
        ans = []
        for row in grid:
            count = 0
            for i in range(len(row)):
                if row[i] == 1:
                    count += 1
            ans.append(count)
        return ans

    def count_ones_col(self, grid):
        ans = [0 for i in range(len(grid[0]))]
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    ans[i] += 1
        return ans