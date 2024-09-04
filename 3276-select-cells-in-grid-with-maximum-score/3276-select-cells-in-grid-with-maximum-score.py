class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        @cache
        def get_ans(num, mask):
            if num > 100 or mask == (1 << M) - 1:
                return 0
            
            
            curr_ans = 0
            for i in range(M):
                if not (mask & (1 << i)):
                    for j in range(N):
                        if grid[i][j] == num:
                            curr_ans = max(curr_ans, num + get_ans(num + 1, (mask | (1 << i))))
            curr_ans = max(curr_ans, get_ans(num + 1, mask))
            
            return curr_ans
            
        
        M = len(grid)
        N = len(grid[0])
        
        return get_ans(1, 0)
        