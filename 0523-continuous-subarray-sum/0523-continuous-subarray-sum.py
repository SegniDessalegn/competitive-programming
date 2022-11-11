class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0: 0}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k not in rem:
                rem[curr_sum % k] = i + 1
            elif rem[curr_sum % k] < i:
                return True
        return False