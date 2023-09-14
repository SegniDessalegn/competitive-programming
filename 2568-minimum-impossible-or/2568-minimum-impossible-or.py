class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        
        ans = 1
        for num in nums:
            if (num & (num - 1)) == 0:
                if num == ans:
                    ans = ans << 1
                else:
                    break
        
        return ans