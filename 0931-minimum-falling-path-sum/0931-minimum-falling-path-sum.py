class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        @cache
        def get_ans(i, j):
            if not (0 <= j < N):
                return float("inf")
            if i < 0:
                return 0
            
            return matrix[i][j] + min(get_ans(i - 1, j - 1), get_ans(i - 1, j), get_ans(i - 1, j + 1))
        
        N = len(matrix)
        
        ans = float("inf")
        for j in range(N):
            ans = min(ans, get_ans(N - 1, j))
        
        return ans
    