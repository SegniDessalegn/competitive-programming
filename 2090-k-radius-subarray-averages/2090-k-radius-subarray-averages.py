class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        averages = [-1 for _ in range(len(nums))]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if i >= 2 * k:
                averages[i - k] = curr_sum // (2*k + 1)
                curr_sum -= nums[i - 2*k]
        
        return averages