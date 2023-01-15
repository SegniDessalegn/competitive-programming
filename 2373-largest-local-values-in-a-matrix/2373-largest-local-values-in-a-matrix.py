class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        self.grid = grid
        ans = []
        for i in range(len(grid) - 2):
            curr = []
            for j in range(len(grid) - 2):
                curr.append(self.max_num(i, j))
            ans.append(curr)
        
        return ans
    
    def max_num(self, i, j):
        max_n = self.grid[i][j]
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                max_n = max(max_n, self.grid[r][c])
        return max_n