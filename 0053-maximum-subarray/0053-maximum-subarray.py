class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        max_neg = nums[0]
        for n in nums:
            curr_sum += n
            curr_sum = max(curr_sum, 0)
            max_sum = max(max_sum, curr_sum)
        return max_sum if max_sum != 0 else max(nums)