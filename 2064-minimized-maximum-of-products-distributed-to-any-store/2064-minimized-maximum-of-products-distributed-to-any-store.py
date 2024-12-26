class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def good(x):
            count = 0
            for curr in quantities:
                count += (curr + x - 1) // x
            
            return count <= n
        
        left = 0
        right = max(quantities)
        while right - left > 1:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid
        
        return right
    