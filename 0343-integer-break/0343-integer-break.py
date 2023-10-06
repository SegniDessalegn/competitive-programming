class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def get_prod(length, s):
            if length == 0:
                return 1 if s == n else 0
            
            curr_prod = 1
            for i in range(1, n // length + 1):
                if i + s <= n:
                    curr_prod = max(curr_prod, i * get_prod(length - 1, s + i))
            
            return curr_prod
        
        ans = 1
        for length in range(2, n + 1):
            ans = max(ans, get_prod(length, 0))
        
        return ans
