class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - nums[i] == s - curr_sum:
                return i
        return -1