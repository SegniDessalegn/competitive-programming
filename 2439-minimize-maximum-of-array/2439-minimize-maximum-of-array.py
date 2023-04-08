class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref = 0
        ans = nums[0]
        for i in range(len(nums)):
            pref += nums[i]
            ans = max(ans, math.ceil(pref / (i + 1)))
        
        return ans