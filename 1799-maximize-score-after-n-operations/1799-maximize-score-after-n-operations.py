class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        @cache
        def get_ans(op, mask):
            if mask == (1 << N) - 1:
                return 0
            
            curr_max = 0
            for i in range(N):
                for j in range(i + 1, N):
                    if not (mask & (1 << i)) and not (mask & (1 << j)):
                        curr_max = max(curr_max, (op * (gcd(nums[i], nums[j]))) + get_ans(op + 1, mask | (1 << i) | (1 << j)))
            
            return curr_max
        
        N = len(nums)
        return get_ans(1, 0)