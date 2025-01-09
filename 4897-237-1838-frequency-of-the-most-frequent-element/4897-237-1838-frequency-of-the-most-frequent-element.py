class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        left = 0
        curr_sum = 0
        ans = 0
        for right in range(N):
            curr_sum += nums[right]
            while (nums[right] * (right - left + 1)) - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
    