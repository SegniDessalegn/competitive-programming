class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        
        def good(mid):
            total = 0
            i = N - 1
            j = 0
            
            while i >= 0 and j < N:
                if matrix[i][j] <= mid:
                    total += i + 1
                    j += 1
                else:
                    i -= 1
            
            return total >= k
        
        
        left = matrix[0][0] - 1
        right = matrix[N - 1][N - 1]
        
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
        