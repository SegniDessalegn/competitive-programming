class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                s = set()
                row_sum = []
                for r in range(3):
                    curr_sum = 0
                    for c in range(3):
                        s.add(grid[i + r][j + c])
                        curr_sum += grid[i + r][j + c]
                    row_sum.append(curr_sum)
                
                if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    continue
                if row_sum[0] != row_sum[1] or row_sum[0] != row_sum[2] or row_sum[1] != row_sum[2]:
                    continue
                
                col_sum = []
                for c in range(3):
                    curr_sum = 0
                    for r in range(3):
                        curr_sum += grid[i + r][j + c]
                    col_sum.append(curr_sum)
                if col_sum[0] != col_sum[1] or col_sum[0] != col_sum[2] or col_sum[1] != col_sum[2] or col_sum[0] != row_sum[0]:
                    continue
                
                diagonal = 0
                for r in range(3):
                    diagonal += grid[i + r][j + r]
                if diagonal != row_sum[0]:
                    continue
                
                diagonal = 0
                col = 2
                for r in range(3):
                    diagonal += grid[i + r][j + col]
                    col -= 1
                if diagonal != row_sum[0]:
                    continue
                
                count += 1
        
        return count