class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - (self.less_than_goal(nums, goal) + self.greater_than_goal(nums, goal))
    
    def less_than_goal(self, nums, goal):
        n = len(nums)
        count = 0
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while left <= right and curr_sum >= goal:
                curr_sum -= nums[left]
                left += 1
            count += right - left + 1
        
        return count
        
    def greater_than_goal(self, nums, goal):
        n = len(nums)
        count = 0
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while left <= right and curr_sum > goal:
                count += n - right
                curr_sum -= nums[left]
                left += 1
        
        return count
            