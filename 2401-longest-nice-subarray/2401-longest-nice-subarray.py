class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        def update(n, add):
            i = 0
            while n:
                if add:
                    setBits[i] += n & 1
                else:
                    setBits[i] -= n & 1
                n >>= 1
                i += 1
            
            for i in range(30):
                if setBits[i] >= 2:
                    return False
            
            return True
        
        setBits = [0] * 30
        count = 0
        left = 0
        right = 0
        ans = 1
        while right < len(nums):
            valid = update(nums[right], True)
            while not valid:
                valid = update(nums[left], False)
                left += 1
            if right - left + 1 > ans:
                ans = right - left + 1
            right += 1
        
        return ans