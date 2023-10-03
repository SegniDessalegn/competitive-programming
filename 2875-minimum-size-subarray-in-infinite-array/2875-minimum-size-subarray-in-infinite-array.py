class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        s = sum(nums)
        extra_length = N * (target // s)
        target %= s
        
        if target == 0:
            return extra_length
        
        nums = nums + nums
        N = len(nums)
        
        curr_sum = 0
        left = 0
        length = N + 1
        for right in range(N):
            curr_sum += nums[right]
            
            while left < right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                length = min(length, right - left + 1)
        
        if length == N + 1:
            return -1
        
        return length + extra_length