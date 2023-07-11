class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        # bitmask + dynamic programming
        
        MOD = 10 ** 9 + 7
        N = len(nums)
        full = (1 << N) - 1
        
        @cache
        def recur(last, mask):
            
            if mask == full:
                return 1
            
            curr_count = 0
            for i in range(N):
                if (mask & 1 << i == 0) and (nums[i] % nums[last] == 0 or nums[last] % nums[i] == 0):
                    curr_count += recur(i, mask | (1 << i))
                    curr_count %= MOD
            
            return curr_count
        
        count = 0
        for i in range(N):
            count += recur(i, 1 << i)
            count %= MOD
        
        return count