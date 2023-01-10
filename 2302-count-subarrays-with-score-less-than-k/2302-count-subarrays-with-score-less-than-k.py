class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        curr_sum = 0
        count = 0
        while right < len(nums):
            curr_sum += nums[right]
            while (right - left + 1) * curr_sum >= k:
                curr_sum -= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        
        return count