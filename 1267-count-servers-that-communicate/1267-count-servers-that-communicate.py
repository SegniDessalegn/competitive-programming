class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        row_count = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_count[i] += 1
        
        col_count = defaultdict(int)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    col_count[j] += 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        ans += 1
        
        return ans