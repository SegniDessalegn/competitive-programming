class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        nums = [0, 1]
        for i in range(1, (n // 2) + 1):
            nums.append(nums[i])
            nums.append(nums[i] + nums[i + 1])
        
        if len(nums) > n + 1:
            nums.pop()
        
        return max(nums)