class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        left, right = 0, 0
        counter = 0
        max_freq = 0
        while right < len(nums):
            counter += nums[left] - nums[right]
            while counter > k:
                counter -= (nums[left] - nums[left + 1]) * (right - left)
                left += 1
            max_freq = max(max_freq, right - left + 1)
            right += 1
        return max_freq