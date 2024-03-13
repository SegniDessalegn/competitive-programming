class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        directions = [(1, 0, 1, 0), (1, 0, 1, -1), (1, 0, 1, 1), (1, -1, 1, 0), (1, -1, 1, -1), (1, -1, 1, 1), (1, 1, 1, 0), (1, 1, 1, -1), (1, 1, 1, 1)]
        
        @cache
        def get_ans(i, j, k, l):
            if i == m or k == m:
                return 0
            
            max_sum = 0
            for di, dj, dk, dl in directions:
                
                ni = i + di
                nj = j + dj
                nk = k + dk
                nl = l + dl
                
                if not (0 <= nj < n) or not(0 <= nl < n):
                    continue
                
                curr_sum = get_ans(ni, nj, nk, nl)
                max_sum = max(max_sum, grid[i][j] + grid[k][l] + curr_sum)
            
            if (i, j) == (k, l):
                max_sum -= grid[i][j]
            
            return max_sum
        
        return get_ans(0, 0, 0, n - 1)
    