class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        return max(0, nums[-1] - nums[0] - 2 * k) if len(nums) > 1 else 0